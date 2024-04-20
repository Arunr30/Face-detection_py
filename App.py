from flask import Flask, render_template, request, session, flash

import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/OfficerLogin')
def OfficerLogin():
    return render_template('OfficerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("you are successfully Login")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AComplaintInfo")
def AComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb  where Status='waiting' ")
    data = cur.fetchall()
    return render_template('AComplaintInfo.html', data=data)



@app.route("/FindInfo")
def FindInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb  where Status='find' ")
    data = cur.fetchall()
    return render_template('FindInfo.html', data=data)

@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash('Username or Password is wrong')
            return render_template('UserLogin.html', data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()
            flash("you are successfully logged in")
            return render_template('UserHome.html', data=data)


@app.route("/NewComplaint")
def NewComplaint():
    return render_template('NewComplaint.html', uname=session['uname'])


@app.route("/newcomplaint", methods=['GET', 'POST'])
def newcomplaint():
    if request.method == 'POST':
        uname = session['uname']
        name = request.form['name']
        umobile = request.form['mobile']
        email = request.form['email']
        Address = request.form['address']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = name + ".png"
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  username='" + uname + "'")
        data = cursor.fetchone()

        if data:
            mobile = data[2]

        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into complainttb values('','" + uname + "','" + mobile + "','" + name + "','" + umobile + "','" + email + "','" + Address + "','" + savename + "','waiting','')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM complainttb where username='" + uname + "'  ")
        data = cur.fetchall()
        flash('Complaint Post Successfully!')
        return render_template('UComplaintInfo.html', data=data)


@app.route("/UComplaintInfo")
def UComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where username='" + session['uname'] + "' and Status='waiting' ")
    data = cur.fetchall()
    return render_template('UComplaintInfo.html', data=data)


@app.route("/UActionInfo")
def UActionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where username='" + session['uname'] + "' and Status !='waiting' ")
    data = cur.fetchall()
    return render_template('UActionInfo.html', data=data)


@app.route("/action")
def action():
    id = request.args.get('id')
    session["cid"] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
    data = cursor.fetchone()

    if data:
        Image = data[7]

    else:
        return 'Incorrect username / password !'

    return render_template('Action.html', face=Image)



@app.route("/action1")
def action1():
    id = request.args.get('id')
    session["cid"] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
    data = cursor.fetchone()

    if data:
        Image = data[7]

    else:
        return 'Incorrect username / password !'

    return render_template('Action1.html', face=Image)

@app.route("/predictvideo", methods=['GET', 'POST'])
def predictvideo():
    if request.method == 'POST':
        print( request.form['submit'])
        if  request.form['submit'] != 'Camera':
            location = request.form['location']
            import random
            file = request.files['file']
            file.save("static/video/" + file.filename)

            id = session["cid"]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
            data = cursor.fetchone()

            if data:
                mobile = data[2]
                MName = data[3]

                imagea = data[7]
            else:
                return 'Incorrect username / password !'

            import cv2
            frame_out = 0
            from simple_facerec import SimpleFacerec

            # Encode faces from a folder
            sfr = SimpleFacerec()
            sfr.load_encoding_images("static/upload/")

            # Load Camera
            cap = cv2.VideoCapture('static/video/' + file.filename)

            while True:
                ret, frame = cap.read()
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

                # Detect Faces
                face_locations, face_names = sfr.detect_known_faces(frame)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                    if name == MName:
                        frame_out += 1
                        print(frame_out)

                        if frame_out >= 20:
                            msg = "Person find Location " + location
                            sendmsg(mobile, msg)

                            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                           database='1facevideodb')
                            cursor = conn.cursor()
                            cursor.execute(
                                "update   complainttb set 	Location='" + msg + "',Status='find' where id='" + id + "'")
                            conn.commit()
                            conn.close()

                            cap.release()
                            cv2.destroyAllWindows()

                            return render_template('AComplaintInfo.html')

                cv2.imshow("Frame", frame)

                key = cv2.waitKey(1)
                if key == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

            return render_template('AComplaintInfo.html')
        else:

            location = request.form['location']
            import random

            id = session["cid"]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facevideodb')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
            data = cursor.fetchone()

            if data:
                mobile = data[2]
                MName = data[3]

                imagea = data[7]
            else:
                return 'Incorrect username / password !'

            import cv2
            frame_out = 0
            from simple_facerec import SimpleFacerec

            # Encode faces from a folder
            sfr = SimpleFacerec()
            sfr.load_encoding_images("static/upload/")

            # Load Camera
            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

                # Detect Faces
                face_locations, face_names = sfr.detect_known_faces(frame)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                    if name == MName:
                        frame_out += 1
                        print(frame_out)

                        if frame_out >= 10:
                            msg = "Person find Location " + location
                            sendmsg(mobile, msg)

                            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                           database='1facevideodb')
                            cursor = conn.cursor()
                            cursor.execute(
                                "update   complainttb set 	Location='" + msg + "',Status='find' where id='" + id + "'")
                            conn.commit()
                            conn.close()
                            cap.release()
                            cv2.destroyAllWindows()
                            return render_template('AComplaintInfo.html')

                cv2.imshow("Frame", frame)

                key = cv2.waitKey(1)
                if key == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

            return render_template('AComplaintInfo.html')




def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
