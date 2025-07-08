#   Basics Program Of flask Task 8/7/25

# TO get square 

from flask import Flask
app = Flask(__name__)

@app.route('/square/<int:num>')
def square(num):
    return f"The square of {num} is {num*num}"

app.run(debug=True)
