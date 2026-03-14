import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",port=3307,password="123456",database="courier_service_system2")
cust1=conn.cursor()
for i in range(0,76):
    print("welcome to batman courier service")
    print("1.courier_order and customer_details")
    print("2.billing_procedure")
    print("3.courier_service_boys")
    print("4.exit")
    choice=int(input("enter the section you want to access (1,2,3 or 4)"))
    if choice==1:
        print("A.courier placement")
        print("B.courier order list")
        sect=str(input("enter  the section that you want to access"))
        if sect=="A":
            print("COURIER ORDER")
            a=(input("enter customer name"))
            b=int(input("enter  customer mobile no"))
            c=(input("enter customer address"))
            d=(input("enter receiver name"))
            e=int(input("enter receiver mobile number"))
            f=(input("enter receiver address"))
            cust1.execute("INSERT INTO couriers VALUES('"+a+"','"+str(b)+"','"+c+"','"+d+"','"+str(e)+"','"+f+"')")
            conn.commit()
            print(cust1.rowcount,'courier(s) placed')
            print('===================================================================================================================================================')
        elif sect=="B":
             S=str(input("do you want to see your courier orders(yes...\..no)"))
             if S=="yes":
                 a=input("enter customer mobile number")
                 cust1.execute('select * from couriers where customer_mobile_number="{}"'.format(a))
                 order=cust1.fetchall()
                 print('customer name,','custome mob no,','customer address,','receiver name,','receiver mob no,','receiver address,') 
                 for j in order:
                     print(j)
                 print("====================================================================================================================================================")
             else:
                     print("thank you")
                     print("===================================================================================================================================================")
    elif choice==2:
        
       
        wt=input("Enter weight in Kg")
        cust1.execute("select * from couriers2 where weight_in_kgs='{}'".format(wt))
        
        bill=cust1.fetchall()
        print("Billing procedure:[weight_in_kgs.......and.......cost_in_rupees]")
        for x in bill:
            print(x)
        print("=========================================================================================================================================================")
    if choice==3:
        city1=input("enter your city name")
        cust1.execute("select * from couriers3 where city='{}'".format(city1))
        boys=cust1.fetchall()
        print('City       courier_boy          mobile no')
        for y in boys:
            print(y)
        print("============================================================================================================================================================")
    elif choice==4:
        quit()
                           
