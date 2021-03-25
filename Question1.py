from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Please input a string through the URL :)"

@app.route("/<name>")
def generateResponse(name):
    new_name = ""
    if name.isalpha():
        for ch in name:
            if ch.islower():
                new_name += ch.upper()
            else:
                new_name += ch.lower()
    else:
        for ch in name:
            if ch.isalpha():
                new_name += ch
    return "Welcome to our new website, " + new_name + "!"

if __name__ == "__main__":
    app.run(debug=True)
        
