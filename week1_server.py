from flask import Flask

app = Flask(__name__)

# members API Route


@app.route("/words")
def words():
    return {"words": ["This is week 1 Project", "To fetch the Word", "TALENT PLUS"]}


if __name__ == "__main__":
    app.run(debug=True)
