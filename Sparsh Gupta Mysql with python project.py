import mysql.connector as sqlc
import time
import datetime

while True:
    
    try:
        
        co=sqlc.connect(host="localhost",user="root",password="123456",charset='utf8')
        if co.is_connected():
           print("Connected.....")
           print()
           break

    except:

           print("*****WRONG PASSWORD*****")

print("connection ok ",co.is_connected())


Curobj=co.cursor()
now = datetime.datetime.now()


def codatabase():
    
    try:
        Curobj.execute("create database if not exists sportscomplex")
        Curobj.execute("use sportscomplex")
        Curobj.execute("create table if not exists items(INO int primary key , INAME char(50) not null , IQUANTITY int not null , IBRAND char(50) not null , IPRICE int not null);")


    except:
        print()
        print("**** NO DATABASE EXIST ****")

    

def landingpage():
    
    try:
        
        while True:

            print()
            print("_"*80)
            print("""
                             ***SPARSH SPORTS COMPLEX***                     {}
         
    0)EXIT
    1)LOGIN 
    2)VIEW ALL ITEMS
    3)SEARCH ITEMS
    
    """.format(now.strftime('%d-%m-%Y %H:%M')))
            
            
            val = intinput("CHOOSE THE TASK : ")
            if val == 0:
                print("THANKS FOR VISITING...")
                break
            elif val == 1:
                loginpage()
            elif val == 2:
                viewpage()
            elif val == 3:
                searchpage()
            else:
                print()
                print("PLEASE ENTER CORRECT TASK !! ")
                
    except:
       print()
       print(" SOMETHING WENT WRONG !!!")
       print(" TRY AGAIN ")

       

def loginpage():
    
    try:
        
        print()
        usern=input("ENTER USERNAME-")
        print()
        paws=input("ENTER PASSWORD-")
        if usern.lower()=="user" and paws.lower() == "sportscomplex":
            print()
            print("LOADING",end="")
            for _ in range(3):
                print(".",end="")
                time.sleep(0.5)
            print()
            print("LOGGED IN TO SYSTEM ---")
            print()
            while True:
                global now
                now = datetime.datetime.now()
                print("_"*75)
                print("""
                                   WELCOME TO COMPLEX                         {}
    0)EXIT
    1)ADD ITEMS
    2)SORT ITEMS
    3)UPDATE ITEMS
    4)DELETE ITEMS
    
    """.format(now.strftime('%d-%m-%Y %H:%M')))
                
                print()
                val=intinput("CHOOSE THE TASK : ")
                if val == 0:
                       return
                elif val == 1:
                    print()
                    addrecord()
                elif val == 2:
                    print()
                    sortingpage()
                elif val == 3:
                    print()
                    update()
                elif val == 4:
                    print()
                    delete()
                else:
                    print()
                    print("PLEASE ENTER CORRECT TASK !! ")    
            
        else:
            print()
            print("INCORRECT USERNAME OR PASSWORD!!!")
            print("TRY AGAIN..")
            loginpage()
            
    except:
        print()
        print(" SOMETHING WENT WRONG !!!")
        print(" TRY AGAIN ")

        

def viewpage():
    
    try:
        
        while True:
             global now
             now = datetime.datetime.now()
             print()
             print("_"*75)
             print("""
                                       VIEW ITEMS                         {}
    0)EXIT
    1)VIEW ALL ITEMS
    2)VIEW ITEMS BY NAME

    """.format(now.strftime('%d-%m-%Y %H:%M')))
             
             print()
             val=intinput("CHOOSE THE TASK : ")
             if val == 0:
                return
             elif val == 1:
                viewrecord()
             elif val == 2:
                viewbyname()
             else:
                 print()
                 print("PLEASE ENTER CORRECT TASK !! ")


    except:
         print()
         print(" SOMETHING WENT WRONG !!!")
         print(" TRY AGAIN ")

        
