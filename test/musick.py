>>> from bible import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pi/python/bible/search.py", line 103, in __getattr__
    if len(bs)!=1: raise AttributeError('No attribute '+name)
AttributeError: No attribute ch
>>> b.chapter(254)
1 Samuel 18:1-30 (30 verses)
>>> 254.6*2**(10/12)
453.6456272770607
>>> 254.6*2**(9/12)
428.1844546471914
>>> 254.6*2**(8/12)
404.15230783110354
>>> b/'music'
1 Samuel 18:6;1 Chronicles 15:16;16:42;2 Chronicles 5:13;7:6;23:13;34:12;Nehemiah 12:36;Ecclesiastes 2:8;12:4;Lamentations 3:63;5:14;Daniel 3:5,7,10,15;6:18;Amos 6:5;Luke 15:25;Revelation 18:22 (20 verses)
>>> [c.chn() for c in _.chapters()]
[254, 353, 354, 372, 374, 390, 401, 425, 661, 671, 800, 802, 853, 856, 885, 988, 1185]
>>> p(b/'music')
1 Samuel 18:6 And it came to pass as they came, when David was returned from the slaughter of the Philistine, that the women came out of all cities of Israel, singing and dancing, to meet king Saul, with tabrets, with joy, and with instruments of musick.
1 Chronicles 15:16 And David spake to the chief of the Levites to appoint their brethren to be the singers with instruments of musick, psalteries and harps and cymbals, sounding, by lifting up the voice with joy.
1 Chronicles 16:42 And with them Heman and Jeduthun with trumpets and cymbals for those that should make a sound, and with musical instruments of God. And the sons of Jeduthun were porters.
2 Chronicles 5:13 It came even to pass, as the trumpeters and singers were as one, to make one sound to be heard in praising and thanking the LORD; and when they lifted up their voice with the trumpets and cymbals and instruments of musick, and praised the LORD, saying, For he is good; for his mercy endureth for ever: that then the house was filled with a cloud, even the house of the LORD;
2 Chronicles 7:6 And the priests waited on their offices: the Levites also with instruments of musick of the LORD, which David the king had made to praise the LORD, because his mercy endureth for ever, when David praised by their ministry; and the priests sounded trumpets before them, and all Israel stood.
2 Chronicles 23:13 And she looked, and, behold, the king stood at his pillar at the entering in, and the princes and the trumpets by the king: and all the people of the land rejoiced, and sounded with trumpets, also the singers with instruments of musick, and such as taught to sing praise. Then Athaliah rent her clothes, and said, Treason, Treason.
2 Chronicles 34:12 And the men did the work faithfully: and the overseers of them were Jahath and Obadiah, the Levites, of the sons of Merari; and Zechariah and Meshullam, of the sons of the Kohathites, to set it forward; and other of the Levites, all that could skill of instruments of musick.
Nehemiah 12:36 And his brethren, Shemaiah, and Azarael, Milalai, Gilalai, Maai, Nethaneel, and Judah, Hanani, with the musical instruments of David the man of God, and Ezra the scribe before them.
Ecclesiastes 2:8 I gathered me also silver and gold, and the peculiar treasure of kings and of the provinces: I gat me men singers and women singers, and the delights of the sons of men, as musical instruments, and that of all sorts.
Ecclesiastes 12:4 And the doors shall be shut in the streets, when the sound of the grinding is low, and he shall rise up at the voice of the bird, and all the daughters of musick shall be brought low;
Lamentations 3:63 Behold their sitting down, and their rising up; I am their musick.
Lamentations 5:14 The elders have ceased from the gate, the young men from their musick.
Daniel 3
5 That at what time ye hear the sound of the cornet, flute, harp, sackbut, psaltery, dulcimer, and all kinds of musick, ye fall down and worship the golden image that Nebuchadnezzar the king hath set up:
7 Therefore at that time, when all the people heard the sound of the cornet, flute, harp, sackbut, psaltery, and all kinds of musick, all the people, the nations, and the languages, fell down and worshipped the golden image that Nebuchadnezzar the king had set up.
10 Thou, O king, hast made a decree, that every man that shall hear the sound of the cornet, flute, harp, sackbut, psaltery, and dulcimer, and all kinds of musick, shall fall down and worship the golden image:
15 Now if ye be ready that at what time ye hear the sound of the cornet, flute, harp, sackbut, psaltery, and dulcimer, and all kinds of musick, ye fall down and worship the image which I have made; well: but if ye worship not, ye shall be cast the same hour into the midst of a burning fiery furnace; and who is that God that shall deliver you out of my hands?
Daniel 6:18 Then the king went to his palace, and passed the night fasting: neither were instruments of musick brought before him: and his sleep went from him.
Amos 6:5 That chant to the sound of the viol, and invent to themselves instruments of musick, like David;
Luke 15:25 Now his elder son was in the field: and as he came and drew nigh to the house, he heard musick and dancing.
Revelation 18:22 And the voice of harpers, and musicians, and of pipers, and trumpeters, shall be heard no more at all in thee; and no craftsman, of whatsoever craft he be, shall be found any more in thee; and the sound of a millstone shall be heard no more at all in thee;
>>> [c.chn() for c in (b/'music').chapters()]
[254, 353, 354, 372, 374, 390, 401, 425, 661, 671, 800, 802, 853, 856, 885, 988, 1185]
>>> [c.chn() for c in (b/'music').chapters()]@(lambda x:math.log2(x/254)*12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for @: 'list' and 'function'
>>> [c.chn() for c in (b/'music').chapters()]@F(lambda x:math.log2(x/254)*12)
[0.0, 5.6980762379881735, 5.747050359729979, 6.605689492030386, 6.698517277385649, 7.423747523729337, 7.905284876193053, 8.91161213103478, 16.55786129682631, 16.817811233136215, 19.862058036030707, 19.905284876193054, 20.97260693455349, 21.033387595547772, 21.610187498378327, 23.51619053775014, 26.663839884161465]
>>> [c.chn() for c in (b/'music').chapters()]@F(lambda x:math.log2(x/353)*12)
[-5.698076237988173, 0.0, 0.048974121741804745, 0.9076132540422124, 1.0004410393974774, 1.7256712857411645, 2.2072086382048797, 3.2135358930466067, 10.859785058838138, 11.119734995148038, 14.163981798042531, 14.207208638204879, 15.274530696565321, 15.3353113575596, 15.912111260390155, 17.81811429976197, 20.965763646173293]
>>> [c.chn() for c in (b/'music').chapters()]@F(lambda x:math.log2(x/401)*12)
[-7.905284876193054, -2.20720863820488, -2.1582345164630747, -1.2995953841626677, -1.2067675988074043, -0.48153735246371454, 0.0, 1.0063272548417264, 8.652576420633256, 8.912526356943157, 11.956773159837653, 12.0, 13.067322058360437, 13.128102719354718, 13.704902622185273, 15.61090566155709, 18.75855500796841]
>>> [c.chn() for c in (b/'music').chapters()]@F(lambda x:math.log2(x/374)*12)
[-6.6985172773856485, -1.0004410393974765, -0.9514669176556705, -0.09282778535526366, 0.0, 0.7252302463436875, 1.2067675988074047, 2.213094853649131, 9.859344019440659, 10.119293955750564, 13.163540758645059, 13.206767598807405, 14.274089657167842, 14.334870318162121, 14.911670220992676, 16.817673260364494, 19.965322606775818]
>>> [c.chn() for c in (b/'music').chapters()]@F(lambda x:math.log2(x/425)*12)
[-8.91161213103478, -3.213535893046606, -3.1645617713048013, -2.3059226390043936, -2.213094853649129, -1.487864607305442, -1.0063272548417266, 0.0, 7.64624916579153, 7.906199102101433, 10.950445904995927, 10.993672745158273, 12.060994803518712, 12.121775464512993, 12.698575367343548, 14.604578406715362, 17.752227753126686]
>>> b.chapter(401)
2 Chronicles 34:1-33 (33 verses)
>>> b.chapter(802)
Lamentations 5:1-22 (22 verses)
>>> Lamentations
Lamentations 1:1-5:22 (154 verses)
>>> log2(401/256)*12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'log2' is not defined
>>> math.log2(401/256)*12
7.769501117459044
>>> math.log2(401/256)*7
4.532208985184442
>>> math.log2(401/256)*13
8.416959543913965
>>> math.log2(401/256)*14
9.064417970368885
>>> math.log2(401/256)*16
10.359334823278726
>>> math.log2(401/256)*18
11.654251676188567
>>> 401*2**(1/12)
424.8447008380774
>>> 401*2**(2/12)
450.1072813720586
>>> 1185*2**(-1-3/12)
498.23112603782585
>>> 1185*2**(-1-4/12)
470.2675616455791
>>> 1185*2**(-1-5/12)
443.8734715247169
>>> 1822*ns
[2, 911] [1, 156]
>>> b.chapter(911)
Haggai 2:1-23 (23 verses)
>>> 444*4
1776
>>> 444*2
888
>>> 
