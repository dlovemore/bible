>>> from bible import *
>>> r=b/'hallowed'
>>> p(r)
Exodus 20:11 For in six days the LORD made heaven and earth, the sea, and all that in them is, and rested the seventh day: wherefore the LORD blessed the sabbath day, and hallowed it.
Exodus 29:21 And thou shalt take of the blood that is upon the altar, and of the anointing oil, and sprinkle it upon Aaron, and upon his garments, and upon his sons, and upon the garments of his sons with him: and he shall be hallowed, and his garments, and his sons, and his sons' garments with him.
Leviticus 12:4 And she shall then continue in the blood of her purifying three and thirty days; she shall touch no hallowed thing, nor come into the sanctuary, until the days of her purifying be fulfilled.
Leviticus 19:8 Therefore every one that eateth it shall bear his iniquity, because he hath profaned the hallowed thing of the LORD: and that soul shall be cut off from among his people.
Leviticus 22:32 Neither shall ye profane my holy name; but I will be hallowed among the children of Israel: I am the LORD which hallow you,
Numbers 3:13 Because all the firstborn are mine; for on the day that I smote all the firstborn in the land of Egypt I hallowed unto me all the firstborn in Israel, both man and beast: mine shall they be: I am the LORD.
Numbers 5:10 And every man's hallowed things shall be his: whatsoever any man giveth the priest, it shall be his.
Numbers 16:37 Speak unto Eleazar the son of Aaron the priest, that he take up the censers out of the burning, and scatter thou the fire yonder; for they are hallowed.
Numbers 16:38 The censers of these sinners against their own souls, let them make them broad plates for a covering of the altar: for they offered them before the LORD, therefore they are hallowed: and they shall be a sign unto the children of Israel.
Numbers 18:8 And the LORD spake unto Aaron, Behold, I also have given thee the charge of mine heave offerings of all the hallowed things of the children of Israel; unto thee have I given them by reason of the anointing, and to thy sons, by an ordinance for ever.
Numbers 18:29 Out of all your gifts ye shall offer every heave offering of the LORD, of all the best thereof, even the hallowed part thereof out of it.
Deuteronomy 26:13 Then thou shalt say before the LORD thy God, I have brought away the hallowed things out of mine house, and also have given them unto the Levite, and unto the stranger, to the fatherless, and to the widow, according to all thy commandments which thou hast commanded me: I have not transgressed thy commandments, neither have I forgotten them.
1 Samuel 21:4 And the priest answered David, and said, There is no common bread under mine hand, but there is hallowed bread; if the young men have kept themselves at least from women.
1 Samuel 21:6 So the priest gave him hallowed bread: for there was no bread there but the shewbread, that was taken from before the LORD, to put hot bread in the day when it was taken away.
1 Kings 9:3 And the LORD said unto him, I have heard thy prayer and thy supplication, that thou hast made before me: I have hallowed this house, which thou hast built, to put my name there for ever; and mine eyes and mine heart shall be there perpetually.
1 Kings 9:7 Then will I cut off Israel out of the land which I have given them; and this house, which I have hallowed for my name, will I cast out of my sight; and Israel shall be a proverb and a byword among all people:
2 Kings 12:18 And Jehoash king of Judah took all the hallowed things that Jehoshaphat, and Jehoram, and Ahaziah, his fathers, kings of Judah, had dedicated, and his own hallowed things, and all the gold that was found in the treasures of the house of the LORD, and in the king's house, and sent it to Hazael king of Syria: and he went away from Jerusalem.
2 Chronicles 7:7 Moreover Solomon hallowed the middle of the court that was before the house of the LORD: for there he offered burnt offerings, and the fat of the peace offerings, because the brasen altar which Solomon had made was not able to receive the burnt offerings, and the meat offerings, and the fat.
2 Chronicles 36:14 Moreover all the chief of the priests, and the people, transgressed very much after all the abominations of the heathen; and polluted the house of the LORD which he had hallowed in Jerusalem.
Matthew 6:9 After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.
Luke 11:2 And he said unto them, When ye pray, say, Our Father which art in heaven, Hallowed be thy name. Thy kingdom come. Thy will be done, as in heaven, so in earth.
>>> 
>>> r
Exodus 20:11;29:21;Leviticus 12:4;19:8;22:32;Numbers 3:13;5:10;16:37-38;18:8,29;Deuteronomy 26:13;1 Samuel 21:4,6;1 Kings 9:3,7;2 Kings 12:18;2 Chronicles 7:7;36:14;Matthew 6:9;Luke 11:2 (21 verses)
>>> r.vns()
[2063, 2358, 3049, 3290, 3402, 3706, 3803, 4232, 4233, 4266, 4287, 5580, 7777, 7779, 9055, 9059, 9869, 11332, 12008, 23292, 25408]
>>> Row(_)@factors
Row([[2063], [2, 3, 3, 131], [3049], [2, 5, 7, 47], [2, 3, 3, 3, 3, 3, 7], [2, 17, 109], [3803], [2, 2, 2, 23, 23], [3, 17, 83], [2, 3, 3, 3, 79], [3, 1429], [2, 2, 3, 3, 5, 31], [7, 11, 101], [3, 2593], [5, 1811], [9059], [71, 139], [2, 2, 2833], [2, 2, 2, 19, 79], [2, 2, 3, 3, 647], [2, 2, 2, 2, 2, 2, 397]])
>>> Row([2063,3049,3803,2593,1811,9059,2833])@np
Row([311, 437, 529, 378, 280, 1126, 411])
>>> 23*23
529
>>> pn(529)
3803
>>> 
>>> 
>>> tri(7777)-tri(7773)
31102
>>> b.verse(7774)
1 Samuel 21:1 Then came David to Nob to Ahimelech the priest: and Ahimelech was afraid at the meeting of David, and said unto him, Why art thou alone, and no man with thee?
>>> b.verse(7774+7775)
Psalms 102:27 But thou art the same, and thy years shall have no end.
>>> 7774+7775
15549
>>> pf(_)
Counter({3: 1, 71: 1, 73: 1})
>>> b.verse(7774+7775+7776)
Matthew 7:8 For every one that asketh receiveth; and he that seeketh findeth; and to him that knocketh it shall be opened.
>>> Matthew[7:8].vn()-Matthew.vn()+1
180
>>> Matthew[7:8].vn()
23325
>>> 
>>> 
>>> 
>>> 7777+7774
15551
>>> ISamuel[21:1:4].wcs()
[31, 50, 21, 31]
>>> 
>>> ISamuel[21:4]
1 Samuel 21:4 And the priest answered David, and said, There is no common bread under mine hand, but there is hallowed bread; if the young men have kept themselves at least from women.
>>> 31+50+21+19
121
>>> tell('hallowed bread',lsum,osum,ssum)
hallowed bread  =
   8       5    13
   80      30  110
  638     102  740
>>> tell('Jesus the+Christ')
Jesus the+Christ  =
  74     110     184
>>> 
