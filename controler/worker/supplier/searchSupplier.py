from model.conn_creatTables.conn import conn

def All():
    req = "SELECT * FROM SUPPLIER ;"
    curs = conn.cursor()
    curs.execute(req)
    rows = curs.fetchall()
    curs.close()
    conn.close   
    return rows

def searchByNumber(number):
    req = "SELECT * FROM SUPPLIER WHERE NUMSUP = %s;"
    curs = conn.cursor()
    curs.execute(req, (number,))
    rows = curs.fetchall()
    curs.close()
    conn.close
    return rows

def searchByName(name):
    req = "SELECT * FROM SUPPLIER WHERE LASTNAMESUP = %s;"
    curs = conn.cursor()
    curs.execute(req, (name,))
    rows = curs.fetchall()
    curs.close()
    conn.close
    return rows
