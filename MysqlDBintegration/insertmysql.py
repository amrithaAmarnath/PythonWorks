# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="Am@6nTh245",database="november")
# con=db.cursor()
# sqlquery = "insert into t1 values(%s,%s,%s)"
# val=(11,'Manju','30')
# con.execute(sqlquery,val)
# db.commit()
# print('Inserted')


import pymysql
connection=pymysql.connect(host='localhost',user='root',password='Am@6nTh245',database='november')
cursor=connection.cursor()
select_query='select * from t1'
cursor.execute(select_query)
records=cursor.fetchall()
print('records',records)

print(f'id  Name{" "*4}  Age')
for i in records:
    id=i[0]
    na=i[1]
    ag=i[2]
    print(f'{id}   {na}{" "*5}  {ag}')

