app_name = "creative"
app_title = "creative"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = """ERP made simple"""
app_icon = "fa fa-th"
app_color = "#e74c3c"
app_email = "info@creative.com"
app_license = "GNU General Public License (v3)"
source_link = "https://github.com/frappe/creative"
app_logo_url = "/assets/creative/images/creative-logo.svg"


develop_version = "14.x.x-develop"

app_include_js = "creative.bundle.js"
app_include_css = "creative.bundle.css"
web_include_js = "creative-web.bundle.js"
web_include_css = "creative-web.bundle.css"
email_css = "email_creative.bundle.css"

doctype_js = {
	"Address": "public/js/address.js",
	"Communication": "public/js/communication.js",
	"Event": "public/js/event.js",
	"Newsletter": "public/js/newsletter.js",
	"Contact": "public/js/contact.js",
}

override_doctype_class = {"Address": "creative.accounts.custom.address.creativeAddress"}

welcome_email = "creative.setup.utils.welcome_email"

# setup wizard
setup_wizard_requires = "assets/creative/js/setup_wizard.js"
setup_wizard_stages = "creative.setup.setup_wizard.setup_wizard.get_setup_stages"
setup_wizard_test = "creative.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"

before_install = "creative.setup.install.check_setup_wizard_not_completed"
after_install = "creative.setup.install.after_install"

boot_session = "creative.startup.boot.boot_session"
notification_config = "creative.startup.notifications.get_notification_config"
get_help_messages = "creative.utilities.activation.get_help_messages"
leaderboards = "creative.startup.leaderboard.get_leaderboards"
filters_config = "creative.startup.filters.get_filters_config"
additional_print_settings = "creative.controllers.print_settings.get_print_settings"

on_session_creation = [
	"creative.portal.utils.create_customer_or_supplier",
	"creative.e_commerce.shopping_cart.utils.set_cart_count",
]
on_logout = "creative.e_commerce.shopping_cart.utils.clear_cart_count"

treeviews = [
	"Account",
	"Cost Center",
	"Warehouse",
	"Item Group",
	"Customer Group",
	"Supplier Group",
	"Sales Person",
	"Territory",
	"Department",
]

# website
update_website_context = [
	"creative.e_commerce.shopping_cart.utils.update_website_context",
]
my_account_context = "creative.e_commerce.shopping_cart.utils.update_my_account_context"
webform_list_context = "creative.controllers.website_list_for_contact.get_webform_list_context"

calendars = [
	"Task",
	"Work Order",
	"Leave Application",
	"Sales Order",
	"Holiday List",
]

website_generators = ["Item Group", "Website Item", "BOM", "Sales Partner"]

website_context = {
	"favicon": "/assets/creative/images/creative-favicon.svg",
	"splash_image": "/assets/creative/images/creative-logo.svg",
}

# nosemgrep
website_route_rules = [
	{"from_route": "/orders", "to_route": "Sales Order"},
	{
		"from_route": "/orders/<path:name>",
		"to_route": "order",
		"defaults": {"doctype": "Sales Order", "parents": [{"label": "Orders", "route": "orders"}]},
	},
	{"from_route": "/invoices", "to_route": "Sales Invoice"},
	{
		"from_route": "/invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Sales Invoice",
			"parents": [{"label": "Invoices", "route": "invoices"}],
		},
	},
	{"from_route": "/supplier-quotations", "to_route": "Supplier Quotation"},
	{
		"from_route": "/supplier-quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Supplier Quotation",
			"parents": [{"label": "Supplier Quotation", "route": "supplier-quotations"}],
		},
	},
	{"from_route": "/purchase-orders", "to_route": "Purchase Order"},
	{
		"from_route": "/purchase-orders/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Order",
			"parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
		},
	},
	{"from_route": "/purchase-invoices", "to_route": "Purchase Invoice"},
	{
		"from_route": "/purchase-invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Invoice",
			"parents": [{"label": "Purchase Invoice", "route": "purchase-invoices"}],
		},
	},
	{"from_route": "/quotations", "to_route": "Quotation"},
	{
		"from_route": "/quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Quotation",
			"parents": [{"label": "Quotations", "route": "quotations"}],
		},
	},
	{"from_route": "/shipments", "to_route": "Delivery Note"},
	{
		"from_route": "/shipments/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Delivery Note",
			"parents": [{"label": "Shipments", "route": "shipments"}],
		},
	},
	{"from_route": "/rfq", "to_route": "Request for Quotation"},
	{
		"from_route": "/rfq/<path:name>",
		"to_route": "rfq",
		"defaults": {
			"doctype": "Request for Quotation",
			"parents": [{"label": "Request for Quotation", "route": "rfq"}],
		},
	},
	{"from_route": "/addresses", "to_route": "Address"},
	{
		"from_route": "/addresses/<path:name>",
		"to_route": "addresses",
		"defaults": {"doctype": "Address", "parents": [{"label": "Addresses", "route": "addresses"}]},
	},
	{"from_route": "/boms", "to_route": "BOM"},
	{"from_route": "/timesheets", "to_route": "Timesheet"},
	{"from_route": "/material-requests", "to_route": "Material Request"},
	{
		"from_route": "/material-requests/<path:name>",
		"to_route": "material_request_info",
		"defaults": {
			"doctype": "Material Request",
			"parents": [{"label": "Material Request", "route": "material-requests"}],
		},
	},
	{"from_route": "/project", "to_route": "Project"},
	{"from_route": "/tasks", "to_route": "Task"},
]

