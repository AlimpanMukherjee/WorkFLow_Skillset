#In  this we will serve t=static files in our website
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(port=8000,debug=True)


#here in the home.html page we wil have to provide the tag that will  help to download the file
#The file that we will be downloading from the website should be present inside the static folder