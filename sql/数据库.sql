USE STONE;

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
    Obsolete      bool   not null,
    TenderNumber  varchar(20)  not null,
    Remarks      varchar(100)  not null,
    MatchingDegree   int   not null,
    ScanDate      datetime   not null,
    ImgName      varchar(100)  not null
);

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

create table Member
(
    MemberNum    varchar(10)  not null,
    MemberName   varchar(10)  not null,
    MemberPhone  varchar(20)  not null,
    MemberAddress varchar(30)  not null,
    RegistrationTime  date    not null,
    BlackList    bool          not null

);

create table Jade
(
    StoneNum      varchar(10)   not null,
    BottomPrice   varchar(10) not null,
    WinningBidPrice  varchar(10) not null,
    MemberName varchar(10) not null,
    StoneDescription       varchar(10) not null

);

create table Obsolete
(
    ObsoleteSheet    varchar(10) not null,
    ObsoleteTime     date         not null,
    ObsoleteReason   varchar(100) not null
);

create table WinningBid
(
    StoneNum    varchar(10) not null,
    MemberNum   varchar(10) not null,
    Membername varchar(10) not null,
    MemberPhone  varchar(20)  not null,
    WinningBidPrice  varchar(10) not null,

);

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