 
import frappe

from creative.regional.united_arab_emirates.setup import setup


def execute():
	company = frappe.get_all("Company", filters={"country": "United Arab Emirates"})
	if not company:
		return

	frappe.reload_doc("regional", "report", "uae_vat_201")
	frappe.reload_doc("regional", "doctype", "uae_vat_settings")
	frappe.reload_doc("regional", "doctype", "uae_vat_account")

	setup()
