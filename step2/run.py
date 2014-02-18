from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_with_template():
	return render_template('hello.html')

@app.route("/well/")
def well_hello_with_template():
	return render_template('well_hello.html')

@app.route("/again/")
def again_hello_with_template():
	return render_template('again_hello.html')

if __name__ == "__main__":
    app.run()