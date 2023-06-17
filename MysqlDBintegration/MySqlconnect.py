import pymysql

# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# sqlquery = "insert into t1 values(%s,%s,%s)"
# val=(7,'Manju','24')
# con.execute(sqlquery,val)
# db.commit()
# print('Inserted')

#take input from keyboard
#id=int(input("Enter id"))
# name=input("Enter the name");
# age=int(input("Enter age"))

# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# sqlquery = "insert into t1 values(%s,%s,%s)"
# val=(id,name,age)
# con.execute(sqlquery,val)
# db.commit()
# print('Inserted')

#Delete Query
# id=int(input("Enter id"))
#
# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# delQuery="delete from t1 where id='%d'"%(id)
# con.execute(delQuery)
# db.commit()
# print('Deleted')



# #Update Query
# y=input("Do you want to update?")
# if(y == 'yes'):
#     id=int(input("Enter id"))
#     name=input("Enter the name");
#     age=int(input("Enter age"))
#     db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
#     con=db.cursor()
#     sqlquery = "update t1 set name='%s',Age='%d' where id='%d'" %(name,age,id)
#     con.execute(sqlquery)
#     db.commit()
#     print('Updated')
#
# else:
#     if y == 'no':
#         print('Exit')


#Select Query

# id=int(input("Enter id"))
#
# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# sqlquery = "select * from t1 where id=%d"%(id)
# con.execute(sqlquery)
# i=con.fetchone()
# id=i[0]
# na=i[1]
# age=i[2]
#
# print(f'id= {id}, name= {na} , age={age}')

#Select Query all records


# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# sqlquery = "select * from t1 "
# con.execute(sqlquery)
# data=con.fetchall()
# for i in data:
#     id=i[0]
#     na=i[1]
#     age=i[2]
#     print(f'id= {id}, name= {na} , age={age}')



