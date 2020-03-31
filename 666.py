>>> from bible import *
>>> b/666
1 Kings 10:14;2 Chronicles 9:13;Ezra 2:13;Revelation 13:18 (4 verses)
>>> b/777
Genesis 5:31 And all the days of Lamech were seven hundred seventy and seven years: and he died.
>>> _.tell(lsum,osum,ssum)
And all the days of Lamech were seven hundred seventy and seven years: and he died.
 3 + 3 + 3 + 4  +2 +  6   + 4  +  5  +   7   +   7   + 3 +  5  +  5   + 3 +2 +  4  = 66
 19+ 25+ 33+ 49 +21+  42  + 51 +  65 +   74  +  110  + 19+  65 +  68  + 19+13+  22 =695
 55+ 61+213+805 +66+  87  +600 + 560 +  461  +  1460 + 55+ 560 + 896  + 55+13+  22 =5969
>>> tell('seventy times seven')
seventy times seven
  110  +  66 +  65 =241
>>> tell('fold')
f o  l  d
6+15+12+4=37
>>> 
>>> from bible import *
>>> tell=tellmd
>>> Row(['כיסר','ורנסס'])@partial(tell,ssum)

|כ||י||ס||ר|||
|-|-|-|-|-|-|-|-|-|
|20|+|10|+|60|+|200|=|290|


|ו||ר||נ||ס||ס|||
|-|-|-|-|-|-|-|-|-|-|-|
|6|+|200|+|50|+|60|+|60|=|376|

Row([None, None])
>>> 
>>> 
>>> 
>>> tell('Καισαροσ φρανσι',ssum)

|Καισαροσ||φρανσι|||
|-|-|-|-|-|
|602|+|861|=|1463|

>>> 
>>> tell('Nero Caesar',ssum)

|Nero||Caesar|||
|||||
|205|+|200|=|405|
|205|+|200|=|405|

>>> tell('Jorge Mario Bergoglio',ssum)

|Jorge||Mario||Bergoglio|||
|||||||
|172|+|200|+|270|=|642|
|172|+|200|+|270|=|642|

>>> tell('Franciscus',ssum)

|F||r||a||n||c||i||s||c||u||s|||
|||||||||||||||||||||
|6|+|90|+|1|+|50|+|3|+|9|+|100|+|3|+|300|+|100|=|662|
|6|+|90|+|1|+|50|+|3|+|9|+|100|+|3|+|300|+|100|=|662|

>>> tell('BERGOGLIO',ord)

|B||E||R||G||O||G||L||I||O|||
|||||||||||||||||||
|2|+|5|+|90|+|7|+|60|+|7|+|30|+|9|+|60|=|270|
|66|+|69|+|82|+|71|+|79|+|71|+|76|+|73|+|79|=|666|

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
