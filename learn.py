from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/skills')
def skill_page():
    items = [
        {
            'name': 'Java',
            'level': 'Intermediate',
            'percent': 70,
            'description': 'Object-oriented programming, collections, basic Spring Boot APIs'
        },
        {
            'name': 'Python',
            'level': 'Intermediate',
            'percent': 80,
            'description': 'Django web apps, Flask web apps, REST APIs, automation scripts'
        },
        {
            'name': 'JavaScript',
            'level': 'Intermediate',
            'percent': 65,
            'description': 'DOM manipulation, basic frontend logic'
        }
    ]
    return render_template('skills.html', items=items)

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}</h1>'