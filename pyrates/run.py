# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask,render_template
from flask_mysqldb import MySQL 
from localStoragePy import localStoragePy
from flask import Flask, render_template,redirect,url_for,session,request,flash
import mysql.connector

app = Flask(__name__)

#mysql connection setup process

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="brainbeam"
app.config["MYSQL_DB"]="pizza"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
app.secret_key = 'keykeykey'
  
  
  


#user login Backend process
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    try:
        if request.method == 'POST':  
            cursor = mysql.connection.cursor()
            email = request.form['email']  
            password = request.form['password'] 
            cursor.execute(
                'SELECT * FROM registers WHERE email = %s AND password = %s', (email, password,))
            emp = cursor.fetchone()
            result=emp
           
            if emp:
                session['loggedin'] = True
                session['email'] = email
                session['password'] = password
                return render_template('index.html',token=result)
            else:
                flash('Enter Correct Username or Password!')
                return render_template('userlogin.html')
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST': 
            cursor = mysql.connection.cursor()
            firstname = request.form['firstname']  
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password'] 
            mobilenumber = request.form['mobilenumber']
            address = request.form['address']
            cursor.execute(
                "INSERT INTO registers(Firstname,Lastname,Email,Password,MobileNumber,Address)VALUES(%s,%s,%s,%s,%s,%s)", (firstname, lastname, email, password, mobilenumber,address))
            mysql.connection.commit()
            cursor.close()
            mysql.connection.close()
            flash("registered Successfully")
            return redirect(url_for('login'))
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('register.html')



@app.route('/changepassword', methods=['GET', 'POST'])
def changepassword():
    try:    
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            email = request.form['email']  
            password = request.form['password']  
            cursor.execute("update registers set password=%s where email=%s",(password,email))
            mysql.connection.commit()
            flash("Updated Successfully")
            return redirect(url_for('login'))
        return render_template('forgetpswd.html')
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('forgetpswd.html')
     

        
#admin backend process
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        if request.method == 'POST':
            
            cursor = mysql.connection.cursor()
            username = request.form['username']  # ADMIN
            password = request.form['password']  # ADMIN
            cursor.execute(
                'SELECT * FROM admin WHERE username = %s AND password = %s', (username, password,))
            admin = cursor.fetchone()
            if admin:
                session['loggedin'] = True
                session['username'] = username
                session['password'] = password
                flash('Logged in successfully !')
                return redirect(url_for('allordersview'))   
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('adminlogin.html')

        
#admin change password        
@app.route('/adminchangepassword', methods=['GET', 'POST'])
def adminchangepassword():
   try:
        if request.method == 'POST':
            cursor = mysql.connection.cursor()

            username = request.form['username']  

            password = request.form['password']  

            cursor.execute("update admin set password=%s where username=%s",(password,username))

            mysql.connection.commit()
            flash("Updated Successfully")
            return redirect(url_for('adminlogin'))

        return render_template('adminforgetpswd.html')
   except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('adminlogin.html')
  
     

        

@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        items = request.form['items']  
        amount = request.form['amount']
        cursor.execute(
            "INSERT INTO addtocart(items,amount)VALUES(%s,%s)", (items, amount))
        mysql.connection.commit()
    return render_template('mycart.html')


@app.route('/login')
def login():
    return render_template('userlogin.html')


@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/forgetpswd')
def forgetpswd():
    return render_template('forgetpswd.html')

@app.route('/logout')
def logout():
    return render_template('userlogin.html')



@app.route('/registerpage')
def registerpage():
    return render_template('register.html')

@app.route('/cart')
def cart():
    return render_template('addtocart.html')

@app.route('/landingpage')
def landingpage():
    return render_template('landpage.html')



#landing page
@app.route('/')
def main():
	return render_template('userlogin.html')

#home pafe
@app.route('/home')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT * FROM customers')
    admin = cursor.fetchone()
    
    return render_template('index.html',message=admin)


#Addpizzaitems
@app.route('/menu')
def menu():
    try:  
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM pizzaitems')
        displaylist = list(cursor.fetchall())
        return render_template('menu.html',pizzaitems=displaylist)
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('menu.html')


#Adddrinksitems
@app.route('/drinks')
def drinks():
    try:  
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM drinkitems')
        displaylist = list(cursor.fetchall())
        return render_template('drinks.html',drinkitems=displaylist)
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('drinks.html')


#Addburgeritems
@app.route('/burger')
def burger():
    try:  
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM burgeritems')
        displaylist = list(cursor.fetchall())
        return render_template('burger.html',burgeritems=displaylist)
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('burger.html')


