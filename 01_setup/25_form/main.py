from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        with open("file.txt", "w") as f:
            f.write(f"My name is {request.form['Name']} and my email id is {request.form['Email']}")
        return render_template("home.html")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)


'''
@app.route("/", methods=['GET', 'POST'])

✔ Defines the home page (/) that can handle both GET and POST requests.

🔹if request.method == 'POST':
    with open("file.txt", "w") as f:
        f.write(f"My name is {request.form['Name']} and my email id is {request.form['Email']}")
        
✔ Checks if the request is POST → Meaning the user has submitted the form.
✔ Opens file.txt in write mode ("w") → Saves user input inside the file.
✔ Writes user details (Name, Email) using request.form[]. 
'''