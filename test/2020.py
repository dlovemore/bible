>>> from bible import *
>>> 
>>> b.vi(20200)
Jeremiah 50:33 Thus saith the LORD of hosts; The children of Israel and the children of Judah were oppressed together: and all that took them captives held them fast; they refused to let them go.
>>> b.vi(20202)
Jeremiah 50:35 A sword is upon the Chaldeans, saith the LORD, and upon the inhabitants of Babylon, and upon her princes, and upon her wise men.
>>> b.vi(22222)
Hosea 9:13 Ephraim, as I saw Tyrus, is planted in a pleasant place: but Ephraim shall bring forth his children to the murderer.
>>> b.vi(2020)
Exodus 18:20 And thou shalt teach them ordinances and laws, and shalt shew them the way wherein they must walk, and the work that they must do.
>>> b.vi(202)
Genesis 8:18 And Noah went forth, and his sons, and his wife, and his sons' wives with him:
>>> g1=Genesis[1]
>>> g1123=Genesis[1:1]-Genesis[2:3]
>>> g1.count('and')
97
>>> g1123.count('and')
104
>>> g1.count('And God said')
10
>>> g1.count('And God')
28
>>> g1123.count('And God said')
10
>>> b.count('And God said')
30
>>> 
>>> g1123.count('made')
8
>>> 
>>> g1123/'made'
Genesis 1:7,16,25,31;2:2-3 (6 verses)
>>> Genesis[2:22]
Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
>>> Genesis/'may fly'
Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
>>> sums('deoxyribonucleic acid')
(201, 1947)
>>> 
>>> 500+10+1+150+99+101+500
1361
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
