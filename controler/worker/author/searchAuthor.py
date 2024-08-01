from model.conn_creatTables.conn import conn
def All():
    req="SELECT * FROM author"
    curs=conn.cursor()
    curs.execute(req)
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByNumber(number):
    req="SELECT * FROM author WHERE NUMAUT = %s;"
    curs=conn.cursor()
    curs.execute(req,(number,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByName(name):
    req="SELECT * FROM author WHERE LASTNAMEAUT = %s;"
    curs=conn.cursor()
    curs.execute(req,(name,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByNumBook(numBook):
    req="""select a.*
        from  author as a inner join book as b on b.numaut = a.numaut
        where NUMBOOK=%s"""
    curs=conn.cursor()
    curs.execute(req,(numBook,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows

