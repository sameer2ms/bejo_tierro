// Copyright (c) 2023, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product Booking', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Product Booking Item', {
    items_add: function(frm, cdt, cdn) {
        calculateTotalQtyAndRate(frm);
    },
    qty: function(frm, cdt, cdn) {
		calculateAmount(frm, cdt, cdn);
        calculateTotalQtyAndRate(frm);
    },
    rate: function(frm, cdt, cdn) {
		calculateAmount(frm, cdt, cdn);
        calculateTotalQtyAndRate(frm);
    }
});

function calculateTotalQtyAndRate(frm) {
    var total_qty = 0;
    var total_amount = 0;

    $.each(frm.doc.items || [], function(i, item) {
        total_qty += item.qty;
        total_amount += item.amount;
    });

    frm.set_value('total_qty', total_qty);
    frm.set_value('total_amount', total_amount);
}

function calculateAmount(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var qty = child.qty || 0;
    var rate = child.rate || 0;

    var amount = qty * rate;
    frappe.model.set_value(cdt, cdn, 'amount', amount);
}
