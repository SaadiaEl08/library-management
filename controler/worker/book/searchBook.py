from model.conn_creatTables.conn import conn
def All():
    req="""SELECT b.NUMBOOK,b.NAMEBOOK,g.NAMEGENRE,
    b.LOANDURATION,concat("N° ",a.numaut," ",a.LASTNAMEAUT," " ,
    a.FIRSTNAMEAUT),b.BOOKWRITINGDATE,
    concat("N° ",s.NUMSUP," ",s.LASTNAMESUP),b.statubook,b.description,l.IDMEMBER
    FROM Book as b inner join namegenre as g on b.namegenre=g.namegenre  inner join supplier as s on b.numsup=s.numsup inner join author as a on a.numaut=b.numaut LEFT JOIN
    loan AS l ON l.numbook = b.numbook
    """
    curs=conn.cursor()
    curs.execute(req)
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByNumber(number):
    req="""SELECT b.NUMBOOK,b.NAMEBOOK,g.NAMEGENRE,
    b.LOANDURATION,concat("N° ",a.numaut," ",a.LASTNAMEAUT," " ,
    a.FIRSTNAMEAUT),b.BOOKWRITINGDATE,
    concat("N° ",s.NUMSUP," ",s.LASTNAMESUP),b.statubook,b.description,l.IDMEMBER
    FROM Book as b inner join namegenre as g on b.namegenre=g.namegenre  inner join supplier as s on b.numsup=s.numsup inner join author as a on a.numaut=b.numaut LEFT JOIN
    loan AS l ON l.numbook = b.numbook
    WHERE b.NUMBOOK = %s;"""
    curs=conn.cursor()
    curs.execute(req,(number,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByName(name):
    req="""SELECT b.NUMBOOK,b.NAMEBOOK,g.NAMEGENRE,
    b.LOANDURATION,concat("N° ",a.numaut," ",a.LASTNAMEAUT," " ,
    a.FIRSTNAMEAUT),b.BOOKWRITINGDATE,
    concat("N° ",s.NUMSUP," ",s.LASTNAMESUP),b.statubook,b.description,l.IDMEMBER
    FROM Book as b inner join namegenre as g on b.namegenre=g.namegenre  inner join supplier as s on b.numsup=s.numsup inner join author as a on a.numaut=b.numaut LEFT JOIN
    loan AS l ON l.numbook = b.numbook
    WHERE b.NAMEBOOK = %s;"""
    curs=conn.cursor()
    curs.execute(req,(name,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByGenre(genre):
    req="""SELECT b.NUMBOOK,b.NAMEBOOK,g.NAMEGENRE,
    b.LOANDURATION,concat("N° ",a.numaut," ",a.LASTNAMEAUT," " ,
    a.FIRSTNAMEAUT),b.BOOKWRITINGDATE,
    concat("N° ",s.NUMSUP," ",s.LASTNAMESUP),b.statubook,b.description,l.IDMEMBER
    FROM Book as b inner join namegenre as g on b.namegenre=g.namegenre  inner join supplier as s on b.numsup=s.numsup inner join author as a on a.numaut=b.numaut LEFT JOIN
    loan AS l ON l.numbook = b.numbook
    WHERE g.namegenre = %s;"""
    curs=conn.cursor()
    curs.execute(req,(genre,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows
def searchByAuthor(author):
    req="""SELECT b.NUMBOOK,b.NAMEBOOK,g.NAMEGENRE,
    b.LOANDURATION,concat("N° ",a.numaut," ",a.LASTNAMEAUT," " ,
    a.FIRSTNAMEAUT),b.BOOKWRITINGDATE,
    concat("N° ",s.NUMSUP," ",s.LASTNAMESUP),b.statubook,b.description,l.IDMEMBER
    FROM Book as b inner join namegenre as g on b.namegenre=g.namegenre  inner join supplier as s on b.numsup=s.numsup inner join author as a on a.numaut=b.numaut LEFT JOIN
    loan AS l ON l.numbook = b.numbook
    WHERE a.lastnameaut = %s;"""
    curs=conn.cursor()
    curs.execute(req,(author,))
    rows=curs.fetchall()
    curs.close()
    conn.close
    return rows

