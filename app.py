from flask import Flask, render_template, request, session, url_for, redirect, jsonify, make_response
from werkzeug.utils import secure_filename
import os
import pymysql

app = Flask(__name__)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/landdetails/'
app.config['UPLOADED_PHOTOS_DEST1'] = 'static/landdocumentfromuser/'
app.config['UPLOADED_PHOTOS_DEST2'] = 'static/landdocumentfromseller/'

app.secret_key = 'any random string'


def dbConnection():
    try:
        connection = pymysql.connect( host="localhost", user="root", password="root", database="landmanagement", autocommit=True)
      
        return connection
    except:
        print("Something went wrong in database Connection")


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")


con = dbConnection()
cursor = con.cursor()


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/index')
def index():
    user = session["user"]
    return render_template('index.html',user=user)


@app.route('/logout')
def logout():
    return render_template('main.html')


@app.route('/about1')
def about1():
    return render_template('about1.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        username = request.form.get("username")
        emailaddress = request.form.get("emailaddress")
        phoneno = request.form.get("phoneno")
        subjct = request.form.get("subjct")
        
        print(username,emailaddress,phoneno,subjct)
        con = dbConnection()
        cursor = con.cursor()
        sql2 = "INSERT INTO contact1(username,email,phone,subject) VALUES (%s, %s, %s, %s)"
        val2 = (str(username), str(emailaddress), str(phoneno), str(subjct))
        cursor.execute(sql2, val2)
        con.commit()
        return render_template('contact.html')
    return render_template('contact.html')
################################################login part###################################################################


@app.route('/adminlogin1', methods=['POST', 'GET'])
def adminlogin1():
    msg = ''
    if request.method == "POST":
           username = request.form.get("username")
           print("username", username)
           password = request.form.get("password")
           con = dbConnection()
           cursor = con.cursor()
           cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password))
           result = cursor.fetchone()
           print("result", result)
           if result:
               session['admin'] = result[0]
               return redirect(url_for('adminindex'))

           else:
               msg = 'Incorrect username/password!'
               return msg
               return render_template('adminlogin.html')
    return render_template('adminlogin.html')


@app.route('/user', methods=['POST', 'GET'])
def user():
    msg = ''
    if request.method == "POST":
        username = request.form.get("username")
        print("username", username)
        password = request.form.get("password")
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM sellerregistration WHERE username = %s AND password = %s', (username, password))
        result = cursor.fetchone()
        
        print("result", result)
        if result:
            session['user'] = result[0]
            
            return redirect(url_for('index'))
        else:
            msg = 'Incorrect username/password!'
            return msg

    return render_template('sellerlogin.html')


################################################login part###################################################################


################################################register part###################################################################


@app.route('/adminregister', methods=['POST', 'GET'])
def adminregister():
    return render_template('adminlogin.html')


@app.route('/userregister', methods=['POST', 'GET'])
def userregister():
    if request.method == "POST":
       details = request.form
       username1 = details['username1']
       print("username", username1)

       mailid1 = details['email1']
       password1 = details['password1']

       sql2 = "INSERT INTO sellerregistration(username,emailid,password) VALUES (%s, %s, %s)"
       val2 = (str(username1), str(mailid1), str(password1))
       cursor.execute(sql2, val2)
       con.commit()
       return render_template('sellerlogin.html')

    return render_template('sellerlogin.html')

################################################register part###################################################################


################################################admin part###################################################################
@app.route('/adminindex', methods=['POST', 'GET'])
def adminindex():
    return render_template('adminindex.html')



@app.route('/calculategst',methods=['POST','GET'])
def calculategst():
    
    landprise = request.args.get("landprise")
    print(landprise)
    uname = request.args.get("uname")
    uid = request.args.get("uid")
    userinputstring=landprise
    useroriginalprice=float(userinputstring)
    percent=(15/100) * useroriginalprice
    value=str(percent)
    print("percenttage",percent)
    
    return value
    # return redirect(url_for('verifydocuments',value=value))
   


@app.route('/verifylanddocument', methods=['POST', 'GET'])
def verifylanddocument():
    status="not_verify"
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT sellername,filenamepath,Landprice,Email FROM addland  WHERE admin = %s ",(status))
    result1 = cursor.fetchall()
    
    print(result1)
  
    return render_template('viewland.html',result1=result1)


