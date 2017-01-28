from flask import Flask, render_template, request, jsonify, redirect
from flask_mail import Mail, Message
import re
import os
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)




app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ojasok@gmail.com'
app.config['MAIL_PASSWORD'] = ''
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

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)