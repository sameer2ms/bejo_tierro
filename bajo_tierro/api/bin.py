import frappe

def get_all_bin_stock(item_code):
    bin = frappe.get_all("Bin", {"item_code": item_code})
    return bin