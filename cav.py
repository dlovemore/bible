    >>> from bible import *
    >>> 715+36
    751
    >>> 
    >>> np(751)
    133
    >>> 
    >>> 
    >>> pf(744)
    Counter({2: 3, 3: 1, 31: 1})
    >>> 
    >>> tell('the son of')
    the son of
     33+ 48+21 = 102
    >>> 3567-102*12
    2343
    >>> pf(2343)
    Counter({3: 1, 11: 1, 71: 1})
    >>> 33*71
    2343
    >>> 
    >>> sum([(lambda x: x*(x+1)//2)(ch.vc()) for ch in bible.chapters()])
    530083
    >>> pf(530083)
    Counter({113: 1, 4691: 1})
    >>> npf(530083)
    {113: 30, 4691: 634}
    >>> sum([(lambda x,y: x*(x+1)//2+y)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    557422
    >>> sum([(lambda x,y: x*(x+1)//2-1+y)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    556233
    >>> p(pf(_))
    Counter({3: 1, 31: 1, 5981: 1})
    >>> npf(_)
    {3: 2, 31: 11, 5981: 782}
    >>> sum([(lambda x,y: x*(x+1)//2+y*x)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    1171756
    >>> pf(_)
    Counter({2: 2, 197: 1, 1487: 1})
    >>> 
    >>> sum([(lambda x,y: x*(x+1)//2+y*x)(ch.vc(), ch.chapter()) for ch in bible.chapters()])+(1+2)*6+1+2+3
    1171780
    >>> pf(_)
    Counter({2: 2, 5: 1, 41: 1, 1429: 1})
    >>> 
    >>> [book.vc()+1 for book in bible.books() if book.chaptercount()==1]
    [22, 26, 14, 15, 26]
    >>> sum(_)
    103
    >>> 1171780-103
    1171677
Sum of all verse numbers + sum of all chapter numbers (ch*vs)
plus 1 and 2 for Samuel, Kings, Chronicles, Corinthians, Thessalonians, Timothy, Peter
plus 1 2 3 for letters of John
- 1 for chapter number and versecount for chapters of single chapter books.
    >>> sum([(lambda vs,ch: tri(vs)+vs*ch)(ch.vc(), ch.chapter()) for ch in bible.chapters()])+(1+2)*7+1+2+3-sum([book.vc() for book in bible.books() if book.chaptercount()==1])
    1171685
    >>> p(pf(_))
    Counter({5: 1, 89: 1, 2633: 1})
    >>> _-8
    1171677
    >>> pf(_)
    Counter({13: 2, 3: 1, 2311: 1})
    >>> 13**2*3*2311
    1171677
    >>> np(2311)
    344
    >>> np(1123)
    188
    >>> 
    >>> npf(_)
    {2: 1, 47: 15}
    >>> pf(_)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/home/pi/bible/primes.py", line 82, in pf
        return collections.Counter(factors(n))
      File "/home/pi/bible/primes.py", line 69, in factors
        for p in (prime(j) for j in range(1,n)):
    TypeError: 'dict' object cannot be interpreted as an integer
    >>> 
    >>> 
    >>> 
    >>> 
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==1]; p(x,sum(x))
    [22, 26, 14, 15, 26] 103
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==2]; p(x,sum(x))
    [39] 39
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==3]; p(x,sum(x))
    [74, 48, 57, 54, 48, 47, 62] 390
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==4]; p(x,sum(x))
    [86, 49, 56, 105, 96, 84] 476
    >>> pf(476)
    Counter({2: 2, 7: 1, 17: 1})
    >>> 119*4
    476
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==5]; p(x,sum(x))
    [155, 90, 109, 106, 106] 566
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==6]; p(x,sum(x))
    [150, 156, 114] 420
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==7]; p(x,sum(x))
    [106] 106
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==8]; p(x,sum(x))
    [118] 118
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==9]; p(x,sum(x))
    [147] 147
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==10]; p(x,sum(x))
    [281, 168] 449
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==11]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==12]; p(x,sum(x))
    [223, 358] 581
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==13]; p(x,sum(x))
    [407, 258, 304] 969
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==14]; p(x,sum(x))
    [198, 212] 410
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==15]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==16]; p(x,sum(x))
    [679, 434, 438] 1551
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==17]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==18]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==19]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==20]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==21]; p(x,sum(x))
    [619, 880] 1499
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==22]; p(x,sum(x))
    [817, 405] 1222
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==23]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==24]; p(x,sum(x))
    [659, 696, 1152] 2507
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==25]; p(x,sum(x))
    [720] 720
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==26]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==27]; p(x,sum(x))
    [860] 860
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==28]; p(x,sum(x))
    [1072, 1008] 2080
    >>> ITimothy
    1 Timothy 1:1-6:21 (113 verses)
    >>> [book.vc() for book in bible.books()]
    [1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55, 1071, 678, 1151, 879, 1007, 433, 437, 257, 149, 155, 104, 95, 89, 47, 113, 83, 46, 25, 303, 108, 105, 61, 105, 13, 14, 25, 404]
    1 Timothy 1:1-6:21 (113 verses)
    >>> sorted(_)
    [1 Timothy 1:1 Paul, an apostle of Jesus Christ by the commandment of God our Saviour, and Lord Jesus Christ, which is our hope;, 1 Timothy 1:2 Unto Timothy, my own son in the faith: Grace, mercy, and peace, from God our Father and Jesus Christ our Lord., 1 Timothy 1:3 As I besought thee to abide still at Ephesus, when I went into Macedonia, that thou mightest charge some that they teach no other doctrine,, 1 Timothy 1:4 Neither give heed to fables and endless genealogies, which minister questions, rather than godly edifying which is in faith: so do., 1 Timothy 1:5 Now the end of the commandment is charity out of a pure heart, and of a good conscience, and of faith unfeigned:, 1 Timothy 1:6 From which some having swerved have turned aside unto vain jangling;, 1 Timothy 1:7 Desiring to be teachers of the law; understanding neither what they say, nor whereof they affirm., 1 Timothy 1:8 But we know that the law is good, if a man use it lawfully;, 1 Timothy 1:9 Knowing this, that the law is not made for a righteous man, but for the lawless and disobedient, for the ungodly and for sinners, for unholy and profane, for murderers of fathers and murderers of mothers, for manslayers,, 1 Timothy 1:10 For whoremongers, for them that defile themselves with mankind, for menstealers, for liars, for perjured persons, and if there be any other thing that is contrary to sound doctrine;, 1 Timothy 1:11 According to the glorious gospel of the blessed God, which was committed to my trust., 1 Timothy 1:12 And I thank Christ Jesus our Lord, who hath enabled me, for that he counted me faithful, putting me into the ministry;, 1 Timothy 1:13 Who was before a blasphemer, and a persecutor, and injurious: but I obtained mercy, because I did it ignorantly in unbelief., 1 Timothy 1:14 And the grace of our Lord was exceeding abundant with faith and love which is in Christ Jesus., 1 Timothy 1:15 This is a faithful saying, and worthy of all acceptation, that Christ Jesus came into the world to save sinners; of whom I am chief., 1 Timothy 1:16 Howbeit for this cause I obtained mercy, that in me first Jesus Christ might shew forth all longsuffering, for a pattern to them which should hereafter believe on him to life everlasting., 1 Timothy 1:17 Now unto the King eternal, immortal, invisible, the only wise God, be honour and glory for ever and ever. Amen., 1 Timothy 1:18 This charge I commit unto thee, son Timothy, according to the prophecies which went before on thee, that thou by them mightest war a good warfare;, 1 Timothy 1:19 Holding faith, and a good conscience; which some having put away concerning faith have made shipwreck:, 1 Timothy 1:20 Of whom is Hymenaeus and Alexander; whom I have delivered unto Satan, that they may learn not to blaspheme., 1 Timothy 2:1 I exhort therefore, that, first of all, supplications, prayers, intercessions, and giving of thanks, be made for all men;, 1 Timothy 2:2 For kings, and for all that are in authority; that we may lead a quiet and peaceable life in all godliness and honesty., 1 Timothy 2:3 For this is good and acceptable in the sight of God our Saviour;, 1 Timothy 2:4 Who will have all men to be saved, and to come unto the knowledge of the truth., 1 Timothy 2:5 For there is one God, and one mediator between God and men, the man Christ Jesus;, 1 Timothy 2:6 Who gave himself a ransom for all, to be testified in due time., 1 Timothy 2:7 Whereunto I am ordained a preacher, and an apostle, (I speak the truth in Christ, and lie not;) a teacher of the Gentiles in faith and verity., 1 Timothy 2:8 I will therefore that men pray every where, lifting up holy hands, without wrath and doubting., 1 Timothy 2:9 In like manner also, that women adorn themselves in modest apparel, with shamefacedness and sobriety; not with broided hair, or gold, or pearls, or costly array;, 1 Timothy 2:10 But (which becometh women professing godliness) with good works., 1 Timothy 2:11 Let the woman learn in silence with all subjection., 1 Timothy 2:12 But I suffer not a woman to teach, nor to usurp authority over the man, but to be in silence., 1 Timothy 2:13 For Adam was first formed, then Eve., 1 Timothy 2:14 And Adam was not deceived, but the woman being deceived was in the transgression., 1 Timothy 2:15 Notwithstanding she shall be saved in childbearing, if they continue in faith and charity and holiness with sobriety., 1 Timothy 3:1 This is a true saying, If a man desire the office of a bishop, he desireth a good work., 1 Timothy 3:2 A bishop then must be blameless, the husband of one wife, vigilant, sober, of good behaviour, given to hospitality, apt to teach;, 1 Timothy 3:3 Not given to wine, no striker, not greedy of filthy lucre; but patient, not a brawler, not covetous;, 1 Timothy 3:4 One that ruleth well his own house, having his children in subjection with all gravity;, 1 Timothy 3:5 (For if a man know not how to rule his own house, how shall he take care of the church of God?), 1 Timothy 3:6 Not a novice, lest being lifted up with pride he fall into the condemnation of the devil., 1 Timothy 3:7 Moreover he must have a good report of them which are without; lest he fall into reproach and the snare of the devil., 1 Timothy 3:8 Likewise must the deacons be grave, not doubletongued, not given to much wine, not greedy of filthy lucre;, 1 Timothy 3:9 Holding the mystery of the faith in a pure conscience., 1 Timothy 3:10 And let these also first be proved; then let them use the office of a deacon, being found blameless., 1 Timothy 3:11 Even so must their wives be grave, not slanderers, sober, faithful in all things., 1 Timothy 3:12 Let the deacons be the husbands of one wife, ruling their children and their own houses well., 1 Timothy 3:13 For they that have used the office of a deacon well purchase to themselves a good degree, and great boldness in the faith which is in Christ Jesus., 1 Timothy 3:14 These things write I unto thee, hoping to come unto thee shortly:, 1 Timothy 3:15 But if I tarry long, that thou mayest know how thou oughtest to behave thyself in the house of God, which is the church of the living God, the pillar and ground of the truth., 1 Timothy 3:16 And without controversy great is the mystery of godliness: God was manifest in the flesh, justified in the Spirit, seen of angels, preached unto the Gentiles, believed on in the world, received up into glory., 1 Timothy 4:1 Now the Spirit speaketh expressly, that in the latter times some shall depart from the faith, giving heed to seducing spirits, and doctrines of devils;, 1 Timothy 4:2 Speaking lies in hypocrisy; having their conscience seared with a hot iron;, 1 Timothy 4:3 Forbidding to marry, and commanding to abstain from meats, which God hath created to be received with thanksgiving of them which believe and know the truth., 1 Timothy 4:4 For every creature of God is good, and nothing to be refused, if it be received with thanksgiving:, 1 Timothy 4:5 For it is sanctified by the word of God and prayer., 1 Timothy 4:6 If thou put the brethren in remembrance of these things, thou shalt be a good minister of Jesus Christ, nourished up in the words of faith and of good doctrine, whereunto thou hast attained., 1 Timothy 4:7 But refuse profane and old wives' fables, and exercise thyself rather unto godliness., 1 Timothy 4:8 For bodily exercise profiteth little: but godliness is profitable unto all things, having promise of the life that now is, and of that which is to come., 1 Timothy 4:9 This is a faithful saying and worthy of all acceptation., 1 Timothy 4:10 For therefore we both labour and suffer reproach, because we trust in the living God, who is the Saviour of all men, specially of those that believe., 1 Timothy 4:11 These things command and teach., 1 Timothy 4:12 Let no man despise thy youth; but be thou an example of the believers, in word, in conversation, in charity, in spirit, in faith, in purity., 1 Timothy 4:13 Till I come, give attendance to reading, to exhortation, to doctrine., 1 Timothy 4:14 Neglect not the gift that is in thee, which was given thee by prophecy, with the laying on of the hands of the presbytery., 1 Timothy 4:15 Meditate upon these things; give thyself wholly to them; that thy profiting may appear to all., 1 Timothy 4:16 Take heed unto thyself, and unto the doctrine; continue in them: for in doing this thou shalt both save thyself, and them that hear thee., 1 Timothy 5:1 Rebuke not an elder, but intreat him as a father; and the younger men as brethren;, 1 Timothy 5:2 The elder women as mothers; the younger as sisters, with all purity., 1 Timothy 5:3 Honour widows that are widows indeed., 1 Timothy 5:4 But if any widow have children or nephews, let them learn first to shew piety at home, and to requite their parents: for that is good and acceptable before God., 1 Timothy 5:5 Now she that is a widow indeed, and desolate, trusteth in God, and continueth in supplications and prayers night and day., 1 Timothy 5:6 But she that liveth in pleasure is dead while she liveth., 1 Timothy 5:7 And these things give in charge, that they may be blameless., 1 Timothy 5:8 But if any provide not for his own, and specially for those of his own house, he hath denied the faith, and is worse than an infidel., 1 Timothy 5:9 Let not a widow be taken into the number under threescore years old, having been the wife of one man., 1 Timothy 5:10 Well reported of for good works; if she have brought up children, if she have lodged strangers, if she have washed the saints' feet, if she have relieved the afflicted, if she have diligently followed every good work., 1 Timothy 5:11 But the younger widows refuse: for when they have begun to wax wanton against Christ, they will marry;, 1 Timothy 5:12 Having damnation, because they have cast off their first faith., 1 Timothy 5:13 And withal they learn to be idle, wandering about from house to house; and not only idle, but tattlers also and busybodies, speaking things which they ought not., 1 Timothy 5:14 I will therefore that the younger women marry, bear children, guide the house, give none occasion to the adversary to speak reproachfully., 1 Timothy 5:15 For some are already turned aside after Satan., 1 Timothy 5:16 If any man or woman that believeth have widows, let them relieve them, and let not the church be charged; that it may relieve them that are widows indeed., 1 Timothy 5:17 Let the elders that rule well be counted worthy of double honour, especially they who labour in the word and doctrine., 1 Timothy 5:18 For the scripture saith, Thou shalt not muzzle the ox that treadeth out the corn. And, The labourer is worthy of his reward., 1 Timothy 5:19 Against an elder receive not an accusation, but before two or three witnesses., 1 Timothy 5:20 Them that sin rebuke before all, that others also may fear., 1 Timothy 5:21 I charge thee before God, and the Lord Jesus Christ, and the elect angels, that thou observe these things without preferring one before another, doing nothing by partiality., 1 Timothy 5:22 Lay hands suddenly on no man, neither be partaker of other men's sins: keep thyself pure., 1 Timothy 5:23 Drink no longer water, but use a little wine for thy stomach's sake and thine often infirmities., 1 Timothy 5:24 Some men's sins are open beforehand, going before to judgment; and some men they follow after., 1 Timothy 5:25 Likewise also the good works of some are manifest beforehand; and they that are otherwise cannot be hid., 1 Timothy 6:1 Let as many servants as are under the yoke count their own masters worthy of all honour, that the name of God and his doctrine be not blasphemed., 1 Timothy 6:2 And they that have believing masters, let them not despise them, because they are brethren; but rather do them service, because they are faithful and beloved, partakers of the benefit. These things teach and exhort., 1 Timothy 6:3 If any man teach otherwise, and consent not to wholesome words, even the words of our Lord Jesus Christ, and to the doctrine which is according to godliness;, 1 Timothy 6:4 He is proud, knowing nothing, but doting about questions and strifes of words, whereof cometh envy, strife, railings, evil surmisings,, 1 Timothy 6:5 Perverse disputings of men of corrupt minds, and destitute of the truth, supposing that gain is godliness: from such withdraw thyself., 1 Timothy 6:6 But godliness with contentment is great gain., 1 Timothy 6:7 For we brought nothing into this world, and it is certain we can carry nothing out., 1 Timothy 6:8 And having food and raiment let us be therewith content., 1 Timothy 6:9 But they that will be rich fall into temptation and a snare, and into many foolish and hurtful lusts, which drown men in destruction and perdition., 1 Timothy 6:10 For the love of money is the root of all evil: which while some coveted after, they have erred from the faith, and pierced themselves through with many sorrows., 1 Timothy 6:11 But thou, O man of God, flee these things; and follow after righteousness, godliness, faith, love, patience, meekness., 1 Timothy 6:12 Fight the good fight of faith, lay hold on eternal life, whereunto thou art also called, and hast professed a good profession before many witnesses., 1 Timothy 6:13 I give thee charge in the sight of God, who quickeneth all things, and before Christ Jesus, who before Pontius Pilate witnessed a good confession;, 1 Timothy 6:14 That thou keep this commandment without spot, unrebukable, until the appearing of our Lord Jesus Christ:, 1 Timothy 6:15 Which in his times he shall shew, who is the blessed and only Potentate, the King of kings, and Lord of lords;, 1 Timothy 6:16 Who only hath immortality, dwelling in the light which no man can approach unto; whom no man hath seen, nor can see: to whom be honour and power everlasting. Amen., 1 Timothy 6:17 Charge them that are rich in this world, that they be not highminded, nor trust in uncertain riches, but in the living God, who giveth us richly all things to enjoy;, 1 Timothy 6:18 That they do good, that they be rich in good works, ready to distribute, willing to communicate;, 1 Timothy 6:19 Laying up in store for themselves a good foundation against the time to come, that they may lay hold on eternal life., 1 Timothy 6:20 O Timothy, keep that which is committed to thy trust, avoiding profane and vain babblings, and oppositions of science falsely so called:, 1 Timothy 6:21 Which some professing have erred concerning the faith. Grace be with thee. Amen.]
    >>> pf(2461)
    Counter({23: 1, 107: 1})
    >>> np(107)
    28
    >>> 
