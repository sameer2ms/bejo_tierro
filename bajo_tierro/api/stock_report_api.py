
from bajo_tierro_customization.bajo_tierro_customization.report.stock_balance_custom.stock_balance_custom import execute
import frappe

@frappe.whitelist()
def get_data_from_stock_report(from_date, to_date, company, item_code, warehouse = None):
    
    # print("\n\n this are filters", from_date, to_date, company, warehouse, item_code)
    # company from_date to_date item_code warehouse
    filters = {
        "from_date": from_date, 
        "to_date": to_date, 
        "company": company, 
        "warehouse": warehouse, 
        "item_code": item_code
    }
    # print("\n\n this are filters", filters)
    data = execute(filters)

    return data[1]