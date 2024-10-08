from flask import *
import mysql.connector
con=mysql.connector.connect(user="root",password="",database="bank")
cur=con.cursor()

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    return render_template("index.html")

@app.route("/AdminLogin")
def AdminLogin():
    return render_template("AdminLogin.html")


@app.route("/home")
def home():
    return render_template("AdminHome.html")

@app.route("/AddCustomer")
def AddCustomer():
    return render_template("AddCustomer.html")


@app.route("/AddCustomerDB",methods=['POST'])
def AddCustomerDB():
    ano=request.form['ano']
    name=request.form['name']
    mail=request.form['mail']
    pwd=request.form['pwd']
    contact=request.form['cont']
    amt=request.form['amt']

    sql="insert into customer values(%s,'%s','%s','%s','%s',%s)"%(ano,name,mail,pwd,contact,amt)
    cur.execute(sql)
    con.commit()
    import smtplib
    smtp = smtplib.SMTP('smtp.gmail.com', 587) #gmail port number
    smtp.starttls()

    smtp.login("pravashranjansahoo@gmail.com", "olik sxxr gmbc jwdr")
    ms="Your Account Number is "+str(ano)+" and Your Password is "+pwd
    smtp.sendmail("pravashranjansahoo@gmail.com", "rupha145@gmail.com", ms)
    smtp.quit()

    
    return render_template("AddCustomer.html",msg="Customer Added Successfully...")

@app.route("/ViewCustomer")
def ViewCustomer():
    cur.execute("select * from customer")
    data=cur.fetchall()
    return render_template("ViewCustomer.html",d=data)


@app.route("/DeleteCustomer",methods=['GET'])
def DeleteCustomer():
    ano=request.args['ano']
    sql="delete from customer where ano="+str(ano)
    cur.execute(sql)
    con.commit()
    cur.execute("select * from customer")
    data=cur.fetchall()
    return render_template("ViewCustomer.html",d=data)



@app.route("/CustomerLogin")
def CustomerLogin():
    return render_template("CustomerLogin.html")

@app.route("/AdminLoginCheck",methods=['POST'])
def AdminLoginCheck():
    un=request.form['uname']
    pwd=request.form['pwd']
    if un=='Admin' and pwd=='Hello':
        return render_template("AdminHome.html")
    else:
        return render_template("AdminLogin.html",msg="Pls Check the Credentials...")


app.run(debug=True,port=1234)
