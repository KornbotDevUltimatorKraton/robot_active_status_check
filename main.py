from flask import Flask,render_template,url_for,redirect,jsonify,request 

app = Flask(__name__) 


@app.route("/")
def index():

     return render_template("index.html")
@app.route("/router_status")
def router_status():

     return render_template("index2.html")
if __name__ == "__main__":

        app.run(debug=True,threaded=True,host="0.0.0.0",port=9567)
