>>> from bible import *
>>> sorted=F(sorted)
>>> sorted
Func(<built-in function sorted>)
>>> sorted([3,2,4])
[2, 3, 4]
>>> 
>>> sortbylen=sorted(...,key=len)
>>> sortbylen(['a','dfwg','zed'])
['a', 'zed', 'dfwg']
>>> sorted(['a','deed','zed'])
['a', 'deed', 'zed']
>>> 
>>> ws=set(b.ws())*sorted(...,key=len)
>>> 
>>> ws[::-1][:10]
['Mahershalalhashbaz', 'Chushanrishathaim', 'covenantbreakers', 'lovingkindnesses', 'Selahammahlekoth', 'Chepharhaammonai', 'unprofitableness', 'Bashanhavothjair', 'evilfavouredness', 'Kibrothhattaavah']
>>> ppr=F(pprint.pprint)
>>> ppr(_)
['Mahershalalhashbaz',
 'Chushanrishathaim',
 'covenantbreakers',
 'lovingkindnesses',
 'Selahammahlekoth',
 'Chepharhaammonai',
 'unprofitableness',
 'Bashanhavothjair',
 'evilfavouredness',
 'Kibrothhattaavah']
>>> len('Mahershalalhashbaz')
18
>>> b/'Mahershalalhashbaz'
Isaiah 8:1 Moreover the LORD said unto me, Take thee a great roll, and write in it with a man's pen concerning Mahershalalhashbaz.
Isaiah 8:3 And I went unto the prophetess; and she conceived, and bare a son. Then said the LORD to me, Call his name Mahershalalhashbaz.
>>> Isaiah[8:1].vn()
17809
>>> b[17][8:9]
Esther 8:9 Then were the king's scribes called at that time in the third month, that is, the month Sivan, on the three and twentieth day thereof; and it was written according to all that Mordecai commanded unto the Jews, and to the lieutenants, and the deputies and rulers of the provinces which are from India unto Ethiopia, an hundred twenty and seven provinces, unto every province according to the writing thereof, and unto every people after their language, and to the Jews according to their writing, and according to their language.
>>> _.wc()
90
>>> b/'Chushanrishathaim'
Judges 3:8 Therefore the anger of the LORD was hot against Israel, and he sold them into the hand of Chushanrishathaim king of Mesopotamia: and the children of Israel served Chushanrishathaim eight years.
Judges 3:10 And the Spirit of the LORD came upon him, and he judged Israel, and went out to war: and the LORD delivered Chushanrishathaim king of Mesopotamia into his hand; and his hand prevailed against Chushanrishathaim.
>>> _.vn(),_.wc()
(6577, 66)
>>> 
>>> 
>>> sums('Mahershalalhashbaz')
(18, 163, 1234)
>>> sums('Chushanrishathaim')
(17, 180, 936)
>>> ppr(sorted(b,key=method.wc,reverse=True)[:5])
[Esther 8:9 Then were the king's scribes called at that time in the third month, that is, the month Sivan, on the three and twentieth day thereof; and it was written according to all that Mordecai commanded unto the Jews, and to the lieutenants, and the deputies and rulers of the provinces which are from India unto Ethiopia, an hundred twenty and seven provinces, unto every province according to the writing thereof, and unto every people after their language, and to the Jews according to their writing, and according to their language.,
 Jeremiah 21:7 And afterward, saith the LORD, I will deliver Zedekiah king of Judah, and his servants, and the people, and such as are left in this city from the pestilence, from the sword, and from the famine, into the hand of Nebuchadrezzar king of Babylon, and into the hand of their enemies, and into the hand of those that seek their life: and he shall smite them with the edge of the sword; he shall not spare them, neither have pity, nor have mercy.,
 Ezekiel 46:9 But when the people of the land shall come before the LORD in the solemn feasts, he that entereth in by the way of the north gate to worship shall go out by the way of the south gate; and he that entereth by the way of the south gate shall go forth by the way of the north gate: he shall not return by the way of the gate whereby he came in, but shall go forth over against it.,
 Joshua 8:33 And all Israel, and their elders, and officers, and their judges, stood on this side the ark and on that side before the priests the Levites, which bare the ark of the covenant of the LORD, as well the stranger, as he that was born among them; half of them over against mount Gerizim, and half of them over against mount Ebal; as Moses the servant of the LORD had commanded before, that they should bless the people of Israel.,
 2 Chronicles 2:14 The son of a woman of the daughters of Dan, and his father was a man of Tyre, skilful to work in gold, and in silver, in brass, in iron, in stone, and in timber, in purple, in blue, and in fine linen, and in crimson; also to grave any manner of graving, and to find out every device which shall be put to him, with thy cunning men, and with the cunning men of my lord David thy father.]
>>> 
>>> 
