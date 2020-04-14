>>> from bible import *
>>> [tell(b.name()) for b in bible.books()]
G e  n e  s i  s
7+5+14+5+19+9+19 = 78
E  x  o d  u  s
5+24+15+4+21+19 = 88
 L e  v i  t i c  u  s
12+5+22+9+20+9+3+21+19 = 120
 N  u  m b e  r  s
14+21+13+2+5+18+19 = 92
D e  u  t e  r  o  n  o  m  y
4+5+21+20+5+18+15+14+15+13+25 = 155
 J  o  s h  u a
10+15+19+8+21+1 = 74
 J  u d g e  s
10+21+4+7+5+19 = 66
 R  u  t h
18+21+20+8 = 67
1 Samuel
0+    71 = 71
2 Samuel
0+    71 = 71
1 Kings
0+   60 = 60
2 Kings
0+   60 = 60
1 Chronicles
0+       106 = 106
2 Chronicles
0+       106 = 106
E  z  r a
5+26+18+1 = 50
 N e h e  m i a h
14+5+8+5+13+9+1+8 = 63
E  s  t h e  r
5+19+20+8+5+18 = 75
 J  o b
10+15+2 = 27
 P  s a  l  m  s
16+19+1+12+13+19 = 80
 P  r  o  v e  r b  s
16+18+15+22+5+18+2+19 = 115
E c c  l e  s i a  s  t e  s
5+3+3+12+5+19+9+1+19+20+5+19 = 120
Song of Solomon
  55+21+    103 = 179
I  s a i a h
9+19+1+9+1+8 = 47
 J e  r e  m i a h
10+5+18+5+13+9+1+8 = 69
 L a  m e  n  t a  t i  o  n  s
12+1+13+5+14+20+1+20+9+15+14+19 = 143
E  z e  k i e  l
5+26+5+11+9+5+12 = 73
D a  n i e  l
4+1+14+9+5+12 = 45
H  o  s e a
8+15+19+5+1 = 48
 J  o e  l
10+15+5+12 = 42
A  m  o  s
1+13+15+19 = 48
 O b a d i a h
15+2+1+4+9+1+8 = 40
 J  o  n a h
10+15+14+1+8 = 48
 M i c a h
13+9+3+1+8 = 34
 N a h  u  m
14+1+8+21+13 = 57
H a b a  k  k  u  k
8+1+2+1+11+11+21+11 = 66
 Z e  p h a  n i a h
26+5+16+8+1+14+9+1+8 = 88
H a g g a i
8+1+7+7+1+9 = 33
 Z e c h a  r i a h
26+5+3+8+1+18+9+1+8 = 79
 M a  l a c h i
13+1+12+1+3+8+9 = 47
 M a  t  t h e  w
13+1+20+20+8+5+23 = 90
 M a  r  k
13+1+18+11 = 43
 L  u  k e
12+21+11+5 = 49
 J  o h  n
10+15+8+14 = 47
A c  t  s
1+3+20+19 = 43
 R  o  m a  n  s
18+15+13+1+14+19 = 80
1 Corinthians
0+        130 = 130
2 Corinthians
0+        130 = 130
G a  l a  t i a  n  s
7+1+12+1+20+9+1+14+19 = 84
E  p h e  s i a  n  s
5+16+8+5+19+9+1+14+19 = 96
 P h i  l i  p  p i a  n  s
16+8+9+12+9+16+16+9+1+14+19 = 129
C  o  l  o  s  s i a  n  s
3+15+12+15+19+19+9+1+14+19 = 126
1 Thessalonians
0+          156 = 156
2 Thessalonians
0+          156 = 156
1 Timothy
0+    110 = 110
2 Timothy
0+    110 = 110
 T i  t  u  s
20+9+20+21+19 = 89
 P h i  l e  m  o  n
16+8+9+12+5+13+15+14 = 92
H e b  r e  w  s
8+5+2+18+5+23+19 = 80
 J a  m e  s
10+1+13+5+19 = 48
1 Peter
0+   64 = 64
2 Peter
0+   64 = 64
1 John
0+  47 = 47
2 John
0+  47 = 47
3 John
0+  47 = 47
 J  u d e
10+21+4+5 = 40
 R e  v e  l a  t i  o  n
