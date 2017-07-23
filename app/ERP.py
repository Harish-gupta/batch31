'''
import sys
#sys.path.append('/home/tcloudost/Desktop')
sys.path.insert(0, '/home/tcloudost/Desktop')
print sys.path
import sales
import pur
print sales.__file__
print pur.__file__
import sales
import pur
#from sales import create_customer
print "ERP sales process satrted."
print "creatig customer."
#res_cust = create_customer(1, "cust1", "address1")
res_cust = sales.create_customer(1, "cust1", "address1")
print res_cust
print "ERP purchanse process started."
print "creating supplier."
print pur.create_supplier(1, "sup1", "address1")
'''
import data