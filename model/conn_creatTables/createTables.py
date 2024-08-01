from .createdb import *
from customtkinter import *
from model.conn_creatTables.conn import conn
class CreateTables:
    def __init__(self):
        self.conn=conn
        self.req="""
        create table  if not exists AUTHOR 
        (
            NUMAUT               integer                        not null auto_increment primary key,
            LASTNAMEAUT          varchar(30)                    not null,
            FIRSTNAMEAUT         varchar(30)                    not null,
            TELAUT               integer                        not null,
            EMAILAUT             varchar(50)                    not null
        );
        create table if not exists SUPPLIER 
        (
            NUMSUP               integer                        not null auto_increment primary key,
            LASTNAMESUP          char(20)                       not null,
            TELSUP               integer                        not null,
            EMAILSUP             varchar(50)                    not null
        );
        create table if not exists NAMEGENRE
        (
            NAMEGENRE            varchar(20)                    not null primary key
            
        );
        create table if not exists MEMBER
        (
            IDMEMBER          int                            not null auto_increment primary key,
            LASTNAMEMEMBER    char(20)                       not null,
            FIRSTNAMEMEMBER   char(20)                       not null,
            LOGINMEMBER       varchar(50)                    not null,
            PASSWORDMEMBER    varchar(255)                   not null,
            CITYMEMBER        varchar(20)                    not null,
            TELMEMBER         numeric(15)                    not null
        );
        create table if not exists BOOK 
        (
            NUMBOOK              integer                        not null auto_increment unique primary key,
            NUMSUP               integer                        not null,
            NAMEGENRE            varchar(20)                    not null,
            NUMAUT               integer                        not null,
            NAMEBOOK             varchar(30)                    not null,
            LOANDURATION         integer                        not null,
            BOOKWRITINGDATE      date                           not null,
            STATUBOOK            char(30)                       not null,
            DESCRIPTION          varchar(300)                   not null,
            foreign key (NUMSUP) references SUPPLIER(NUMSUP) on update cascade on delete cascade,
            foreign key (NAMEGENRE) references NAMEGENRE(NAMEGENRE) on update cascade on delete cascade,
            foreign key (NUMAUT) references AUTHOR(NUMAUT) on update cascade on delete cascade
        
        
        );
        CREATE TABLE if not exists LOAN (
            IDMEMBER            int                            not null, 
            NUMBOOK             integer                        not null UNIQUE,
            DATELOAN            date                           not null,
            primary key (IDMEMBER, NUMBOOK),
            foreign key (IDMEMBER) references MEMBER(IDMEMBER) on update cascade on delete cascade,
            foreign key (NUMBOOK) references BOOK(NUMBOOK) on update cascade on delete cascade
        );
        """
        
        self.curs=self.conn.cursor()
        statements = self.req.split(";")
        for statement in statements:
            if statement.strip():  
                self.curs.execute(statement)
        self.conn.commit()
        self.curs.close()
        self.conn.close
CreateTables()
        