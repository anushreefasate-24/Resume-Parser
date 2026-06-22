from flask import Flask, render_template, request
import pdfplumber
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    return {
        "emails": emails,
        "preview": text[:500]
    }

if __name__ == '__main__':
    app.run(debug=True)