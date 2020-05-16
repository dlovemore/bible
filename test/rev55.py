>>> from bible import *
>>> Revelation[5:5]
Revelation 5:5 And one of the elders saith unto me, Weep not: behold, the Lion of the tribe of Juda, the Root of David, hath prevailed to open the book, and to loose the seven seals thereof.
>>> _&method.letters
'andoneoftheelderssaithuntomeweepnotbeholdthelionofthetribeofjudatherootofdavidhathprevailedtoopenthebookandtoloosethesevensealsthereof'
>>> t=Genesis[1:1].text()
>>> stats=meth.split(' ')*len+lsum+osum+ssum
>>> ss=stats+(letters/vowels.__contains__)*stats
>>> vowels.__contains__
<built-in method __contains__ of set object at 0xb6495dc8>
>>> t*+stats
('In the beginning God created the heaven and the earth.', 10, 44, 411, 2094)
>>> t*(letters/vowels.__contains__)*stats
(1, 17, 91, 136)
>>> t*+ss
('In the beginning God created the heaven and the earth.', 10, 44, 411, 2094, (1, 17, 91, 136))
>>> Genesis[1:1].text()*+ss
('In the beginning God created the heaven and the earth.', 10, 44, 411, 2094, (1, 17, 91, 136))
>>> Revelation[22:21].text()*+ss
('The grace of our Lord Jesus Christ be with you all. Amen.', 12, 44, 528, 3885, (1, 17, 169, 1186))
>>> IJohn[5:7].text()*+ss
>>> IJohn[5:8].text()*+ss
('For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.', 22, 88, 946, 5878, (1, 34, 202, 472))
>>> 10+12,44+44,17+17
(22, 88, 34)
>>> 528+411,2094+3885
(939, 5979)
>>> 5*979
4895
>>> John[1:1].text()*+ss
('In the beginning was the Word, and the Word was with God, and the Word was God.', 17, 60, 695, 5834, (1, 19, 141, 366))
>>> ns(695)
[5, 139] [3, 34]
>>> 
>>> 
>>> IJohn[5:8].text()*+ss
('And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.', 23, 92, 982, 5743, (1, 37, 195, 330))
>>> 
>>> 
>>> Revelation[5:5].text()*ss
(35, 134, 1510, 8674, (1, 57, 495, 1908))
>>> Revelation/'alpha'
Revelation 1:8,11;21:6;22:13 (4 verses)
>>> p(_)
Revelation 1:8 I am Alpha and Omega, the beginning and the ending, saith the Lord, which is, and which was, and which is to come, the Almighty.
Revelation 1:11 Saying, I am Alpha and Omega, the first and the last: and, What thou seest, write in a book, and send it unto the seven churches which are in Asia; unto Ephesus, and unto Smyrna, and unto Pergamos, and unto Thyatira, and unto Sardis, and unto Philadelphia, and unto Laodicea.
Revelation 21:6 And he said unto me, It is done. I am Alpha and Omega, the beginning and the end. I will give unto him that is athirst of the fountain of the water of life freely.
Revelation 22:13 I am Alpha and Omega, the beginning and the end, the first and the last.
>>> 
>>> Revelation[1:8].text()*+ss
('I am Alpha and Omega, the beginning and the ending, saith the Lord, which is, and which was, and which is to come, the Almighty.', 25, 97, 968, 5927, (1, 34, 210, 390))
>>> Revelation[1:11].text()*+ss
('Saying, I am Alpha and Omega, the first and the last: and, What thou seest, write in a book, and send it unto the seven churches which are in Asia; unto Ephesus, and unto Smyrna, and unto Pergamos, and unto Thyatira, and unto Sardis, and unto Philadelphia, and unto Laodicea.', 50, 212, 2425, 16690, (1, 86, 682, 4381))
>>> Revelation[21:6].text()*+ss
('And he said unto me, It is done. I am Alpha and Omega, the beginning and the end. I will give unto him that is athirst of the fountain of the water of life freely.', 35, 124, 1337, 8105, (1, 52, 396, 1593))
>>> Revelation[22:13].text()*+ss
('I am Alpha and Omega, the beginning and the end, the first and the last.', 15, 55, 519, 2274, (1, 20, 94, 139))
>>> tells('Alpha and Omega')
Alpha and Omega  =
  5    3    5    13
  38   19   41   98
 110   55  113  278
>>> 
>>> 
>>> 
