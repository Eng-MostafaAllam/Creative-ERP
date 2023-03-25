 
from datetime import datetime

import frappe
from frappe.tests.utils import FrappeTestCase

from creative.buying.doctype.purchase_order.purchase_order import make_purchase_receipt
from creative.buying.report.procurement_tracker.procurement_tracker import execute
from creative.stock.doctype.material_request.material_request import make_purchase_order
from creative.stock.doctype.material_request.test_material_request import make_material_request
from creative.stock.doctype.warehouse.test_warehouse import create_warehouse


class TestProcurementTracker(FrappeTestCase):
	pass