#Addpastaitems
@app.route('/pasta')
def pasta():
    try:  
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM pastaitems')
        displaylist = list(cursor.fetchall())
        return render_template('pasta.html',pastaitems=displaylist)
    except Exception as e:
        flash("sorry some problem on server try again later")
        return render_template('pasta.html')

#service page
@app.route('/services')
def services():
	return render_template('services.html')


#service page
@app.route('/sales')
def sales():
	return render_template('salesdata.html')


#blog page
@app.route('/blog')
def blog():
	return render_template('blog.html')

#about page
@app.route('/about')
def about():
	return render_template('about.html')




#contact page
@app.route('/contact')
def contact():
	return render_template('contact.html')

#update profile page
@app.route('/getupdateuser')
def getupdateuser():
	return render_template('getupdateuser.html')




#user profile landing page
@app.route('/profile')
def profile():
	return render_template('my_profile.html')


#pizza order form page
@app.route('/pizzaorderform',methods=['POST','GET'])
def pizzaorderform():

   
        if request.method=='POST':
            productname=request.form['productname']
            username=request.form['username']
            email=request.form['email']
            quantity=request.form['quantity'] 
            price=request.form['price'] 
            mobilenumber=request.form['mobilenumber']
            orderdate=request.form['orderdate']
            address=request.form['address'] 
            totalprice=(int(quantity)*int(price))
            cursor=mysql.connection.cursor()
            cursor.execute("insert into orders(product_name,username,email,quantity,mobilenumber,orderdate,address,price,totalcost)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(productname,username,email,quantity,mobilenumber,orderdate,address,price,totalprice))
            mysql.connection.commit()
            flash(" Ordered Successfully go to check your door! happy pizza day")
            flash(f"your ordered {productname} quantity {quantity} total amount ₹{totalprice} you pay once get {productname}")
            return redirect(url_for('menu'))
        return render_template('pizza_order_form.html')



#user myorder history page
@app.route('/myorder')
def myorder():
 try:   
    cursor = mysql.connection.cursor()
    cursor.execute(
            'SELECT * FROM orders')
    displaylist = cursor.fetchall()
    return render_template('my_order.html',message=displaylist)
 except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')



#update order
@app.route('/editorder/<int:id>',methods=['POST','GET'])
def editorder(id):
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            productname=request.form['productname']
            username=request.form['username']
            email=request.form['email']
            quantity=request.form['quantity'] 
            mobilenumber=request.form['mobilenumber']
            orderdate=request.form['orderdate']
            address=request.form['address'] 
            totalcost=request.form['totalprice'] 
            cursor=mysql.connection.cursor()
            cursor.execute("update orders set productname=%s,username=%s,email=%s,quantity=%s,mobilenumber=%s,orderdate=%s,address=%s,totalcost=%s where id=%s",(productname,username,email,quantity,mobilenumber,orderdate,address,totalcost,id))
            mysql.connection.commit()
            cursor.close()
            flash("Record Has Been Updated Successfully")
            return redirect(url_for('getuserdata'))   
        sql="select * from orders where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('editorder.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')
        
#update order
@app.route('/orderstatus/<int:id>',methods=['POST','GET'])
def orderstatus(id):
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            productname=request.form['productname']
            username=request.form['username']
            email=request.form['email']
            quantity=request.form['quantity'] 
            mobilenumber=request.form['mobilenumber']
            orderdate=request.form['orderdate']
            address=request.form['address']
            price=request.form['price']  
            totalcost=request.form['totalprice'] 
            orderstatus=request.form['orderstatus'] 
            cursor=mysql.connection.cursor()
            cursor.execute("update orders set productname=%s,username=%s,email=%s,quantity=%s,mobilenumber=%s,orderdate=%s,address=%s,price=%s,totalcost=%s,orderstatus=%s where id=%s",(productname,username,email,quantity,mobilenumber,orderdate,address,price,totalcost,orderstatus,id))
            mysql.connection.commit()
            cursor.close()
            flash("Record Has Been Updated Successfully")
            return redirect(url_for('allordersview'))   
        sql="select * from orders where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('adminupdateorders.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')
        


#update profile
@app.route('/updatefile',methods=['POST','GET'])
def updatefile():
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            id=request.form['email']
            sql="select * from registers where email=%s"
            cursor.execute(sql,[id])
            result=cursor.fetchone()
            return render_template('updateuserprofile.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')
    

#update profile
@app.route('/getcustomerlist/<string:id>',methods=['POST','GET'])
def getcustomerlist(id):
    try:
        cursor = mysql.connection.cursor()    
        if request.method=='POST':
            firstname=request.form['productname']
            lastname=request.form['username']
            email=request.form['email']
            password=request.form['quantity'] 
            mobilenumber=request.form['mobilenumber']
        
            address=request.form['address'] 
        
            cursor=mysql.connection.cursor()
            cursor.execute("update registers set firstname=%s,lastname=%s,email=%s,password=%s,mobilenumber=%s,address=%s where email=%s",(firstname,lastname,email,password,mobilenumber,address,id))
            mysql.connection.commit()
            cursor.close()
            flash("Record Has Been Updated Successfully")
            return redirect(url_for('customerslist'))
        sql="select * from registers where email=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('adminupdateusers.html',data=result)   
        
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')
        
#user customerlist page
@app.route('/customerslist')
def customerslist():
 try:   
    cursor = mysql.connection.cursor()
    cursor.execute(
            'SELECT * FROM registers')
    displaylist = cursor.fetchall()
    return render_template('getcustomerlist.html',data=displaylist)
 except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')

#deleteuser
@app.route('/deletecustomer/<string:id>',methods=['POST','GET'])
def deletecustomer(id):
        flash("Record Has Been Deleted Successfully")
        cursor=mysql.connection.cursor()
        cursor.execute("delete from registers where email like %s ",[id])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('customerslist'))
    
        
        
