from flask import Flask, render_template, redirect, request
from user import User
app = Flask (__name__)


# route to create page
@app.route('/new_user')
def new_user():
    return render_template ('create.html')

# CREATE
@app.route("/create_user", methods=['POST'])
def create_user():
    # from user.py classmethod
    # if you name attributes in your html the same as columns in db, you can just pass request.form 
    User.create_user(request.form)
    return redirect ('/home')

# READ
@app.route("/home")
def get_all():
    #this is how we get data from db
    users = User.get_all()
    return render_template ('read.html', thiscanbeanything = users)

@app.route("/display_one/<int:id>")
def get_one(id):
    user = User.get_one(id)
    return render_template ('read_one.html', user = user)

#edit user
@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = User.get_one(id)
    return render_template ('update.html', user = user) 


# UPDATE
@app.route('/update_user/<int:id>', methods=['POST'])
def update(id):
    # need to bring in the whole dictionary from server
    data = { 'id':id,
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email': request.form['email']}
    User.update(data)
    return redirect (f"/display_one/{request.form['id']}")

# DELETE
@app.route('/delete_user/<int:id>')
def delete(id):
    User.delete(id)
    return redirect ('/home')



if __name__ == "__main__":
    app.run(debug=True)