def searchpage():
    
    try:
    
        while True:
            global now
            now = datetime.datetime.now()
            print()
            print("_"*75)
            print("""
                                       SEARCH ITEMS                         {}
    0)EXIT
    1)SEARCH BY ITEM NUMBER
    2)SEARCH BY ITEM NAME
    3)SEARCH BY ITEM QUANTITY
    4)SEARCH BY ITEM BRAND
    5)SEARCH BY ITEM PRICE
    
    """.format(now.strftime('%d-%m-%Y %H:%M')))
            
            print()
            val=intinput("CHOOSE THE TASK : ")
            if val == 0:
                return
            elif val == 1:
                number = intinput("ENTER THE ITEM NUMBER YOU WANT TO SEARCH:")
                searchbyitem_no(number)
            
            elif val == 2:
                name=input("ENTER THE ITEM NAME YOU WANT TO SEARCH:")
                searchbyname(name)
            
            elif val == 3:
                lowerv=intinput("ENTER THE LOWER VALUE QUANTITY YOU WANT TO SEARCH:")
                upperv=intinput("ENTER THE UPPER VALUE QUANTITY YOU WANT TO SEARCH:")
                searchbyquantity(lowerv,upperv)
            
            elif val == 4:
                brand=input("ENTER THE ITEM BRAND YOU WANT TO SEARCH:")
                searchbybrand(brand)
            
            elif val == 5:
                lowerv=intinput("ENTER THE LOWER VALUE PRICE YOU WANT TO SEARCH:")
                upperv=intinput("ENTER THE UPPER VALUE PRICE YOU WANT TO SEARCH:")
                searchbyprice(lowerv,upperv)

            else:
                 print()
                 print("PLEASE ENTER CORRECT TASK !! ")

                 
    except:
         print()
         print(" SOMETHING WENT WRONG !!!")
         print(" TRY AGAIN ")

         
def sortingpage():
    
    try:
        
        while True:
            global now
            now = datetime.datetime.now()
            print()
            print("_"*75)
            print("""
                                        SORT ITEMS                         {}
    0)EXIT
    1)SORT BY ITEM NAME
    2)SORT BY ITEM QUANTITY
    3)SORT BY ITEM BRAND
    4)SORT BY ITEM PRICE
    
    """.format(now.strftime('%d-%m-%Y %H:%M')))
            
            print()
            val=intinput("CHOOSE THE TASK : ")
            if val == 0:
                return
            elif val == 1:
                sortbyname()
            elif val == 2:
                sortbyquantity()
            elif val == 3:
                sortbybrand()
            elif val == 4:
                sortbyprice()
            else:
                print()
                print("PLEASE ENTER CORRECT TASK !! ")
                 
    except:
          print()
          print(" SOMETHING WENT WRONG !!!")
          print(" TRY AGAIN ")        
                 

def intinput(statement):
    
    while True:
        
        try:
            x=int(input(statement))
            return x   
            
        except:
            print()
            print("****Integer Value Required****")
            print()

    
def addstatics():

    try:

        Curobj.execute("Insert into items values (1,'BAT',10,'SS',2000)")
        Curobj.execute("Insert into items values (2,'BAT',20,'SGG',1000)")
        Curobj.execute("Insert into items values (3,'BAT',30,'TON',200)")
        Curobj.execute("Insert into items values (4,'BAT',40,'NB',4000)")
        Curobj.execute("Insert into items values (5,'BALL',50,'COSCO',20)")
        Curobj.execute("Insert into items values (6,'BALL',100,'VICKY',60)")
        Curobj.execute("Insert into items values (7,'SHOES',70,'JORDON',6000)")
        Curobj.execute("Insert into items values (8,'SHOES',20,'BATA',2000)")
        Curobj.execute("Insert into items values (9,'FOOTBALL',90,'ADDIDAS',500)")
        Curobj.execute("Insert into items values (10,'FOOTBALL',40,'NIKI',200)")
        Curobj.execute("Insert into items values (11,'SHIRTS',50,'VAN HUSEN',2000)")
        Curobj.execute("Insert into items values (12,'BADMINTON',90,'YONEX',2000)")
        Curobj.execute("Insert into items values (13,'BADMINTON',100,'COSCO',400)")
        Curobj.execute("Insert into items values (14,'BADMINTON',50,'POWER',200)")
        Curobj.execute("Insert into items values (15,'CRICKET GLOVES',100,'SS',150)")
        Curobj.execute("Insert into items values (16,'CRICKET PADS',120,'SG',2000)")
        Curobj.execute("Insert into items values (17,'PUMP',90,'YONEX',200)")
        Curobj.execute("Insert into items values (18,'SOCKS',40,'ADDIDAS',300)")
        Curobj.execute("Insert into items values (19,'GOLF STICK',90,'COSCO',2000)")
        Curobj.execute("Insert into items values (20,'GOLF KIT',90,'YONEX',10000)")

        Curobj.execute("commit")

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")
    


