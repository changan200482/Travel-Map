from flask import Flask
import pymysql

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '200482'
app.config['MYSQL_DB'] = 'users'

def get_connection():
    return pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
    )

@app.route('/')
def hello():
    return 'Flask运行中...  请访问 /users 获取用户信息'

@app.route('/users')
def get_users():
    mysql = get_connection()
    try:
        with mysql.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            return {'users': users}
        
    except Exception as e:
        return {'error': str(e)}
    
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )
