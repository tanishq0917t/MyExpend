from flask import *
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("upload.html")

@app.route('/view')
def vv():
    return render_template("a.html")

@app.route('/start',methods=['POST','GET'])
def setUp():
    if request.method=="POST":
        a=request.form

        fname=""
        if a['user'].upper()=="TANISHQ" and a['pass']=="Tanishq@1710h": fname="tanishq.txt"
        elif a['user'].upper()=="HONEY" and a['pass']=="Tanishq@1710h": fname="honey.txt"
        else: return "0"
        with open(fname,"a+") as file:
            d=str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year)
            file.write(d)
            file.write("\n")
            file.write(a['amount'])
            file.write("\n")
            file.write(a['note'])
            file.write("\n")
        return "1"

@app.route('/give',methods=['POST','GET'])
def set():
    if request.method=="POST":
        a=request.form
        fname=""
        if a['user'].upper()=="TANISHQ" and a['pass']=="Tanishq@1710h": fname="tanishq.txt"
        elif a['user'].upper()=="HONEY" and a['pass']=="Tanishq@1710h": fname="honey.txt"
        else: return "0"
        a=open(fname,"r").read().strip()
        a=a.split("\n")
        print(a)
        aa=""
        for i in a:
            aa+=i
            aa+=","
        aa=aa[0:-1]
        return aa
        
if __name__ == '__main__':
    app.run(debug = True)
