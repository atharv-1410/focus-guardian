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
    port = int(os.environ.get("PORT", 5000))  # default to 5000 if PORT not set
    app.run(host="0.0.0.0", port=port)
