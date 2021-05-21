from flask import Flask,render_template,request

import pyodbc

server = 'mcdev001.database.windows.net'
database = 'DMRE_Demo_1st'
username = 'mcroot'
password = 'mlG0klf$3_6r'   
driver= '{ODBC Driver 17 for SQL Server}'

def connectSQL():

    server = 'mcdev001.database.windows.net'
    database = 'DMRE_Demo_1st'
    username = 'mcroot'
    password = 'mlG0klf$3_6r'   
    driver= '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    print("SQL Connect OK")
    return conn,cursor

def closeSQL(_cursor,_conn):
    _cursor.close()
    _conn.close()
    print("SQL Close OK")
    return

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        text = "ここに結果が出力されます"
        return render_template("page.html",text=text)
    elif request.method == 'POST':
        name = request.form["name"]

        cn,cur = connectSQL()

        cur.execute("select * from Tbl_D_注文書番号")
        rows = cur.fetchall()

        closeSQL(cur,cn)

        text = "該当データなし"
        print()
        for r in rows:
            print(r[0])
            if int(name) == r[0]:
                text = "選択ID：" + name + "    該当内容：" + r[1]
                break
#            print(r[1])
#            print(r[2])
#            print(r[3])

        return render_template("page.html",text=text)

## 実行
if __name__ == "__main__":
    app.run(debug=True)