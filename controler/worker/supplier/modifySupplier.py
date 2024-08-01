
def modifySupplier(id,supplier):
    from model.conn_creatTables.conn import conn
    req="""update  `db_library`.`supplier`
    set
    `LASTNAMESUP`=%s,
    `TELSUP`=%s,
    `EMAILSUP`=%s
    where `NUMSUP`=%s
    """
    try:
      curs=conn.cursor()
      curs.execute(req,(supplier.LASTNAMESUP,supplier.TELSUP,supplier.EMAILSUP,id))
      conn.commit()
      curs.close()
      conn.close
      return True
    except:
      return False