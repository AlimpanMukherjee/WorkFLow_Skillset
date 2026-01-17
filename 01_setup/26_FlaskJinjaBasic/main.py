from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    students={'John':87,'Jill':98,'Jack':85,'Jenny':56}
    return render_template("index.html",students=students)
              

if __name__ == "__main__":
    app.run(port=8000, debug=True)