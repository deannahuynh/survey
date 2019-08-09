from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def surveyInput():
    print("Survey info received!")
    print(request.form)
    return render_template('info.html', name=request.form["name"], location=request.form['location'], language=request.form["language"], interest=request.form.getlist('interest'), comment=request.form["comment"])

if __name__=="__main__":
    app.run(debug=True)
