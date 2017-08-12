import unittest
from app import add
class testcases(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "loginto the machine"
		cls.user_inst =  "instance belongs to use"
	def setUp(self):
		print "pre configuraion"
	def tearDown(self):
		print "remove preconfiguration."
	def test_110_20(self):
		print "test1"
		print self.user_inst
		a=10
		b=20
		act=add(a,b)
		exp=30
		self.assertEqual(act, exp, "%s,%s test failed"%(a,b))
	def test_2str1_str2(self):
		print "test2"
		print self.user_inst
		a="str1"
		b="str2"
		act=add(a,b)
		exp="str1str2"
		self.assertEqual(act, exp, "%s, %s test failed"%(a,b))
	def test_310_str2(self):
		print "test3"
		print self.user_inst
		a="str1"
		b=10
		act=add(a,b)
		exp=None
		self.assertEqual(act, exp, "%s, %s test failed"%(a,b))
	@classmethod
	def tearDownClass(cls):
		print "logout "
		cls.user_inst=None
unittest.main()