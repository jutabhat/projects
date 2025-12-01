from flask import Flask, render_template, request

app = Flask(__name__)

image_url = "https://img.freepik.com/free-vector/gradient-ui-ux-elements-background_23-2149056159.jpg?semt=ais_hybrid&w=740&q=80"
response_text1 = "Hi Everyone,"
response_text2 = "This is a simple web application."

@app.route('/')
def content():
    browser_headers = request.headers
    return render_template('index.html', text1=response_text1, text2=response_text2, image_url=image_url)

#if __name__ == '__main__':
#    app.run(debug=True)
