import app
a=10
b=20
act=app.add(a,b)
exp=300
if act!=exp:
	print a,b,"test vase failed"
a="str1"
b="str2"

act=app.add(a,b)
exp="str1str2"
if act!=exp:
	print a,b,"test vase failed"
a=[1,2,3]
b=[4,5,6]
act=app.add(a,b)
exp=[1,2,3,4,5,6]
if act!=exp:
	print a,b,"test vase failed"
a=10
b="str1"
act=app.add(a,b)
exp=None
if act!=exp:
	print a,b,"test vase failed"
