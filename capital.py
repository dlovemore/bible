>>> from bible import *
>>> from pprint import pprint as pp
>>> sorted(bible.pattern('[A-Z][A-Z ,]*[A-Z][A-Z]'))
['A GOOD', 'BRANCH', 'GOD', 'HOLINESS TO THE LORD', 'HOLINESS UNTO THE LORD', 'I AM', 'I AM THAT I AM', 'I, O LORD', 'JAH', 'JEHOVAH', 'JESUS', 'JESUS OF NAZARETH THE KING OF THE JEWS', 'KING OF KINGS, AND LORD OF LORDS', 'LORD', 'LORD GOD', 'LORD JEHOVAH', 'MENE', 'MENE, MENE, TEKEL, UPHARSIN', 'MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH', 'O GOD', 'O LORD', 'PERES', 'TEKEL', 'THE KING OF THE JEWS', 'THE LORD OUR RIGHTEOUSNESS', 'THE LORD THY GOD', 'THERE', 'THIS IS JESUS THE KING OF THE JEWS', 'THIS IS THE KING OF THE JEWS', 'TO THE UNKNOWN GOD']
>>> pp(sorted([(count(s),s) for s in _]))
[(19, 'JAH'),
 (23, 'I AM'),
 (26, 'GOD'),
 (37, 'MENE'),
 (41, 'O GOD'),
 (42, 'A GOOD'),
 (46, 'BRANCH'),
 (49, 'LORD'),
 (53, 'TEKEL'),
 (56, 'THERE'),
 (63, 'PERES'),
 (64, 'O LORD'),
 (69, 'JEHOVAH'),
 (73, 'I, O LORD'),
 (74, 'JESUS'),
 (75, 'LORD GOD'),
 (95, 'I AM THAT I AM'),
 (118, 'LORD JEHOVAH'),
 (161, 'THE LORD THY GOD'),
 (185, 'THE KING OF THE JEWS'),
 (206, 'TO THE UNKNOWN GOD'),
 (218, 'HOLINESS TO THE LORD'),
 (233, 'MENE, MENE, TEKEL, UPHARSIN'),
 (253, 'HOLINESS UNTO THE LORD'),
 (269, 'THIS IS THE KING OF THE JEWS'),
 (279, 'KING OF KINGS, AND LORD OF LORDS'),
 (315, 'THE LORD OUR RIGHTEOUSNESS'),
 (343, 'THIS IS JESUS THE KING OF THE JEWS'),
 (373, 'JESUS OF NAZARETH THE KING OF THE JEWS'),
 (763,
  'MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE '
  'EARTH')]
>>> pp(sorted([(ssum(s),s) for s in _]))
[(19, 'JAH'),
 (50, 'I AM'),
 (71, 'GOD'),
 (100, 'MENE'),
 (131, 'O GOD'),
 (132, 'A GOOD'),
 (154, 'BRANCH'),
 (184, 'LORD'),
 (244, 'O LORD'),
 (253, 'I, O LORD'),
 (255, 'LORD GOD'),
 (260, 'TEKEL'),
 (270, 'PERES'),
 (308, 'THERE'),
 (492, 'JEHOVAH'),
 (509, 'I AM THAT I AM'),
 (515, 'JESUS'),
 (676, 'LORD JEHOVAH'),
 (927, 'KING OF KINGS, AND LORD OF LORDS'),
 (1019, 'HOLINESS TO THE LORD'),
 (1088, 'MENE, MENE, TEKEL, UPHARSIN'),
 (1193, 'THE KING OF THE JEWS'),
 (1369, 'HOLINESS UNTO THE LORD'),
 (1376, 'THE LORD THY GOD'),
 (1574, 'TO THE UNKNOWN GOD'),
 (1619, 'THIS IS THE KING OF THE JEWS'),
 (1881, 'THE LORD OUR RIGHTEOUSNESS'),
 (2134, 'THIS IS JESUS THE KING OF THE JEWS'),
 (2929, 'JESUS OF NAZARETH THE KING OF THE JEWS'),
 (5587,
  'MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE '
  'EARTH')]
>>> 26**2
676
>>> 
>>> fs(75),fs(255)
([3, 5, 5], [3, 5, 17])
>>> fs(5587)
[37, 151]
>>> fs(763)
[7, 109]
>>> tell('THE BRANCH')
THE BRANCH
 33+  46  =79
>>> tell('THE BRANCH',ssum)
THE BRANCH
213+ 154  =367
>>> 26*26
676
>>> tell('
>>> pf(492)
Counter({2: 2, 3: 1, 41: 1})
>>> 
>>> 
>>> np(373)
74
>>> npp(373)
13
>>> fs(676)
[2, 2, 13, 13]
>>> fs(2929)
[29, 101]
>>> npf(2929)
{29: 10, 101: 26}
>>> sums('rib')
(29, 101)
>>> 29*101
2929
>>> tell('JESUS OF NAZARETH KING OF THE JEWS',ssum)
JESUS OF NAZARETH KING OF THE JEWS
 515 +66+  1155  + 86 +66+213+615 =2716
>>> b.pattern('AND LORD OF')
{'AND LORD OF'}
>>> b/'AND LORD OF LORDS'
Deuteronomy 10:17...Revelation 19:16 (3 verses)
>>> p(_)
Deuteronomy 10:17 For the LORD your God is God of gods, and Lord of lords, a great God, a mighty, and a terrible, which regardeth not persons, nor taketh reward:
1 Timothy 6:15 Which in his times he shall shew, who is the blessed and only Potentate, the King of kings, and Lord of lords;
Revelation 19:16 And he hath on his vesture and on his thigh a name written, KING OF KINGS, AND LORD OF LORDS.
>>> sums('KING OF KINGS')
(122, 338)
>>> sums('LORD OF LORDS')
(138, 534)
>>> 
>>> tell('THIS IS JESUS THE KING OF THE JEWS')
THIS IS JESUS THE KING OF THE JEWS
 56 +28+  74 + 33+ 41 +21+ 33+ 57 =343
>>> tell('JESUS OF NAZARETH THE KING OF THE JEWS')
JESUS OF NAZARETH THE KING OF THE JEWS
  74 +21+   93   + 33+ 41 +21+ 33+ 57 =373
>>> prime(74)
373
>>> fs(269)
[269]
>>> np(269)
57
>>> pf(1376)
Counter({2: 5, 43: 1})
>>> 32*43
1376
>>> ssum('TEKEL')
260
>>> (Matthew-Revelation).chaptercount()
260
>>> tell('TEKEL UPHARSIN')
TEKEL UPHARSIN
  53 +  106   =159
>>> fs(159)
[3, 53]
>>> tell('TEKEL UPHARSIN',ssum)
TEKEL UPHARSIN
 260 +  628   =888
>>> sums('MENE MENE')
(74, 200)
>>> b.chapter(628)
Psalms 150:1-6 (6 verses)
>>> sums('PERES')
(63, 270)
>>> sums('Jehoshuah')
(95, 500)
>>> sums('I AM THAT I AM')
(95, 509)
>>> 
