>>> from bible import *
>>> b.verse(77)
Genesis 3:21 Unto Adam also and to his wife did the LORD God make coats of skins, and clothed them.
>>> b.verse(53)
Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
>>> b.verse(74)
Genesis 3:18 Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field;
>>> b.verse(151)
Genesis 6:13 And God said unto Noah, The end of all flesh is come before me; for the earth is filled with violence through them; and, behold, I will destroy them with the earth.
>>> b.verse(200)
Genesis 8:16 Go forth of the ark, thou, and thy wife, and thy sons, and thy sons' wives with thee.
>>> b.verse(343)
Genesis 14:6 And the Horites in their mount Seir, unto Elparan, which is by the wilderness.
>>> b.verse(346)
Genesis 14:9 With Chedorlaomer the king of Elam, and with Tidal king of nations, and Amraphel king of Shinar, and Arioch king of Ellasar; four kings with five.
>>> b.verse(400)
Genesis 17:2 And I will make my covenant between me and thee, and will multiply thee exceedingly.
>>> b.verse(797)
Genesis 29:1 Then Jacob went on his journey, and came into the land of the people of the east.
>>> b.verse(888)
Genesis 31:14 And Rachel and Leah answered and said unto him, Is there yet any portion or inheritance for us in our father's house?
>>> 
>>> tell('Christ')
C h  r i  s  t
3+8+18+9+19+20 = 77
>>> tell('stars')
 s  t a  r  s
19+20+1+18+19 = 77
>>> p(b/'number'/'stars')
Genesis 15:5 And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
Deuteronomy 28:62 And ye shall be left few in number, whereas ye were as the stars of heaven for multitude; because thou wouldest not obey the voice of the LORD thy God.
1 Chronicles 27:23 But David took not the number of them from twenty years old and under: because the LORD had said he would increase Israel like to the stars of the heavens.
Psalms 147:4 He telleth the number of the stars; he calleth them all by their names.
>>> b/'Orion'
Job 9:9...Amos 5:8 (3 verses)
>>> p(_)
Job 9:9 Which maketh Arcturus, Orion, and Pleiades, and the chambers of the south.
Job 38:31 Canst thou bind the sweet influences of Pleiades, or loose the bands of Orion?
Amos 5:8 Seek him that maketh the seven stars and Orion, and turneth the shadow of death into the morning, and maketh the day dark with night: that calleth for the waters of the sea, and poureth them out upon the face of the earth: The LORD is his name:
>>> Job[38:31]-32
Job 38:31 Canst thou bind the sweet influences of Pleiades, or loose the bands of Orion?
Job 38:32 Canst thou bring forth Mazzaroth in his season? or canst thou guide Arcturus with his sons?
>>> _.tell()
38:31 Canst thou bind the sweet influences of Pleiades, or loose the bands of Orion?
    0+   57+  64+  29+ 33+   72+       108+21+       71+33+   66+ 33+   40+21+    71 = 719
38:32 Canst thou bring forth Mazzaroth in his season? or canst thou guide Arcturus with his sons?
    0+   57+  64+   50+   67+      128+23+ 36+     73+33+   57+  64+   46+     121+  60+ 36+   67 = 982
>>> _.tell(ssum)
38:31 Canst thou bind the sweet influences of Pleiades,  or loose the bands of Orion?
    0+  354+ 568+  65+213+  810+       558+66+      224+150+  255+213+  157+66+   269 = 3968
38:32 Canst thou bring forth Mazzaroth in his season?  or canst thou guide Arcturus with his sons?
    0+  354+ 568+  158+  364+     2000+59+117+    316+150+  354+ 568+  325+    1084+ 717+117+  310 = 7561
>>> 
>>> tell('Orion')
 O  r i  o  n
15+18+9+15+14 = 71
>>> tell('Pleiades')
 P  l e i a d e  s
16+12+5+9+1+4+5+19 = 71
>>> ssum('God')
71
>>> tell('Mazzaroth')
 M a  z  z a  r  o  t h
13+1+26+26+1+18+15+20+8 = 128
>>> tell('Arcturus sons')
Arcturus sons
     121+  67 = 188
>>> tell('season')
 s e a  s  o  n
19+5+1+19+15+14 = 73
>>> tell('chambers')
c h a  m b e  r  s
3+8+1+13+2+5+18+19 = 69
>>> tell('Jehovah')
 J e h  o  v a h
10+5+8+15+22+1+8 = 69
>>> tell('influences')
i  n f  l  u e  n c e  s
9+14+6+12+21+5+14+3+5+19 = 108
>>> tell('כוכבימ')
 כ ו  כ ב  י  מ
11+6+11+2+10+13 = 53
>>> tell('הכוכבימ',ssum)
ה  כ ו  כ ב  י  מ
5+20+6+20+2+10+40 = 103
>>> tell('the stars')
the stars
 33+   77 = 110
>>> tell('sky')
 s  k  y
19+11+25 = 55
>>> 
