from flask import Flask,render_template,request
import requests
import smtplib
import os

print(__name__)
app = Flask(__name__)

url = 'https://api.npoint.io/43644ec4f0013682fc0d'
posts = requests.get(url).json()

for post in posts:
    post['author'] = 'Cyrus'


@app.route('/')
def home():
    return render_template('index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html',message_sent=False)
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        my_email = "calcguru2020@gmail.com"
        to_address = "ctabatab@gmail.com"
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=os.environ.get('PASSWORD'))
            connection.sendmail(from_addr=my_email,to_addrs=to_address,msg=f"Subject: Contact!\n\nName: {name}\n Email: {email}\n Phone: {phone}\nMessage: {message}")
        
        return render_template('contact.html',message_sent=True)

@app.route('/post/<int:post_id>')
def get_post(post_id):

    for post in posts:
        if post["id"] == post_id:
            break


    return render_template('post.html',post=post)






    
if __name__ == "__main__":
    
    app.run(debug=True)

