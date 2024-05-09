from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Verify if the request is from GitHub if necessary
        # Execute git pull
        print("Success")
        subprocess.call(['git', 'pull'])
        return 'Success', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
