from flask import Flask, render_template, request, jsonify, redirect
from flask_mail import Mail, Message
import re

app = Flask(__name__)

#app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_PORT'] = 465
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME']='ojasok@gmail.com'
#app.config['MAIL_PASSWORD ']='12ka4mynameisojas'



####Adding extra fields here

from flask.ext.mail import Mail, Message
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ojasok@gmail.com'
app.config['MAIL_PASSWORD'] = '12ka4mynameisojas'
app.config['DEFAULT_MAIL_SUBJECT'] = 'Tesst Email'
app.config['DEFAULT_MAIL_SENDER'] = 'Admin <ojasok@gmail.com>'
app.config['SECRET_KEY'] = 'akcjbakjsckjassn'
app.config['DEFAULT_ADMIN'] = 'Admin <ojasok@gmail.com>'

##those end here


mail = Mail(app)
 

@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template ("about.html")    

@app.route("/gallery")
def gallery():
    return render_template ("gallery.html")  

@app.route("/blog")
def blog():
    return render_template ("blog.html")  


    	
@app.route("/contact", methods = ['POST','GET'])
def contact():
    if request.method == 'POST':
        m= request.form['message']
        e= request.form['email']
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        if not re.match(pattern, e):
            return render_template ("contact.html", err="Please Enter the valid Email Address")    

        n= request.form['name']
        m += " "+ "sent by: "+n+"  Email: "+e 
        msg = Message(m,sender="ojasok@gmail.com",recipients=['ojasok@gmail.com'])
        mail.send(msg)
        return render_template ("contact.html", err="Message has been sent successfully!!")

    else:
    	print "In GET"
        return render_template ("contact.html")  

if __name__ == "__main__":
    app.run(debug = True)