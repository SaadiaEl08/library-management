from model.conn_creatTables.conn import conn

def All():
    req="SELECT * FROM loan;"
    curs=conn.cursor()
    curs.execute(req)
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByBookNumber(number):
    req="SELECT * FROM loan WHERE NUMBOOK = %s;"
    curs=conn.cursor()
    curs.execute(req,(number,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByMemberNumber(num):
    req="SELECT * FROM loan WHERE IDMEMBER = %s;"
    curs=conn.cursor()
    curs.execute(req,(num,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows


