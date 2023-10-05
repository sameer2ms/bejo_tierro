# Copyright (c) 2023, Sameer and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar


def execute(filters=None):
	# data = [{"item_code":"A", "col1":100, "col2": 123, "col3": 12,}]
	columns = get_columns(filters)
	data = get_date(filters)
	return columns, data

def get_columns(filters):
	from_date = datetime.strptime(filters.get("from_date"), '%Y-%m-%d')
	to_date = datetime.strptime(filters.get("to_date"), '%Y-%m-%d')
	
	delta = relativedelta(to_date, from_date)
	months = delta.years * 12 + delta.months
	
	# month error if >12 and less then 6
	if months >12:
		frappe.throw(" Date range cannot be more than 12 months")
	elif months+1 < 6:
		frappe.throw(" Date range cannot be less than 6 months")	

	first_day = from_date.replace(day=1)	


	year = to_date.year
	month = to_date.month
	last_day = calendar.monthrange(year, month)[1]
	last_day_date = to_date.replace(day=last_day)


	current_date = from_date
	month_names_and_years = []

	while current_date <= to_date:
		year = current_date.year
		month = current_date.month
		month_name = calendar.month_abbr[month]
		# month_name
		# month_name = calendar.month_name[month]
		month_names_and_years.append(f"{month_name} {year}")
		
		if month == 12:
			current_date = current_date.replace(year=year + 1, month=1)
		else:
			current_date += timedelta(days=calendar.monthrange(year, month)[1])
			
	columns = [
		{
			"label": _("Item"),
			"fieldtype": "Link",
			"fieldname": "item_code",
			"options": "Item",
			"width": 150,
		},
		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "item_name",
			"width": 150,
		},
		{
			"label": _("Item Group"),
			"fieldtype": "Link",
			"fieldname": "item_group",
			"options": "Item Group",
			"width": 150,
		},
	]	

	total_len = len(month_names_and_years) 
	
	for m in month_names_and_years:

		columns.append({
			"label": _(m),
			"fieldtype": "int",
			"fieldname": "col_"+ str(total_len),
			"options": "Item Group",
			"width": 150,
		})
		total_len -= 1

	
	columns.extend([

		{
			"label": _("Total Sales"),
			"fieldtype": "Int",
			"fieldname": "total",
			"width": 100,
		},
		{
			"label": _("Stock in PCS"),
			"fieldtype": "Int",
			"fieldname": "stock",
			"width": 100,
		},
		{
			"label": _("Avg Sales 3 Months"),
			"fieldtype": "Int",
			"fieldname": "avg3",
			"width": 100,
		},
		{
			"label": _("Avg Sales 6 Months"),
			"fieldtype": "Int",
			"fieldname": "avg6",
			"width": 100,
		},
		{
			"label": _("Actual Avg Sales 3 Months"),
			"fieldtype": "Int",
			"fieldname": "actual3",
			"width": 100,
		},
		{
			"label": _("Sales to Stock Ratio"),
			"fieldtype": "int",
			"fieldname": "ratio",
			"width": 100,
		},
		{
			"label": _("Unique/Non-unique"),
			"fieldtype": "data",
			"fieldname": "unique",
			"width": 100,
		},
		{
			"label": _("Moving"),
			"fieldtype": "data",
			"fieldname": "moving",
			"width": 100,
		},
		{
			"label": _("3 Months Stock"),
			"fieldtype": "Int",
			"fieldname": "month3",
			"width": 100,
		},
		{
			"label": _("5 Months Stock"),
			"fieldtype": "Int",
			"fieldname": "month5",
			"width": 100,
		},
		{
			"label": _("Lead Time"),
			"fieldtype": "Int",
			"fieldname": "lead_time",
			"width": 100,
		},
		{
			"label": _("In-Transit"),
			"fieldtype": "Int",
			"fieldname": "in_transit",
			"width": 100,
		},
		{
			"label": _("Total Stock 3 Months"),
			"fieldtype": "Int",
			"fieldname": "stock3month",
			"width": 100,
		},
		{
			"label": _("ROQ"),
			"fieldtype": "Int",
			"fieldname": "roq",
			"width": 100,
		},
	])

	return columns

def get_date(filters):
	from_date = datetime.strptime(filters.get("from_date"), '%Y-%m-%d')
	to_date = datetime.strptime(filters.get("to_date"), '%Y-%m-%d')
	
	delta = relativedelta(to_date, from_date)
	months = delta.years * 12 + delta.months
	
	# month error if >12 and less then 6
	if months >12:
		frappe.throw(" Date range cannot be more than 12 months")
	elif months+1 < 6:
		frappe.throw(" Date range cannot be less than 6 months")	

	first_day = to_date.replace(day=1)	


	year = from_date.year
	month = from_date.month
	last_day = calendar.monthrange(year, month)[1]
	last_day_date = from_date.replace(day=last_day)


	current_date = from_date
	month_names_and_years = []

	while current_date <= to_date:
		year = current_date.year
		month = current_date.month
		month_name = calendar.month_name[month]
		month_names_and_years.append(f"{month_name} {year}")
		
		if month == 12:
			current_date = current_date.replace(year=year + 1, month=1)
		else:
			current_date += timedelta(days=calendar.monthrange(year, month)[1])

	condition = " and 1 = 1 "	
	in_transit_add = " and 1=1"

	if filters.get("item"):
		condition += " and tsii.item_code = '{0}' ".format(filters.get("item"))

	warehouse_cond = " and 1 = 1 "
	if filters.get("company"):
		
		condition += " and tsi.company = '{0}' ".format(filters.get("company"))
		in_transit_add += " and tpr.company = '{0}' ".format(filters.get("company"))

		warehouse = frappe.get_all("Warehouse", {"company": filters.get("company")})
		warehouse_str = "("
		for index, w in enumerate(warehouse):
			if index == len(warehouse) - 1:
				warehouse_str += "'"+w.name+"'" 
			else: 	
				warehouse_str += "'"+w.name+"'," 
		warehouse_str += ")"
		warehouse_cond += f" and tb.warehouse in  {warehouse_str}"
		

	if filters.get("item_group"):
		condition += " and tsii.item_group = '{0}' ".format(filters.get("item_group"))	

	total_len = len(month_names_and_years) - 1
	inner_query = ""

	result_list = month_names_and_years[1:-1]

	inner_query += "SUM(CASE WHEN tsii.creation between '{0}' and '{1}' THEN qty ELSE 0 END) AS col_{2}, ".format(from_date,last_day_date , len(month_names_and_years))

	for m in result_list:
		month, year = m.split()

		inner_query += " SUM(CASE WHEN MONTHNAME(tsii.creation) = '{0}' AND YEAR(tsii.creation) = '{1}' THEN qty ELSE 0 END) AS col_{2}, ".format(month, year, total_len)

		total_len -= 1

	# in-transit
	

	transit = f"""( Select sum(tpri.accepted_quantity_nos) 
					from `tabPurchase Receipt Item` tpri
					Left Join `tabPurchase Receipt` tpr on tpr.name = tpri.parent 
					WHERE tpri.docstatus = 0
					and tpri.creation BETWEEN '{from_date}' and '{to_date}' 
					and tpri.item_code = tsii.item_code {in_transit_add}) as in_transit, """
	

	# last date added
	inner_query += "SUM(CASE WHEN tsii.creation between '{0}' and '{1}' THEN qty ELSE 0 END) AS col_1, ".format(first_day, to_date)
	query = frappe.db.sql("""
			SELECT tsii.item_code, tsii.item_name, tsii.item_group, 
			{1}
		    {4}   
			SUM(CASE WHEN tsii.creation between '{2}' and '{3}' THEN qty ELSE 0 END) AS total,
			(SELECT SUM(actual_qty) from `tabBin` tb   
						WHERE tb.item_code = tsii.item_code {5}
						group by item_code) as stock,
		    (Select lead_time_days from `tabItem` where name = tsii.item_code) as  lead_time 
						FROM
						`tabSales Invoice Item` tsii 
		       			Left Join `tabSales Invoice` tsi on tsi.name = tsii.parent	
						WHERE
						tsii.docstatus = 1
						and tsi.is_return = 0	
		      				{0}
						GROUP BY
							tsii.item_code;

						""".format(condition, inner_query, from_date, to_date, transit, warehouse_cond), as_dict = 1, debug = 0)	


	if query:
		for d in query:
			stock3month_sub = stock = 0
			if d.stock == None:
				stock = 1
				stock3month_sub = 0
			elif d.stock == 0.0:
				stock = 1	
			else:
				stock = d.stock
				stock3month_sub = d.stock
					
			avg3_1 = round(d.col_1 + d.col_2 + d.col_3)/3 
			avg6_1 = round(d.col_2 + d.col_3 + d.col_4 + d.col_5 + d.col_6 + d.col_1)/6

			avg3_ = int(avg3_1) + (1 if avg3_1 - int(avg3_1) >= 0.5 else 0)
			avg6_ = int(avg6_1) + (1 if avg6_1 - int(avg6_1) >= 0.5 else 0)
			
			ratio_ = (avg3_/stock if stock > 0 else 1)*100

			moving_ = ""
			if ratio_ <= 5:
				moving_ = "Non-moving"
			elif ratio_ <= 20:
				moving_	= "Slow-moving"
			elif ratio_ <=50:
				moving_ = "Moving"
			else: 	
				moving_ = "Fast_moving"	

			# =IF(AA2>=0, (AA2+(X2-W2)+(Y2/30)*R2),0)	
			new_stock_3_month = 0
			stock3month_ = 0
			if d.stock == None:
				stock3month_= (int(avg6_) * 3) - 0,
				
			elif d.stock == 0.0:
				stock3month_= (int(avg6_) * 3) - 0,
			else:
				stock3month_= int((int(avg6_) * 3) - int(d.stock))
			# stock3month_= (int(avg6_) * 3) - stock,
			
			

			if isinstance(stock3month_, int):
				new_stock_3_month = stock3month_
				
				if int(stock3month_) >= 0:

					r = int(stock3month_) + ((int(avg6_) * 5) - (int(avg6_) * 3)) + (d.lead_time/30) * int(avg6_)
					if r > 0:
						roq_ = r
					else: roq_ = 0 
					
				else: roq_ = 0
			else : 
					
				new_stock_3_month = int(stock3month_[0])
				if int(stock3month_[0]) >= 0:

					r = int(stock3month_[0]) + ((int(avg6_) * 5) - (int(avg6_) * 3)) + (d.lead_time/30) * int(avg6_)
					if r > 0:
						roq_ = r
					else: roq_ = 0 
					
				else: roq_ = 0	
			d.update({
				'avg3': avg3_,
				'avg6': avg6_,
				'actual3': stock/3 ,
				'ratio': int(ratio_) ,
				'moving': moving_,
				'unique': "abc",
				'month3': int(avg6_) * 3,
				'month5': int(avg6_) * 5,
				'stock3month': new_stock_3_month,
				'roq': roq_,
				'in_transit': d.in_transit if d.in_transit else 0

		})
	return query
