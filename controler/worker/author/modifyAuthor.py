from model.conn_creatTables.conn import conn
def modifyAuthor(id,author):
    req="""update  `db_library`.`author`
    set
    `FIRSTNAMEAUT`=%s,
    `LASTNAMEAUT`=%s,
    `TELAUT`=%s,
    `EMAILAUT`=%s
    where `NUMAUT`=%s
    """
    try:
      curs=conn.cursor()
      curs.execute(req,(author.FIRSTNAMEAUT,author.LASTNAMEAUT,author.TELAUT,author.EMAILAUT,id))
      conn.commit()
      curs.close()
      conn.close
      return True
    except Exception as e:
      print(e)
      return False