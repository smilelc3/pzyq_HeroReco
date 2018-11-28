import pymysql

def createtable_MySQL():#创建三个表
    conn = pymysql.connect(host='192.168.54.241', user='root', password='zdd123', db='STONE', charset="utf8")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS BidSheetIdentification")
    sqlc = '''
                       create table BidSheetIdentification
                        (
                            StoneNum      varchar(10)   not null,
                            BottomPrice   varchar(10) not null,
                            TenderPriceLowercase varchar(10)     not null,
                            TenderPriceCapital varchar(20)     not null,
                            TenderTime     date     not null,
                            MemberNum   varchar(10)  not null,
                            MemberName   varchar(10)  not null,
                            MemberPhone   varchar(20)  not null,
                            Obsolete      boolean   not null,
                            TenderNumber  varchar(20)  not null,
                            Remarks      varchar(100)  not null,
                            MatchingDegree   int   not null,
                            ScanDate      datetime   not null,
                            ImgName      varchar(100)  not null
                        );
                    '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS BidSheet")
    sqlc = '''
              create table BidSheet
                (
                    StoneNum      varchar(10)   not null,
                    BottomPrice       char(10) not null,
                    TenderPriceLowercase varchar(10)     not null,
                    TenderPriceCapital varchar(20)     not null,
                    TenderTime     date     not null,
                    MemberNum   varchar(10)  not null,
                    MemberName   varchar(10)  not null,
                    MemberPhone   varchar(20)  not null,
                    Remarks      varchar(100)  not null
                
                );
            '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Member")
    sqlc = '''
          create table Member
            (
                MemberNum    varchar(10)  not null,
                MemberName   varchar(10)  not null,
                MemberPhone  varchar(20)  not null,
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
        StoneNum      varchar(10)   not null,
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
            StoneNum    varchar(10) not null,
            MemberNum   varchar(10) not null,
            Membername varchar(10) not null,
            MemberPhone  varchar(20)  not null,
            WinningBidPrice  varchar(10) not null,
        
        );
    
    '''
    cur.execute(sqlc)

    cur.execute("DROP TABLE IF EXISTS Notice")
    sqlc = '''
    
    create table Notice
    (
        TenderTime     date     not null,
        StoneNum    varchar(10) not null,
        MemberNum   varchar(10) not null,
        MemberName varchar(10) not null,
        MemberPhone  varchar(20)  not null,
        WinningBidPrice  varchar(10) not null,
        AssociationPhone  varchar(20)  not null
    );
    
                            '''
    cur.execute(sqlc)

    conn.commit()
    print('连接创建成功')

def inserttable_MySQL():
    sqla = '''
            insert into BidSheetIdentification(StoneNum,BottomPrice,TenderPriceLowercase,TenderPriceCapital,TenderTime,MemberNum,MemberName,MemberPhone,Obsolete,TenderNumber,Remarks,MatchingDegree,ScanDate,ImgName)     
            values(%s,%s,%s,%s);
            '''
    cur.execute(sqla, (str1, str2, str3, str4))
    conn.commit()
    print('插入BidSheetIdentification成功')
