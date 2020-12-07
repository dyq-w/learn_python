# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:31:25 2020

@author: 段永强
"""

from flask import Flask, request
import sqlite3

class ClassSys():
    
    #学生信息表
    stu_table = '''

        CREATE TABLE students(id INTEGER, name TEXT, idCard INTEGER, sex TEXT);

    '''
    
    #老师的信息表
    tea_table = '''
        CREATE TABLE teachers(id INTEGER, name TEXT, sex TEXT, course TEXT);
    '''
    
    #职务表
    duty_table = '''

        CREATE TABLE duty(id INTEGER, duty TEXT);

    '''
    
    #打卡表
    stu_class_table = ''' 
        CREATE TABLE stu_class(stu_id INTEGER, day1 TEXT,day2 TEXT, day3 TEXT,day4 TEXT,day5 TEXT);
    '''
    
    #课程表
    course_table = ''' 
        CREATE TABLE course(id INTEGER, day1 TEXT,day2 TEXT, day3 TEXT,day4 TEXT,day5 TEXT);
    '''
    
    #学生职务表
    stu_duty_ship = '''

        CREATE TABLE stu_duty_ship(stu_id INTEGER, duty_id INTEGER);

    '''

    def __init__(self):

        self.conn = sqlite3.connect('classSys.db')

        self.cursor = self.conn.cursor()

    def create_table(self):#初始化数据库

        self.cursor.execute(self.stu_table)
        self.cursor.execute(self.tea_table)
        self.cursor.execute(self.duty_table)
        self.cursor.execute(self.stu_class_table)
        self.cursor.execute(self.course_table)
        self.cursor.execute(self.stu_duty_ship)

        self.conn.commit()

    def create_data(self):

        stu_data = [
            (1, '小红', 1156231333, '女'),
            (2, '小明', 1665465465, '男'),
            (3, '小王', 1895641123, '男'),
            (4, '小花', 1145646213, '女'),
            (5, '小李', 1963156884, '男'),
        ]

        tea_data = [

            (1, '老赵','男','语文'),
            (2, '老孙','女','数学'),
            (3, '老钱','男','英语'),
            (4, '老王','女','生物'),
            (5, '老张','男','物理'),
            (6, '老送','男','化学'),
            (7, '老房','女','体育'),
        ]
        
        stu_class_data =[
            (1,'null','null','null','null','null'),
            (2,'null','null','null','null','null'),
            (3,'null','null','null','null','null'),
            (4,'null','null','null','null','null'),
            (5,'null','null','null','null','null'),
        ]

        duty_data = [

            (1, '班长'),
            (2, '学委'),
            (3, '体委'),
            (4, '学生'),
        ]
        
        course_data = [
            (1, '数学', '化学', '生物', '英语', '数学'),
            (2, '物理', '数学', '英语', '化学', '语文'),
            (3, '语文', '语文', '数学', '英语', '化学'),
            (4, '数学', '体育', '语文', '数学', '生物'),
            (5, '生物', '英语', '物理', '语文', '语文'),
            (6, '语文', '数学', '英语', '物理', '英语'),                
                ]
        
        ship_data = [

            (1, 1),
            (2, 4),
            (3, 2),
            (4, 4),
            (5, 3),

        ]


        self.cursor.executemany('INSERT INTO students VALUES (?,?,?,?)', stu_data)
        self.cursor.executemany('INSERT INTO teachers VALUES (?,?,?,?)', tea_data)
        self.cursor.executemany('INSERT INTO duty VALUES (?,?)', duty_data)
        self.cursor.executemany('INSERT INTO stu_class VALUES (?,?,?,?,?,?)', stu_class_data)
        self.cursor.executemany('INSERT INTO course VALUES (?,?,?,?,?,?)', course_data)
        self.cursor.executemany('INSERT INTO stu_duty_ship VALUES (?,?)', ship_data)

        print('*'*19)

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


app = Flask(__name__)

conn = sqlite3.connect('classSys.db', check_same_thread=False)
cursor = conn.cursor()


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stu_info')

def stu_info():
    
    sql = 'SELECT * FROM students'

    cursor.execute(sql)

    result = cursor.fetchall()

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody': result
    }
    
@app.route('/tea_info')

def tea_info():
    
    sql = 'SELECT * FROM teachers'

    cursor.execute(sql)

    result = cursor.fetchall()

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody': result
    }


@app.route('/duty_id_to_stu_id')
def duty_id_to_stu_id():

    args = request.args

    duty_id = args.get('duty_id')

    if duty_id == None:

        return {
            
            'status': -1,
            'errorCode': 1,
            'errorMsg': '缺少duty_id参数',
            'resultBody': None
            
        }

    cursor.execute('SELECT * FROM  stu_duty_ship WHERE duty_id=?', (duty_id,))

    result = cursor.fetchall()

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody': result
    }


@app.route('/course_to_tea')
def course_to_tea():

    args = request.args

    course = args.get('course')

    if course == None:

        return {
            
            'status': -1,
            'errorCode': 1,
            'errorMsg': '缺少course参数',
            'resultBody': None
            
        }

    cursor.execute('SELECT * FROM teachers WHERE course=?', (course,))

    result = cursor.fetchall()

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody': result
    }

@app.route('/stu_class_com')

def stu_class_com():

    args = request.args

    stu_id = args.get('stu_id')
    
    day = args.get('day')

    if stu_id ==None or day == None:

        return {
            
            'status': -1,
            'errorCode': 1,
            'errorMsg': '缺少stu_id或day参数',
            'resultBody': None
            
        }

    cursor.execute(f'''UPDATE stu_class SET day{day}='yes' WHERE stu_id='{stu_id}' ''')

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody':' 打卡成功!'
    }
    

@app.route('/find_stu_class')
def find_stu_class():

    args = request.args

    stu_id = args.get('stu_id')

    if stu_id == None:

        return {
            
            'status': -1,
            'errorCode': 1,
            'errorMsg': '缺少stu_id参数',
            'resultBody': None
            
        }

    cursor.execute('SELECT * FROM stu_class WHERE stu_id=?', (stu_id,))

    result = cursor.fetchall()

    return {
        'status': 1,
        'errorCode': None,
        'errorMsg': None,
        'resultBody': result
    }
   

if __name__ == '__main__':

    obj = ClassSys()

    obj.create_table()

    obj.create_data()
    
    app.run(debug=True)

   
    
