>>> from bible import *
>>> words=method.split
>>> letters('i am')
'iam'
>>> words('i am')
['i', 'am']
>>> @Func
... def wsum(s):
...     return sum(osum(c)*i for i,c in enumerate(letters(s),start=1))
... 
>>> wsum('cube')
71
>>> tell(wsum,'Lord Jesus Christ')
Lord Jesus Christ  =
112   256   324   692
>>> 4**4
256
>>> 'love'*wsum
128
>>> wsum('God')
49
>>> 112*ns
[2, 2, 2, 2, 7] [1, 1, 1, 1, 4]
>>> 16*7
112
>>> allfactors(112)
[1, 2, 4, 7, 8, 14, 16, 28, 56, 112]
>>> 28*4
112
>>> ns(324)
[2, 2, 3, 3, 3, 3] [1, 1, 2, 2, 2, 2]
>>> 4*81
324
>>> tell(wsum,'in the beginning')
in the beginning  =
37  51    461    549
>>> tell('the truth',wsum)
the truth  =
 51  239  290
>>> tell('the truth is true',wsum)
the truth is true  =
 51  239  47 139  476
>>> 
