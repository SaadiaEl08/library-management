from model.conn_creatTables.conn import conn

def addAuthor(author):
    req=f"""INSERT INTO `db_library`.`Author`
    (
    `LASTNAMEAUT`,
    `FIRSTNAMEAUT`,
    `TELAUT`,
    `EMAILAUT`)
    VALUES
    (
    '{author.FIRSTNAMEAUT}',
    '{author.LASTNAMEAUT}',
    '{author.TELAUT}',
    '{author.EMAILAUT}'
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