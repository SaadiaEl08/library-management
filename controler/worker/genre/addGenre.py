from model.conn_creatTables.conn import conn
def addGenre(genre):
    req=f"""INSERT INTO `db_library`.`namegenre`
    (
    `NAMEGENRE`)
    VALUES
    (
    '{genre.NAMEGENRE}'
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