def addrecord():
    
    try:
        print("ADD PRODUCT".center(70,'*'))
        print()
        INO=countrecords()+ 1
        print()
        INAME=input("ENTER ITEM NAME TO ADD :")
        print()
        IQUAN=intinput("ENTER ITEM QUANTITY TO ADD :")
        print()
        IBRAND=input("ENTER ITEM BRAND TO ADD :")
        print()
        IPRICE=intinput("ENTER ITEM PRICE TO ADD :")
        print()
        RECORDS=(INO,INAME,IQUAN,IBRAND,IPRICE)
        
        while True:
            
            confirm=input("ENTER CONFIRMATION Y / N :")
            
            if confirm.lower() == "y":
               print()
               Curobj.execute("Insert into items values {}".format(RECORDS))
               Curobj.execute("commit")
               print()
               print("ITEM ADDED.... ")
               print()
               return
    
            elif confirm.lower() == "n":
                 print()
                 print("NO ITEM ADDED !!")
                 print()
                 return      

            else:
                 print()
                 print("PLEASE ENTER CORRECT VALUE ")
                 print()
             

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")



def viewrecord():
    
    try:
        
       print("ALL ITEMS IN COMPLEX---- ")
       print()
       Curobj.execute("desc items")
       recs=Curobj.fetchall()
       print(recs[0][0].ljust(7),recs[1][0].ljust(20),recs[2][0].ljust(15),recs[3][0].ljust(20),recs[4][0].ljust(10),sep="")
       Curobj.execute("select * from items")
       recs=Curobj.fetchall()
       for w in recs:
           print(str(w[0]).ljust(7),w[1].ljust(20),str(w[2]).ljust(15),w[3].ljust(20),str(w[4]).ljust(10),sep="")
       

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")

        

def viewbyname():
    
    try:
        
        Curobj.execute("select INAME , count(*) from items group by INAME")
        recs=Curobj.fetchall()
        for w in recs:
            print(w[0])
            
    except:
         print()
         print("SOMETHING WENT WRONG !!!")
         print("TRY AGAIN ")
         

def isitemexist(number):
    try:
        Curobj.execute("select * from items where INO = {}".format(number))
        recs = Curobj.fetchall()
        if len(recs) == 0:
            return False
        return True

    except:
        print()
        print("SOMETHING WENT WRONG!!")
        print("TRY AGAIN")

        
def searchbyitem_no(number):
    
    try:
        
        print()
        Curobj.execute("select * from items where INO={}".format(number))
        recs=Curobj.fetchall()
        if len(recs) == 0:
            print("RECORD DOES NOT EXIST!!")
            return
        table(recs)

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")



def searchbyname(name):

    try:
        
        print()
        Curobj.execute("select * from items where INAME='{}'".format(name))
        recs=Curobj.fetchall()
        if len(recs) == 0:
            print("RECORD DOES NOT EXIST!!")
            return
        table(recs)

    except:
           print()
           print("SOMETHING WENT WRONG !!!")
           print("TRY AGAIN ")

    

def searchbyquantity(lowerv,upperv):

    try:
        
        print()    
        Curobj.execute("select * from items where IQUANTITY  between '{}' and '{}'".format(lowerv,upperv))
        recs=Curobj.fetchall()
        if len(recs) == 0:
            print("RECORD DOES NOT EXIST!!")
            return
        table(recs)

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")


    
    
def searchbybrand(brand):

    try:
        
        print()
        Curobj.execute("select * from items where IBRAND='{}'".format(brand))
        recs=Curobj.fetchall()
        if len(recs) == 0:
            print("RECORD DOES NOT EXIST!!")
            return
        table(recs)

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")    


    
def searchbyprice(lowerv,upperv):

    try:
        
        print()
        Curobj.execute("select * from items where IPRICE between '{}' and '{}'".format(lowerv,upperv))
        recs=Curobj.fetchall()
        if len(recs) == 0:
            print("RECORD DOES NOT EXIST!!")
            return
        table(recs)

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")


def sortbyname():

    try:
        
        print()
        print("SORT BY ITEM NAME -")
        print()
        Curobj.execute("select * from items order by INAME asc")
        recs=Curobj.fetchall()
        table(recs)

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")    
    

def sortbybrand():

    try:
        
        print()
        print("SORT BY ITEM BRAND -")
        print()
        Curobj.execute("select * from items order by IBRAND asc")
        recs=Curobj.fetchall()
        table(recs)
        
    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")

          

