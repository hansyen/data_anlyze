import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# rs = redis.StrictRedis(host='redis', port=6379, charset='utf-8', db=0, decode_responses=True)

# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

dbname = 'ohya'

def drop_db():
	try:
		db.engine.execute(f'DROP DATABASE {dbname}')
		print(f'=== drop {dbname} DB complete ===')
	except:
		print('db connection fail')
		pass

def create_db():
	try:
		db.engine.execute(f'CREATE DATABASE {dbname} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
		print(f'=== Create {dbname} DB success. ===')
	except:
		pass

	print('=== Start Migrate DB ===')
	os.system("rm -r /app/database/migrations")
	os.system("python3.6 /app/database/sql_creater.py db init")
	os.system("python3.6 /app/database/sql_creater.py db migrate")
	os.system("python3.6 /app/database/sql_creater.py db upgrade")
	print('=== Migrate DB complete ===')

# def reset_redis():
# 	rs.flushdb()

if __name__ == '__main__':
	drop_db()
	create_db()
	# reset_redis()