import pymysql

def createdatabase_MySQL():

    conn = pymysql.connect(host='192.168.54.241', user='root', password='zdd123',charset="utf8")
    cur = conn.cursor()
    cur.execute("drop database if exists STONE")
    cur.execute("create database STONE character set utf8")
    conn.commit()

def createtable_MySQL():#创建三个表
    cur.execute("DROP TABLE IF EXISTS BidSheetIdentification")
    sqlc = '''
                       create table BidSheetIdentification
                        (
                            id             int(11) not null auto_increment primary key,
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
    cur.execute(sqla,('10001','12345678','33324525','叁贰叁贰肆伍贰伍','2010-01-02','47510','呵呵呵','13825692561','1','PZ0000000001','不还','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:09:00','20100101000001.jpg'))
    cur.execute(sqla,('10002','12345678','43324525','肆贰叁贰肆伍贰伍','2010-01-03','47511','呼呼呼','13825692562','1','PZ0000000002','不不不','90.5/93.5/86.3/96.2/56.3/94.2','2010-01-01 00:00:40','2010010100020.jpg'))
    cur.execute(sqla,('10003','12345678','53324525','伍贰叁贰肆伍贰伍','2010-01-04','47512','刷刷刷','13825692563','0','PZ0000000003','行吧','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:03:00','20100101000003.jpg'))
    cur.execute(sqla,('10004','12345678','63324525','陆贰叁贰肆伍贰伍','2010-01-05','47513','啪啪啪','13825692564','1','PZ0000000004','再见','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:00:09','20100101000008.jpg'))
    cur.execute(sqla,('10005','12345678','73324525','柒贰叁贰肆伍贰伍','2010-01-06','47514','哒哒哒','13825692565','0','PZ0000000005','拜拜','90.5/93.5/86.3/96.2/55.8/90.2','2010-01-01 00:02:00','20100101045600.jpg'))
    cur.execute(sqla,('10006','12345678','83324525','捌贰叁贰肆伍贰伍','2010-01-07','47515','啦啦啦','13825692566','1','PZ0000000006','内地','90.5/93.5/87.3/96.2/56.3/90.2','2010-01-01 00:08:00','20100101007800.jpg'))
    cur.execute(sqla,('10007','12345678','93324525','玖贰叁贰肆伍贰伍','2010-01-08','47516','哗哗哗','13825692567','0','PZ0000000007','次世代次世代','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:08:00','20100101012000.jpg'))
    cur.execute(sqla,('10008','12345678','10324525','贰零叁贰肆伍贰伍','2010-01-09','47517','哼哼哼','13825692568','1','PZ0000000008','字段','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:07:00','20100101000890.jpg'))
    cur.execute(sqla,('10009','12345678','11324525','壹壹叁贰肆伍贰伍','2010-01-10','47518','呲呲呲','13825692569','1','PZ0000000009','当时的','90.5/93.5/86.3/96.2/56.4/90.2','2010-01-01 00:00:02','20100101052000.jpg'))
    cur.execute(sqla,('10010','12345678','12324525','壹贰叁贰肆伍贰伍','2010-01-11','47519','嘀嘀嘀','13825692510','1','PZ0000000010','算法的反对法','90.5/93.5/86.3/96.2/56.3/90.2','2010-01-01 00:11:00','20100101030000.jpg'))
    conn.commit()
    print('插入BidSheetIdentification表10条成功')


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
    conn = pymysql.connect(host='192.168.54.241', user='root', password='zdd123', charset="utf8")
    cur = conn.cursor()
    #createdatabase_MySQL()
    #cur.execute("use STONE")
    #createtable_MySQL()
    #cur.execute("use STONE")
    #inserttable_MySQL()
    cur.execute("use STONE")
    BidSheetIdentificationCollectfield()

