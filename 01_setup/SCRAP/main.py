from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API keys for NewsAPI and GNews
NEWS_API_KEY = "476854c16d91497b8b44f5d4e09361eb"
GNEWS_API_KEY = "caafc58195a6118dd6a6d6e7924dfa15"

@app.route("/", methods=['GET', 'POST'])
def home():
    articles = []

    if request.method == "POST":
        choice = request.form.get("choice")  # ✅ Correctly retrieve the choice
        topic = request.form.get("topic")

        print(f"User selected: {choice}")  # ✅ Debugging choice selection

        if choice == "1":
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
        elif choice == "2":
            url = f"https://gnews.io/api/v4/search?q={topic}&apikey={GNEWS_API_KEY}"
        else:
            return "Invalid choice."

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

    return render_template("home.html", articles=articles)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