standard_portal_menu_items = [
	{"title": "Projects", "route": "/project", "reference_doctype": "Project"},
	{
		"title": "Request for Quotations",
		"route": "/rfq",
		"reference_doctype": "Request for Quotation",
		"role": "Supplier",
	},
	{
		"title": "Supplier Quotation",
		"route": "/supplier-quotations",
		"reference_doctype": "Supplier Quotation",
		"role": "Supplier",
	},
	{
		"title": "Purchase Orders",
		"route": "/purchase-orders",
		"reference_doctype": "Purchase Order",
		"role": "Supplier",
	},
	{
		"title": "Purchase Invoices",
		"route": "/purchase-invoices",
		"reference_doctype": "Purchase Invoice",
		"role": "Supplier",
	},
	{
		"title": "Quotations",
		"route": "/quotations",
		"reference_doctype": "Quotation",
		"role": "Customer",
	},
	{
		"title": "Orders",
		"route": "/orders",
		"reference_doctype": "Sales Order",
		"role": "Customer",
	},
	{
		"title": "Invoices",
		"route": "/invoices",
		"reference_doctype": "Sales Invoice",
		"role": "Customer",
	},
	{
		"title": "Shipments",
		"route": "/shipments",
		"reference_doctype": "Delivery Note",
		"role": "Customer",
	},
	{"title": "Issues", "route": "/issues", "reference_doctype": "Issue", "role": "Customer"},
	{"title": "Addresses", "route": "/addresses", "reference_doctype": "Address"},
	{
		"title": "Timesheets",
		"route": "/timesheets",
		"reference_doctype": "Timesheet",
		"role": "Customer",
	},
	{"title": "Newsletter", "route": "/newsletters", "reference_doctype": "Newsletter"},
	{
		"title": "Material Request",
		"route": "/material-requests",
		"reference_doctype": "Material Request",
		"role": "Customer",
	},
	{"title": "Appointment Booking", "route": "/book_appointment"},
]

default_roles = [
	{"role": "Customer", "doctype": "Contact", "email_field": "email_id"},
	{"role": "Supplier", "doctype": "Contact", "email_field": "email_id"},
]

sounds = [
	{"name": "incoming-call", "src": "/assets/creative/sounds/incoming-call.mp3", "volume": 0.2},
	{"name": "call-disconnect", "src": "/assets/creative/sounds/call-disconnect.mp3", "volume": 0.2},
]

has_upload_permission = {
	"Employee": "creative.setup.doctype.employee.employee.has_upload_permission"
}

has_website_permission = {
	"Sales Order": "creative.controllers.website_list_for_contact.has_website_permission",
	"Quotation": "creative.controllers.website_list_for_contact.has_website_permission",
	"Sales Invoice": "creative.controllers.website_list_for_contact.has_website_permission",
	"Supplier Quotation": "creative.controllers.website_list_for_contact.has_website_permission",
	"Purchase Order": "creative.controllers.website_list_for_contact.has_website_permission",
	"Purchase Invoice": "creative.controllers.website_list_for_contact.has_website_permission",
	"Material Request": "creative.controllers.website_list_for_contact.has_website_permission",
	"Delivery Note": "creative.controllers.website_list_for_contact.has_website_permission",
	"Issue": "creative.support.doctype.issue.issue.has_website_permission",
	"Timesheet": "creative.controllers.website_list_for_contact.has_website_permission",
}

