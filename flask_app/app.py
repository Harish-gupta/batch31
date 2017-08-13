from flask import Flask, render_template, request
import json
from db_operations import get_data, create
app = Flask(__name__)

@app.route("/", methods=['GET','POST','PUT'])
def home():
	#return "<h1>This is my first flask url</h1>"
	'''
	f=open("home.html")
	data=f.read()
	return data
	'''
	status = ""
	msg=""
	if request.method=="POST":
		book_id = request.form.get('id')
		book_name = request.form.get('name')
		status, msg = create(book_id, book_name)
	if request.method=="PUT":
		pass

	return render_template('home.html',status=status, msg=msg)



@app.route("/books")
def user():
	#users=['user1','user2','user3']
	return json.dumps(get_data())


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0",)