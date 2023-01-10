from flask import *
from werkzeug.utils import secure_filename

from src.dbop import *
app=Flask(__name__)
app.secret_key ="32"
@app.route('/')
def main():
     return render_template('login.html')
@app.route('/admin_home')
def admin_home():
    return render_template('admin home.html')
@app.route('/attendance')
def attendance():
    if 'lid' in session:

        qry="SELECT DISTINCT `date` FROM `attendence` WHERE `date`!=CURDATE()"
        res=selectall(qry)

        for r in res:
            qry="SELECT `staff`.`LID` FROM `staff` WHERE `LID` NOT IN(SELECT `sid` FROM `attendence` WHERE `date`=%s)"
            re=selectalls(qry,(r[0],))
            for rr in re:
                qry="INSERT INTO `attendence` VALUES(NULL,%s,%s,0)"
                val=(str(rr[0]),str(r[0]))
                iud(qry,val)

        qry = "SELECT `staff`.FNAME,`LNAME`,COUNT(*) twd,SUM(`attendance`) tpd ,ROUND((SUM(`attendance`)/COUNT(*))*100) AS attendance FROM staff JOIN `attendence` ON `attendence`.`sid`=`staff`.`LID` GROUP BY `attendence`.sid"
        res = selectall(qry)
        return render_template('attendance.html',val=res)
    else:
        return '''<script>alert('please login..........');window.location='/'</script>'''
@app.route('/mask_notification')
def mask_notification():
    if 'lid' in session:
        qry = "SELECT mask_violation.*,`staff`.`FNAME`,`LNAME` FROM mask_violation JOIN `staff` ON `mask_violation`.`uid`=`staff`.`LID`"
        res = selectall(qry)
        return render_template('mask notification.html', val=res)
    else:
        return '''<script>alert('please login..........');window.location='/'</script>'''
@app.route('/notification')
def notification():
    if 'lid' in session:
        qry = "select * from notification"
        res = selectall(qry)
        return render_template('notification.html',val=res)
    else:
        return '''<script>alert('please login..........');window.location='/'</script>'''
@app.route('/notification2',methods=['post'])
def notification2():
    return render_template('notification2.html')
@app.route('/staff_registration',methods=['post'])
def staff_registration():
    return render_template('staff registration.html')
@app.route('/work_allocation')
def work_allocation():
    if 'lid' in session:
        qry = "SELECT STAFF.FNAME,WORK.* FROM STAFF JOIN WORK ON STAFF.`LID`=`work`.`sid`"
        res = selectall(qry)
        return render_template('work allocation.html',val=res)
    else:
        return '''<script>alert('please login..........');window.location='/'</script>'''


@app.route('/work_allocation2',methods=['post'])
def work_allocation2():
    qry="SELECT*FROM`staff`"
    res=selectall(qry)
    return render_template('work allocation 2.html',val=res)
@app.route('/workallocation3',methods=['post'])
def workallocation():
    staffid=request.form['select']
    print(staffid)
    work=request.form['textfield2']
    print(work)
    description=request.form['textfield3']
    print(description)
    qry="insert into work values(null,%s,%s,%s,curdate(),'pending')"
    val=(str(staffid),work,description)
    iud(qry,val)
    return '''<script>alert('success');window.location='/work_allocation'</script>'''


@app.route('/staff_home')
def staff_home():
    return render_template('staff home.html')
@app.route('/view_work')
def view_work():
    return render_template('view work.html')
@app.route('/view_work2')
def view_work2():
    return render_template('view work2.html')
@app.route('/feedback')
def feedback():
    if 'lid' in session:
        qry="SELECT staff.fname,lname,feedback.feedback,date FROM staff JOIN feedback ON staff.lid=feedback.sid"
        res=selectall(qry)
        return render_template('feedback.html',val=res)
    else:
        return '''<script>alert('please login..........');window.location='/'</script>'''
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

@app.route('/login',methods=['post'])
def login():
    uname=request.form['textfield']
    pwd=request.form['textfield2']

    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(uname,pwd)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert('Invalid username or password');window.location='/'</script>'''
    else:
        session['lid']=res[0]
        return redirect('/admin_home')
@app.route('/addstaff',methods=['post'])
def addstaff():
    try:
        fisrtname=request.form['textfield']
        lastname=request.form['textfield2']
        gender=request.form['radiobutton']
        dob=request.form['textfield3']
        qualification=request.form.getlist('checkbox')
        post=request.form['textfield4']
        email=request.form['textfield5']
        phonenumber=request.form['textfield6']
        image=request.files['file']
        fname=secure_filename(image.filename)
        image.save('static/uploads/'+fname)
        username=request.form['textfield7']
        password=request.form['textfield8']
        qry="insert into login values(null,%s,%s,'staff')"
        val=(username,password)
        id=iud (qry,val)
        qry = "insert into staff values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id,fisrtname,lastname,gender,dob,qualification,post,phonenumber,email,fname)
        iud(qry, val)
        return '''<script>alert('registration success');window.location='/admin_home'</script>'''
    except Exception as e:
        print(str(e))
        if 'username' in str(e):
            return '''<script>alert('username already exist..........! ');window.location='/admin_home'</script>'''
        else:
            return '''<script>alert('email id already exist..........! ');window.location='/admin_home'</script>'''




@app.route('/addnotification',methods=['post'])
def addnotification():

    notification=request.form['textfield']
    qry = "insert into notification values(null,%s,curdate())"
    val = (notification)
    iud(qry,val)
    return '''<script>alert('insertion success');window.location='/notification'</script>'''
@app.route('/addviewstaff')
def addviewstaff():
    if 'lid' in session:
        qry="select * from staff"
        res=selectall(qry)
        return render_template('viewstaff.html',val=res)
    else:
        return '''<script>alert('Please Login...!');window.location='/admin_home'</script>'''
@app.route('/staffdelete')
def staffdelete():
    id=request.args.get('id')
    qry="delete from login where id =%s"
    iud(qry,id)
    qry = "delete from staff where lid =%s"
    iud(qry,id)
    return '''<script>alert('deleted');window.location='/addviewstaff'</script>'''
@app.route('/notificationdelete')
def notificationdelete():
    id=request.args.get('nid')
    qry="delete from notification where nid =%s"
    iud(qry,id)
    return '''<script>alert('deleted');window.location='/notification'</script>'''
@app.route('/workallocationdelete')
def workallocationdelete():
    id=request.args.get('work_id')
    qry="delete from work where work_id =%s"
    iud(qry,id)
    return '''<script>alert('deleted');window.location='/work_allocation'</script>'''
app.run(debug=True)

