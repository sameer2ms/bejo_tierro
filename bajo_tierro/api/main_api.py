from bajo_tierro.api.bin import get_all_bin_stock
from bajo_tierro.api.customer import check_customer_by_mobile, validate_customer_from_mobile
from bajo_tierro.api.stock_report_api import get_data_from_stock_report
import frappe 

@frappe.whitelist()
def validate_customer(item):
    return validate_customer_from_mobile(item)


@frappe.whitelist()
def create_new_lead(lead):
    return create_lead(lead)

@frappe.whitelist()
def check_customer_from_mobile_no(mobile_number):
    return check_customer_by_mobile(mobile_number)

@frappe.whitelist()
def get_stock_data(from_date, to_date, company, item_code, warehouse = None):
    return get_data_from_stock_report(from_date, to_date, company, item_code, warehouse)

@frappe.whitelist()
def get_bin_stock(item_code):
    return get_all_bin_stock(item_code)