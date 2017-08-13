import sqlite3
def get_con():
	con=sqlite3.connect('db1.db')
	cur = con.cursor()
	return con,cur
def con_close(con,cur):
	cur.close()
	con.close()

def get_data():
	try:
		con,cur=get_con()
		cur.execute("select * from books")
		data = cur.fetchall()
	except Exception as err:
		return err
	finally:
		con_close(con,cur)
	return data
def create(b_id, name):
	try:
		q="insert into books values(%s, '%s')"%(b_id, name)
		con,cur=get_con()
		cur.execute(q)
		con.commit()
		return True, "record inserted successfully!"
	except Exception as err:
		return False, err
	finally:
		con_close(con,cur)