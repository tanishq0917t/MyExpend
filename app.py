from flask import *
app = Flask(__name__)
@app.route('/authenticate',methods=['POST','GET'])
def upload():
    if request.method=="POST":
        a=request.form
        if a['us'].upper()=="*******" and a['ps']=="******":
            return render_template("upload.html")
        elif a['us'].upper()=="*****" and a['ps']=="******":
            return render_template("upload.html")
        else:
            return render_template("index.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start',methods=['POST','GET'])
def setUp():
    if request.method=="POST":
        a=request.form
        if a['user'].upper()=="*****":
            with open("****.txt","a+") as file:
                file.write(a['amount'])
                file.write("\n")
            return "1"
        elif a['user'].upper()=="****":
            with open("****.txt","a+") as file:
                file.write(a['amount'])
                file.write("\n")
            return "1"
        else:
            return "0"
if __name__ == '__main__':
    app.run(debug = True)
