 

import frappe

from creative.regional.italy.setup import add_permissions


def execute():
	countries = frappe.get_all("Company", fields="country")
	countries = [country["country"] for country in countries]
	if "Italy" in countries:
		add_permissions()
