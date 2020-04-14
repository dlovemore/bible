>>> from bible import *
>>> def csb(n=1189): return sum([i*bible.chapter(i).vc() for i in span(1,n)])
... 
>>> csb(1189)
18055094
>>> csb(500)
3365134
>>> csb(256)
982156
>>> csb(128)
274094
>>> csb(64)
63450
>>> csb(32)
17304
>>> csb(16)
3207
>>> csb(8)
893
>>> csb(4)
257
>>> csb(3)
153
>>> csb(6)
549
>>> csb(5)
417
>>> 
>>> 94-29
65
>>> fs(65)
[5, 13]
>>> 
>>> 
>>> def cs1(l): return sum([(i*x) for i,x in enumerate(l,start=1)])
... 
>>> cs1(l),cs1(l2)
<console>:1: 'functools.partial' object is not iterable
    auto=<module 'auto.auto' from '/home/pi/python/auto/auto.py'>
    imported_modules={'sys': <module 'sys' (built-in)>}
    Importer=<class 'auto.auto.Importer'>
    module_names=<function module_names at 0xb65332b8>
    autos=<function autos at 0xb6533468>
    re=Importer('re')
    difflib=Importer('difflib')
    textwrap=Importer('textwrap')
    unicodedata=Importer('unicodedata')
    stringprep=Importer('stringprep')
    readline=Importer('readline')
    rlcompleter=Importer('rlcompleter')
    struct=Importer('struct')
    codecs=Importer('codecs')
    datetime=Importer('datetime')
    calendar=Importer('calendar')
    collections=Importer('collections''abc')
    heapq=Importer('heapq')
    bisect=Importer('bisect')
    array=Importer('array')
    weakref=Importer('weakref')
    types=Importer('types')
    copy=Importer('copy')
    pprint=Importer('pprint')
    reprlib=Importer('reprlib')
    enum=Importer('enum')
    numbers=Importer('numbers')
    math=Importer('math')
    cmath=Importer('cmath')
    decimal=Importer('decimal')
    fractions=Importer('fractions')
    random=Importer('random')
    statistics=Importer('statistics')
    itertools=Importer('itertools')
    functools=Importer('functools')
    operator=<module 'operator' from '/usr/lib/python3.7/operator.py'>
    pathlib=Importer('pathlib')
    fileinput=Importer('fileinput')
    stat=Importer('stat')
    filecmp=Importer('filecmp')
    tempfile=Importer('tempfile')
    glob=Importer('glob')
    fnmatch=Importer('fnmatch')
    linecache=Importer('linecache')
    shutil=Importer('shutil')
    macpath=Importer('macpath')
    pickle=Importer('pickle')
    copyreg=Importer('copyreg')
    shelve=Importer('shelve')
    marshal=Importer('marshal')
    dbm=Importer('dbm')
    sqlite3=Importer('sqlite3')
    zlib=Importer('zlib')
    gzip=Importer('gzip')
    bz2=Importer('bz2')
    lzma=Importer('lzma')
    zipfile=Importer('zipfile')
    tarfile=Importer('tarfile')
    csv=Importer('csv')
    configparser=Importer('configparser')
    netrc=Importer('netrc')
    xdrlib=Importer('xdrlib')
    plistlib=Importer('plistlib')
    hashlib=Importer('hashlib')
    hmac=Importer('hmac')
    os=Importer('os''path')
    io=Importer('io')
    time=Importer('time')
    argparse=Importer('argparse')
    getopt=Importer('getopt')
    logging=Importer('logging''config''handlers')
    getpass=Importer('getpass')
    curses=Importer('curses''textpad''ascii''panel')
    platform=Importer('platform')
    errno=Importer('errno')
    ctypes=Importer('ctypes')
    threading=Importer('threading')
    multiprocessing=Importer('multiprocessing')
    concurrent=Importer('concurrent''futures')
    subprocess=Importer('subprocess')
    sched=Importer('sched')
    queue=Importer('queue')
    dummy_threading=Importer('dummy_threading')
    socket=Importer('socket')
    ssl=Importer('ssl')
    select=Importer('select')
    selectors=Importer('selectors')
    asyncio=Importer('asyncio')
    asyncore=Importer('asyncore')
    asynchat=Importer('asynchat')
    signal=Importer('signal')
    mmap=Importer('mmap')
    email=Importer('email''charset''contentmanager''encoders''errors'...
    json=Importer('json')
    mailcap=Importer('mailcap')
    mailbox=Importer('mailbox')
    mimetypes=Importer('mimetypes')
    base64=Importer('base64')
    binhex=Importer('binhex')
    binascii=Importer('binascii')
    quopri=Importer('quopri')
    uu=Importer('uu')
    html=Importer('html''parser''entities')
    xml=Importer('xml'('etree', 'ElementTree')('dom', 'minidom', 'pul...
    webbrowser=Importer('webbrowser')
    cgi=Importer('cgi')
    cgitb=Importer('cgitb')
    wsgiref=Importer('wsgiref')
    urllib=Importer('urllib''request''response''parse''error''robotpa...
    http=Importer('http''server''cookies''cookiejar')
    ftplib=Importer('ftplib')
    poplib=Importer('poplib')
    imaplib=Importer('imaplib')
    nntplib=Importer('nntplib')
    smtplib=Importer('smtplib')
    smtpd=Importer('smtpd')
    telnetlib=Importer('telnetlib')
    uuid=Importer('uuid')
    socketserver=Importer('socketserver')
    xmlrpc=Importer('xmlrpc''client''server')
    ipaddress=Importer('ipaddress')
    audioop=Importer('audioop')
    aifc=Importer('aifc')
    sunau=Importer('sunau')
    wave=Importer('wave')
    chunk=Importer('chunk')
    colorsys=Importer('colorsys')
    imghdr=Importer('imghdr')
    sndhdr=Importer('sndhdr')
    ossaudiodev=Importer('ossaudiodev')
    gettext=Importer('gettext')
    locale=Importer('locale')
    turtle=Importer('turtle')
    cmd=Importer('cmd')
    shlex=Importer('shlex')
    tkinter=Importer('tkinter''ttk''tix''scrolledtext')
    IDLE=Importer('IDLE')
    Other=Importer('Other')
    typing=Importer('typing')
    pydoc=Importer('pydoc')
    doctest=Importer('doctest')
    unittest=Importer('unittest''mock')
    test=Importer('test''support')
    bdb=Importer('bdb')
    faulthandler=Importer('faulthandler')
    pdb=Importer('pdb')
    The=Importer('The')
    timeit=Importer('timeit')
    trace=Importer('trace')
    tracemalloc=Importer('tracemalloc')
    distutils=Importer('distutils')
    ensurepip=Importer('ensurepip')
    venv=Importer('venv')
    zipapp=Importer('zipapp')
    sys=Importer('sys')
    sysconfig=Importer('sysconfig')
    builtins=Importer('builtins')
    warnings=Importer('warnings')
    contextlib=Importer('contextlib')
    abc=Importer('abc')
    atexit=Importer('atexit')
    traceback=Importer('traceback')
    gc=Importer('gc')
    inspect=Importer('inspect')
    site=Importer('site')
    fpectl=Importer('fpectl')
    code=Importer('code')
    codeop=Importer('codeop')
    zipimport=Importer('zipimport')
    pkgutil=Importer('pkgutil')
    modulefinder=Importer('modulefinder')
    runpy=Importer('runpy')
    importlib=Importer('importlib''resources')
    parser=Importer('parser')
    ast=Importer('ast')
    symtable=Importer('symtable')
    symbol=Importer('symbol')
    token=Importer('token')
    keyword=Importer('keyword')
    tokenize=Importer('tokenize')
    tabnanny=Importer('tabnanny')
    pyclbr=Importer('pyclbr')
    py_compile=Importer('py_compile')
    compileall=Importer('compileall')
    dis=Importer('dis')
    pickletools=Importer('pickletools')
    formatter=Importer('formatter')
    msilib=Importer('msilib')
    msvcrt=Importer('msvcrt')
    winreg=Importer('winreg')
    winsound=Importer('winsound')
    posix=Importer('posix')
    pwd=Importer('pwd')
    spwd=Importer('spwd')
    grp=Importer('grp')
    crypt=Importer('crypt')
    termios=Importer('termios')
    tty=Importer('tty')
    pty=Importer('pty')
    fcntl=Importer('fcntl')
    pipes=Importer('pipes')
    resource=Importer('resource')
    nis=Importer('nis')
    syslog=Importer('syslog')
    optparse=Importer('optparse')
    imp=Importer('imp')
    ntpath=Importer('ntpath')
    posixpath=Importer('posixpath')
    secrets=Importer('secrets')
    contextvars=Importer('contextvars')
    dataclasses=Importer('dataclasses')
    bisect_right=<built-in function bisect_right>
    prod=<function prod at 0xb6421270>
    primes=<function primes at 0xb6416f60>
    prime=<function prime at 0xb64210c0>
    ispalindromic=<function ispalindromic at 0xb6421108>
    pp=<function pp at 0xb6421150>
    isprime=<function isprime at 0xb6421198>
    isperfect=<function isperfect at 0xb64211e0>
    issublime=<function issublime at 0xb6421228>
    factors=<function factors at 0xb65339c0>
    fs=<function factors at 0xb65339c0>
    pf=<function pf at 0xb64212b8>
    npf=<function npf at 0xb6421348>
    allfactors=<function allfactors at 0xb6421300>
    sof=<function sof at 0xb6421390>
    nof=<function nof at 0xb64213d8>
    som=<function som at 0xb6421420>
    lookupas=<function lookupas at 0xb6421468>
    φ=1.618033988749895
    ψ=-0.6180339887498949
    F=<class 'func.F'>
    Fibonacci=<function F at 0xb64214b0>
    base=<function base at 0xb64214f8>
    bases=<function bases at 0xb6421540>
    rebase=<function rebase at 0xb6421588>
    fbase=<function fbase at 0xb64215d0>
    tri=<function tri at 0xb6421618>
    np=<function np at 0xb6421660>
    npp=<function npp at 0xb64216a8>
    ntri=<function ntri at 0xb64216f0>
    nsq=<function nsq at 0xb6421738>
    ncube=<function ncube at 0xb6421780>
    nF=<function nF at 0xb64217c8>
    nsof=<function nsof at 0xb6421810>
    pn=<function pn at 0xb6421858>
    partial=<class 'functools.partial'>
    reduce=<built-in function reduce>
    li=<class 'operator.itemgetter'>
    Attr=<class 'func.Attr'>
    GetItem=<class 'func.GetItem'>
    I=<function I at 0xb64788a0>
    Unique=<class 'func.Unique'>
    e=e
    redparts=<function redparts at 0xb6478ae0>
    callmethod=<function callmethod at 0xb6478c48>
    method=Attr(<function method at 0xb6478c00>)
    meth=Attr(<function meth at 0xb6478bb8>)
    getprop=<function getprop at 0xb6478c90>
    prop=Attr(<function prop at 0xb6478cd8>)
    aslist=<function aslist at 0xb6478d20>
    compose=<function compose at 0xb6478d68>
    star=<function star at 0xb6478db0>
    apply=<function apply at 0xb6478df8>
    unstar=<function unstar at 0xb6478e40>
    l=functools.partial(<function star.<locals>.star at 0xb6478e88>, ...
    orr=<function orr at 0xb6478ed0>
    default=<function default at 0xb6478f18>
    Func=<class 'func.Func'>
    RightOp=<class 'func.RightOp'>
    LeftOp=<class 'func.LeftOp'>
    Binop=<class 'func.Binop'>
    OrFunc=<class 'func.OrFunc'>
    add=Binop(<function Binop.__init__.<locals>.binop at 0xb6478f60>)
    sub=Binop(<function Binop.__init__.<locals>.binop at 0xb648d2b8>)
    pow=Binop(<function Binop.__init__.<locals>.binop at 0xb648d300>)
    divide=Binop(<function Binop.__init__.<locals>.binop at 0xb648d34...
    div=Binop(<function Binop.__init__.<locals>.binop at 0xb648d390>)
    mul=Binop(<function Binop.__init__.<locals>.binop at 0xb648d3d8>)
    Dict={}
    windows=<function windows at 0xb648d420>
    failas=<function failas at 0xb648d588>
    inks=functools.partial(<function aslist.<locals>.tolist at 0xb648...
    pairs=functools.partial(<function windows at 0xb648d420>, 2)
    twos=functools.partial(<function aslist.<locals>.tolist at 0xb648...
    threes=functools.partial(<function aslist.<locals>.tolist at 0xb6...
    withoutrepeats=functools.partial(<function aslist.<locals>.tolist...
    splitat=<function splitat at 0xb648d6f0>
    positions=<function positions at 0xb648d738>
    perm=<function perm at 0xb648d780>
    permargs=<function permargs at 0xb648d7c8>
    fggf=<function fggf at 0xb648d810>
    swap=functools.partial(<function star.<locals>.star at 0xb648d8a0...
    swapargs=<function permargs.<locals>.permargs at 0xb648d8e8>
    c=299792458
    ab=abcdefghijklmnopqrstuvwxyz
    αβ=αβγδεϝζηθικλμνξοπϙρστυφχψωϡ
    אב=אבגדהוזחטיכלמנסעפצקרשת
    nn=0123456789
    pos={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h':...
    characters={'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f'...
    vowels={'ο', 'a', 'o', 'η', 'υ', 'ι', 'u', 'e', 'ω', 'α', 'i', 'ε...
    begin=<function begin at 0xb64218a0>
    isletter=<function isletter at 0xb64218e8>
    letters=<functools._lru_cache_wrapper object at 0xb63f9ad0>
    ovals=<function ovals at 0xb6421930>
    count=<function count at 0xb64219c0>
    osum=<function count at 0xb64219c0>
    pdigits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70...
    ssum=<function ssum at 0xb6421a08>
    lsum=<function lsum at 0xb6421a50>
    ascsum=<function ascsum at 0xb6421a98>
    sums=<function sums at 0xb6421ae0>
    psum=<function ssum at 0xb6421a08>
    showalphas=<function showalphas at 0xb6421b28>
    join=<function join at 0xb6421b70>
    htmldraw=<module 'htmldraw' from '/home/pi/python/parle/htmldraw....
    tale=<function tale at 0xb6416150>
    table=<function table at 0xb6416270>
    modifierlen=<function modifierlen at 0xb64161e0>
    justify=<function justify at 0xb6416228>
    Row=<func.GetItem object at 0xb641e2f0>
    Index=<class 'table.Index'>
    diff=<function diff at 0xb6416198>
    lookup=<function lookup at 0xb6416738>
    Table=<class 'table.Table'>
    tell=<function tell at 0xb6421bb8>
    texttable=<function texttable at 0xb6421c00>
    tt=<function tt at 0xb6421c48>
    chain=<class 'itertools.chain'>
    word2num=functools.partial(<function aslist.<locals>.tolist at 0x...
    span=<function span at 0xb6533660>
    get=<function get at 0xb6421d20>
    middle=<function middle at 0xb6421d68>
    tekel=<function tekel at 0xb6421db0>
    upharsin=<function upharsin at 0xb6421df8>
    wc=<function wc at 0xb6421e40>
    contranges=functools.partial(<function aslist.<locals>.tolist at ...
    Sel=<class 'search.Sel'>
    verselist=<function verselist at 0xb6421f18>
    p=<built-in function print>
    kjv=[('Genesis', 1, 1, 'In the beginning God created the heaven a...
    b=Genesis 1
1 In the beginning God created the heaven and the ear...
    bible=Genesis 1
1 In the beginning God created the heaven and the...
    Genesis=Genesis 1
1 In the beginning God created the heaven and t...
    Exodus=Exodus 1
1 Now these are the names of the children of Isra...
    Leviticus=Leviticus 1
1 And the LORD called unto Moses, and spake...
    Numbers=Numbers 1
1 And the LORD spake unto Moses in the wilderne...
    Deuteronomy=Deuteronomy 1
1 These be the words which Moses spake ...
    Joshua=Joshua 1
1 Now after the death of Moses the servant of the...
    Judges=Judges 1
1 Now after the death of Joshua it came to pass, ...
    Ruth=Ruth 1
1 Now it came to pass in the days when the judges rul...
    ISamuel=1 Samuel 1
1 Now there was a certain man of Ramathaimzoph...
    IISamuel=2 Samuel 1
1 Now it came to pass after the death of Saul...
    IKings=1 Kings 1
1 Now king David was old and stricken in years; ...
    IIKings=2 Kings 1
1 Then Moab rebelled against Israel after the d...
    IChronicles=1 Chronicles 1
1 Adam, Sheth, Enosh,
2 Kenan, Mahalal...
    IIChronicles=2 Chronicles 1
1 And Solomon the son of David was st...
    Ezra=Ezra 1
1 Now in the first year of Cyrus king of Persia, that...
    Nehemiah=Nehemiah 1
1 The words of Nehemiah the son of Hachaliah....
    Esther=Esther 1
1 Now it came to pass in the days of Ahasuerus, (...
    Job=Job 1
1 There was a man in the land of Uz, whose name was Job...
    Psalm=Psalms 1
1 Blessed is the man that walketh not in the couns...
    Psalms=Psalms 1
1 Blessed is the man that walketh not in the coun...
    Proverb=Proverbs 1
1 The proverbs of Solomon the son of David, ki...
    Proverbs=Proverbs 1
1 The proverbs of Solomon the son of David, k...
    Ecclesiastes=Ecclesiastes 1
1 The words of the Preacher, the son ...
    Song=Song of Solomon 1
1 The song of songs, which is Solomon's.
2...
    Solomon=Song of Solomon 1
1 The song of songs, which is Solomon's...
    Songs=Song of Solomon 1
1 The song of songs, which is Solomon's.
...
    Isaiah=Isaiah 1
1 The vision of Isaiah the son of Amoz, which he ...
    Jeremiah=Jeremiah 1
1 The words of Jeremiah the son of Hilkiah, o...
    Lamentations=Lamentations 1
1 How doth the city sit solitary, tha...
    Ezekiel=Ezekiel 1
1 Now it came to pass in the thirtieth year, in...
    Daniel=Daniel 1
1 In the third year of the reign of Jehoiakim kin...
    Hosea=Hosea 1
1 The word of the LORD that came unto Hosea, the so...
    Joel=Joel 1
1 The word of the LORD that came to Joel the son of P...
    Amos=Amos 1
1 The words of Amos, who was among the herdmen of Tek...
    Obadiah=Obadiah 1
1 The vision of Obadiah. Thus saith the Lord GO...
    Jonah=Jonah 1
1 Now the word of the LORD came unto Jonah the son ...
    Micah=Micah 1
1 The word of the LORD that came to Micah the Moras...
    Nahum=Nahum 1
1 The burden of Nineveh. The book of the vision of ...
    Habakkuk=Habakkuk 1
1 The burden which Habakkuk the prophet did s...
    Zephaniah=Zephaniah 1
1 The word of the LORD which came unto Zeph...
    Haggai=Haggai 1
1 In the second year of Darius the king, in the s...
    Zechariah=Zechariah 1
1 In the eighth month, in the second year o...
    Malachi=Malachi 1
1 The burden of the word of the LORD to Israel ...
    Matthew=Matthew 1
1 The book of the generation of Jesus Christ, t...
    Mark=Mark 1
1 The beginning of the gospel of Jesus Christ, the So...
    Luke=Luke 1
1 Forasmuch as many have taken in hand to set forth i...
    John=John 1
1 In the beginning was the Word, and the Word was wit...
    Acts=Acts 1
1 The former treatise have I made, O Theophilus, of a...
    Romans=Romans 1
1 Paul, a servant of Jesus Christ, called to be a...
    ICorinthians=1 Corinthians 1
1 Paul called to be an apostle of Je...
    IICorinthains=2 Corinthians 1
1 Paul, an apostle of Jesus Christ ...
    Galatians=Galatians 1
1 Paul, an apostle, (not of men, neither by...
    Ephesians=Ephesians 1
1 Paul, an apostle of Jesus Christ by the w...
    Philippians=Philippians 1
1 Paul and Timotheus, the servants of J...
    Colossians=Colossians 1
1 Paul, an apostle of Jesus Christ by the...
    IThessalonians=1 Thessalonians 1
1 Paul, and Silvanus, and Timoth...
    IIThessalonians=2 Thessalonians 1
1 Paul, and Silvanus, and Timot...
    ITimothy=1 Timothy 1
1 Paul, an apostle of Jesus Christ by the co...
    IITimothy=2 Timothy 1
1 Paul, an apostle of Jesus Christ by the w...
    Titus=Titus 1
1 Paul, a servant of God, and an apostle of Jesus C...
    Philemon=Philemon 1
1 Paul, a prisoner of Jesus Christ, and Timot...
    IPeter=1 Peter 1
1 Peter, an apostle of Jesus Christ, to the stra...
    IIPeter=2 Peter 1
1 Simon Peter, a servant and an apostle of Jesu...
    Hebrews=Hebrews 1
1 God, who at sundry times and in divers manner...
    James=James 1
1 James, a servant of God and of the Lord Jesus Chr...
    IJohn=1 John 1
1 That which was from the beginning, which we have...
    IIJohn=2 John 1
1 The elder unto the elect lady and her children,...
    IIIJohn=3 John 1
1 The elder unto the wellbeloved Gaius, whom I l...
    Jude=Jude 1
1 Jude, the servant of Jesus Christ, and brother of J...
    Revelation=Revelation 1
1 The Revelation of Jesus Christ, which G...
    OT=Genesis 1
1 In the beginning God created the heaven and the ea...
    ot=Genesis 1
1 In the beginning God created the heaven and the ea...
    NT=Matthew 1
1 The book of the generation of Jesus Christ, the so...
    nt=Matthew 1
1 The book of the generation of Jesus Christ, the so...
    show=<function show at 0xb6533198>
    csb=<function csb at 0xb67717c8>
    cs1=<function cs1 at 0xb588d540>
<console>:1: 'functools.partial' object is not iterable
    l=functools.partial(<function star.<locals>.star at 0xb6478e88>, ...
>>> cs1([v.vn() for v in bible])
10029161883455
>>> tell(ssum,'Solomon')
 S  o  l  o  m  o  n
100+60+30+60+40+60+50=400
>>> ssum('Solomon')//2
200
>>> tell('Lord Jesus Christ')
Lord Jesus Christ
 49 +  74 +  77  =200
>>> 
>>> b/'half was not told'
1 Kings 10:7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
>>> 
>>> 
>>> for c in enumerate('fred'): print(c)
... 
(0, 'f')
(1, 'r')
(2, 'e')
(3, 'd')
>>> for i,c in enumerate('fred'): print(i,c)
... 
0 f
1 r
2 e
3 d
>>> from auto import *
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.choice('abcdef')
'a'
>>> random.choice('abcdef')
'c'
>>> 
>>> 
>>> sum([v.verse()+v.chapter() for v in bible])
1171756
>>> sum([v.verse()*v.chapter() for v in bible])
11626744
>>> sum([v.vn()*v.verse()*v.chapter() for v in bible][:120])
304565
>>> b.verse(121)
Genesis 5:15 And Mahalaleel lived sixty and five years, and begat Jared:
>>> 
>>> 
>>> sum([v.vn()*v.verse()*v.chapter() for v in bible])
168968085881
>>> Jude[1].vn()
30674
>>> 31102*22*21
14369124
>>> 
>>> 
>>> fs(_)
[2, 2, 3, 7, 11, 15551]
>>> 
>>> 2**32
4294967296
>>> 31102/299792458
0.00010374510488852925
>>> 31102/66/150
3.1416161616161618
>>> math.pi
3.141592653589793
>>> 31102-29979
1123
>>> 1189-1123
66
>>> math.exp(1)
2.718281828459045
>>> 31102-27183
3919
>>> np(_)
543
>>> 
>>> sum([i*v.chapter()*v.verse() for i,v in enumerate(bible)])
168956459137
>>> sum([i*v.chapter()*v.verse() for i,v in enumerate(bible,start=1)])
168968085881
>>> 
>>> Deuteronomy.vc()
959
>>> 
