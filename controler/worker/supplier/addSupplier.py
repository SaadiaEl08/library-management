from model.conn_creatTables.conn import conn
def addSupplier(supplier):
    req=f"""INSERT INTO `db_library`.`supplier`
    (
    `LASTNAMESUP`,
    `TELSUP`,
    `EMAILSUP`)
    VALUES
    (
    '{supplier.LASTNAMESUP}',
    '{supplier.TELSUP}',
    '{supplier.EMAILSUP}'
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