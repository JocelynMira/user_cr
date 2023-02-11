from flask import Flask, render_template, redirect, request
from user import User
app = Flask (__name__)

@app.route("/")
def index():
    #this is how we get data from db
    users = User.get_all()
    return render_template ('read.html', thiscanbeanything = users)

@app.route('/new_user')
def new_user():
    return render_template ('create.html')

@app.route("/create_user", methods=['POST'])
def create_user():
    #from user.py classmethod
    User.create_user(request.form)
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)