from flask import *


from src.dbop import *
app=Flask(__name__)
app.secret_key ="32"

@app.route("/logincode",methods=['post'])
def logincode():
    uname=request.form['username']
    password=request.form['password']
    qry="select * from login where username=%s and password=%s and usertype='staff'"
    val=uname,password
    res=selectone(qry,val)
    if res is None:
        return jsonify({'task': 'invalid'})
    else:
        return jsonify({'task': 'success','lid':res[0]})

@app.route("/viewwork",methods=['post'])
def viewwork():
    staffid=request.form['staffid']
    print(staffid)
    qry="select * from work where sid=%s and status='pending'"
    val=(staffid)
    res=androidselectallnew(qry,val)

    return (res)

@app.route("/updatework",methods=['post'])
def updatework():
    wid=request.form['wid']
    status=request.form['status']
    qry="update work set status=%s where work_id=%s"
    val=(status,wid)
    iud(qry,val)
    return jsonify({'task': 'success'})

@app.route("/feedback",methods=['post'])
def feedback():
    staffid=request.form['staffid']
    feedback=request.form['feedback']
    print(staffid)
    qry="insert into feedback values(null,%s,%s,curdate())"
    val=(staffid,feedback)
    iud(qry,val)
    return jsonify({'task': 'success'})

@app.route("/viewfeedback",methods=['post'])
def viewfeedback():
    staffid=request.form['staffid']
    qry="select*from feedback where sid=%s"
    val=(staffid)
    res=androidselectallnew(qry,val)
    return (res)

@app.route("/viewnotification",methods=['post'])
def viewnotification():

    qry="select*from notification "
    res=androidselectall(qry)
    return (res)



app.run(host="0.0.0.0", port=5000)