before_tests = "creative.setup.utils.before_tests"

standard_queries = {
	"Customer": "creative.controllers.queries.customer_query",
}

doc_events = {
	"*": {
		"validate": "creative.support.doctype.service_level_agreement.service_level_agreement.apply",
	},
	"Stock Entry": {
		"on_submit": "creative.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
		"on_cancel": "creative.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
	},
	"User": {
		"after_insert": "frappe.contacts.doctype.contact.contact.update_contact",
		"validate": "creative.setup.doctype.employee.employee.validate_employee_role",
		"on_update": [
			"creative.setup.doctype.employee.employee.update_user_permissions",
			"creative.portal.utils.set_default_role",
		],
	},
	"Communication": {
		"on_update": [
			"creative.support.doctype.service_level_agreement.service_level_agreement.on_communication_update",
			"creative.support.doctype.issue.issue.set_first_response_time",
		],
		"after_insert": "creative.crm.utils.link_communications_with_prospect",
	},
	"Event": {
		"after_insert": "creative.crm.utils.link_events_with_prospect",
	},
	"Sales Taxes and Charges Template": {
		"on_update": "creative.e_commerce.doctype.e_commerce_settings.e_commerce_settings.validate_cart_settings"
	},
	"Sales Invoice": {
		"on_submit": [
			"creative.regional.create_transaction_log",
			"creative.regional.italy.utils.sales_invoice_on_submit",
		],
		"on_cancel": ["creative.regional.italy.utils.sales_invoice_on_cancel"],
		"on_trash": "creative.regional.check_deletion_permission",
	},
	"Purchase Invoice": {
		"validate": [
			"creative.regional.united_arab_emirates.utils.update_grand_total_for_rcm",
			"creative.regional.united_arab_emirates.utils.validate_returns",
		]
	},
	"Payment Entry": {
		"on_submit": [
			"creative.regional.create_transaction_log",
			"creative.accounts.doctype.payment_request.payment_request.update_payment_req_status",
			"creative.accounts.doctype.dunning.dunning.resolve_dunning",
		],
		"on_trash": "creative.regional.check_deletion_permission",
	},
	"Address": {
		"validate": [
			"creative.regional.italy.utils.set_state_code",
		],
	},
	"Contact": {
		"on_trash": "creative.support.doctype.issue.issue.update_issue",
		"after_insert": "creative.telephony.doctype.call_log.call_log.link_existing_conversations",
		"validate": ["creative.crm.utils.update_lead_phone_numbers"],
	},
	"Email Unsubscribe": {
		"after_insert": "creative.crm.doctype.email_campaign.email_campaign.unsubscribe_recipient"
	},
	"Integration Request": {
		"validate": "creative.accounts.doctype.payment_request.payment_request.validate_payment"
	},
}

# On cancel event Payment Entry will be exempted and all linked submittable doctype will get cancelled.
# to maintain data integrity we exempted payment entry. it will un-link when sales invoice get cancelled.
# if payment entry not in auto cancel exempted doctypes it will cancel payment entry.
auto_cancel_exempted_doctypes = [
	"Payment Entry",
]

