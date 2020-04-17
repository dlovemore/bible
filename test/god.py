# >>> from bible import *
# >>> from primes import *
# <console>:1: ModuleNotFoundError: No module named 'primes'
# >>> behold=b.Is[42:9]
# >>> p(behold)
# Isaiah 42:9 Behold, the former things are come to pass, and new things do I declare: before they spring forth I tell you of them.
# >>> 
# >>> sums(behold.vs())
# (91, 1040, 6341)
# >>> 1040-930
# 110
# >>> factors(1040)
# [2, 2, 2, 2, 5, 13]
# >>> pf(6431)
# Counter({59: 1, 109: 1})
# >>> sof(6431)
# 6600
# >>> 37+73
# 110
# >>> fnw=behold.words()
# >>> fnw
# ['Behold,', 'the', 'former', 'things', 'are', 'come', 'to', 'pass,', 'and', 'new', 'things', 'do', 'I', 'declare:', 'before', 'they', 'spring', 'forth', 'I', 'tell', 'you', 'of', 'them.']
# >>> tell(' '.join(_))
# Behold, the former things are come to pass, and new things do I declare: before they spring forth I tell you of them.  =
#    46    33   75     77    24  36  35   55   19  42   77   19 9    48      51    58    83     67  9  49   61 21   46  1040
# >>> [osum(w) for w in fnw]
# [46, 33, 75, 77, 24, 36, 35, 55, 19, 42, 77, 19, 9, 48, 51, 58, 83, 67, 9, 49, 61, 21, 46]
# >>> tale(_)
# [46, 79, 154, 231, 255, 291, 326, 381, 400, 442, 519, 538, 547, 595, 646, 704, 787, 854, 863, 912, 973, 994, 1040]
# >>> sums('new things')
# (9, 119, 929)
# >>> tell('new things')
# new things  =
#  42   77   119
# >>> tell('new things', ssum)
# new things  =
# 555  374   929
# >>> b.chapter(555)
# Psalms 77:1-20 (20 verses)
# >>> b.chapter(374)
# 2 Chronicles 7:1-22 (22 verses)
# >>> tell('you of them')
# you of them  =
#  61 21  46  128
# >>> tell('you of them',ssum)
# you  of them  =
# 1060 66 253  1379
# >>> 
# >>> sums('do I')
# (3, 28, 73)
# >>> [psum(w) for w in fnw]
# [109, 213, 291, 374, 96, 108, 260, 271, 55, 555, 374, 64, 9, 138, 168, 913, 326, 364, 9, 265, 1060, 66, 253]
# >>> tale(_)
# [109, 322, 613, 987, 1083, 1191, 1451, 1722, 1777, 2332, 2706, 2770, 2779, 2917, 3085, 3998, 4324, 4688, 4697, 4962, 6022, 6088, 6341]
# >>> 265*2-1
# 529
# >>> b.chapter(530)
# Psalms 52:1-9 (9 verses)
# >>> b.chapter(109)
# Leviticus 19:1-37 (37 verses)
# >>> b.chapter(1040)
# Acts 22:1-30 (30 verses)
# >>> p(_[:28])
# Acts 22:28 And the chief captain answered, With a great sum obtained I this freedom. And Paul said, But I was free born.
# >>> 
# >>> b.Is[42:9].wcs()
# [23]
# >>> fnw=b.Is[42:9].words()
# >>> [sums(w) for w in fnw]
# [(6, 46, 109), (3, 33, 213), (6, 75, 291), (6, 77, 374), (3, 24, 96), (4, 36, 108), (2, 35, 260), (4, 55, 271), (3, 19, 55), (3, 42, 555), (6, 77, 374), (2, 19, 64), (1, 9, 9), (7, 48, 138), (6, 51, 168), (4, 58, 913), (6, 83, 326), (5, 67, 364), (1, 9, 9), (4, 49, 265), (3, 61, 1060), (2, 21, 66), (4, 46, 253)]
# >>> 
# >>> 
# >>> 
# >>> sums('freedom')
# (7, 66, 210)
# >>> sums('great')
# (5, 51, 303)
# >>> sums('sum')
# (3, 53, 440)
# >>> sums('Jesus')
# (5, 74, 515)
# >>> tell('LORD OF LORDS')
# LORD OF LORDS  =
#  49  21   68  138
# >>> tell('KING OF KINGS')
# KING OF KINGS  =
#  41  21   60  122
# >>> tell('Immanuel')
# I m  m  a n  u  e l  =
# 9 13 13 1 14 21 5 12 88
# >>> tell('el')
# e l  =
# 5 12 17
# >>> tell('el o him')
# el o  him =
# 17 15  30 62
# >>> tell('In the beginning')
# In the beginning  =
# 23  33     81    137
# >>> 
# >>> tell("Κυριος Ιησους Χριστος")
# Κυριος Ιησους Χριστος  =
#   98     96     130   324
# >>> tell("Κυριος Ιησους Χριστος",ssum)
# Κυριος Ιησους Χριστος  =
#  800    888     1480  3168
# >>> 3168/22
# 144.0
# >>> 144*22
# 3168
# >>> tell('יא  מֵעֲמַל נַפְשׁוֹ, יִרְאֶה יִשְׂבָּע--בְּדַעְתּוֹ יַצְדִּיק צַדִּיק עַבְדִּי, לָרַבִּים; וַעֲוֺנֹתָם, הוּא יִסְבֹּל.',osum,ssum) # Isaiah 53:11
# יא מֵעֲמַל נַפְשׁוֹ, יִרְאֶה יִשְׂבָּע--בְּדַעְתּוֹ יַצְדִּיק צַדִּיק עַבְדִּי, לָרַבִּים; וַעֲוֺנֹתָם, הוּא יִסְבֹּל.  =
# 11  54    58   36       99       61   51    32    57      77    12   39  587
# 11 180   436  216      864      214  204    86   282     572    12  102  3179
# >>> tell('מֵעֲמַל נַפְשׁוֹ, יִרְאֶה יִשְׂבָּע--בְּדַעְתּוֹ יַצְדִּיק צַדִּיק עַבְדִּי, לָרַבִּים; וַעֲוֺנֹתָם, הוּא יִסְבֹּל.',osum,ssum)
# מֵעֲמַל נַפְשׁוֹ, יִרְאֶה יִשְׂבָּע--בְּדַעְתּוֹ יַצְדִּיק צַדִּיק עַבְדִּי, לָרַבִּים; וַעֲוֺנֹתָם, הוּא יִסְבֹּל.  =
#  54    58   36       99       61   51    32    57      77    12   39  576
# 180   436  216      864      214  204    86   282     572    12  102  3168
# >>> Isaiah[53:11].tell(osum,ssum)
# He shall see of the travail of his soul, and shall be satisfied:  by his knowledge shall  my righteous servant justify many; for he shall bear their iniquities.   =
# 13   52   29 21  33    83   21  36   67   19   52  7      92      27  36     96      52   38    122       99     110     53   39 13   52   26    60      132      1480
# 13  169  110 66 213   731   66 117  490   55  169  7     434     702 117    681     169  740    779      846     1325   791  156 13  169   98   312      771     10309
# >>> 
# >>> 
# >>> 53*11
# 583
# >>> 587-11
# 576
# >>> 583-576
# 7
# >>> 3168//22
# 144
# >>> 144822
# 144822
# >>> 144*22
# 3168
# >>> Isaiah[53:11].tell()
# He shall see of the travail of his soul, and shall be satisfied: by his knowledge shall my righteous servant justify many; for he shall bear their iniquities.  =
# 13   52   29 21  33    83   21  36   67   19   52  7      92     27  36     96      52  38    122       99     110     53   39 13   52   26    60      132     1480
# >>> fs(1480)
# [2, 2, 2, 5, 37]
# >>> 40*37
# 1480
# >>> 24*37
# 888
# >>> pf(800)
# Counter({2: 5, 5: 2})
# >>> 
# >>> Isaiah[53:11].tell(ssum)
# He shall see of the travail of his soul, and shall be satisfied:  by his knowledge shall  my righteous servant justify many; for he shall bear their iniquities.   =
# 13  169  110 66 213   731   66 117  490   55  169  7     434     702 117    681     169  740    779      846     1325   791  156 13  169   98   312      771     10309
# >>> factors(10309)
# [13, 13, 61]
# >>> p(Isaiah[53])
# Isaiah 53
# 1 Who hath believed our report? and to whom is the arm of the LORD revealed?
# 2 For he shall grow up before him as a tender plant, and as a root out of a dry ground: he hath no form nor comeliness; and when we shall see him, there is no beauty that we should desire him.
# 3 He is despised and rejected of men; a man of sorrows, and acquainted with grief: and we hid as it were our faces from him; he was despised, and we esteemed him not.
# 4 Surely he hath borne our griefs, and carried our sorrows: yet we did esteem him stricken, smitten of God, and afflicted.
# 5 But he was wounded for our transgressions, he was bruised for our iniquities: the chastisement of our peace was upon him; and with his stripes we are healed.
# 6 All we like sheep have gone astray; we have turned every one to his own way; and the LORD hath laid on him the iniquity of us all.
# 7 He was oppressed, and he was afflicted, yet he opened not his mouth: he is brought as a lamb to the slaughter, and as a sheep before her shearers is dumb, so he openeth not his mouth.
# 8 He was taken from prison and from judgment: and who shall declare his generation? for he was cut off out of the land of the living: for the transgression of my people was he stricken.
# 9 And he made his grave with the wicked, and with the rich in his death; because he had done no violence, neither was any deceit in his mouth.
# 10 Yet it pleased the LORD to bruise him; he hath put him to grief: when thou shalt make his soul an offering for sin, he shall see his seed, he shall prolong his days, and the pleasure of the LORD shall prosper in his hand.
# 11 He shall see of the travail of his soul, and shall be satisfied: by his knowledge shall my righteous servant justify many; for he shall bear their iniquities.
# 12 Therefore will I divide him a portion with the great, and he shall divide the spoil with the strong; because he hath poured out his soul unto death: and he was numbered with the transgressors; and he bare the sin of many, and made intercession for the transgressors.
# >>> Isaiah[53:8].tell()
# He was taken from prison and from judgment: and who shall declare his generation? for he was cut off out of the land of the living: for the transgression of my people was he stricken.  =
# 13  43   51   52    91    19  52      94     19  46   52     48    36     108      39 13  43  44  27  56 21  33  31  21  33    73    39  33      178      21 38   69    43 13     99    1691
# >>> Isaiah[53:8].tell(ssum)
# He was taken from prison and from judgment: and who shall declare his generation? for he was cut off out of the land of the living: for the transgression of  my people was he stricken.   =
# 13 601  276  196   379    55 196     616     55 568  169    138   117     477     156 13 601 503  72 560 66 213  85  66 213   505   156 213      862      66 740  240   601 13    477    10277
# >>> 
# >>> factors(1691)
# [19, 89]
# >>> 
# >>> tell('word')
# w  o  r  d =
# 23 15 18 4 60
# >>> tell('word',ssum)
#  w  o  r  d  =
# 500 60 90 4 654
# >>> tell('Word of God')
# Word of God  =
#  60  21  26 107
# >>> tell('Word of God',ssum)
# Word of God  =
# 654  66  71 791
# >>> factors(791)
# [7, 113]
# >>> tell('Lord Jesus Christ',ssum)
# Lord Jesus Christ  =
# 184   515   410   1109
# >>> factors(1109)
# [1109]
# >>> np(1109)
# 186
# >>> 
# >>> 
# >>> factors(186)
# [2, 3, 31]
# >>> 1189-1109
# 80
# >>> tell('Lord Jesus Christ',ssum)
# Lord Jesus Christ  =
# 184   515   410   1109
# >>> b/r'jah\b'
# Psalms 68:4 Sing unto God, sing praises to his name: extol him that rideth upon the heavens by his name JAH, and rejoice before him.
# >>> tell('JAH')
# J  A H =
# 10 1 8 19
# >>> tell('and',ssum)
# a n  d =
# 1 50 4 55
# >>> 103*5
# 515
# >>> 
# >>> tell('יְהֹוָה')
#  יְ הֹ וָ ה =
# 10 5 6 5 26
# >>> tell('אֱלֹהִים',osum)
# אֱ  לֹ הִ י  ם  =
# 1 12 5 10 13 41
# >>> tell('אֱלֹהִים',ssum)
# אֱ  לֹ הִ י  ם  =
# 1 30 5 10 40 86
# >>> sums("king")
# (41, 86)
# >>> sums('shiloh')
# (71, 215)
# >>> b/'shiloh'
# Genesis 49:10;Joshua 18:1,8-10;19:51;21:2;22:9,12;Judges 18:31;21:12,19,21;1 Samuel 1:3,9,24;2:14;3:21;4:3-4,12;14:3;1 Kings 2:27;14:2,4;Psalms 78:60;Jeremiah 7:12,14;26:6,9;41:5 (31 verses)
# >>> p(_)
# Genesis 49:10 The sceptre shall not depart from Judah, nor a lawgiver from between his feet, until Shiloh come; and unto him shall the gathering of the people be.
# Joshua 18
# 1 And the whole congregation of the children of Israel assembled together at Shiloh, and set up the tabernacle of the congregation there. And the land was subdued before them.
# 8 And the men arose, and went away: and Joshua charged them that went to describe the land, saying, Go and walk through the land, and describe it, and come again to me, that I may here cast lots for you before the LORD in Shiloh.
# 9 And the men went and passed through the land, and described it by cities into seven parts in a book, and came again to Joshua to the host at Shiloh.
# 10 And Joshua cast lots for them in Shiloh before the LORD: and there Joshua divided the land unto the children of Israel according to their divisions.
# Joshua 19:51 These are the inheritances, which Eleazar the priest, and Joshua the son of Nun, and the heads of the fathers of the tribes of the children of Israel, divided for an inheritance by lot in Shiloh before the LORD, at the door of the tabernacle of the congregation. So they made an end of dividing the country.
# Joshua 21:2 And they spake unto them at Shiloh in the land of Canaan, saying, The LORD commanded by the hand of Moses to give us cities to dwell in, with the suburbs thereof for our cattle.
# Joshua 22:9 And the children of Reuben and the children of Gad and the half tribe of Manasseh returned, and departed from the children of Israel out of Shiloh, which is in the land of Canaan, to go unto the country of Gilead, to the land of their possession, whereof they were possessed, according to the word of the LORD by the hand of Moses.
# Joshua 22:12 And when the children of Israel heard of it, the whole congregation of the children of Israel gathered themselves together at Shiloh, to go up to war against them.
# Judges 18:31 And they set them up Micah's graven image, which he made, all the time that the house of God was in Shiloh.
# Judges 21
# 12 And they found among the inhabitants of Jabeshgilead four hundred young virgins, that had known no man by lying with any male: and they brought them unto the camp to Shiloh, which is in the land of Canaan.
# 19 Then they said, Behold, there is a feast of the LORD in Shiloh yearly in a place which is on the north side of Bethel, on the east side of the highway that goeth up from Bethel to Shechem, and on the south of Lebonah.
# 21 And see, and, behold, if the daughters of Shiloh come out to dance in dances, then come ye out of the vineyards, and catch you every man his wife of the daughters of Shiloh, and go to the land of Benjamin.
# 1 Samuel 1
# 3 And this man went up out of his city yearly to worship and to sacrifice unto the LORD of hosts in Shiloh. And the two sons of Eli, Hophni and Phinehas, the priests of the LORD, were there.
# 9 So Hannah rose up after they had eaten in Shiloh, and after they had drunk. Now Eli the priest sat upon a seat by a post of the temple of the LORD.
# 24 And when she had weaned him, she took him up with her, with three bullocks, and one ephah of flour, and a bottle of wine, and brought him unto the house of the LORD in Shiloh: and the child was young.
# 1 Samuel 2:14 And he struck it into the pan, or kettle, or caldron, or pot; all that the fleshhook brought up the priest took for himself. So they did in Shiloh unto all the Israelites that came thither.
# 1 Samuel 3:21 And the LORD appeared again in Shiloh: for the LORD revealed himself to Samuel in Shiloh by the word of the LORD.
# 1 Samuel 4
# 3 And when the people were come into the camp, the elders of Israel said, Wherefore hath the LORD smitten us to day before the Philistines? Let us fetch the ark of the covenant of the LORD out of Shiloh unto us, that, when it cometh among us, it may save us out of the hand of our enemies.
# 4 So the people sent to Shiloh, that they might bring from thence the ark of the covenant of the LORD of hosts, which dwelleth between the cherubims: and the two sons of Eli, Hophni and Phinehas, were there with the ark of the covenant of God.
# 12 And there ran a man of Benjamin out of the army, and came to Shiloh the same day with his clothes rent, and with earth upon his head.
# 1 Samuel 14:3 And Ahiah, the son of Ahitub, Ichabod's brother, the son of Phinehas, the son of Eli, the LORD's priest in Shiloh, wearing an ephod. And the people knew not that Jonathan was gone.
# 1 Kings 2:27 So Solomon thrust out Abiathar from being priest unto the LORD; that he might fulfil the word of the LORD, which he spake concerning the house of Eli in Shiloh.
# 1 Kings 14:2 And Jeroboam said to his wife, Arise, I pray thee, and disguise thyself, that thou be not known to be the wife of Jeroboam; and get thee to Shiloh: behold, there is Ahijah the prophet, which told me that I should be king over this people.
# 1 Kings 14:4 And Jeroboam's wife did so, and arose, and went to Shiloh, and came to the house of Ahijah. But Ahijah could not see; for his eyes were set by reason of his age.
# Psalms 78:60 So that he forsook the tabernacle of Shiloh, the tent which he placed among men;
# Jeremiah 7:12 But go ye now unto my place which was in Shiloh, where I set my name at the first, and see what I did to it for the wickedness of my people Israel.
# Jeremiah 7:14 Therefore will I do unto this house, which is called by my name, wherein ye trust, and unto the place which I gave to you and to your fathers, as I have done to Shiloh.
# Jeremiah 26:6 Then will I make this house like Shiloh, and will make this city a curse to all the nations of the earth.
# Jeremiah 26:9 Why hast thou prophesied in the name of the LORD, saying, This house shall be like Shiloh, and this city shall be desolate without an inhabitant? And all the people were gathered against Jeremiah in the house of the LORD.
# Jeremiah 41:5 That there came certain from Shechem, from Shiloh, and from Samaria, even fourscore men, having their beards shaven, and their clothes rent, and having cut themselves, with offerings and incense in their hand, to bring them to the house of the LORD.
# >>> pf(515)
# Counter({5: 1, 103: 1})
# >>> 
# >>> tell('κύριος ἰησοῦς χριστὸς')
# κύριος ἰησοῦς χριστὸς  =
#   98     96     130   324
# >>> tell('κύριος ἰησοῦς χριστὸς',ssum)
# κύριος ἰησοῦς χριστὸς  =
#  800    888     1480  3168
# >>> sums('יהושוע')
# (64, 397)
# >>> sums('יהוֹשֻׁעַ')
# (58, 391)
# >>> 
