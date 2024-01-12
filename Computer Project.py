def database():
    try:
        import mysql.connector
        db=mysql.connector.connect(
            user="root",
            host="localhost",
            passwd=sqlpassword)
        mycursor=db.cursor()
        mycursor.execute("create database dpsmis")
    except:
        print("database already exists")
def table():
    try:
        import mysql.connector
        db=mysql.connector.connect(
            user="root",
            host="localhost",
            passwd=sqlpassword,
            database="dpsmis")
        mycursor=db.cursor()
        mycursor.execute("create table account(account varchar(30),username varchar(30),password varchar(30),gender char(1))")
    except:
        print("table already exists")
def create():
    database()
    table()

def acc():
    account=input("enter mails, only gmail.com and yahoo.com accepted:")
    if account[-10:]=="@gmail.com" or account[-10:]=="@yahoo.com":
        return account
    else:
        print("re-enter account")
        acc()



def user():
    username=input("enter username,only letters and number allowed:")
    if username.isalnum():
        return username
    else:
        print("password should contain only letters and numbers")
        user()

def passwd():
    password=input("enter password:")
    if len(password)>=8:
        passwordconfirm=input("re-enter your password:")
        if passwordconfirm==password:
            return password
        else:
            print("password isnt the same")
            passwd()
        
    else:
        print("password must be minimum 8 characters long")
        passwd()

def gndr():
    gender=input("enter M for male,F for female,O for other:").upper()
    if gender=="M" or gender=="O" or gender=="F":
        return gender
    else:
        print("invalid input")
        gndr()
       
def register():
    account=acc()
    username=user()
    password=passwd()
    gender=gndr()
    import mysql.connector
    db=mysql.connector.connect(
        user="root",
        host="localhost",
        passwd=sqlpassword,
        database="dpsmis")
    mycursor=db.cursor()
    mycursor.execute("insert into account values('{}','{}','{}','{}')".format(account,username,password,gender))
    db.commit()
    print("account successfully created")

def login():
    import mysql.connector
    db=mysql.connector.connect(
        user="root",
        host="localhost",
        passwd=sqlpassword,
        database="dpsmis")
    mycursor=db.cursor()
    mycursor.execute("select * from account")
    records=mycursor.fetchall()
    C=input("enter username or account:")
    for i in records:
        if C[-10:]=="@gmail.com" or C[-10:]=="@yahoo.com":
            if i[0]==C:
                print("enter password next:")
                passwordentry=input("enter password:")
                for i in records:
                    if i[0]==C or i[1]==C:
                        if i[2]==passwordentry:
                            print("you've successfully logged in")
                        else:
                            print("password is wrong")
                            login()                       
    
        elif i[1]==C:
            print("enter password next")
            passwordentry=input("enter password")
            for i in records:
                if i[0]==C or i[1]==C:
                    if i[2]==passwordentry:
                        print("you've successfully logged in")
                    else:
                        print("password is wrong")
                        login()
        else:   
            print("account or username does not exist")

def update():
    import mysql.connector
    db=mysql.connector.connect(
        user="root",
        host="localhost",
        passwd=sqlpassword,
        database="dpsmis")
    mycursor=db.cursor()
    mycursor.execute("select * from account")
    records=mycursor.fetchall()
    print("1 for changing account")
    print("2 for changing username")
    print("3 for changing password")
    choice=int(input("enter your choice:"))
    if choice==1:
        account=input("enter account to be updated:")
        updateaccount=acc()
        for i in records:
            while account==i[0]:
                password=input("enter password to make sure its you:")
                if password==i[2]:
                    mycursor.execute("update account set account='{}' where account='{}'".format(updateaccount,account))
                    db.commit()
                else:
                    print("invalid password try again")
                account=1
    if choice==2:
        account=input("enter account of which username is to be changed:")
        updateusername=user()
        for i in records:
            while account==i[0]:
                password=input("enter password to make sure its you:")
                if password==i[2]:
                    mycursor.execute("update account set username='{}' where account='{}'".format(updateusername,account))
                    db.commit()
                else:
                    print("invalid password try again")
                    update()
                account=1
    if choice==3:
        account=input("enter account of which password is to be changed:")
        updatepassword=passwd()
        for i in records:
            while account==i[0]:
                password=input("enter password to make sure its you:")
                if password==i[2]:
                    mycursor.execute("update account set password='{}' where account='{}'".format(updatepassword,account))
                    db.commit()
                else:
                    print("invalid password try again")
                    passwd()
                account=1


def delacc():
    deleteaccount=input("enter mail to be deleted:")
    password=input("enter password to make sure its you:")
    import mysql.connector
    db=mysql.connector.connect(
        user="root",
        host="localhost",
        passwd=sqlpassword,
        database="dpsmis")
    mycursor=db.cursor()
    mycursor.execute("select * from account")
    records=mycursor.fetchall()
    for i in records:
        while deleteaccount==i[0]:
            if password==i[2]:
                mycursor.execute("delete from account where account='{}'".format(deleteaccount))
                db.commit()
            else:
                print("invalid account try again")
                delacc()
            account=1
global sqlpassword
sqlpassword=input("enter password of your mysql:")
a=0
while a==0:
    print("1 for creating database and table (NECESSARY TO DO FIRST)")
    print("2 for regstering")
    print("3 for login")
    print("4 for updating details")
    print("5 for deleting account")
    print("6 for signing out")
    Ch=int(input("enter option:"))
    if Ch==1:
        create()
    elif Ch==2:
        register()
    elif Ch==3:
        login()
    elif Ch==4:
        update()
    elif Ch==5:
        delacc()
    elif Ch==6:
        exit()
    else:
        print("invalid choice")
    continuation=input("do you want to continue,y for yes and n for no:").upper()
    if continuation=="Y":
        a=0
    elif continuation=="N":
        a=1
    else:
        print("invalid input")
