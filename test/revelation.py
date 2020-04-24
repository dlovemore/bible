>>> from bible import *
>>> b/1260
Revelation 11:3 And I will give power unto my two witnesses, and they shall prophesy a thousand two hundred and threescore days, clothed in sackcloth.
Revelation 12:6 And the woman fled into the wilderness, where she hath a place prepared of God, that they should feed her there a thousand two hundred and threescore days.
>>> Revelation/42
Revelation 11:2 But the court which is without the temple leave out, and measure it not; for it is given unto the Gentiles: and the holy city shall they tread under foot forty and two months.
Revelation 13:5 And there was given unto him a mouth speaking great things and blasphemies; and power was given unto him to continue forty and two months.
>>> p(_)
Revelation 11:2 But the court which is without the temple leave out, and measure it not; for it is given unto the Gentiles: and the holy city shall they tread under foot forty and two months.
Revelation 13:5 And there was given unto him a mouth speaking great things and blasphemies; and power was given unto him to continue forty and two months.
>>> Revelation/3/'half'
Revelation 11:9 And they of the people and kindreds and tongues and nations shall see their dead bodies three days and an half, and shall not suffer their dead bodies to be put in graves.
Revelation 11:11 And after three days and an half the spirit of life from God entered into them, and they stood upon their feet; and great fear fell upon them which saw them.
>>> divmod(42,12)
(3, 6)
>>> 3*12+6
42
>>> 
>>> sof(42)
96
>>> sof(1189)
1260
>>> sof(1123)
1124
>>> np(1123)
188
>>> 
>>> 12443-404-44
11995
>>> 5*26
130
>>> 5*27
135
>>> [b.wc() for b in Revelation[5]]
[26, 24, 22, 21, 35, 50, 19, 38, 43, 17, 36, 27, 54, 23]
>>> r5wcs=_
>>> add//Row(_)
26 50 72 93 128 178 197 235 278 295 331 358 412 435
>>> Revelation[13:18]
Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
>>> 600*60+6
36006
>>> _-31102
4904
>>> rwcs=Row([c.wc() for c in Revelation.chapters()])
>>> add//rwcs
592 1394 2052 2400 2835 3375 3866 4263 4855 5208 5788 6285 6823 7474 7726 8293 8815 9562 10196 10673 11422 11995
>>> p(Table([rwcs,add//rwcs]))
592  802  658  348  435  540  491  397  592  353  580  497  538  651  252  567  522  747   634   477   749   573
592 1394 2052 2400 2835 3375 3866 4263 4855 5208 5788 6285 6823 7474 7726 8293 8815 9562 10196 10673 11422 11995

>>> _@(lambda x: x%7)
4 1 1 6 0 1 2 0 4 0 6 6 5 5 5 5 2 0 4 5 5 4
>>> rwcs=Row(list(rwcs)[::-1])
>>> p(Table([rwcs,add//rwcs]))
573  749  477  634  747  522  567  252  651  538  497  580  353  592  397  491  540  435  348   658   802   592
573 1322 1799 2433 3180 3702 4269 4521 5172 5710 6207 6787 7140 7732 8129 8620 9160 9595 9943 10601 11403 11995

>>> _@(lambda x: x%7)
4 1 1 6 0 1 2 0 4 0 6 6 5 5 5 5 2 0 4 5 5 4
>>> 
>>> 
>>> Psalm[114:3:7]
Psalms 114:3-7 (5 verses)
>>> 
>>> b.vi(7474)
1 Samuel 12:13 Now therefore behold the king whom ye have chosen, and whom ye have desired! and, behold, the LORD hath set a king over you.
>>> b.vi(7477)
1 Samuel 12:16 Now therefore stand and see this great thing, which the LORD will do before your eyes.
>>> b/'great thing'
Deuteronomy 4:32;1 Samuel 12:16,24;26:25;2 Samuel 7:21,23;2 Kings 5:13;8:4,13;1 Chronicles 17:19;Job 5:9;9:10;37:5;Psalms 71:19;106:21;126:2-3;Jeremiah 45:5;Daniel 7:8,20;Hosea 8:12;Joel 2:20-21;Mark 3:8;5:19-20;Luke 1:49;8:39;Acts 9:16;1 Corinthians 9:11;2 Corinthians 11:15;James 3:5;Revelation 13:5 (33 verses)
>>> p(_)
Deuteronomy 4:32 For ask now of the days that are past, which were before thee, since the day that God created man upon the earth, and ask from the one side of heaven unto the other, whether there hath been any such thing as this great thing is, or hath been heard like it?
1 Samuel 12:16 Now therefore stand and see this great thing, which the LORD will do before your eyes.
1 Samuel 12:24 Only fear the LORD, and serve him in truth with all your heart: for consider how great things he hath done for you.
1 Samuel 26:25 Then Saul said to David, Blessed be thou, my son David: thou shalt both do great things, and also shalt still prevail. So David went on his way, and Saul returned to his place.
2 Samuel 7:21 For thy word's sake, and according to thine own heart, hast thou done all these great things, to make thy servant know them.
2 Samuel 7:23 And what one nation in the earth is like thy people, even like Israel, whom God went to redeem for a people to himself, and to make him a name, and to do for you great things and terrible, for thy land, before thy people, which thou redeemedst to thee from Egypt, from the nations and their gods?
2 Kings 5:13 And his servants came near, and spake unto him, and said, My father, if the prophet had bid thee do some great thing, wouldest thou not have done it? how much rather then, when he saith to thee, Wash, and be clean?
2 Kings 8:4 And the king talked with Gehazi the servant of the man of God, saying, Tell me, I pray thee, all the great things that Elisha hath done.
2 Kings 8:13 And Hazael said, But what, is thy servant a dog, that he should do this great thing? And Elisha answered, The LORD hath shewed me that thou shalt be king over Syria.
1 Chronicles 17:19 O LORD, for thy servant's sake, and according to thine own heart, hast thou done all this greatness, in making known all these great things.
Job 5:9 Which doeth great things and unsearchable; marvellous things without number:
Job 9:10 Which doeth great things past finding out; yea, and wonders without number.
Job 37:5 God thundereth marvellously with his voice; great things doeth he, which we cannot comprehend.
Psalms 71:19 Thy righteousness also, O God, is very high, who hast done great things: O God, who is like unto thee!
Psalms 106:21 They forgat God their saviour, which had done great things in Egypt;
Psalms 126:2 Then was our mouth filled with laughter, and our tongue with singing: then said they among the heathen, The LORD hath done great things for them.
Psalms 126:3 The LORD hath done great things for us; whereof we are glad.
Jeremiah 45:5 And seekest thou great things for thyself? seek them not: for, behold, I will bring evil upon all flesh, saith the LORD: but thy life will I give unto thee for a prey in all places whither thou goest.
Daniel 7:8 I considered the horns, and, behold, there came up among them another little horn, before whom there were three of the first horns plucked up by the roots: and, behold, in this horn were eyes like the eyes of man, and a mouth speaking great things.
Daniel 7:20 And of the ten horns that were in his head, and of the other which came up, and before whom three fell; even of that horn that had eyes, and a mouth that spake very great things, whose look was more stout than his fellows.
Hosea 8:12 I have written to him the great things of my law, but they were counted as a strange thing.
Joel 2:20 But I will remove far off from you the northern army, and will drive him into a land barren and desolate, with his face toward the east sea, and his hinder part toward the utmost sea, and his stink shall come up, and his ill savour shall come up, because he hath done great things.
Joel 2:21 Fear not, O land; be glad and rejoice: for the LORD will do great things.
Mark 3:8 And from Jerusalem, and from Idumaea, and from beyond Jordan; and they about Tyre and Sidon, a great multitude, when they had heard what great things he did, came unto him.
Mark 5:19 Howbeit Jesus suffered him not, but saith unto him, Go home to thy friends, and tell them how great things the Lord hath done for thee, and hath had compassion on thee.
Mark 5:20 And he departed, and began to publish in Decapolis how great things Jesus had done for him: and all men did marvel.
Luke 1:49 For he that is mighty hath done to me great things; and holy is his name.
Luke 8:39 Return to thine own house, and shew how great things God hath done unto thee. And he went his way, and published throughout the whole city how great things Jesus had done unto him.
Acts 9:16 For I will shew him how great things he must suffer for my name's sake.
1 Corinthians 9:11 If we have sown unto you spiritual things, is it a great thing if we shall reap your carnal things?
2 Corinthians 11:15 Therefore it is no great thing if his ministers also be transformed as the ministers of righteousness; whose end shall be according to their works.
James 3:5 Even so the tongue is a little member, and boasteth great things. Behold, how great a matter a little fire kindleth!
Revelation 13:5 And there was given unto him a mouth speaking great things and blasphemies; and power was given unto him to continue forty and two months.
>>> Deuteronomy[4:32].vn()
5037
>>> b.count('great things')
28
>>> nt.vc()
7957
>>> fs(_)
[73, 109]
>>> _@F(np)
[21, 29]
>>> fs(23145)
[3, 5, 1543]
>>> np(1543)
243
>>> fs(23146)
[2, 71, 163]
>>> base(33,23145)
[21, 8, 12]
>>> 3*7*33**2+2*2*2*33+2*2*3
23145
>>> int('l8c',33)
23145
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
