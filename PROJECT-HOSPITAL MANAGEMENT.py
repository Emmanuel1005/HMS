import mysql.connector as msc
import csv
import random
mdb=msc.connect(host="localhost",user="root",passwd="emmanuel@123")
mc=mdb.cursor()
print("\t\t\tWELCOME TO EVA CLINIC")
mc.execute("create database if not exists hospital")
mc.execute("use hospital")
mc.execute("create table if not exists login(username varchar(20) primary key,password varchar(20))")
print('1.login\n2.sign up')
ch=int(input("Enter choice"))
if ch==1:
    un=input('Enter username:')
    pw=input('Enter password:')
    mc.execute('select * from login where username="%s" and password="%s"',(un,pw))
    eu=mc.fetchall()
    for i in eu:
        if eu[0]==un and pw==eu[1]:
            print('Login sucessful')
        else:
            print('Incorrect username/password. Please try again')
elif ch==2:
    nu=input('Enter new username:')
    npw=input('Enter password:')
    cpw=input('Confirm password:')
    if npw==cpw:
        mc.execute('insert into login values(%s,%s)',(nu,npw))
        mdb.commit()
        print('Login successful')
    else:
        print('Password does not match')
def registration():
    f=open("registration.csv","a",newline='')
    w=csv.writer(f,delimiter=",")
    global id1
    id1=0
    an='y'
    while an=='y':
        nm=input("Enter name of the patient:")
        ip=input("Enter name of the insurance provider:")
        mn=int(input("Enter mobile number(eg:05XXXXXXXX):"))
        dob=input("Enter date of birth(dd/mm/yyyy):")
        g=input("Enter gender(male/female):")
        y="2023"
        b="DSO"
        id1=id1+1
        pid=y+b+str(id1)
        print("YOUR PATIENT ID NUMBER IS",pid)
        w.writerow([nm,ip,mn,dob,pid,g])
        ch=input("DO YOU WANT TO ADD MORE REGISTRATIONS??(y/n):")
        
        if ch.lower()=='y':
            continue
        elif ch.lower()=='n':
            break
    f.close()
def appoinment():
    nm1=input("Enter name of the patient:")
    d1=input("Enter name of doctor to be consulted:")
    mn1=int(input("Enter mobile number(eg:05XXXXXXXX):"))
    dob=input("Enter date of birth(dd/mm/yyyy):")
    da1=input("Enter date to book an appoinment:")
    t1=input("Enter time(BETWEEN 09:00 HRS TO 20:00 HRS(E.G:13,12,15)):")
    g1=input("Enter gender:")
    rf2=open("appoinment.csv","r")
    r2=csv.reader(rf2)
    for d in r2:
        print(d[2],d[4],d[5])
        if d1 == d[2] and da1==d[5] and t1==d[6]:
            print("SORRY!!!!! DR.",d1, "IS BUSY AT THAT TIME. ")
            t1=input("Enter time(BETWEEN 09:00 HRS TO 20:00 HRS(E.G:13,12,15)):")
            continue
    f2=open("appoinment.csv","a",newline='')
    wa=csv.writer(f2,delimiter=",")
    al=[nm1,g1,d1,mn1,dob,da1,t1]
    wa.writerow(al)
    f2.close()
    a=random.randint(65,91)
    b=random.randint(1,9)
    c=random.randint(1,9)
    d=random.randint(1,9)
    e=random.randint(1,9)
    print("NOTE!!!!!!")
    print("PLease visit the doctor once your patient id number is called or displayed on Digital board")
    print("Your token number is",chr(a)+str(b)+str(c)+str(d)+str(e))
    
def prescription():
    d=input("Enter doctor name:")
    n=int(input("Enter number of medicines/medicine:"))
    dl=[]
    for i in range(n):
        nm=input("Enter name of the medicine:")
        h=input("Enter duration of medicine to be taken:")
        dl.append([nm,h])
    print("DOCTOR NAME:",d)
    print("MEDICINE NAME \t","DURATION(in days)")
    for j in dl:
        print(j[0],"\t\t",j[1])
        
