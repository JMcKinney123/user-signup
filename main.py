from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def basic():
    return render_template("indexhome.html")

@app.route("/answer", methods=['POST'])
def all():
    error_username = ""
    error_password = ""
    error_verify = ""
    error_email = ""

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    for i in username:
        if i.isspace():
            error_username = "Error: No spaces allowed in username."
    if username == "":
        error_username = "Error: Username is blank."
    elif len(username) < 3 or len(username) > 20:
        error_username = "Error: Username must be between 3 and 20 characters."
        username = ""
    
    for i in password:
        if i.isspace():
            error_password = "Error: No spaces allowed in password."
    if username == "":
        error_password = "Error: Password is blank."
    elif len(password) < 3 or len(password) > 20:
        error_password = "Error: Password must be between 3 and 20 characters."
        password = ""
    
    if verify == "":
        error_verify = "Error: Verification must match password."
    elif verify != password:
        error_verify = "Error: Verification must match password." 
        verify = ""
    
    for i in email:
        if i.isspace():
            error_email = "Error: Invalid email."
    if email != "" and ("." not in email or "@" not in email):
        error_email = "Error: Invalid email still."
    elif email != "" and len(email) < 3 or len(email) > 20: 
        error_email = "Error: Email must be between 3 and 20 characters."
        email = ""
        
    
    
    if not error_username and not error_password and not error_verify and not error_email:
        return render_template("welcome.html", username=username)
    else:    
        return render_template("indexhome.html", error_username=error_username, error_password=error_password, error_verify=error_verify, error_email=error_email)          
    

app.run()