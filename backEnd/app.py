from flask import Flask
from flask import request
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
            cursor.execute('SELECT * FROM Users')
            users = cursor.fetchall()
            return {'users': users}
        
    except Exception as e:
        return {'error': str(e)}
    
    finally:
        cursor.close()

@app.route('/login', methods=['POST', 'GET'])
def login():
    result = ''
    mysql = get_connection()

    if request.method == 'POST':
        data = request.get_json()
        email = data.get('acount')
        password = data.get('password')
        print(email, password)
        try:
            with mysql.cursor() as cursor:
                cursor.execute('SELECT UserPassword,Username FROM Users WHERE UserEmail = %s', (email))
                selectResult = cursor.fetchone()
                if selectResult:
                    if selectResult[0] == password:
                        result = selectResult[1]
                    else:
                        result = 'loginfail'
                else:
                    result = 'notfound'

                print(selectResult,result)
        except Exception as e:
            return {'error': str(e)}
        finally:
            cursor.close()
        
        return result

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )
