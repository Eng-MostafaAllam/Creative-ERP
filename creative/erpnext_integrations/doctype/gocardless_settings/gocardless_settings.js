 
frappe.ui.form.on('GoCardless Settings', {
	refresh: function(frm) {
		creative.utils.check_payments_app();
	}
});
