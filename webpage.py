import flask


webpage=flask.Flask(__name__)

@webpage.route("/")
def first_page():
    return flask.render_template("login.html")

@webpage.route("/newuser")
def second_page():
    return flask.render_template("newuserregister.html")

@webpage.route("/registeruser", methods=['post'])
def third_page():
    entered_username=flask.request.form.get("username")
    entered_password=flask.request.form.get("password")
    entered_email=flask.request.form.get("email")
    entered_location=flask.request.form.get("location")
    import sqlite3
    con=sqlite3.connect("my_database.sqlite3")
    cur=con.cursor()
    my_table_query="create table if not exists userstable(name varchar(50),password varchar(50),email varchar(50),location varchar(50))"
    cur.execute(my_table_query)
    cur.execute(f"select email from userstable where email='{entered_email}'")
    result=cur.fetchone()
    if result!=None:
        return "This email is already registered! Try to login with other account."
    else:
        my_insert_query=f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_location}')"
        cur.execute(my_insert_query)
        con.commit()
        return "Successfully registered"


if __name__=="__main__":
    webpage.run(debug=True) 