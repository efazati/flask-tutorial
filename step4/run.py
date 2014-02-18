from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_with_base():
	return render_template('index.html')

@app.route("/msg/<msg>/")
def msg(msg):
	return render_template('msg.html', msg=msg)


@app.route('/default_msg/', defaults={'msg': 'there is no msg'})
@app.route("/default_msg/<msg>/")
def default_msg(msg):
	return render_template('msg.html', msg=msg)


if __name__ == "__main__":
    app.run()