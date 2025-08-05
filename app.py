from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 IBM Cloud Code Engine Flask App</h1>
    <p>This application is live on <strong>IBM Cloud</strong> using <em>Code Engine</em> with CI/CD integration.</p>
    <p>Edit this message on <a href='https://github.com/ArjunJagdale/flask-on-codeengine' target='_blank'>GitHub</a> and push to automatically redeploy.</p>
    <p><small>Deployed using IBM Toolchain & Cloud CLI • Region: us-south</small></p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
