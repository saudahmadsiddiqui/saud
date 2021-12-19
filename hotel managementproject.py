import sqlite3
conn=sqlite3.connect('hotel.db')
#conn.execute("create table hotel(name text,id int,city text,roomNO int);")
print("table created")

print("________customer Details");
print("enter name")
nam=input();
print("enter city");
city=input();
print("enter id");
id=int(input());
print("select your roomNO");
print("1.101 \n 2.102 \n 3.103 \n 4.104")
select=int(input());
if (select==1):
           print("your room no is ...101")
elif (select==2):
           print("your room no is ...102")
elif (select==3):
           print("your room no is ...103")
elif (select==4):
           print("your room no is ...104");
else:
    
    print("Room is not available")

conn.execute("""insert into hotel(name,id,city,roomNo) values(?,?,?,?)""",(nam,id,city,select));
print("data inserted");
data = conn.execute("select * from hotel");

for row in data:
    print("Name = ",row[0])
    print("id = ",row[1])
    print("city = ",row[2])
    print("roomNo = ",row[3])
conn.close();
