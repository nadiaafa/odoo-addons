from odoo.tests.common import TransactionCase

class TestModeTest(TransactionCase):
	
	def setUp(self):
		super(TestModeTest,self).setUp()


	def test_count_function(self): 
		value = self.env['count.count'].count(1,9)
		self.assertEqual(value,10)