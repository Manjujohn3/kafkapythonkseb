import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'ksebdb')
mycursor = mydb.cursor()
while True:
    
    print("Select an option")
    print("1 Add consumer")
    print("2 search consumer")
    print("3 delete consumer")
    print("4 update consumer")
    print("5 view all consumer")
    print("6 Generate bill")
    print("7 view bill")
    print("8 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("add consumer selected")
        consumerid= input("enter the id:")
        name = input("enter the name:")
        address = input("enter the address:")
        phone = input("enter the number:")
        emailid = input("enter the email:")
        sql = 'INSERT INTO `consumer`(`consumerid`, `name`, `address`, `phone`, `email`) VALUES (%s,%s,%s,%s,%s)'
        data = (consumerid,name,address,phone,emailid)
        mycursor.execute(sql,data)
        mydb.commit()
        print("value inserted succesfully") 
   
    elif(choice==2):
        print("search consumer selected")

    elif(choice==3):
        print("delete consumer selected")
    
    elif(choice==4):
        print("update consumer selected")

    elif(choice==5):
        print("view all consumer selected")

    elif(choice==6):
        print("generate bill selected")

    elif(choice==7):
        print("view billselected")
    
    elif(choice==8):
        break


    

