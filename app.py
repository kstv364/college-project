from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os


dirpath = os.getcwd()
print("current directory is : " + dirpath)


app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def home():
    if request.method == 'POST':
        abstract = request.form['text']

        # call predict
        # something like 
        # result , unklist = model.predct(abstract = abstract)

        result = None
        unklist = ["test","A","b"]

        result = result if result else abstract


        return render_template('home.html', abstract=abstract, result=abstract, unklist=unklist)
    return render_template('home.html')


@app.route("/clear")
def clear():
    return render_template('home.html')


if __name__ == '__main__':


    ## INit model here
    ## model = load_model()

    app.run(debug=True)
