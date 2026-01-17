from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # name="Ali"
    # token=1287
    if 'name' in request.args and 'tokens' in request.args:
        name = request.args['name']
        token = request.args['tokens']
        return render_template("index.html", name=name, token=token)
    else:
        return "Please provide both 'name' and 'tokens' as query parameters."

##we can also change the way we access the static file while running the link we will be directed to a page then 
##from there in the url we will have to add "eg.  /?name=Alimpan&tokens=9876 "


app.run(port=8000,debug=True)