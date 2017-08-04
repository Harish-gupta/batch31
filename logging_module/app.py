import logging
import pur
logging.basicConfig(filename="log1.txt", level=logging.DEBUG, format="%(asctime)s->%(levelname)s->%(message)s")
pur.create_customer(1,"name2")
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
logging.debug("a=%s, b=%s"%(a,b))
if not a.isdigit() or not b.isdigit():
	logging.warn("Excpecting digits only but Got: %s, %s"%(a,b))
try:
	a=float(a)
	b=float(b)
	res=a/b
	logging.debug("result=%s",res)
except Exception as err:
	logging.exception("%s"%err)