def billing():
    dc=float(input("Enter cousultation fee:"))
    c=[]
    tc=[]
    n=int(input("Enter number of medicines:"))
    for i in range(n):
        m=input("Enter name of the medicine:")
        ct=float(input("Enter cost of the coreesponding medicine:"))
        c.append([m,ct])
        tc.append(ct)
    print("Consultation fee",dc)
    print("MEDICINE NAME\t","COST(IN AED)")
    for j in c:
        print(j[0],"\t",j[1])
    s=sum(tc)+dc
    print("TOTAL COST",s,"AED")
def display_patients():
    rf=open("registration.csv","r")
    rd=csv.reader(rf)
    for i in rd:
        print(i)
    rf.close()
def find():
    nm=input("Enter name of the patient:")
    rf=open("registration.csv","r")
    rd=csv.reader(rf)
    for i in rd:
        if i[0]==nm:
            print(i)
    rf.close()
def doctors():
    df=open("doctors.txt","r")
    rdf=csv.reader(df)
    for i in rdf:
        print(i[0],i[1])
    df.close()
def add():
    n=int(input("Enter number of doctor details to be entered/added:"))
    df=open("doctors.txt","a",newline="")
    wdf=csv.writer(df,delimiter=",")
    for i in range(n):
        dt=input("Enter name of the new doctor:")
        sp=input("Enter specialization:")
        wdf.writerow([dt,sp])
    df.close()
def delete():
    rdf=open("doctors.txt","r")
    r=csv.reader(rdf)
    f=False
    l=[]
    
    for i in r:
        l.append(i)
    rdf.close()

    print("THE AVAILABLE DOCTOR DETAILS ARE:")
    doctors()
    
    nm=input("Enter name of the doctor to be removed:")
    for j in l:
        if j[0].lower()==nm or nm.lower()==j[0]:
            l.remove(j)
            f=True
    
    if f==False:
        print("DOCTOR NOT FOUND")
    else:
        print("DOCTOR DETAILS DELETED SUCCESSFULLY")
        
    wdf=open("doctors.txt","w",newline="")
    w=csv.writer(wdf,delimiter=",")
    for k in l:
        w.writerow(k)
    wdf.close()
        

def create_file():
    f=open("registration.csv","w",newline='')
    w=csv.writer(f,delimiter=",")
    w.writerow(["NAME OF THE PATIENT","NAME OF INSURANCE PROVIDER","MOBILE NUMBER","DATE OF BIRTH","PATIENT ID","GENDER"])
    f.close()
    
    f2=open("appoinment.csv","w",newline='')
    wa=csv.writer(f2,delimiter=",")
    wa.writerow(["NAME OF PATIENT","GENDER","NAME OF DOCTOR PRESCIBED","MOBILE NUMBER","DATE OF BIRTH","APPOINMENT DATE","TIME"])
    f2.close()

create_file()
while True:
    print("Enter choice 1 to register")
    print("Enter choice 2 to book an appoinment with doctor")
    print("Enter choice 3 to print/display prescription")
    print("Enter choice 4 to print/display bill payment")
    print("Enter choice 5 to display registered patient information")
    print("Enter choice 6 to find details of a specific patient")
    print("Enter choice 7 to find doctors available and their details")
    print("Enter choice 8 to add doctor")
    print("Enter choice 9 to delete a doctor")
    print("Enter choice 10 to exit")
    c=int(input("Enter a choice:"))
    if c==1:
        registration()
    elif c==2:
        appoinment()
    elif c==3:
        prescription()
    elif c==4:
        billing()
    elif c==5:
        display_patients()
    elif c==6:
        find()
    elif c==7:
        doctors()
    elif c==8:
        add()
    elif c==9:
        delete()
    elif c==10:
        break
    else:
        print("INVALID INPUT")

