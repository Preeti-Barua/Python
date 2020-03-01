import sqlite3


connection=sqlite3.connect("connect.db")
cursor=connection.cursor()
cursor.execute("drop table if exists Emp")
sql_command="""create table Emp(Emp_id INT , fname varchar(20),lname varchar(20));"""
cursor.execute(sql_command)
staff_data=[(101,"preeti","abc"),(102,"shruti","xyz")]
for p in staff_data:
    format_str="""Insert into Emp(Emp_id,fname,lname)values("{id}","{first}","{last}");"""
    
    sql_command=format_str.format(id=p[0],first=p[1],last=p[2])
    cursor.execute(sql_command)
cursor.execute("select *from emp")        
myresult=cursor.fetchall()
for x in myresult:
    print (x)
connection.close()
        
