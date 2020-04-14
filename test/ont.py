>>> from bible import *
>>> ot
Genesis 1:1-Malachi 4:6 (23145 verses)
>>> ont=ot+Matthew+John
>>> ont.wc()
652026
>>> ont.vc()
25095
>>> pf(_)
Counter({3: 1, 5: 1, 7: 1, 239: 1})
>>> [b.vc() for b in ot.books()]
[1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55]
>>> ont.midch()
Psalms 11:1-12:8 (15 verses)
>>> p(_)
Psalms 11
1 In the LORD put I my trust: how say ye to my soul, Flee as a bird to your mountain?
2 For, lo, the wicked bend their bow, they make ready their arrow upon the string, that they may privily shoot at the upright in heart.
3 If the foundations be destroyed, what can the righteous do?
4 The LORD is in his holy temple, the LORD's throne is in heaven: his eyes behold, his eyelids try, the children of men.
5 The LORD trieth the righteous: but the wicked and him that loveth violence his soul hateth.
6 Upon the wicked he shall rain snares, fire and brimstone, and an horrible tempest: this shall be the portion of their cup.
7 For the righteous LORD loveth righteousness; his countenance doth behold the upright.
Psalms 12
1 Help, LORD; for the godly man ceaseth; for the faithful fail from among the children of men.
2 They speak vanity every one with his neighbour: with flattering lips and with a double heart do they speak.
3 The LORD shall cut off all flattering lips, and the tongue that speaketh proud things:
4 Who have said, With our tongue will we prevail; our lips are our own: who is lord over us?
5 For the oppression of the poor, for the sighing of the needy, now will I arise, saith the LORD; I will set him in safety from him that puffeth at him.
6 The words of the LORD are pure words: as silver tried in a furnace of earth, purified seven times.
7 Thou shalt keep them, O LORD, thou shalt preserve them from this generation for ever.
8 The wicked walk on every side, when the vilest men are exalted.
>>> Psalm[12:6].vn()
14073
>>> Psalm[12].chn()
490
>>> pf(931)
Counter({7: 2, 19: 1})
>>> ont.chc()
978
>>> ont.vc()
25095
>>> ont.midv()
Nehemiah 9:36 Behold, we are servants this day, and for the land that thou gavest unto our fathers to eat the fruit thereof and the good thereof, behold, we are servants in it:
>>> 
>>> 
>>> 
>>> 
>>> 
