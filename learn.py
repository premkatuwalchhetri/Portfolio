from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/skills')
def skill_page():
    items = [
{'id': 1,'name':'java','barcode':'8456445464555','knowledge':'intermidiate'},
{'id': 2,'name':'python','barcode':'1255644546445','knowledge':'intermidiate'},
{'id': 3,'name':'javascript','barcode':'4326445464525','knowledge':'intermidiate'},
    ]
    return render_template('skills.html', items=items)

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}</h1>'