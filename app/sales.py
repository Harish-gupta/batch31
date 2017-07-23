print "sales"
def create_customer(id, name, address):
	c= "process the customer"
	return "Customer created successfully done23567.asdasdas"

def sales_process():
	print "sales process"

def sales_invoice():
	print "invoice process"

if __name__ == "__main__":
	print "this is sales file"
	print "name global attribute value:",__name__
	print "creating customer"
	res  =create_customer(1, "cust1", "address1")
	sales_process()
	sales_invoice()
	print "res=",res	