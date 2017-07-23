print "pur"
def create_supplier(id, name, address):
	c= "process the supplier"
	return "supplier created successfully."

def pur_process():
	print "sales process"

def pur_invoice():
	print "invoice process"

if __name__ == "__main__":
	print "this is purchase file"
	print "name global attribute value:",__name__
	print "creating supplier"
	res  =create_supplier(1, "cust1", "address1")
	pur_process()
	pur_invoice()
	print "res=",res