@app.route('/allverifiedland', methods=['POST', 'GET'])
def allverifiedland():
    status="verify"
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT sellername,filenamepath,Landprice,Email  FROM addland where admin = %s ",(status))
    result1 = cursor.fetchall()
    
    print(result1)
    

    return render_template('allverifyland.html', result1=result1)

@app.route('/verifydocuments', methods=['POST', 'GET'])
def verifydocuments():
    Uname = request.args.get("Uname")
    Imgname = request.args.get("imgname")
    lprice = request.args.get("Lprice")
    
    print(Uname,Imgname,lprice)
    
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland where sellername=%s and filenamepath=%s and Landprice=%s",(Uname,Imgname,lprice))
    result = cursor.fetchall()
    
    print(result)
    
    return render_template('verifyviewgstcalculation.html',result=result)




@app.route('/verify', methods=['POST', 'GET'])
def verify():
    Uname = request.args.get("Uname")
    Imgname = request.args.get("imgname")
    lprice = request.args.get("Lprice")
    
    print(Uname,Imgname,lprice)
    
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland where sellername=%s and filenamepath=%s and Landprice=%s",(Uname,Imgname,lprice))
    result = cursor.fetchall()
    
    print(result)
    
    return render_template('viewinfoveriy.html',result=result)


@app.route('/verified', methods=['POST', 'GET'])
def verified():
    Uname = request.args.get("Uname")
    adharcard = request.args.get("adharcard")
    lprice = request.args.get("Lprice")
    
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland")
    result = cursor.fetchall()
    
    # print(result)
    
  
    ccg="verify"
    con = dbConnection()
    cursor = con.cursor()
    sql1 = "UPDATE addland SET admin = %s WHERE sellername = %s  AND adharcard = %s AND Landprice = %s;"
    val1 = (ccg, Uname ,adharcard,lprice)
    cursor.execute(sql1,val1)
    con.commit()
    # return "sucess"
    return redirect(url_for('allverifiedland'))

################################################admin part###################################################################
################################################seller part###################################################################


@app.route('/addlandproperty', methods=['POST', 'GET'])
def addlandproperty():
     if request.method == "POST":
            user = session["user"]
            sellername = request.form['name']
            Email = request.form['Email']
            Phone = request.form['Phone']
            adharcard = request.form['adharcard']
            serveyno = request.form['servey']
            WARDno = request.form['WARD']
            Plotno = request.form['Plot']
            maplocation = request.form['location']
            
            f2 = request.files['file']
            filename_secure = secure_filename(f2.filename)
            f2.save(os.path.join(
                app.config['UPLOADED_PHOTOS_DEST'], filename_secure))
            filenamepath = os.path.join(
                app.config['UPLOADED_PHOTOS_DEST'], filename_secure)
            print("filenamepath", filenamepath)
           
            f3 = request.files['file1']
            filename_secure = secure_filename(f3.filename)
            f3.save(os.path.join(
                app.config['UPLOADED_PHOTOS_DEST2'], filename_secure))
            filenamepathfordoc = os.path.join(
                app.config['UPLOADED_PHOTOS_DEST2'], filename_secure)
            print("filenamepath",filenamepathfordoc)
            
            state = request.form['state']
            
            city = request.form.get('city')
            area = request.form.get('area')
            Landprice = request.form.get('Landprice')
            status = "Land available"
            
           
            
            sql2 = "INSERT INTO addland(sellername,Email,Phone,adharcard,serveyno,WARDno,Plotno,maplocation,filenamepath,filenamepathfordoc,state,city,area,Landprice,status,user) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val2 = (str(sellername), str(Email), str(Phone), str(adharcard), str(serveyno), str(WARDno), str(Plotno), str(maplocation), str(filenamepath), str(filenamepathfordoc), str(state), str(city), str(area), str(Landprice), str(status), str(user))
            cursor.execute(sql2, val2)
            con.commit()
            # return render_template('addland.html')
            return redirect(url_for('index'))



     return render_template('addland.html')


@app.route('/reqquestfrombuyer',methods=['POST','GET'])
def reqquestfrombuyer():
    user = session["user"]
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM request1 WHERE  request = %s;",(user))
    result1 = cursor.fetchall()
    
    
    return render_template('requestfrombuyer.html',result1=result1)



@app.route('/mysellland',methods=['POST','GET'])
def mysellland():

    
    user = session["user"]
    print(user)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland WHERE  user = %s;",(user))
    result1 = cursor.fetchall()
    
    print(result1)
    
    
    
    return render_template('myland.html',result1=result1)



