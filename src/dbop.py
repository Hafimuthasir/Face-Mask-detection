import pymysql
from flask import jsonify



def iud(qry,val):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='face_mask')
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=con.insert_id()
    con.commit()
    cmd.close()
    con.close()
    return id

def selectone(qry,val):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='face_mask')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()
    con.commit()
    cmd.close()
    con.close()
    return res

def selectall(qry):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='face_mask')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    con.commit()
    cmd.close()
    con.close()
    return res
def selectalls(qry,val):
    con=pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='face_mask')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    con.commit()
    cmd.close()
    con.close()
    return res


def androidselectall(q):
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='face_mask')
    cmd = con.cursor()
    cmd.execute(q)
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)



def androidselectallnew(q,val):
    con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='face_mask')
    cmd = con.cursor()
    cmd.execute(q,val)
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)