@app.route('/updateprofile/<string:id>',methods=['POST','GET'])
def updateprofile(id):
    try:
        cursor = mysql.connection.cursor()    
        if request.method=='POST':
            firstname=request.form['productname']
            lastname=request.form['username']
            email=request.form['email']
            password=request.form['quantity'] 
            mobilenumber=request.form['mobilenumber']
            address=request.form['address'] 
            cursor=mysql.connection.cursor()
            cursor.execute("update registers set firstname=%s,lastname=%s,email=%s,password=%s,mobilenumber=%s,address=%s where email=%s",(firstname,lastname,email,password,mobilenumber,address,id))
            mysql.connection.commit()
            cursor.close()
            flash("Record Has Been Updated Successfully")
            return redirect(url_for('getuserdata'))      
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')
        


#deleteorder
@app.route('/deleteorder/<string:id>',methods=['POST','GET'])
def deleteorder(id):
    try:
        flash("Record Has Been Deleted Successfully")
        cursor=mysql.connection.cursor()
        cursor.execute("delete from orders where id=%s",id)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('getuserdata'))
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')
        
#deleteorder
@app.route('/admindeleteorder/<string:id>',methods=['POST','GET'])
def admindeleteorder(id):
    try:
        flash("Record Has Been Deleted Successfully")
        cursor=mysql.connection.cursor()
        cursor.execute("delete from orders where id=%s",id)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('allordersview'))
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')        


#downloadorder
@app.route('/downloadorder/<int:id>',methods=['POST','GET'])
def downloadorder(id): 
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            productname=request.form['productname']
            username=request.form['username']
            email=request.form['email']
            quantity=request.form['quantity'] 
            mobilenumber=request.form['mobilenumber']
            orderdate=request.form['orderdate']
            address=request.form['address'] 
            totalcost=request.form['totalprice'] 
            cursor=mysql.connection.cursor()
            cursor.execute("update orders set productname=%s,username=%s,email=%s,quantity=%s,mobilenumber=%s,orderdate=%s,address=%s,totalcost=%s where id=%s",(productname,username,email,quantity,mobilenumber,orderdate,address,totalcost,id))
            mysql.connection.commit()
            cursor.close()
            flash("Record Has Been downloaded Successfully")
            return redirect(url_for('getuserdata'))   
        sql="select * from orders where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('downloadorder.html',data=result)  
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html') 



#getuserbydata orderlist
@app.route('/getuserdata',methods=['POST','GET'])
def getuserdata():
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            email=request.form['email']
            cursor=mysql.connection.cursor()
            cursor.execute("select * from orders where email LIKE %s",[email])
            displaylist = cursor.fetchall()
            flash("Successfully Find Your Order list")
            return render_template('my_order.html',message=displaylist)
        return render_template('getuserdata.html') 
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html') 

#admin view all order history page
@app.route('/allordersview')
def allordersview():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("select * from orders")
        displaylist = cursor.fetchall()
        return render_template('admindashboard.html',message=displaylist)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')


#admin view all order history page
@app.route('/totalsales')
def totalsales():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("select sum(totalcost)as total ,count(id)as id from orders")
        displaylist = cursor.fetchone()
       
        return render_template('salesdata.html',message=displaylist)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')


    