scheduler_events = {
	"cron": {
		"0/15 * * * *": [
			"creative.manufacturing.doctype.bom_update_log.bom_update_log.resume_bom_cost_update_jobs",
		],
		"0/30 * * * *": [
			"creative.utilities.doctype.video.video.update_youtube_data",
		],
		# Hourly but offset by 30 minutes
		"30 * * * *": [
			"creative.accounts.doctype.gl_entry.gl_entry.rename_gle_sle_docs",
		],
		# Daily but offset by 45 minutes
		"45 0 * * *": [
			"creative.stock.reorder_item.reorder_item",
		],
	},
	"all": [
		"creative.projects.doctype.project.project.project_status_update_reminder",
		"creative.crm.doctype.social_media_post.social_media_post.process_scheduled_social_media_posts",
	],
	"hourly": [
		"creative.creative_integrations.doctype.plaid_settings.plaid_settings.automatic_synchronization",
		"creative.projects.doctype.project.project.hourly_reminder",
		"creative.projects.doctype.project.project.collect_project_status",
	],
	"hourly_long": [
		"creative.accounts.doctype.subscription.subscription.process_all",
		"creative.stock.doctype.repost_item_valuation.repost_item_valuation.repost_entries",
		"creative.bulk_transaction.doctype.bulk_transaction_log.bulk_transaction_log.retry_failing_transaction",
	],
	"daily": [
		"creative.support.doctype.issue.issue.auto_close_tickets",
		"creative.crm.doctype.opportunity.opportunity.auto_close_opportunity",
		"creative.controllers.accounts_controller.update_invoice_status",
		"creative.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
		"creative.projects.doctype.task.task.set_tasks_as_overdue",
		"creative.assets.doctype.asset.depreciation.post_depreciation_entries",
		"creative.stock.doctype.serial_no.serial_no.update_maintenance_status",
		"creative.buying.doctype.supplier_scorecard.supplier_scorecard.refresh_scorecards",
		"creative.setup.doctype.company.company.cache_companies_monthly_sales_history",
		"creative.assets.doctype.asset.asset.update_maintenance_status",
		"creative.assets.doctype.asset.asset.make_post_gl_entry",
		"creative.crm.doctype.contract.contract.update_status_for_contracts",
		"creative.projects.doctype.project.project.update_project_sales_billing",
		"creative.projects.doctype.project.project.send_project_status_email_to_users",
		"creative.quality_management.doctype.quality_review.quality_review.review",
		"creative.support.doctype.service_level_agreement.service_level_agreement.check_agreement_status",
		"creative.crm.doctype.email_campaign.email_campaign.send_email_to_leads_or_contacts",
		"creative.crm.doctype.email_campaign.email_campaign.set_email_campaign_status",
		"creative.selling.doctype.quotation.quotation.set_expired_status",
		"creative.buying.doctype.supplier_quotation.supplier_quotation.set_expired_status",
		"creative.accounts.doctype.process_statement_of_accounts.process_statement_of_accounts.send_auto_email",
	],
	"daily_long": [
		"creative.setup.doctype.email_digest.email_digest.send",
		"creative.manufacturing.doctype.bom_update_tool.bom_update_tool.auto_update_latest_price_in_all_boms",
		"creative.loan_management.doctype.process_loan_security_shortfall.process_loan_security_shortfall.create_process_loan_security_shortfall",
		"creative.loan_management.doctype.process_loan_interest_accrual.process_loan_interest_accrual.process_loan_interest_accrual_for_term_loans",
		"creative.crm.utils.open_leads_opportunities_based_on_todays_event",
	],
	"monthly_long": [
		"creative.accounts.deferred_revenue.process_deferred_accounting",
		"creative.loan_management.doctype.process_loan_interest_accrual.process_loan_interest_accrual.process_loan_interest_accrual_for_demand_loans",
	],
}

email_brand_image = "assets/creative/images/creative-logo.jpg"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://creative.com?source=via_email_footer" target="_blank">
			creative
		</a>
	</span>
