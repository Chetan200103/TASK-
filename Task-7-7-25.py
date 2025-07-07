
" ROUTING IN FLASK TASK 7/7/25"

 # HELLO WORLD PROGRAM
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello Wtt  company'

# ABOUT PAGE
@app.route("/about")
def about():
    return 'This is simple about us page'

# USER NAME AND AGE 
@app.route("/user/<username>/<age>")
def show_user_profile(username,age):
    return "user %s,%s" % (username,age)

##  numerical variable to check post 

@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return "post id %s" % post_id

## float variable to check price 

@app.route('/price/<float:amount>')
def show_price(amount):
    return "price is %s" % amount

# route with GET method only 
@app.route('/get-only', methods=['GET'])
def get_only():
    return "Only GET allowed"

# GET - Post Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Login Page (GET or POST)"

if __name__ == '__main__':  
    app.run(debug=True)
