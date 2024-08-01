from model.conn_creatTables.conn import conn

def All():
    req="SELECT * FROM Member ;"
    curs=conn.cursor()
    curs.execute(req)
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByNumber(number):
    req="SELECT * FROM Member WHERE IDMEMBER = %s;"
    curs=conn.cursor()
    curs.execute(req,(number,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByName(name):
    req="SELECT * FROM Member WHERE LASTNAMEMEMBER = %s;"
    curs=conn.cursor()
    curs.execute(req,(name,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByLogin(login):
    req="SELECT * FROM Member WHERE loginmember = %s;"
    curs=conn.cursor()
    curs.execute(req,(login,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows

