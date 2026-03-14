import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",port=3307,password="123456",database="courier_service_system2")
cust1=conn.cursor()
print("welcome to batman courier service")
print("HI")
o=input("press enter to begin your courier surfing")
print("1.create your courier service account")
print("2.login")
choose=int(input("enter (1) for new account or (2) for login"))
if choose==1:
    name=input("enter username")
    password=input("set your password")
    password1=input("confirm password")
    cust1.execute("INSERT INTO login values('"+name+"','"+password+"')")
    conn.commit()
    print("account created")
    move_in=input("press enter to login")
    import B_COURIER_MENU
elif choose==2:
    username=input("enter your username")
    passd=input("enter password")
    cust1.execute('select * from login where user_name="'+username+'"and password="'+passd+'"')
    if cust1.fetchone()is None:
        print("sorry wrong password")
    else:
        import B_COURIER_MENU               
