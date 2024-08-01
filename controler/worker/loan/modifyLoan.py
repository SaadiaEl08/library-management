from model.conn_creatTables.conn import conn
from datetime import datetime

def modifyLoan(id,loan):
    req="""update  `db_library`.`loan`
    set
    `IDMEMBER`=%s,
    `NUMBOOK`=%s
    `DATELOAN`=%s
    where `IDMEMBER`=%s
    """
    try:
      curs=conn.cursor()
      curs.execute(req,(loan.IDMEMBER,loan.NUMBOOK,datetime.now().strftime("%Y,%m,%d"),id))
      conn.commit()
      curs.close()
      conn.close
      return True
    except:
      return False