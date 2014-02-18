from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_with_base():
	return render_template('index.html')

@app.route("/msg/")
def msg():
	msg = "this is msg from your code!"
	return render_template('msg.html', msg=msg)

@app.route("/complex/")
def complex():
	msg = "this is msg from your code!"
	return render_template('complex.html', msg=msg)


if __name__ == "__main__":
    app.run()