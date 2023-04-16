# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Priyansh"
    age = "13"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Narayan" # write your name
    age = "45" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Madhu" # write your name
    age = "43" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Adi" # write your name
    age = "12" # write your age




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
