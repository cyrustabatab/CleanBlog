from flask import Flask,render_template
import requests

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def get_post(post_id):

    for post in posts:
        if post["id"] == post_id:
            break


    return render_template('post.html',post=post)

if __name__ == "__main__":
    
    app.run(debug=True)

