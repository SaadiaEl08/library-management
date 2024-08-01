from model.conn_creatTables.conn import conn

def addMember(member):
    req=f"""INSERT INTO `db_library`.`member`
    (
    `LASTNAMEMEMBER`,
    `TELMEMBER`,
    `FIRSTNAMEMEMBER`,
    `LOGINMEMBER`,
    `PASSWORDMEMBER`,
    `CITYMEMBER`)
    VALUES
    (
    '{member.LASTNAMEMEMBER}',
    '{member.TELMEMBER}',
    '{member.FIRSTNAMEMEMBER}',
    '{member.LOGINMEMBER}',
    '{member.PASSWORDMEMBER}',
    '{member.CITYMEMBER}'
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