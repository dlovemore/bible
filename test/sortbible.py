
>>> import re
>>> def cvtotup(x): return list(eval(x).items())[0]
... 
>>> with open('texts/bible4.txt') as f:
...     b4=f.readlines()
... 
>>> with open('texts/KJBIBLE.txt') as f:
...     b=f.readlines()
... 
>>> t='\n'.join(b4)
>>> len(b)
80464
>>> b[:10]
['The King James Version of the\n', 'Holy Bible\n', 'www.davince.com/bible\n', '\n', 'Table of Contents\n', 'Preface to PDF Version\n', 'Preface to 1611 Translation\n', 'Old Testament\n', ' Genesis ... 1\n', ' Exodus ... 31\n']
>>> def cv(s): return re.findall(r'{[0-9]+:[0-9]+}', s)
... 
>>> cvs=cv(t)
>>> cvs[:10]
['{1:1}', '{1:2}', '{1:3}', '{1:4}', '{1:5}', '{1:6}', '{1:7}', '{1:8}', '{1:9}', '{1:10}']
>>> cvs2=' '.join(cvs)
>>> cvs3=cvs2.split('{1:1}')
>>> def chgood(ch):
...     ch=ch.split()
...     ch=list(map(cvtotup,ch))
...     ch[0:100]
...     return (sorted(ch)==ch)
... 
>>> 
>>> list(map(chgood, cvs3))
[True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, True, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> [sorted(x)==x for x in b.chapters().split(';')]
<console>:1: NameError: name 'ch' is not defined
>>> 
>>> 
>>> 
>>> eval(cvs[1])
{1: 2}
>>> cvs=list(map(cvtotup,cvs))
>>> 
>>> cvs[0:10]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]
>>> sorted(cvs)==cvs
False
>>> 
>>> 
