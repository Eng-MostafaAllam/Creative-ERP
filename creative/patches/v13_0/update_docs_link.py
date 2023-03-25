

import frappe


def execute():
	navbar_settings = frappe.get_single("Navbar Settings")
	for item in navbar_settings.help_dropdown:
		if item.is_standard and item.route == "http://creative-ps.org":
			item.route = "http://creative-ps.org"

	navbar_settings.save()
