from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={'Jack':87,'Jill':98}
    return  jsonify(marks)

app.run(debug=True)