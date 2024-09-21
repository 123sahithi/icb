from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import mysql.connector
n=''
e=''
d=''
p=''
b=''
de=''
a=''
l=''
ex=''
i=''
f=''

def web1(request):
    global n,e,d,p
    if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='name':
              n=value
          if key=='email':
              e=value
          if key=='phonenumber':
              d=value
          if key=='password':
              p=value
        c="insert into sign (name,email,phonenumber,password) values('{}','{}','{}','{}')".format(n,e,d,p) 
        cursor.execute(c)
        m.commit()
    return render(request,'signin.html')

def web2(request):
      global e,p
      if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='email':
              e=value
          if key=='password':
              p=value
        c="select * from sign where email=%s and password=%s"
        cursor.execute(c,[e,p])
        t=tuple(cursor.fetchall())
        if t==():
           return render(request,'login.html')
        else:
            return render(request,'business.html')
      return render(request,'login.html')

def web3(request):
    return render(request,'user.html')
def web4(request):
    return render(request,'business.html')
def web5(request):
    return render(request,'investor.html')
def web6(request):
    return render(request,'banker.html')
def web7(request):
    return render(request,'businessadviser.html')
def web8(request):
    return render(request,'home.html')
def web10(request):
    global n,e,d,i,f
    if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='name':
              n=value
          if key=='email':
              e=value
          if key=='phonenumber':
              d=value
          if key=='idea':
              i=value
          if key=='file':
              f=value
        c="insert into idea (name,email,phonenumber,idea,file) values('{}','{}','{}','{}','{}')".format(n,e,d,i,f) 
        cursor.execute(c)
        m.commit()
    return render(request,'idea.html')
def web11(request):
     global n,e,d,p,b,de
     if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='name':
              n=value
          if key=='email':
              e=value
          if key=='phonenumber':
              d=value
          if key=='bio':
              b=value
          if key=='details':
              de=value
          if key=='password':
              p=value
        c="insert into isign (name,email,phonenumber,bio,details,password) values('{}','{}','{}','{}','{}','{}')".format(n,e,d,b,de,p) 
        cursor.execute(c)
        m.commit()
     return render(request,'isign.html')
def web12(request):
    global e,p
    if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='email':
              e=value
          if key=='password':
              p=value
        c="select * from isign where email=%s and password=%s"
        cursor.execute(c,[e,p])
        t=tuple(cursor.fetchall())
        if t==():
           return render(request,'ilog.html')
        else:
            return render(request,'investor.html')
            
    return render(request,'ilog.html')
def web13(request):
     global n,e,d,a,l,p
     if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='name':
              n=value
          if key=='email':
              e=value
          if key=='phonenumber':
              d=value
          if key=='address':
              a=value
          if key=='loan':
              l=value
          if key=='password':
              p=value
        c="insert into bsign (name,email,phonenumber,address,loan,password) values('{}','{}','{}','{}','{}','{}')".format(n,e,d,a,l,p) 
        cursor.execute(c)
        m.commit()
     return render(request,'bsign.html')
def web14(request):
    global e,p
    if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='email':
              e=value
          if key=='password':
              p=value
        c="select * from bsign where email=%s and password=%s"
        cursor.execute(c,[e,p])
        t=tuple(cursor.fetchall())
        if t==():
           return render(request,'blog.html')
        else:
            return render(request,'banker.html')
    return render(request,'blog.html')
def web15(request):
     global n,e,d,b,ex,p
     if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='name':
              n=value
          if key=='email':
              e=value
          if key=='phonenumber':
              d=value
          if key=='bio':
              b=value
          if key=='experience':
              ex=value
          if key=='password':
              p=value
        c="insert into basign (name,email,phonenumber,bio,experience,password) values('{}','{}','{}','{}','{}','{}')".format(n,e,d,b,ex,p) 
        cursor.execute(c)
        m.commit()
     return render(request,'basign.html')
def web16(request):
    global e,p
    if request.method=='POST':
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
          if key=='email':
              e=value
          if key=='password':
              p=value
        c="select * from basign where email=%s and password=%s"
        cursor.execute(c,[e,p])
        t=tuple(cursor.fetchall())
        if t==():
           return render(request,'balog.html')
        else:
            return render(request,'businessadviser.html')
    return render(request,'balog.html')
def web17(request):
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        c = "SELECT * FROM isign"
        cursor.execute(c)
        s=list(cursor)
        return render(request,'ilist.html',{'users':s})
def web18(request):
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        c = "SELECT * FROM bsign"
        cursor.execute(c)
        s=list(cursor)
        return render(request,'blist.html',{'users':s})
def web19(request):
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        c = "SELECT * FROM basign"
        cursor.execute(c)
        s=list(cursor)
        return render(request,'balist.html',{'users':s})
def web20(request):
        m=mysql.connector.connect(host="localhost",user="root",passwd="ssr@143",database="icb")
        cursor=m.cursor()
        c = "SELECT * FROM idea"
        cursor.execute(c)
        s=list(cursor)
        return render(request,'list.html',{'users':s})
