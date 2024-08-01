from model.conn_creatTables.conn import conn
def All():
    req="SELECT * FROM namegenre ;"
    curs=conn.cursor()
    curs.execute(req)
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByName(name):
    req="SELECT * FROM namegenre WHERE NAMEGENRE = %s;"
    curs=conn.cursor()
    curs.execute(req,(name,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows

