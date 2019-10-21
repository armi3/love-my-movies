import os
import yaml
from flask import Flask, render_template

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fer González")
environment = os.getenv("ENVIRONMENT", "development")

with open('info.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)

print(info)
print(info['identities']['github'])


@app.route("/")
def home():
    return render_template("home.html", info=info)


@app.route("/list1")
def list1():
    return render_template("list1.html", info=info)


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    print("Local change.")
    app.run(host="0.0.0.0", debug=debug)
