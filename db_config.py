from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'letter'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['SECRET_KEY'] = 'Th1s1sTh3Sup3rS3cr3tK3y'
app.config['SECRET_KEY'] = '1234'
mysql.init_app(app)
