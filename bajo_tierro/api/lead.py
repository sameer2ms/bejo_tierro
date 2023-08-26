import frappe

def create_demo_lead():
    lead = frappe.new_doc("Lead")
    lead.lead_name = "Demo Lead"
    lead.company_name = "Demo Company"
    lead.lead_owner = "Administrator"
    lead.contact_date = "2023-08-09"  # Replace with a valid date
    lead.email_id = "demo@example.com"
    lead.mobile_no = "1234567890"
    lead.save()

if __name__ == "__main__":
    frappe.init(site="your-site-name")
    frappe.connect()
    
    try:
        create_demo_lead()
        frappe.db.commit()
        print("Demo lead created successfully.")
    except Exception as e:
        frappe.db.rollback()
        print("Error creating demo lead:", str(e))
    finally:
        frappe.disconnect()