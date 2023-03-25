// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.require("assets/creative/js/sales_trends_filters.js", function() {
	frappe.query_reports["Quotation Trends"] = {
		filters: creative.get_sales_trends_filters()
	}
});
