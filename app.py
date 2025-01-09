from flask import Flask, Response, render_template, request

app = Flask(__name__)

def is_mobile(user_agent):
    user_agent = user_agent.lower()
    return "iphone" in user_agent or "android" in user_agent

@app.route('/', methods=['GET', 'POST'])
def home():
    user_agent = request.headers.get('User-Agent')
    template = 'mobile.index.html' if is_mobile(user_agent) else 'desktop.index.html'
    return render_template(template)

@app.route('/english', methods=['GET', 'POST'])
def home_eng():
    user_agent = request.headers.get('User-Agent')
    template = 'mobile.en.index.html' if is_mobile(user_agent) else 'desktop.en.index.html'
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)
