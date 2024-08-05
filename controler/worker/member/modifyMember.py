from model.conn_creatTables.conn import conn

def modifyMember(id,member):
    req="""update  `db_library`.`Member`
    set
    `FIRSTNAMEMEMBER`=%s,
    `LASTNAMEMEMBER`=%s,
    `TELMEMBER`=%s,
    `LOGINMEMBER`=%s,
    `PASSWORDMEMBER`=%s,
    `CITYMEMBER`=%s
    where `IDMEMBER`=%s
    """
    try:
      curs=conn.cursor()
      curs.execute(req,(member.FIRSTNAMEMEMBER,member.LASTNAMEMEMBER,member.TELMEMBER,member.LOGINMEMBER,member.PASSWORDMEMBER,member.CITYMEMBER,id,))
      conn.commit()
      curs.close()
      conn.close
      return True
    except:
      return False