#admin view all order history page
@app.route('/datewisesales',methods=['GET','POST'])
def datewisesales():
    try:
        cursor = mysql.connection.cursor()
        if request.method=='POST':
            hello=request.form['date']
            cursor=mysql.connection.cursor()
            cursor.execute("SELECT sum(totalcost)as hello FROM orders WHERE orderdate LIKE %s ", [hello])
            displaylist = cursor.fetchone()
            return render_template('salesdata.html',message=displaylist)    
        return render_template('salesdata.html')
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')


#admin view all order history page
@app.route('/popular')
def popular():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("select count(item)as count,item from survey group by item")
        displaylist = cursor.fetchone()
      
        return render_template('salesdata.html',message=displaylist)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')


    
    
#admin view all survey form datas 
@app.route('/surveyformview')
def surveyformview():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("select * from survey")
        displaylist = cursor.fetchall()
        return render_template('adminviewsurvey.html',message=displaylist)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')

 
    
#admin view user enquiry form datas 
@app.route('/enquiryformview')
def enquiryformview():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("select * from enquiry")
        displaylist = cursor.fetchall()
        return render_template('adminviewenquiry.html',message=displaylist)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')

     
#deleteenquiry
@app.route('/customerenquirydelete/<string:id>',methods=['POST','GET'])
def customerenquirydelete(id):
    try:
        flash("Record Has Been Deleted Successfully")
        cursor=mysql.connection.cursor()
        cursor.execute("delete from enquiry where id=%s",id)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('enquiryformview'))
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')
        
    
#deletesurvey
@app.route('/customersurveydelete/<string:id>',methods=['POST','GET'])
def customersurveydelete(id):
    try:
        flash("Record Has Been Deleted Successfully")
        cursor=mysql.connection.cursor()
        cursor.execute("delete from survey where id=%s",id)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('surveyformview')) 
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('admindashboard.html')



#survey form
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    try:
        cursor = mysql.connection.cursor()  
        if request.method == 'POST':
            
            cursor = mysql.connection.cursor()
            firstname = request.form['name']  
            lastname = request.form['city']
            email = request.form['item']
            password = request.form['day'] 
            mobilenumber = request.form['family']
            address = request.form['month']
            cursor.execute(
                "INSERT INTO survey(username,city,item,favday,family,favmonth)VALUES(%s,%s,%s,%s,%s,%s)", (firstname, lastname, email, password, mobilenumber,address))
            mysql.connection.commit()
            return redirect(url_for('profile'))
        return render_template('surveyform.html')
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')

 
    


#enquiry form
@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    try:
        cursor = mysql.connection.cursor()  
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            username = request.form['name']  
            mobile = request.form['number']
            email = request.form['email']
            need = request.form['need'] 
            message = request.form['message']    
            cursor.execute(
                "INSERT INTO enquiry(username,mobilenumber,email,typeofproblem,message)VALUES(%s,%s,%s,%s,%s)", (username, mobile, email,need,message))
            mysql.connection.commit()
            flash("Pizza Kaaran Support Team Contact You Soon No Worries")
            return redirect(url_for('profile'))
        return render_template('enquiry.html')
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html') 
    
#get pizzaname and price from database
@app.route('/pizzaitem/<int:id>',methods=['POST','GET'])
def pizzaitem(id):
    try:
        cursor = mysql.connection.cursor()  
        sql="select * from pizzaitems where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('pizza_order_form.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')

    
#get burgername and price from database
@app.route('/burgeritem/<int:id>',methods=['POST','GET'])
def burgeritem(id):
    try:
        cursor = mysql.connection.cursor()  
        sql="select * from burgeritems where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('pizza_order_form.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')

#get drinkname and price from database
@app.route('/drinkitem/<int:id>',methods=['POST','GET'])
def drinkitem(id):
    try:
        cursor = mysql.connection.cursor()  
        sql="select * from drinkitems where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        return render_template('pizza_order_form.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')


#get pastaname and price from database
@app.route('/pastaitem/<int:id>',methods=['POST','GET'])
def pastaitem(id):
    try:
        cursor = mysql.connection.cursor()  
        sql="select * from pastaitems where id=%s"
        cursor.execute(sql,[id])
        result=cursor.fetchone()
        print("12")
        print(result)
        return render_template('pizza_order_form.html',data=result)
    except Exception as e:
            flash("sorry some problem on server try again later")
            return render_template('index.html')


# main driver function
if __name__ == '__main__':
	app.run(debug=True)