@app.route('/viewsellerland',methods=['POST','GET'])
def viewsellerland():
    if request.method == "POST":
        username = request.form['username']
        print("username",username)
        slashparts = username.split('&')
        landprice =slashparts[-1]
        emailid =slashparts[-2]
        sellername =slashparts[-3]
        print(sellername,emailid,landprice)
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM addland WHERE  sellername = %s AND  Email = %s AND  Landprice = %s;",(sellername,emailid,landprice))
        result1 = cursor.fetchall()
        print(result1)
        
      
        data= jsonify(result1)
        
        
        return data
        
    #     sellername = details['studentname']
    #     emailid = details['studentname']
    #     landprice = details['studentname']
        

            
            
    #     print(user)
    #     con = dbConnection()
    #     cursor = con.cursor()
    #     cursor.execute("SELECT * FROM addland WHERE  sellername = %s AND  Email = %s AND  Landprice = %s;",(user1,email,Lprice))
    #     result1 = cursor.fetchall()
        
    #     print(result1)
    
    
    
    # return render_template('viewsellerland.html',result1=result1)



################################################seller part###################################################################




@app.route('/update',methods=['POST','GET'])
def update():
    user =request.args.get("user")
    email = request.args.get("email")
    project = request.args.get("project")
    landprice = request.args.get("landprice")
    
    print(user,email,project,landprice)
 
    con = dbConnection()
    cursor = con.cursor()
    ccg= " ACCEPT "
    print(ccg)
 
    sql1 = "UPDATE request1 SET status = %s WHERE user = %s  AND Email = %s AND filepath = %s AND landprice = %s;"
    val1 = (ccg, str(user),str(email),str(project),str(landprice))
    cursor.execute(sql1,val1)
    con.commit()
    
    print("zjdhuhuo")
    return redirect(url_for("reqquestfrombuyer"))
    
 
################################################buyer part###################################################################
@app.route('/request1',methods=['POST','GET'])
def request1():
    print("GET")
    if request.method == "GET":
        print("POST")
        user = session["user"]
        Uname=request.args.get("Uname")
        print(Uname)
        imgname =request.args.get("imgname")
        Lprice = request.args.get("Lprice")
        email = request.args.get("email")
        print(Uname,imgname,Lprice,email)
        
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM addland where sellername = %s AND filenamepath = %s AND Landprice = %s AND Email = %s ",(Uname,imgname,Lprice,email))
        result1 = cursor.fetchall()
        # print(result1)
        
       
        email=result1[0][2]
        filepath=result1[0][9]
        maplocation=result1[0][8]
        landprice=result1[0][14]
        requester=result1[0][18]
     
        
        sql2 = "INSERT INTO request1(user,email,filepath,maplocation,landprice,request) VALUES (%s, %s, %s, %s, %s, %s)"
        val2 = (str(user), str(email), str(filepath), str(maplocation), str(landprice), str(requester))
        cursor.execute(sql2, val2)
        
        
        
        return redirect(url_for('index'))
     
     
        return "success"
    
    return "success"



@app.route('/landproerty1',methods=['POST','GET'])
def landproerty1():

  user = session["user"]
  status=" ACCEPT "
  

      
  con = dbConnection()
  cursor = con.cursor()
  cursor.execute("SELECT * FROM request1 WHERE user = %s AND status = %s;",(user,status))
  result = cursor.fetchall()
    
  print(result)
       
  filepath=result[0][3]
  maplocation=result[0][4] 
  landprice=result[0][5]
    
  print(filepath)
  print(maplocation)
  print(landprice)
  buyer="AVAILABLE"
      
  cursor.execute("SELECT sellername,filenamepathfordoc,Landprice,Email FROM addland WHERE user = %s AND filenamepath = %s  AND maplocation = %s AND Landprice = %s AND buyer = %s;",(user,filepath,maplocation,landprice,buyer))
  result1 = cursor.fetchall()
    
  print(result1)
 
 
 
  return render_template('alllandproperty.html',result1=result1)
    
   



@app.route('/book', methods=['POST', 'GET'])
def book():
    
    Uname = request.args.get("Uname")
    Imgname = request.args.get("imgname")
    lprice = request.args.get("Lprice")
    
    print(Uname,Imgname,lprice)
    
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland where sellername=%s and filenamepathfordoc=%s and Landprice=%s",(Uname,Imgname,lprice))
    result2 = cursor.fetchall()
    
   
    
    # print(result2)
    
    return render_template('viewlandbook.html',result2=result2)



