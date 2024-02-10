from flask import Flask, render_template, request, url_for, redirect 
from email.mime.text import MIMEText 
import smtplib 
from email.message import EmailMessage 
from flask_font_awesome import FontAwesome

app = Flask(__name__) 
font_awesome = FontAwesome(app)

@app.route("/") 
def index(): 
	return render_template("index.html") 

@app.route("/sendemail/", methods=['POST']) 
def sendemail(): 
	if request.method == "POST": 
		name = request.form['name'] 
		email = request.form['_replyto'] 
		message = request.form['message'] 

		# Set your credentials 
		yourEmail = 'a819837d269f83'
		yourPassword = 'bdd904cee510ba'

		# Logging in to our email account 
		server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) 
		server.ehlo() 
		server.starttls() 
		server.login(yourEmail, yourPassword) 

		# Sender's and Receiver's email address 
		msg = EmailMessage() 
		msg.set_content("First Name : "+str(name) 
						+"\nEmail : "+str(email) 
						+"\nMessage : "+str(message)) 
		msg['To'] = email 
		msg['From'] = yourEmail 

		# Send the message via our own SMTP server. 
		try: 
			# sending an email 
			server.send_message(msg) 
			print("Send") 
		except: 
			print("Fail to Send") 
			pass
			
	return redirect('/') 

if __name__ == "__main__": 
	app.run(debug=True)
