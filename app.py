from flask import *
import datetime
from fpdf import FPDF

# Populating DS starts here


credentials=dict()

def loadData():
    f = open('data.json')
    data = json.load(f)
    for i in data:
        credentials[i['user']]=(i['pass'],i['file'])
    print(credentials)

loadData()

# Populating DS ends here


app = Flask(__name__)


# Public URL Mapping Starts here

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("upload.html")

@app.route('/view')
def vv():
    return render_template("a.html")

@app.route('/conf')
def cnf():
    return render_template("configuration.html")

# Public URL Mapping Ends here
#-----------------------------------------------------------------------------------

# Private URL Mapping Starts here

@app.route('/change',methods=['POST','GET'])    #Function to change password
def change():
    if request.method=="POST":
        oldPass=request.form['pass']
        newPass=request.form['newPass']
        inpUser=request.form['user']

        print(oldPass,newPass,inpUser)
        if credentials[inpUser]==None:
            return "0"
        if credentials[inpUser][0]!=oldPass:
            print("Password doesn't match")
            return "0"

        
        credentials[inpUser]=(newPass,credentials[inpUser][1])
        applyChanges()
        return "1"

def applyChanges():     #Utility function for changing password
    newData=[]
    for i in credentials:
        newData.append({"user":i,"pass":credentials[i][0],"file":credentials[i][1]})

    print(newData)

    with open('data.json', 'w') as f:
        json.dump(newData, f, indent=2)


@app.route('/start',methods=['POST','GET'])     #Function to add details
def setUp():
    if request.method=="POST":
        inpUser=request.form['user']
        inpPass=request.form['pass']
        amount=request.form['amount']
        note=request.form['note']
        fname=""
        if credentials[inpUser]!=None and credentials[inpUser][0]==inpPass:
            fname=credentials[inpUser][1]
        else:
            return "0"
        with open(fname,"a+") as file:
            d=str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year)
            file.write(d)
            file.write("\n")
            file.write(amount)
            file.write("\n")
            file.write(note)
            file.write("\n")
        return "1"

@app.route('/give',methods=['POST','GET'])      #Function to view transactions
def set():
    if request.method=="POST":
        inpUser=request.form['user']
        inpPass=request.form['pass']
        fname=""
        if credentials[inpUser]!=None and credentials[inpUser][0]==inpPass:
            fname=credentials[inpUser][1]
        else:
            return "0"
        a=open(fname,"r").read().strip()
        a=a.split("\n")
        print(a)
        aa=""
        for i in a:
            aa+=i
            aa+=","
        aa=aa[0:-1]
        if len(aa)==0:
            aa="None"
        return aa

@app.route('/download',methods=['POST','GET'])      #Function to create PDF
def requestPDF():
    inpUser=request.form['us']
    inpPass=request.form['ps']
    fname=""
    if credentials[inpUser]!=None and credentials[inpUser][0]==inpPass:
        fname=credentials[inpUser][1]
    else:
        return "0"
    dd=open(fname,"r").read().strip()
    dd=dd.split("\n")
    data=[]
    i=0
    x=1
    while(i<len(dd)):
        a=[]
        a.append(str(x))
        a+=dd[i:i+3]
        data.append(a)
        i+=3
        x+=1
    header=[['S.No','Date','Amount','Title']]
    pdf=FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times','',10.0) 
    epw = pdf.w - 2*pdf.l_margin
    col_width = epw/4
    th = pdf.font_size
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'MyExpend Summary', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(0.5)

    for row in header:
        for datum in row:
            pdf.cell(col_width, 2*th, str(datum), border=1)
        pdf.ln(2*th)

    for row in data:
        for datum in row:
            pdf.cell(col_width, 2*th, str(datum), border=1)
        pdf.ln(2*th)

    pdf.output('summary.pdf','F')
    return send_file('summary.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug = True)