"""

get_translated_dict = {
	("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"
}

bot_parsers = [
	"creative.utilities.bot.FindItemBot",
]

get_site_info = "creative.utilities.get_site_info"

payment_gateway_enabled = "creative.accounts.utils.create_payment_gateway_account"

communication_doctypes = ["Customer", "Supplier"]

advance_payment_doctypes = ["Sales Order", "Purchase Order"]

invoice_doctypes = ["Sales Invoice", "Purchase Invoice"]

period_closing_doctypes = [
	"Sales Invoice",
	"Purchase Invoice",
	"Journal Entry",
	"Bank Clearance",
	"Asset",
	"Stock Entry",
]

bank_reconciliation_doctypes = [
	"Payment Entry",
	"Journal Entry",
	"Purchase Invoice",
	"Sales Invoice",
	"Loan Repayment",
	"Loan Disbursement",
]

accounting_dimension_doctypes = [
	"GL Entry",
	"Payment Ledger Entry",
	"Sales Invoice",
	"Purchase Invoice",
	"Payment Entry",
	"Asset",
	"Stock Entry",
	"Budget",
	"Delivery Note",
	"Sales Invoice Item",
	"Purchase Invoice Item",
	"Purchase Order Item",
	"Journal Entry Account",
	"Material Request Item",
	"Delivery Note Item",
	"Purchase Receipt Item",
	"Stock Entry Detail",
	"Payment Entry Deduction",
	"Sales Taxes and Charges",
	"Purchase Taxes and Charges",
	"Shipping Rule",
	"Landed Cost Item",
	"Asset Value Adjustment",
	"Asset Repair",
	"Asset Capitalization",
	"Loyalty Program",
	"Stock Reconciliation",
	"POS Profile",
	"Opening Invoice Creation Tool",
	"Opening Invoice Creation Tool Item",
	"Subscription",
	"Subscription Plan",
	"POS Invoice",
	"POS Invoice Item",
	"Purchase Order",
	"Purchase Receipt",
	"Sales Order",
	"Subcontracting Order",
	"Subcontracting Order Item",
	"Subcontracting Receipt",
	"Subcontracting Receipt Item",
	"Account Closing Balance",
]

# get matching queries for Bank Reconciliation
get_matching_queries = (
	"creative.accounts.doctype.bank_reconciliation_tool.bank_reconciliation_tool.get_matching_queries"
)

regional_overrides = {
	"France": {
		"creative.tests.test_regional.test_method": "creative.regional.france.utils.test_method"
	},
	"United Arab Emirates": {
		"creative.controllers.taxes_and_totals.update_itemised_tax_data": "creative.regional.united_arab_emirates.utils.update_itemised_tax_data",
		"creative.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries": "creative.regional.united_arab_emirates.utils.make_regional_gl_entries",
	},
	"Saudi Arabia": {
		"creative.controllers.taxes_and_totals.update_itemised_tax_data": "creative.regional.united_arab_emirates.utils.update_itemised_tax_data"
	},
	"Italy": {
		"creative.controllers.taxes_and_totals.update_itemised_tax_data": "creative.regional.italy.utils.update_itemised_tax_data",
		"creative.controllers.accounts_controller.validate_regional": "creative.regional.italy.utils.sales_invoice_validate",
	},
}
user_privacy_documents = [
	{
		"doctype": "Lead",
		"match_field": "email_id",
		"personal_fields": ["phone", "mobile_no", "fax", "website", "lead_name"],
	},
	{
		"doctype": "Opportunity",
		"match_field": "contact_email",
		"personal_fields": ["contact_mobile", "contact_display", "customer_name"],
	},
]

# creative doctypes for Global Search
global_search_doctypes = {
	"Default": [
		{"doctype": "Customer", "index": 0},
		{"doctype": "Supplier", "index": 1},
		{"doctype": "Item", "index": 2},
		{"doctype": "Warehouse", "index": 3},
		{"doctype": "Account", "index": 4},
		{"doctype": "Employee", "index": 5},
		{"doctype": "BOM", "index": 6},
		{"doctype": "Sales Invoice", "index": 7},
		{"doctype": "Sales Order", "index": 8},
		{"doctype": "Quotation", "index": 9},
		{"doctype": "Work Order", "index": 10},
		{"doctype": "Purchase Order", "index": 11},
		{"doctype": "Purchase Receipt", "index": 12},
		{"doctype": "Purchase Invoice", "index": 13},
		{"doctype": "Delivery Note", "index": 14},
		{"doctype": "Stock Entry", "index": 15},
		{"doctype": "Material Request", "index": 16},
		{"doctype": "Delivery Trip", "index": 17},
		{"doctype": "Pick List", "index": 18},
		{"doctype": "Payment Entry", "index": 22},
		{"doctype": "Lead", "index": 23},
		{"doctype": "Opportunity", "index": 24},
		{"doctype": "Item Price", "index": 25},
		{"doctype": "Purchase Taxes and Charges Template", "index": 26},
		{"doctype": "Sales Taxes and Charges", "index": 27},
		{"doctype": "Asset", "index": 28},
		{"doctype": "Project", "index": 29},
		{"doctype": "Task", "index": 30},
		{"doctype": "Timesheet", "index": 31},
		{"doctype": "Issue", "index": 32},
		{"doctype": "Serial No", "index": 33},
		{"doctype": "Batch", "index": 34},
		{"doctype": "Branch", "index": 35},
		{"doctype": "Department", "index": 36},
		{"doctype": "Designation", "index": 38},
		{"doctype": "Loan", "index": 44},
		{"doctype": "Maintenance Schedule", "index": 45},
		{"doctype": "Maintenance Visit", "index": 46},
		{"doctype": "Warranty Claim", "index": 47},
	],
}

additional_timeline_content = {
	"*": ["creative.telephony.doctype.call_log.call_log.get_linked_call_logs"]
}
