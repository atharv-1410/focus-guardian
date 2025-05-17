from flask import Flask
import subprocess

app = Flask(__name__)
process = None

@app.route("/")
def start_guardian():
    global process
    if not process:
        process = subprocess.Popen(["python", "guardian.py"])
        return "Started"
    return "Already running"


if __name__ == "__main__":
    app.run(debug=False, port=5000)
