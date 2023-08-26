from bajo_tierro.bajo_tierro.report.re_order_qty.re_order_qty import execute
import frappe

def validate_customer_from_mobile(item):
    print(" this is item", item)
    # this is testing data
    # data = [{ "a": 123, "b":345}, {"a": 234, "b": 890}, {"a": item, "b": item}]
    filters= {"item": "A-002", "year": "2023-2024"}
    data = execute(filters)

    return data



@frappe.whitelist()
def validate_customer(item):
    return validate_customer_from_mobile(item)

# bajo_tierro.bajo_tierro.api.customer.validate_customer?item=your-item-code

def validate_customer_from_mobile(customer):

    print(" this is customer")
    customer = {"name": "Sameer"}
    if customer.get("name"):
        if frappe.db.exists("Customer", customer.get("name")):
            return("Customer already exists")
       

# def create_new_customer(customer):
    
def create_new_customer(customer):
    customer = frappe.new_doc("Customer")
    customer.customer_name = "Demo Customer"
    customer.customer_type = "Company"
    customer.customer_group = "All Customer Groups"
    customer.territory = "All Territories"
    customer.save()

if __name__ == "__main__":
    frappe.init(site="your-site-name")
    frappe.connect()
    
    try:
        create_demo_customer()
        frappe.db.commit()
        print("Demo customer created successfully.")
    except Exception as e:
        frappe.db.rollback()
        print("Error creating demo customer:", str(e))
    finally:
        frappe.disconnect()    

def check_customer_by_mobile(mobile_number):
    filters = {
        "mobile_no": mobile_number
    }
    print(" \n\n this is customer", mobile_number)
    customer_list = frappe.get_list("Customer", filters=filters)
    return len(customer_list) > 0
# mobile_no