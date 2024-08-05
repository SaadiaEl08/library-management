from model.conn_creatTables.conn import conn
from datetime import datetime
def addLoan(loan):
    req1="""INSERT INTO `db_library`.`loan`
    (
    `NUMBOOK`,
    `IDMEMBER`,
    `DATELOAN`
    )
    VALUES
    (
    %s,
    %s,%s
    );
     """
    req2="""
    update `db_library`.`book` set
    STATUBOOK="On Loan" where NUMBOOK = %s;
    """
    try:
      curs=conn.cursor()
      curs.execute(req1,(loan.NUMBOOK,loan.IDMEMBER,datetime.now().strftime('%Y-%m-%d')))
      conn.commit()
      curs.execute(req2,(loan.NUMBOOK,))
      conn.commit()
      curs.close()
      conn.close
      return True
    except Exception as e:
      return False