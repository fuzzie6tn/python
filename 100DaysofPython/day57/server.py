from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year=datetime.datetime.now().year
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')

def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_response = requests.get(age_url)
    age_data= age_response.json()
    age = age_data["age"]

    return render_template("guess.html", name=name, gender=gender,age=age) # extracted from genederize.io

@app.route('/blog')

def blog(): #fetch all the blogs from the URL
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__== '__main__':
    app.run(debug=True)