from model.conn_creatTables.conn import conn
def modifyGenre(oldName,newName):
    req="""update  `db_library`.`namegenre`
    set
    `NAMEGENRE`=%s
    
    where `NAMEGENRE`=%s
    """
    try:
      curs=conn.cursor()
      curs.execute(req,(newName,oldName,))
      conn.commit()
      curs.close()
      conn.close
      return True
    except:
      return False