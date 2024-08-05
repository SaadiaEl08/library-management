from model.conn_creatTables.conn import conn
def addBook(book):
    req=f"""INSERT INTO `db_library`.`book`
    (
    `NAMEBOOK`,
    `LOANDURATION`,
    `STATUBOOK`,
    `NAMEGENRE`,
    `NUMSUP`,
    `NUMAUT`,
    `BOOKWRITINGDATE`,
    `DESCRIPTION`)
    VALUES
    (
    '{book.NAMEBOOK}',
    '{book.LOANDURATION}',
    '{book.STATUBOOK}',
    '{book.NAMEGENRE}',
    '{book.NUMSUP}',
    '{book.NUMAUT}',
    '{book.BOOKWRITINGDATE}',
    '{book.DESCRIPTION }'
    );
    """
    try:
      curs=conn.cursor()
      curs.execute(req)
      conn.commit()
      curs.close()
      conn.close
      return True
    except:
      return False