@app.route('/bookingpage', methods=['POST', 'GET'])
def bookingpage():
    if request.method == "GET":
        Uname = request.args.get("uname")
        uid = request.args.get("uid")
        lprice = request.args.get("landprise")
        email = request.args.get("email")
        print(Uname,uid,lprice,email)
      
    
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM addland where sellername=%s and adharcard=%s and Landprice=%s",(Uname,uid,lprice))
        result2 = cursor.fetchall()
        
        
        
        
        # print(result2)
        
        
        return render_template('bookingpage.html',result2=result2)
    return render_template('bookingpage.html')



# @app.route('/status',methods=['POST','GET'])
# def status():
    
    
#     status="verify"
#     buyerstatus="AVAILABLE"
    
#     con = dbConnection()
#     cursor = con.cursor()
#     cursor.execute("SELECT sellername,filenamepathfordoc,Landprice,Email FROM addland where admin = %s AND buyer  = %s ",(status,buyerstatus))
#     result1 = cursor.fetchall()
    
    
    
#     return render_template('status.html',result1=result1)


@app.route('/status',methods=['POST','GET'])
def status():
    
    name = session["user"]
    status="verify"
    buyerstatus="AVAILABLE"
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM addland where admin = %s AND buyer  = %s  AND user != %s",(status,buyerstatus,name))
    result1 = cursor.fetchall()
    
    
    
    return render_template('status.html',result1=result1)


@app.route('/like',methods=['POST','GET'])
def like():    
    sellerId =request.args.get('sellerId')
    sellerName =request.args.get('sellerName')
    projectpic =request.args.get('projectpic')
    email =request.args.get('email')
    
    print(sellerId,sellerName,projectpic,email)
    print(sellerId,sellerName,projectpic,email)
    
    
    cursor.execute("SELECT likecount from addland where ID=%s and sellername= %s and filenamepath=%s and Email=%s",(sellerId,sellerName,projectpic,email))
    rows = cursor.fetchall()
    project=rows[0][0]
    print("project")
    print(project)
    status=int(project)+1
        
    sql3 = "UPDATE addland SET likecount = %s WHERE ID=%s and sellername= %s and filenamepath=%s and Email=%s"
    val3 = (status,sellerId,sellerName,projectpic,email)
    cursor.execute(sql3,val3)
    con.commit()        
    return redirect(url_for("status"))







@app.route('/buyersmyland',methods=['POST','GET'])
def buyersmyland():
    name = session["user"]
    buyer="NOT AVAILABLE"
    cursor.execute("SELECT * from addland where user=%s and buyer= %s;",(name,buyer))
    rows = cursor.fetchall()
    
    return render_template('buyersland.html',rows=rows)


@app.route('/booked',methods=['POST','GET'])
def booked():
    print("GET")
    if request.method == "GET":
        print("POST")
        user = session["user"]
        name=request.args.get("name")
        print(name)
        name =request.args.get("name")
        email = request.args.get("email")
        address = request.args.get("address")
        city = request.args.get("city")
        state = request.args.get("state")
        zip_code = request.args.get("zip_code")
        
        
        nameofcard = request.args.get("nameofcard")
        cardnumber =request.args.get("cardnumber")
        expmonth = request.args.get("expmonth")
        expyear = request.args.get("expyear")
        CVV = request.args.get("CVV")
        
        
        print("zjdhuhuo")
        
        
        print(name,email,address,city,state,zip_code,nameofcard,cardnumber,expmonth,expyear,CVV)
        con = dbConnection()
        cursor = con.cursor()
        sql2 = "INSERT INTO bankdetails(nameofcard,cardnumber,expmonth,expyear,CVV,zip_code,user) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val2 = (str(nameofcard), str(cardnumber), str(expmonth), str(expyear), str(CVV), str(zip_code), str(user))
        cursor.execute(sql2, val2)
     
        con = dbConnection()
        cursor = con.cursor()
        ccg="NOT AVAILABLE"
        print(ccg)
     
        sql1 = "UPDATE addland SET buyer = %s WHERE sellername = %s  AND Email = %s AND maplocation = %s AND city = %s  AND state = %s;"
        val1 = (ccg, str(name) ,str(email),str(address),str(city),str(state))
        cursor.execute(sql1,val1)
        con.commit()
        
        print("zjdhuhuo")
        
       
        
        
        return "success"
    
    return "success"




################################################buyer part###################################################################

if __name__ == "__main__":
    app.run("0.0.0.0")
    # app.run(debug=True)