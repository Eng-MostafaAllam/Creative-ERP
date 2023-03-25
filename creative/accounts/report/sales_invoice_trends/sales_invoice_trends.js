 
frappe.require("assets/creative/js/sales_trends_filters.js", function() {
	frappe.query_reports["Sales Invoice Trends"] = {
		filters: creative.get_sales_trends_filters()
	}
});