def sortbyquantity():
    
    try:
        
        print()
        print("SORT BY ITEM QUANTITY -")
        x=input("SORT BY ASC/DESC TYPE A/D -")
        if x.lower() == "a":
               Curobj.execute("select * from items order by IQUANTITY asc")
               recs=Curobj.fetchall()
               print()
               table(recs)


        elif x.lower() == "d":
               Curobj.execute("select * from items order by IQUANTITY desc")
               recs=Curobj.fetchall()
               print()
               table(recs)
              
    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")
          

def sortbyprice():

    try:
        
        print()
        print("SORT BY ITEM PRICE -")
        x=input("SORT BY ASC/DESC TYPE A/D -")
        if x.lower() == "a":
           Curobj.execute("select * from items order by IPRICE asc")
           recs=Curobj.fetchall()
           print()
           table(recs)


        elif x.lower() == "d":
             Curobj.execute("select * from items order by IPRICE desc")
             recs=Curobj.fetchall()
             print()
             table(recs)

             
    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")

          

def update():

    try:
        print("UPDATE PRODUCT".center(70,'*'))
        print()
        print()
        viewrecord()
        print()
        ID=intinput("ENTER ITEM NUMBER TO UPDATE -")
        if not isitemexist(ID):
            print()
            print("WRONG ID ENTERED / ID DOES NOT EXIST")
            print()
            return 
        print()
        name=input("ENTER ITEM NAME TO UPDATE -")
        print()
        quantity=intinput("ENTER ITEM QUANTITY TO UPDATE -")
        print()
        brand=input("ENTER ITEM BRAND TO UPDATE -")
        print()
        price=intinput("ENTER ITEM PRICE TO UPDATE -")
        print()
        
        while True:
            
            confirm=input("ENTER CONFIRMATION Y / N : ")
            if confirm.lower() == "y":
                print()
                Curobj.execute("update items set INAME='{}',IQUANTITY={}, IBRAND='{}',IPRICE={} where INO = {}".format(name,quantity,brand,price,ID))
                Curobj.execute("commit")
                print()
                searchbyitem_no(ID)
                print()
                print("ITEM UPDATED.... ")
                print()                    
                return
    
            elif confirm.lower() == "n":
                 print()
                 print("NO ITEM UPDATED !!")
                 print()
                 return      

            else:
                 print()
                 print("PLEASE ENTER CORRECT VALUE ")
                 print()

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")    
    

def delete():
    
    try:
         print("DELETE PRODUCT".center(70,'*'))
         print()
         print()
         viewrecord()
         print()
         ID=intinput("ENTER ITEM NUMBER TO DELETE -")
         if not isitemexist(ID):
            print()
            print("WRONG ID ENTERED / ID DOES NOT EXIST")
            print()
            return 
         print()
         
         while True:
            
            confirm=input("ENTER CONFIRMATION Y / N : ")
            if confirm.lower() == "y":
               print()
               if isitemexist(ID):
                   Curobj.execute("delete from items where INO = {}".format(ID))
                   Curobj.execute("commit")
                   print()
                   print("ITEM IS DELETED....")
                   print()
               else:
                    print()
                    print("WRONG ID ENTERED / ID DOES NOT EXIST")
                    print()
                    
               return
    
            elif confirm.lower() == "n":
                 print()
                 print("NO ITEM DELETED !!")
                 print()
                 return      

            else:
                 print()
                 print("PLEASE ENTER CORRECT VALUE ")
                 print()

    
    except:
            print()
            print("SOMETHING WENT WRONG !!!")
            print("TRY AGAIN ")




def countrecords():

    try:
        
        Curobj.execute("select max(INO) from items")
        recs=Curobj.fetchone()
        print()
        return recs[0]

    except:
        print()
        print("NO RECORD EXIST !!! ")
        print()



def table(recs):

    try:
        
        Curobj.execute("desc items")
        record=Curobj.fetchall()
        print(record[0][0].ljust(7),record[1][0].ljust(20),record[2][0].ljust(15),record[3][0].ljust(20),record[4][0].ljust(10),sep="")
        print()
        
        for w in recs:
            print(str(w[0]).ljust(7),w[1].ljust(20),str(w[2]).ljust(15),w[3].ljust(20),str(w[4]).ljust(10),sep="")

    except:
          print()
          print("SOMETHING WENT WRONG !!!")
          print("TRY AGAIN ")
    


        
def main():
    
    try:
        codatabase()
        landingpage()

    except:
         print("NO FUNCTION CALLED")


main()

