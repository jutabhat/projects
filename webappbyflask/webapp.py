from flask import Flask, render_template, request

app = Flask(__name__)

image_url = "https://img.freepik.com/free-photo/representations-user-experience-interface-design_23-2150104516.jpg?semt=ais_hybrid&w=740&q=80"
response_text1 = "Hi Everyone"
response_text2 = "This is my simple web application for learning Phython and HTML"

@app.route('/')
def content():
    browser_headers = request.headers
    return render_template('index.html', text1=response_text1, text2=response_text2, image_url=image_url, headers=browser_headers)

#if __name__ == '__main__':
#    app.run(debug=True)