18+5+22+5+12+1+20+9+15+14 = 121
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> {b.name():count(b.name()) for b in bible.books()}
{'Genesis': 78, 'Exodus': 88, 'Leviticus': 120, 'Numbers': 92, 'Deuteronomy': 155, 'Joshua': 74, 'Judges': 66, 'Ruth': 67, '1 Samuel': 71, '2 Samuel': 71, '1 Kings': 60, '2 Kings': 60, '1 Chronicles': 106, '2 Chronicles': 106, 'Ezra': 50, 'Nehemiah': 63, 'Esther': 75, 'Job': 27, 'Psalms': 80, 'Proverbs': 115, 'Ecclesiastes': 120, 'Song of Solomon': 179, 'Isaiah': 47, 'Jeremiah': 69, 'Lamentations': 143, 'Ezekiel': 73, 'Daniel': 45, 'Hosea': 48, 'Joel': 42, 'Amos': 48, 'Obadiah': 40, 'Jonah': 48, 'Micah': 34, 'Nahum': 57, 'Habakkuk': 66, 'Zephaniah': 88, 'Haggai': 33, 'Zechariah': 79, 'Malachi': 47, 'Matthew': 90, 'Mark': 43, 'Luke': 49, 'John': 47, 'Acts': 43, 'Romans': 80, '1 Corinthians': 130, '2 Corinthians': 130, 'Galatians': 84, 'Ephesians': 96, 'Philippians': 129, 'Colossians': 126, '1 Thessalonians': 156, '2 Thessalonians': 156, '1 Timothy': 110, '2 Timothy': 110, 'Titus': 89, 'Philemon': 92, 'Hebrews': 80, 'James': 48, '1 Peter': 64, '2 Peter': 64, '1 John': 47, '2 John': 47, '3 John': 47, 'Jude': 40, 'Revelation': 121}
>>> sum([count(b.name()) for b in bible.books()])
5248
>>> 
>>> 
>>> sums('Jesus')
(74, 515)
>>> sums('Joshua')
(74, 479)
>>> b.booknames
{'Genesis': 0, 'Exodus': 1, 'Leviticus': 2, 'Numbers': 3, 'Deuteronomy': 4, 'Joshua': 5, 'Judges': 6, 'Ruth': 7, '1 Samuel': 8, '2 Samuel': 9, '1 Kings': 10, '2 Kings': 11, '1 Chronicles': 12, '2 Chronicles': 13, 'Ezra': 14, 'Nehemiah': 15, 'Esther': 16, 'Job': 17, 'Psalms': 18, 'Proverbs': 19, 'Ecclesiastes': 20, 'Song of Solomon': 21, 'Isaiah': 22, 'Jeremiah': 23, 'Lamentations': 24, 'Ezekiel': 25, 'Daniel': 26, 'Hosea': 27, 'Joel': 28, 'Amos': 29, 'Obadiah': 30, 'Jonah': 31, 'Micah': 32, 'Nahum': 33, 'Habakkuk': 34, 'Zephaniah': 35, 'Haggai': 36, 'Zechariah': 37, 'Malachi': 38, 'Matthew': 39, 'Mark': 40, 'Luke': 41, 'John': 42, 'Acts': 43, 'Romans': 44, '1 Corinthians': 45, '2 Corinthians': 46, 'Galatians': 47, 'Ephesians': 48, 'Philippians': 49, 'Colossians': 50, '1 Thessalonians': 51, '2 Thessalonians': 52, '1 Timothy': 53, '2 Timothy': 54, 'Titus': 55, 'Philemon': 56, 'Hebrews': 57, 'James': 58, '1 Peter': 59, '2 Peter': 60, '1 John': 61, '2 John': 62, '3 John': 63, 'Jude': 64, 'Revelation': 65}
>>> tell('lamentations')
 l a  m e  n  t a  t i  o  n  s
12+1+13+5+14+20+1+20+9+15+14+19 = 143
>>> 
>>> 
>>> [ssum(b.name()) for b in bible.books()]
[276, 1069, 1056, 587, 1514, 479, 426, 598, 476, 476, 186, 186, 358, 358, 896, 126, 408, 72, 341, 817, 561, 683, 128, 168, 746, 874, 99, 174, 105, 201, 85, 129, 61, 399, 372, 952, 33, 925, 92, 954, 151, 355, 128, 304, 341, 580, 580, 399, 348, 426, 513, 714, 714, 1217, 1217, 809, 272, 710, 156, 370, 370, 128, 128, 128, 319, 850]
>>> 
