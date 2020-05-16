>>> from math import *
>>> from bible import *
>>> b[3][14][15].words()[9-1]
'log'
>>> b[3][14][15]
Leviticus 14:15 And the priest shall take some of the log of oil, and pour it into the palm of his own left hand:
>>> p(b/'log')
Leviticus 14
10 And on the eighth day he shall take two he lambs without blemish, and one ewe lamb of the first year without blemish, and three tenth deals of fine flour for a meat offering, mingled with oil, and one log of oil.
12 And the priest shall take one he lamb, and offer him for a trespass offering, and the log of oil, and wave them for a wave offering before the LORD:
15 And the priest shall take some of the log of oil, and pour it into the palm of his own left hand:
21 And if he be poor, and cannot get so much; then he shall take one lamb for a trespass offering to be waved, to make an atonement for him, and one tenth deal of fine flour mingled with oil for a meat offering, and a log of oil;
24 And the priest shall take the lamb of the trespass offering, and the log of oil, and the priest shall wave them for a wave offering before the LORD:
>>> Leviticus[14].ws().index('log')
308
>>> ps=(308,360,472,712,783)
>>> Leviticus[14].ws()*F(li(*ps))
('log', 'log', 'log', 'log', 'log')
>>> ps@add*1
(309, 361, 473, 713, 784)
>>> (ps@add*1)@base(12,...)
([2, 1, 9], [2, 6, 1], [3, 3, 5], [4, 11, 5], [5, 5, 4])
>>> 1611**.25
6.335397736589153
>>> 16.11**.25
2.003428673069719
>>> 
>>> sums('log')
(3, 34, 97)
>>> sums('oil')
(3, 36, 99)
>>> sums('הַשָּׁ֑מֶן')
(4, 53, 395)
>>> sums('of')
(2, 21, 66)
>>> 99+66
165
>>> log(99)
4.59511985013459
>>> log(165)
5.10594547390058
>>> log(99)
4.59511985013459
>>> ns(163)
[163] [38]
>>> (37,39)@pn
(157, 167)
>>> tells(αβ)
α β γ δ ε ϝ ζ η θ ι  κ  λ  μ  ν  ξ  ο  π  ϙ   ρ   σ   τ   υ   φ   χ   ψ   ω   ϡ   =
1 1 1 1 1 1 1 1 1 1  1  1  1  1  1  1  1  1   1   1   1   1   1   1   1   1   1   27
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18  19  20  21  22  23  24  25  26  27 378
1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800 900 4995
>>> 80**3
512000
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
