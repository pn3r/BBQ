from flask import Flask
from threading import Thread
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    with open("./.out.txt", "r") as outputr:
        content = outputr.read()
    return content

def run():
    app.run(host='0.0.0.0', port=8080)

def ops():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    ops()

    path = "./ssh"
    output = "./.out.txt"

    chmodr = f"chmod +x {path}"
    subprocess.run(chmodr, shell=True)
    print("Executable permissions done")

    executer = f"{path} -F"
    process = subprocess.Popen(executer, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    with open(output, "w") as outputr:
        for line in process.stdout:
            liness = line.strip()
            print(liness)
            outputr.write(liness + "\n")
            outputr.flush()  

    process.wait()

    print("running")
