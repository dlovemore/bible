# >>> from bible import *
# >>> b.midch()
# Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
# Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.
# >>> (Psalms-Revelation).chaptercount()
# 711
# >>> len((Psalms-Revelation).chapters())
# 711
# >>> p(b.midv())
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
# >>> ot=b.Genesis[1:1]-b.Malachi[4:6]
# >>> ot
# Genesis 1:1-Malachi 4:6 (23145 verses)
# >>> from math import pi
# >>> 789629/pi
# 251346.71711742046
# >>> b.chapter(629)
# Proverbs 1:1-33 (33 verses)
# >>> b.book(19)
# Psalms 1:1-150:6 (2461 verses)
# >>> b.book(18)
# Job 1:1-42:17 (1070 verses)
# >>> b.book(20)
# Proverbs 1:1-31:31 (915 verses)
# >>> 
# >>> 
# >>> 7*17
# 119
# >>> 
# >>> Genesis.midv()
# Genesis 27:39 And Isaac his father answered and said unto him, Behold, thy dwelling shall be the fatness of the earth, and of the dew of heaven from above;
# >>> (Genesis[1:1]-(2,3)).midv()
# Genesis 1:17 And God set them in the firmament of the heaven to give light upon the earth,
# Genesis 1:18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# >>> Genesis[1:]-Genesis[4:]
# Genesis 1:1-4:26 (106 verses)
# >>> _.midv()
# Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
# Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
# >>> Genesis[1:]-Genesis[6:8]
# Genesis 1:1-6:8 (146 verses)
# >>> _.midv()
# Genesis 3:17 And unto Adam he said, Because thou hast hearkened unto the voice of thy wife, and hast eaten of the tree, of which I commanded thee, saying, Thou shalt not eat of it: cursed is the ground for thy sake; in sorrow shalt thou eat of it all the days of thy life;
# Genesis 3:18 Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field;
# >>> Genesis[1:]-(9,11)
# Genesis 1:1-9:11 (217 verses)
# >>> _.midv()
# Genesis 5:3 And Adam lived an hundred and thirty years, and begat a son in his own likeness, and after his image; and called his name Seth:
# >>> tell('TEKEL')
# T  E K  E L
# 20+5+11+5+12=53
# >>> (Genesis[1:]-(9,11)).midv(tekel)
# Genesis 3:16 Unto the woman he said, I will greatly multiply thy sorrow and thy conception; in sorrow thou shalt bring forth children; and thy desire shall be to thy husband, and he shall rule over thee.
# Genesis 3:17 And unto Adam he said, Because thou hast hearkened unto the voice of thy wife, and hast eaten of the tree, of which I commanded thee, saying, Thou shalt not eat of it: cursed is the ground for thy sake; in sorrow shalt thou eat of it all the days of thy life;
# >>> Genesis[1:]-(11,9)
# Genesis 1:1-11:9 (276 verses)
# >>> _.midv()
# Genesis 5:32 And Noah was five hundred years old: and Noah begat Shem, Ham, and Japheth.
# Genesis 6:1 And it came to pass, when men began to multiply on the face of the earth, and daughters were born unto them,
# >>> Genesis[1:]-Genesis[11:26]
# Genesis 1:1-11:26 (293 verses)
# >>> _.midv()
# Genesis 6:9 These are the generations of Noah: Noah was a just man and perfect in his generations, and Noah walked with God.
# >>> Genesis[1:]-(25,11)
# Genesis 1:1-25:11 (670 verses)
# >>> _.midv()
# Genesis 13:16 And I will make thy seed as the dust of the earth: so that if a man can number the dust of the earth, then shall thy seed also be numbered.
# Genesis 13:17 Arise, walk through the land in the length of it and in the breadth of it; for I will give it unto thee.
# >>> _.tell()
# And I will make thy seed as the dust of the earth: so that if a man can number the dust of the earth, then shall thy seed also be numbered.
#  19+9+ 56 + 30 + 53+ 33 +20+ 33+ 64 +21+ 33+  52  +34+ 49 +15+1+ 28+ 18+  73  + 33+ 64 +21+ 33+  52  + 47 +  52 + 53+ 33 + 47 +7 +    82   =1165
# Arise, walk through the land in the length of it and in the breadth of it; for I will give it unto thee.
#   52  + 47 +   97  + 33+ 31 +23+ 33+  66  +21+29+ 19+23+ 33+   58  +21+ 29+ 39+9+ 56 + 43 +29+ 70 +  38 =899
# >>> tell('the dust of the earth')
# the dust of the earth
#  33+ 64 +21+ 33+  52 =203
# >>> tell('the dust of the earth',ssum)
# the dust of the earth
# 213+604 +66+213+ 304 =1400
# >>> tell('Lord Jesus Christ',ssum)
# Lord Jesus Christ
# 184 + 515 + 410  =1109
# >>> tell('thy seed also',ssum)
# thy seed also
# 908+114 +191 =1213
# >>> 
# >>> Genesis[1:1]-(25,18)
# Genesis 1:1-25:18 (677 verses)
# >>> _.midv()
# Genesis 14:2 That these made war with Bera king of Sodom, and with Birsha king of Gomorrah, Shinab king of Admah, and Shemeber king of Zeboiim, and the king of Bela, which is Zoar.
# >>> 
# >>> Genesis[1:]-Genesis[35:]
# Genesis 1:1-35:29 (1041 verses)
# >>> _.midv()
# Genesis 21:7 And she said, Who would have said unto Abraham, that Sarah should have given children suck? for I have born him a son in his old age.
# >>> Genesis[1:]-Genesis[37:1]
# Genesis 1:1-37:1 (1085 verses)
# >>> _.midv()
# Genesis 21:29 And Abimelech said unto Abraham, What mean these seven ewe lambs which thou hast set by themselves?
# >>> Genesis
# Genesis 1:1-50:26 (1533 verses)
# >>> _.midv()
# Genesis 27:39 And Isaac his father answered and said unto him, Behold, thy dwelling shall be the fatness of the earth, and of the dew of heaven from above;
## NT chapters, OT chapters
# >>> ot
# Genesis 1:1-Malachi 4:6 (23145 verses)
# >>> pf(23145)
# Counter({3: 1, 5: 1, 1543: 1})
# >>> np(1543)
# 243
# >>> pf(243)
# Counter({3: 5})
# >>> 3*5*prime(3**5)
# 23145
# >>> 
# >>> p(ot.midv())
# 2 Chronicles 18:30 Now the king of Syria had commanded the captains of the chariots that were with him, saying, Fight ye not with small or great, save only with the king of Israel.
# >>> ot.midv().wc()
# 31
# >>> 18*30
# 540
# >>> prime(18),prime(30)
# (61, 113)
# >>> 61*113
# 6893
# >>> 
# >>> ot.midch()
# Job 29:1-25 (25 verses)
## Job is 18th book
## So middle chapter of OT is 18th book, 29th chapter
## Middle verse is:
# >>> ot.midv()
# 2 Chronicles 18:30 Now the king of Syria had commanded the captains of the chariots that were with him, saying, Fight ye not with small or great, save only with the king of Israel.
# >>> ot.midv(tekel)
# 1 Samuel 19:8 And there was war again: and David went out, and fought with the Philistines, and slew them with a great slaughter; and they fled from him.
# 1 Samuel 19:9 And the evil spirit from the LORD was upon Saul, as he sat in his house with his javelin in his hand: and David played with his hand.
# >>> ot.midv(upharsin)
# Psalms 93:3 The floods have lifted up, O LORD, the floods have lifted up their voice; the floods lift up their waves.
# Psalms 93:4 The LORD on high is mightier than the noise of many waters, yea, than the mighty waves of the sea.
# >>> nt=Matthew-Revelation
# >>> nt
# Matthew 1:1-Revelation 22:21 (7957 verses)
# >>> pf(7957)
# Counter({73: 1, 109: 1})
# >>> (Genesis[1:1]+Revelation[22:21]).count()
# 939
# >>> 
# >>> 
# >>> 
# >>> nt.midv()
# Acts 7:7 And the nation to whom they shall be in bondage will I judge, said God: and after that shall they come forth, and serve me in this place.
# >>> p(_.wcs());_.tell()
# [28]
# And the nation to whom they shall be in bondage will I judge, said God: and after that shall they come forth, and serve me in this place.
#  19+ 33+  73  +35+ 59 + 58 +  52 +7 +23+   48  + 56 +9+  47  + 33 + 26 + 19+  50 + 49 +  52 + 58 + 36 +  67  + 19+  69 +18+23+ 56 +  37  =1131
# >>> b.chapter(1131)
# Titus 2:1-15 (15 verses)
# >>> 
# >>> osum("Christ")
# 77
# >>> nt.midch()
# Romans 13:1-14:23 (37 verses)
# >>> b.Romans[13:]
# Romans 13:1-14 (14 verses)
# >>> 
# >>> b/"purified"/"seven"
# Psalms 12:6 The words of the LORD are pure words: as silver tried in a furnace of earth, purified seven times.
# >>> _-7
# Psalms 12:6 The words of the LORD are pure words: as silver tried in a furnace of earth, purified seven times.
# Psalms 12:7 Thou shalt keep them, O LORD, thou shalt preserve them from this generation for ever.
## "seven times" can mean seven times or seven years (or both)
## The King James Bible was being prepared 7 years (1604-1610/1611)
## But it was one of several times the bible has been purified.
##
## Each time a new author would add to the work, there would be a new middle.
##
## The first version of the Word of God would be God's account of creation.
## The second version of God's word, would finish with Adam's account.
## and so on with all the 10/11 authors of Genesis
## Genesis would be a completed book, possibly purified by Joseph.
## The Torah (first five books Genesis to Deuteronomy) would have been be compiled by Moses.
## The Hebrew Tanakh the Old Testament in Hebrew. Apparently it was arranged in a different order into 24 not 39 books.
#
# >>> abc=b.Gen[1:1]-b.Genesis[2:3]
# >>> abc
# Genesis 1:1-2:3 (34 verses)
# >>> abc.midword()
# ['may', 'fly']
# >>> mayfly=abc/"may fly"
# >>> p(mayfly)
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> len(mayfly.words()[:18]),mayfly.words()[18:20],len(mayfly.words()[20:])
# (18, ['may', 'fly'], 9)
# >>> mayfly.wc()
# 29
# >>> tell('rib')
# r  i b
# 18+9+2=29
# >>> Genesis/"rib"
# Genesis 2:21 And the LORD God caused a deep sleep to fall upon Adam, and he slept: and he took one of his ribs, and closed up the flesh instead thereof;
# Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
# >>> 
# >>> 
# >>> p(b.Gen/"generations of")
# Genesis 2:4 These are the generations of the heavens and of the earth when they were created, in the day that the LORD God made the earth and the heavens,
# Genesis 5:1 This is the book of the generations of Adam. In the day that God created man, in the likeness of God made he him;
# Genesis 6:9 These are the generations of Noah: Noah was a just man and perfect in his generations, and Noah walked with God.
# Genesis 10:1 Now these are the generations of the sons of Noah, Shem, Ham, and Japheth: and unto them were sons born after the flood.
# Genesis 11:10 These are the generations of Shem: Shem was an hundred years old, and begat Arphaxad two years after the flood:
# Genesis 11:27 Now these are the generations of Terah: Terah begat Abram, Nahor, and Haran; and Haran begat Lot.
# Genesis 25:12 Now these are the generations of Ishmael, Abraham's son, whom Hagar the Egyptian, Sarah's handmaid, bare unto Abraham:
# Genesis 25:19 And these are the generations of Isaac, Abraham's son: Abraham begat Isaac:
# Genesis 36:1 Now these are the generations of Esau, who is Edom.
# Genesis 36:9 And these are the generations of Esau the father of the Edomites in mount Seir:
# Genesis 37:2 These are the generations of Jacob. Joseph, being seventeen years old, was feeding the flock with his brethren; and the lad was with the sons of Bilhah, and with the sons of Zilpah, his father's wives: and Joseph brought unto his father their evil report.
# >>> che=(b.Gen[1:1]-b.Gen[4:])
# >>> che
# Genesis 1:1-4:26 (106 verses)
# >>> che.vc()
# 106
# >>> che.wc()
# 2756
# >>> factors(_)
# [2, 2, 13, 53]
# >>> 26*106
# 2756
# >>> sums('and')
# (19, 55)
# >>> sums('heaven')
# (55, 469)
# >>> b.chapters()[468]
# Job 33:1-33 (33 verses)
# >>> 
# >>> 333/106
# 3.141509433962264
# >>> che.midv()
# Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
# Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
# >>> p(_)
# Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
# Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
## There are 22 pairs of chromosomes + sex chromosomes (XX or XY)
## Making 2*22 numbered chromosomes or 2*23 chromosomes in total
# >>> che.midword()
# ['flesh', 'of']
# >>> b/"flesh of"
# Genesis 2:23...Revelation 19:18 (39 verses)
## >>> p(_)
# Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
# Genesis 17:11 And ye shall circumcise the flesh of your foreskin; and it shall be a token of the covenant betwixt me and you.
# Genesis 17:14 And the uncircumcised man child whose flesh of his foreskin is not circumcised, that soul shall be cut off from his people; he hath broken my covenant.
# Genesis 17:23 And Abraham took Ishmael his son, and all that were born in his house, and all that were bought with his money, every male among the men of Abraham's house; and circumcised the flesh of their foreskin in the selfsame day, as God had said unto him.
# Genesis 17:24 And Abraham was ninety years old and nine, when he was circumcised in the flesh of his foreskin.
# Genesis 17:25 And Ishmael his son was thirteen years old, when he was circumcised in the flesh of his foreskin.
# Exodus 29:14 But the flesh of the bullock, and his skin, and his dung, shalt thou burn with fire without the camp: it is a sin offering.
# Exodus 29:32 And Aaron and his sons shall eat the flesh of the ram, and the bread that is in the basket by the door of the tabernacle of the congregation.
# Exodus 29:34 And if ought of the flesh of the consecrations, or of the bread, remain unto the morning, then thou shalt burn the remainder with fire: it shall not be eaten, because it is holy.
# Leviticus 7:15 And the flesh of the sacrifice of his peace offerings for thanksgiving shall be eaten the same day that it is offered; he shall not leave any of it until the morning.
# Leviticus 7:17 But the remainder of the flesh of the sacrifice on the third day shall be burnt with fire.
# Leviticus 7:18 And if any of the flesh of the sacrifice of his peace offerings be eaten at all on the third day, it shall not be accepted, neither shall it be imputed unto him that offereth it: it shall be an abomination, and the soul that eateth of it shall bear his iniquity.
# Leviticus 7:20 But the soul that eateth of the flesh of the sacrifice of peace offerings, that pertain unto the LORD, having his uncleanness upon him, even that soul shall be cut off from his people.
# Leviticus 7:21 Moreover the soul that shall touch any unclean thing, as the uncleanness of man, or any unclean beast, or any abominable unclean thing, and eat of the flesh of the sacrifice of peace offerings, which pertain unto the LORD, even that soul shall be cut off from his people.
# Leviticus 12:3 And in the eighth day the flesh of his foreskin shall be circumcised.
# Leviticus 15:7 And he that toucheth the flesh of him that hath the issue shall wash his clothes, and bathe himself in water, and be unclean until the even.
# Leviticus 26:29 And ye shall eat the flesh of your sons, and the flesh of your daughters shall ye eat.
# Numbers 18:18 And the flesh of them shall be thine, as the wave breast and as the right shoulder are thine.
# Deuteronomy 28:53 And thou shalt eat the fruit of thine own body, the flesh of thy sons and of thy daughters, which the LORD thy God hath given thee, in the siege, and in the straitness, wherewith thine enemies shall distress thee:
# Deuteronomy 28:55 So that he will not give to any of them of the flesh of his children whom he shall eat: because he hath nothing left him in the siege, and in the straitness, wherewith thine enemies shall distress thee in all thy gates.
# 1 Samuel 2:15 Also before they burnt the fat, the priest's servant came, and said to the man that sacrificed, Give flesh to roast for the priest; for he will not have sodden flesh of thee, but raw.
# 2 Kings 4:34 And he went up, and lay upon the child, and put his mouth upon his mouth, and his eyes upon his eyes, and his hands upon his hands: and stretched himself upon the child; and the flesh of the child waxed warm.
# 2 Kings 5:14 Then went he down, and dipped himself seven times in Jordan, according to the saying of the man of God: and his flesh came again like unto the flesh of a little child, and he was clean.
# 2 Kings 9:36 Wherefore they came again, and told him. And he said, This is the word of the LORD, which he spake by his servant Elijah the Tishbite, saying, In the portion of Jezreel shall dogs eat the flesh of Jezebel:
# Nehemiah 5:5 Yet now our flesh is as the flesh of our brethren, our children as their children: and, lo, we bring into bondage our sons and our daughters to be servants, and some of our daughters are brought unto bondage already: neither is it in our power to redeem them; for other men have our lands and vineyards.
# Job 6:12 Is my strength the strength of stones? or is my flesh of brass?
# Psalms 50:13 Will I eat the flesh of bulls, or drink the blood of goats?
# Psalms 79:2 The dead bodies of thy servants have they given to be meat unto the fowls of the heaven, the flesh of thy saints unto the beasts of the earth.
# Isaiah 9:20 And he shall snatch on the right hand, and be hungry; and he shall eat on the left hand, and they shall not be satisfied: they shall eat every man the flesh of his own arm:
# Jeremiah 19:9 And I will cause them to eat the flesh of their sons and the flesh of their daughters, and they shall eat every one the flesh of his friend in the siege and straitness, wherewith their enemies, and they that seek their lives, shall straiten them.
# Ezekiel 23:20 For she doted upon their paramours, whose flesh is as the flesh of asses, and whose issue is like the issue of horses.
# Ezekiel 39:18 Ye shall eat the flesh of the mighty, and drink the blood of the princes of the earth, of rams, of lambs, and of goats, of bullocks, all of them fatlings of Bashan.
# Ezekiel 40:43 And within were hooks, an hand broad, fastened round about: and upon the tables was the flesh of the offering.
# Micah 3:3 Who also eat the flesh of my people, and flay their skin from off them; and they break their bones, and chop them in pieces, as for the pot, and as flesh within the caldron.
# Zechariah 11:9 Then said I, I will not feed you: that that dieth, let it die; and that that is to be cut off, let it be cut off; and let the rest eat every one the flesh of another.
# Zechariah 11:16 For, lo, I will raise up a shepherd in the land, which shall not visit those that be cut off, neither shall seek the young one, nor heal that that is broken, nor feed that that standeth still: but he shall eat the flesh of the fat, and tear their claws in pieces.
# John 6:53 Then Jesus said unto them, Verily, verily, I say unto you, Except ye eat the flesh of the Son of man, and drink his blood, ye have no life in you.
# 1 Corinthians 15:39 All flesh is not the same flesh: but there is one kind of flesh of men, another flesh of beasts, another of fishes, and another of birds.
# Revelation 19:18 That ye may eat the flesh of kings, and the flesh of captains, and the flesh of mighty men, and the flesh of horses, and of them that sit on them, and the flesh of all men, both free and bond, both small and great.
# >>> 
# >>> b.Genesis.midv()
# Genesis 27:39 And Isaac his father answered and said unto him, Behold, thy dwelling shall be the fatness of the earth, and of the dew of heaven from above;
## 27 books in NT, 39 books in OT
## 38th book is book of Zecharias
# >>> p(b/"Abel"/"Z.charia.")
# Matthew 23:35 That upon you may come all the righteous blood shed upon the earth, from the blood of righteous Abel unto the blood of Zacharias son of Barachias, whom ye slew between the temple and the altar.
# Luke 11:51 From the blood of Abel unto the blood of Zacharias which perished between the altar and the temple: verily I say unto you, It shall be required of this generation.
# >>> αβ
# 'αβγδεϝζηθικλμνξοπϙρστυφχψωϡ'
# >>> from math import *
# >>> sqrt(16000)
# 126.49110640673517
# >>> 
# >>> torah=Genesis-Deuteronomy
# >>> torah
# Genesis 1:1-Deuteronomy 34:12 (5852 verses)
# >>> pf(5852)
# Counter({2: 2, 7: 1, 11: 1, 19: 1})
# >>> 76*77
# 5852
# >>> torah.midch()
# Leviticus 4:1-35 (35 verses)
# >>> torah.midv()
# Leviticus 8:8 And he put the breastplate upon him: also he put in the breastplate the Urim and the Thummim.
# Leviticus 8:9 And he put the mitre upon his head; also upon the mitre, even upon his forefront, did he put the golden plate, the holy crown; as the LORD commanded Moses.
# >>> _.tell(lsum,osum,ssum)
# And he put the breastplate upon him: also he put in the breastplate the Urim and the Thummim.
#  3 +2 + 3 + 3 +     11    + 4  + 3  + 4  +2 + 3 +2 + 3 +     11    + 3 + 4  + 3 + 3 +   7    = 74
#  19+13+ 57+ 33+    119    + 66 + 30 + 47 +13+ 57+23+ 33+    119    + 33+ 61 + 19+ 33+   97   =872
#  55+13+570+213+    704    +480 + 57 +191 +13+570+59+213+    704    +213+439 + 55+213+  637   =5399
# And he put the mitre upon his head; also upon the mitre, even upon his forefront, did he put the golden plate, the holy crown;  as the LORD commanded Moses.
#  3 +2 + 3 + 3 +  5  + 4  + 3 +  4  + 4  + 4  + 3 +  5   + 4  + 4  + 3 +    9     + 3 +2 + 3 + 3 +  6   +  5   + 3 + 4  +  5   + 2 + 3 + 4  +    9    +  5   =120
#  19+13+ 57+ 33+  65 + 66 + 36+  18 + 47 + 66 + 33+  65  + 46 + 66 + 36+   117    + 17+13+ 57+ 33+  57  +  54  + 33+ 60 +  73  + 20+ 33+ 49 +    72   +  71  =1425
#  55+13+570+213+ 344 +480 +117+  18 +191 +480 +213+ 344  +460 +480 +117+   567    + 17+13+570+213+ 156  + 306  +213+798 + 703  +101+213+184 +   207   + 305  =8661
# >>> p(_.words())
# ['And', 'he', 'put', 'the', 'breastplate', 'upon', 'him:', 'also', 'he', 'put', 'in', 'the', 'breastplate', 'the', 'Urim', 'and', 'the', 'Thummim.', 'And', 'he', 'put', 'the', 'mitre', 'upon', 'his', 'head;', 'also', 'upon', 'the', 'mitre,', 'even', 'upon', 'his', 'forefront,', 'did', 'he', 'put', 'the', 'golden', 'plate,', 'the', 'holy', 'crown;', 'as', 'the', 'LORD', 'commanded', 'Moses.']
# >>> 
# >>> _.wcs()
# [18, 30]
# >>> 
# >>> tell(lsum,osum,ssum,'Urim Thummim','Genesis','Deuteronomy')
# Urim Thummim
#  4  +   7   = 11
#  61 +   97  =158
# 439 +  637  =1076
# G e n  e  s  i  s
# 1+1+1 +1+ 1 +1+ 1 = 7
# 7+5+14+5+ 19+9+ 19= 78
# 7+5+50+5+100+9+100=276
# D e  u   t  e r  o  n  o  m   y
# 1+1+ 1 + 1 +1+1 +1 +1 +1 +1 + 1 = 11
# 4+5+ 21+ 20+5+18+15+14+15+13+ 25=155
# 4+5+300+200+5+90+60+50+60+40+700=1514
# >>> 
# >>> 
# >>> p(_.wc())
# 48
# >>> 888
# 888
# >>> b.Psalm[12:]
# Psalms 12:1-8 (8 verses)
# >>> b.Genesis.midv()
# Genesis 27:39 And Isaac his father answered and said unto him, Behold, thy dwelling shall be the fatness of the earth, and of the dew of heaven from above;
# >>> p(_),sums(_.vs()),_.wc()
# Genesis 27:39 And Isaac his father answered and said unto him, Behold, thy dwelling shall be the fatness of the earth, and of the dew of heaven from above;
# (None, (1132, 7315), 27)
# >>> 
# >>> b.chapters().index(b.Hebrews[4:])
# 1136
# >>> b.chapters()[1122]
# 1 Timothy 4:1-16 (16 verses)
# >>> p(_)
# 1 Timothy 4:1 Now the Spirit speaketh expressly, that in the latter times some shall depart from the faith, giving heed to seducing spirits, and doctrines of devils;
# 1 Timothy 4:2 Speaking lies in hypocrisy; having their conscience seared with a hot iron;
# 1 Timothy 4:3 Forbidding to marry, and commanding to abstain from meats, which God hath created to be received with thanksgiving of them which believe and know the truth.
# 1 Timothy 4:4 For every creature of God is good, and nothing to be refused, if it be received with thanksgiving:
# 1 Timothy 4:5 For it is sanctified by the word of God and prayer.
# 1 Timothy 4:6 If thou put the brethren in remembrance of these things, thou shalt be a good minister of Jesus Christ, nourished up in the words of faith and of good doctrine, whereunto thou hast attained.
# 1 Timothy 4:7 But refuse profane and old wives' fables, and exercise thyself rather unto godliness.
# 1 Timothy 4:8 For bodily exercise profiteth little: but godliness is profitable unto all things, having promise of the life that now is, and of that which is to come.
# 1 Timothy 4:9 This is a faithful saying and worthy of all acceptation.
# 1 Timothy 4:10 For therefore we both labour and suffer reproach, because we trust in the living God, who is the Saviour of all men, specially of those that believe.
# 1 Timothy 4:11 These things command and teach.
# 1 Timothy 4:12 Let no man despise thy youth; but be thou an example of the believers, in word, in conversation, in charity, in spirit, in faith, in purity.
# 1 Timothy 4:13 Till I come, give attendance to reading, to exhortation, to doctrine.
# 1 Timothy 4:14 Neglect not the gift that is in thee, which was given thee by prophecy, with the laying on of the hands of the presbytery.
# 1 Timothy 4:15 Meditate upon these things; give thyself wholly to them; that thy profiting may appear to all.
# 1 Timothy 4:16 Take heed unto thyself, and unto the doctrine; continue in them: for in doing this thou shalt both save thyself, and them that hear thee.
# >>> sums("Timothy")
# (110, 1217)
# >>> sof(110),sof(1217)
# (216, 1218)
# >>> factors(216)
# [2, 2, 2, 3, 3, 3]
# >>> list(map(sums,"Lord Jesus Christ".split()))
# [(49, 184), (74, 515), (77, 410)]
# >>> 595-515
# 80
# >>> 117-80
# 37
# >>> b/"day"/"atonement"
# Exodus 29:36...Numbers 6:11 (8 verses)
# >>> p(_)
# Exodus 29:36 And thou shalt offer every day a bullock for a sin offering for atonement: and thou shalt cleanse the altar, when thou hast made an atonement for it, and thou shalt anoint it, to sanctify it.
# Exodus 29:37 Seven days thou shalt make an atonement for the altar, and sanctify it; and it shall be an altar most holy: whatsoever toucheth the altar shall be holy.
# Leviticus 8:34 As he hath done this day, so the LORD hath commanded to do, to make an atonement for you.
# Leviticus 16:30 For on that day shall the priest make an atonement for you, to cleanse you, that ye may be clean from all your sins before the LORD.
# Leviticus 23:27 Also on the tenth day of this seventh month there shall be a day of atonement: it shall be an holy convocation unto you; and ye shall afflict your souls, and offer an offering made by fire unto the LORD.
# Leviticus 23:28 And ye shall do no work in that same day: for it is a day of atonement, to make an atonement for you before the LORD your God.
# Leviticus 25:9 Then shalt thou cause the trumpet of the jubile to sound on the tenth day of the seventh month, in the day of atonement shall ye make the trumpet sound throughout all your land.
# Numbers 6:11 And the priest shall offer the one for a sin offering, and the other for a burnt offering, and make an atonement for him, for that he sinned by the dead, and shall hallow his head that same day.
# >>> day1=b.Gen[1:1]-5
# >>> p(day1)
# Genesis 1:1 In the beginning God created the heaven and the earth.
# Genesis 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
# Genesis 1:3 And God said, Let there be light: and there was light.
# Genesis 1:4 And God saw the light, that it was good: and God divided the light from the darkness.
# Genesis 1:5 And God called the light Day, and the darkness he called Night.  And the evening and the morning were the first day.
# >>> day1.wcs()
# [10, 29, 11, 17, 22]
# >>> day1.midword()
# ['be']
# >>> ovals('be')
# [2, 5]
# >>> b.Gen[1:1].midword()
# ['created', 'the']
# >>> ' '.join(_)
# 'created the'
# >>> sums(_)
# (89, 521)
# >>> sums('cre'),sums('ate'),sums('d'),sums('the')
# ((26, 98), (26, 206), (4, 4), (33, 213))
# >>> chars(b.Gen[1:1].vs())
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'chars' is not defined
# >>> middle(_)
# ((26, 206), (4, 4))
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b.wc()
# 789627
# >>> b.midword()
# ['the']
# >>> sums("mighty")
# (82, 964)
# >>> b.Psalm[59:1]-5
# Psalms 59:1-5 (5 verses)
# >>> p(_)
# Psalms 59:1 Deliver me from mine enemies, O my God: defend me from them that rise up against me.
# Psalms 59:2 Deliver me from the workers of iniquity, and save me from bloody men.
# Psalms 59:3 For, lo, they lie in wait for my soul: the mighty are gathered against me; not for my transgression, nor for my sin, O LORD.
# Psalms 59:4 They run and prepare themselves without my fault: awake to help me, and behold.
# Psalms 59:5 Thou therefore, O LORD God of hosts, the God of Israel, awake to visit all the heathen: be not merciful to any wicked transgressors.  Selah.
# >>> (b.Psalm[59:1]-5).wcs()
# [17, 13, 25, 14, 25]
# >>> tale(_)
# [17, 30, 55, 69, 94]
# >>> pn(33)
# 137
# >>> b.Ps[59:3].vn() 
# 14794
# >>> [factors(i) for i in range(14792,14797)]
# [[2, 2, 2, 43, 43], [3, 4931], [2, 13, 569], [5, 11, 269], [2, 2, 3, 3, 3, 137]]
# >>> pf(11411)
# Counter({11411: 1})
## >>> pps=[(i,pp(i)) for i in range(1,120)]
## >>> pps
# [(1, 2), (2, 3), (3, 5), (4, 7), (5, 11), (6, 101), (7, 131), (8, 151), (9, 181), (10, 191), (11, 313), (12, 353), (13, 373), (14, 383), (15, 727), (16, 757), (17, 787), (18, 797), (19, 919), (20, 929), (21, 10301), (22, 10501), (23, 10601), (24, 11311), (25, 11411), (26, 12421), (27, 12721), (28, 12821), (29, 13331), (30, 13831), (31, 13931), (32, 14341), (33, 14741), (34, 15451), (35, 15551), (36, 16061), (37, 16361), (38, 16561), (39, 16661), (40, 17471), (41, 17971), (42, 18181), (43, 18481), (44, 19391), (45, 19891), (46, 19991), (47, 30103), (48, 30203), (49, 30403), (50, 30703), (51, 30803), (52, 31013), (53, 31513), (54, 32323), (55, 32423), (56, 33533), (57, 34543), (58, 34843), (59, 35053), (60, 35153), (61, 35353), (62, 35753), (63, 36263), (64, 36563), (65, 37273), (66, 37573), (67, 38083), (68, 38183), (69, 38783), (70, 39293), (71, 70207), (72, 70507), (73, 70607), (74, 71317), (75, 71917), (76, 72227), (77, 72727), (78, 73037), (79, 73237), (80, 73637), (81, 74047), (82, 74747), (83, 75557), (84, 76367), (85, 76667), (86, 77377), (87, 77477), (88, 77977), (89, 78487), (90, 78787), (91, 78887), (92, 79397), (93, 79697), (94, 79997), (95, 90709), (96, 91019), (97, 93139), (98, 93239), (99, 93739), (100, 94049), (101, 94349), (102, 94649), (103, 94849), (104, 94949), (105, 95959), (106, 96269), (107, 96469), (108, 96769), (109, 97379), (110, 97579), (111, 97879), (112, 98389), (113, 98689), (114, 1003001), (115, 1008001), (116, 1022201), (117, 1028201), (118, 1035301), (119, 1043401)]
# >>> npp(31102)
# (52, 31013, -89, 31102, 411, 31513, 53)
# >>> 
# >>> 31102-31013
# 89
# >>> 31513-31102
# 411
# >>> 89*411
# 36579
# >>> np(1123)
# 188
# >>> 
# >>> sof(22)
# 36
# >>> sof(33)
# 48
# >>> pn(137)
# 773
# >>> np(137)
# 33
# >>> b.wc()/pi
# 251346.71711742046
# >>> 789629/pi
# 251346.71711742046
# >>> b.Job
# Job 1:1-42:17 (1070 verses)
# >>> b.chapter(629)
# Proverbs 1:1-33 (33 verses)
# >>> 
