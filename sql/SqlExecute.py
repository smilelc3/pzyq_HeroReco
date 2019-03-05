import pymysql

def createdatabase_MySQL():

    conn = pymysql.connect(host='120.76.57.152', user='root', password='stone',charset="utf8")
    cur = conn.cursor()
    cur.execute("drop database if exists STONE")
    cur.execute("create database STONE character set utf8")
    conn.commit()

def createtable_MySQL():#创建三个表
    cur.execute("DROP TABLE IF EXISTS BidSheetIdentification")
    sqlc = '''
                       create table BidSheetIdentification(
                            id      int(11) not null auto_increment primary key,
                            StoneNum      char(5)   not null,
                            BottomPrice   varchar(10) not null,
                            TenderPriceLowercase varchar(10)     not null,
                            TenderPriceCapital varchar(50)     not null,
                            TenderTime     date     not null,
                            MemberNum     char(5)  not null,
                            MemberName   varchar(10)  not null,
                            MemberPhone   char(11)  not null,
                            Obsolete      boolean   not null,
                            TenderNumber  varchar(20)  not null,
                            Remarks      varchar(100)  not null,
                            MatchingDegree   varchar(40)  not null,
                            ScanDate      datetime   not null,
                            ImgName      varchar(100)  not null
                        );
                    '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS BidSheet")
    sqlc = '''
              create table BidSheet
                (
                    StoneNum      char(5)   not null,
                    BottomPrice       char(10) not null,
                    TenderPriceLowercase varchar(10)     not null,
                    TenderPriceCapital varchar(20)     not null,
                    TenderTime     date     not null,
                    MemberNum   char(5)  not null,
                    MemberName   varchar(10)  not null,
                    MemberPhone   char(11)  not null,
                    Remarks      varchar(100)  not null
                
                );
            '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Member")
    sqlc = '''
          create table Member
            (
                id             int(11) not null auto_increment primary key,
                MemberNum    char(5)  not null,
                MemberName   varchar(10)  not null,
                MemberPhone  char(11)  not null,
                MemberAddress varchar(30)  not null,
                RegistrationTime  date    not null,
                BlackList    boolean          not null
            
            );
           '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Jade")
    sqlc = '''
                           
        create table Jade
        (
        id             int(11) not null auto_increment primary key,
        StoneNum      char(5)   not null,
        BottomPrice   varchar(10) not null,
        WinningBidPrice  varchar(10) not null,
        MemberName       varchar(10) not null,
        StoneDescription       varchar(10) not null
        
        );
    
         '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Obsolete")
    sqlc = '''
    
        create table Obsolete
        (
            id             int(11) not null auto_increment primary key,
            ObsoleteSheet    varchar(10) not null,
            ObsoleteTime     date         not null,
            ObsoleteReason   varchar(100) not null
        );
    
     '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS WinningBid")
    sqlc = '''
    
        create table WinningBid
        (
            id           int(11) not null auto_increment primary key,
            StoneNum    char(5) not null,
            MemberNum   char(5) not null,
            Membername varchar(10) not null,
            MemberPhone  char(11)  not null,
            WinningBidPrice  varchar(10) not null 
        );
    
    '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Notice")
    sqlc = '''
    
    create table Notice
    (
        id           int(11) not null auto_increment primary key,
        TenderTime     date     not null,
        StoneNum    char(5) not null,
        MemberNum   char(5) not null,
        MemberName varchar(10) not null,
        MemberPhone  char(11)  not null,
        WinningBidPrice  varchar(10) not null,
        AssociationPhone  varchar(15)  not null
    );
     '''
    cur.execute(sqlc)

    conn.commit()
    print('连接创建成功')



def inserttable_MySQL():
    sqla = '''
            insert into BidSheetIdentification(StoneNum,
                                                BottomPrice,
                                                TenderPriceLowercase,
                                                TenderPriceCapital ,
                                                TenderTime    ,
                                                MemberNum     ,
                                                MemberName   ,
                                                MemberPhone   ,
                                                Obsolete      ,
                                                TenderNumber  ,
                                                Remarks      ,
                                                MatchingDegree ,
                                                ScanDate      ,
            ImgName )   
              
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            '''
    cur.execute(sqla,('10000','12345678','23324525','贰贰叁贰肆伍贰伍','2010-01-01','47589','哈哈哈','13825692560','1','PZ0000000000','和好','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-11 00:00:00','20100101000000.jpg'))
    conn.commit()
    print('插入BidSheetIdentification表1条成功')


def BidSheetIdentificationCollectfield():
    cur.execute("SELECT StoneNum FROM BidSheetIdentification")
    StoneNum = cur.fetchall()
    cur.execute("SELECT BottomPrice FROM BidSheetIdentification")
    BottomPrice = cur.fetchall()
    cur.execute("SELECT TenderPriceLowercase FROM BidSheetIdentification")
    TenderPriceLowercase = cur.fetchall()
    cur.execute("SELECT TenderPriceCapital FROM BidSheetIdentification")
    TenderPriceCapital = cur.fetchall()
    cur.execute("SELECT TenderTime FROM BidSheetIdentification")
    TenderTime = cur.fetchall()
    cur.execute("SELECT MemberNum FROM BidSheetIdentification")
    MemberNum = cur.fetchall()
    cur.execute("SELECT MemberName FROM BidSheetIdentification")
    MemberName = cur.fetchall()
    cur.execute("SELECT MemberPhone FROM BidSheetIdentification")
    MemberPhone = cur.fetchall()
    cur.execute("SELECT Obsolete FROM BidSheetIdentification")
    Obsolete = cur.fetchall()
    cur.execute("SELECT TenderNumber FROM BidSheetIdentification")
    TenderNumber = cur.fetchall()
    cur.execute("SELECT Remarks FROM BidSheetIdentification")
    Remarks = cur.fetchall()
    cur.execute("SELECT MatchingDegree FROM BidSheetIdentification")
    MatchingDegree = cur.fetchall()
    cur.execute("SELECT ScanDate FROM BidSheetIdentification")
    ScanDate = cur.fetchall()
    cur.execute("SELECT ImgName FROM BidSheetIdentification")
    ImgName = cur.fetchall()
    #print(StoneNum, BottomPrice, TenderPriceLowercase,  TenderPriceCapital, TenderTime, MemberNum, MemberName, MemberPhone,Obsolete, TenderNumber, Remarks, MatchingDegree, ScanDate, ImgName)

    return StoneNum, BottomPrice, TenderPriceLowercase,  TenderPriceCapital, TenderTime, MemberNum, MemberName, MemberPhone,Obsolete, TenderNumber, Remarks, MatchingDegree, ScanDate, ImgName


if __name__ == "__main__":
    conn = pymysql.connect(host='120.76.57.152', user='root', password='stone', db='STONE', charset="utf8")
    cur = conn.cursor()
    #createdatabase_MySQL()
    #cur.execute("use STONE")
    createtable_MySQL()
    #cur.execute("use STONE")
    #inserttable_MySQL()
    #cur.execute("use STONE")
    #BidSheetIdentificationCollectfield()

