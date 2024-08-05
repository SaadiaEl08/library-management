from model.conn_creatTables.conn import conn
def modify(id,book):
    req="""UPDATE `db_library`.`book` set
    
    `NAMEBOOK`= %s,
    `LOANDURATION`=%s,
    `STATUBOOK`=%s,
    `NAMEGENRE`=%s,
    `NUMSUP`=%s,
    `NUMAUT`=%s,
    `BOOKWRITINGDATE`=%s,
    `DESCRIPTION`=%s
    where `NUMBOOK`=%s 
    """
    try:
       curs=conn.cursor()
       curs.execute(req,(book.NAMEBOOK,book.LOANDURATION,book.STATUBOOK,book.NAMEGENRE,book.NUMSUP,book.NUMAUT,book.BOOKWRITINGDATE,book.DESCRIPTION,id))
       conn.commit()
       curs.close()
       conn.close
       return True
    except:
       return False