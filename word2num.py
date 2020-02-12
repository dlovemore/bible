from mene import *
from func import *

one2nineteen='one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'
ten2ninety='ten twenty thirty forty fifty sixty seventy eighty ninety'
wordnums={v:i for i,v in enumerate(one2nineteen.split(),start=1)}
wordnums.update({v:i*10 for i,v in enumerate(ten2ninety.split(),start=1)})
wordnums.update({"and":0, "hundred":100, "thousand":1000})
wordnums.update({"score":20, "twoscore":40, "threescore":60, "fourscore":80})

@aslist
def word2num(ws):
    if isinstance(ws, str):
        ws=[w.lower().strip(',.;') for w in ws.split(' ')]
    n=0
    for w in ws:
        if w not in wordnums:
            if n:
                yield n
            n=0
        else:
            k=wordnums[w]
            if k<100:
                if w=='score':
                    assert(k<5)
                    n=n*k
                n+=k
            if k>=100:
                n=n*k if n else k
    if n:
        yield n

# >>> from bible import *
# >>> from word2num import *
# >>> wordnums
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'and': 0, 'hundred': 100, 'thousand': 1000, 'score': 20, 'twoscore': 40, 'threescore': 60, 'fourscore': 80}
# >>> ns=word2num((Genesis[5:1]-31).text())
# >>> ns
# [130, 800, 930, 105, 807, 912, 90, 815, 905, 70, 840, 910, 65, 830, 895, 162, 800, 962, 65, 300, 365, 187, 782, 969, 182, 595, 777]
# >>> Genesis/777
# Genesis 5:31 And all the days of Lamech were seven hundred seventy and seven years: and he died.
# >>> Genesis/60
# Genesis 25:26 And after that came his brother out, and his hand took hold on Esau's heel; and his name was called Jacob: and Isaac was threescore years old when she bare them.
# >>> 
# >>> b/666
# 1 Kings 10:14...Revelation 13:18 (4 verses)
# >>> p(_)
# 1 Kings 10:14 Now the weight of gold that came to Solomon in one year was six hundred threescore and six talents of gold,
# 2 Chronicles 9:13 Now the weight of gold that came to Solomon in one year was six hundred and threescore and six talents of gold;
# Ezra 2:13 The children of Adonikam, six hundred sixty and six.
# Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
# >>> b/5000
# Joshua 8:12...Acts 4:4 (15 verses)
# >>> p(_)
# Joshua 8:12 And he took about five thousand men, and set them to lie in ambush between Bethel and Ai, on the west side of the city.
# Judges 20:45 And they turned and fled toward the wilderness unto the rock of Rimmon: and they gleaned of them in the highways five thousand men; and pursued hard after them unto Gidom, and slew two thousand men of them.
# 1 Samuel 17:5 And he had an helmet of brass upon his head, and he was armed with a coat of mail; and the weight of the coat was five thousand shekels of brass.
# 1 Chronicles 29:7 And gave for the service of the house of God of gold five thousand talents and ten thousand drams, and of silver ten thousand talents, and of brass eighteen thousand talents, and one hundred thousand talents of iron.
# 2 Chronicles 35:9 Conaniah also, and Shemaiah and Nethaneel, his brethren, and Hashabiah and Jeiel and Jozabad, chief of the Levites, gave unto the Levites for passover offerings five thousand small cattle, and five hundred oxen.
# Ezra 2:69 They gave after their ability unto the treasure of the work threescore and one thousand drams of gold, and five thousand pound of silver, and one hundred priests' garments.
# Ezekiel 45:6 And ye shall appoint the possession of the city five thousand broad, and five and twenty thousand long, over against the oblation of the holy portion: it shall be for the whole house of Israel.
# Ezekiel 48:15 And the five thousand, that are left in the breadth over against the five and twenty thousand, shall be a profane place for the city, for dwelling, and for suburbs: and the city shall be in the midst thereof.
# Matthew 14:21 And they that had eaten were about five thousand men, beside women and children.
# Matthew 16:9 Do ye not yet understand, neither remember the five loaves of the five thousand, and how many baskets ye took up?
# Mark 6:44 And they that did eat of the loaves were about five thousand men.
# Mark 8:19 When I brake the five loaves among five thousand, how many baskets full of fragments took ye up? They say unto him, Twelve.
# Luke 9:14 For they were about five thousand men. And he said to his disciples, Make them sit down by fifties in a company.
# John 6:10 And Jesus said, Make the men sit down. Now there was much grass in the place. So the men sat down, in number about five thousand.
# Acts 4:4 Howbeit many of them which heard the word believed; and the number of the men was about five thousand.
# >>> b/61000
# Numbers 31:34 And threescore and one thousand asses,
# Ezra 2:69 They gave after their ability unto the treasure of the work threescore and one thousand drams of gold, and five thousand pound of silver, and one hundred priests' garments.
# >>> b/77
# Judges 8:14 And caught a young man of the men of Succoth, and enquired of him: and he described unto him the princes of Succoth, and the elders thereof, even threescore and seventeen men.
# Ezra 8:35 Also the children of those that had been carried away, which were come out of the captivity, offered burnt offerings unto the God of Israel, twelve bullocks for all Israel, ninety and six rams, seventy and seven lambs, twelve he goats for a sin offering: all this was a burnt offering unto the LORD.
# >>> b/60
# Genesis 25:26...1 Timothy 5:9 (27 verses)
# >>> p(_)
# Genesis 25:26 And after that came his brother out, and his hand took hold on Esau's heel; and his name was called Jacob: and Isaac was threescore years old when she bare them.
# Leviticus 27:3 And thy estimation shall be of the male from twenty years old even unto sixty years old, even thy estimation shall be fifty shekels of silver, after the shekel of the sanctuary.
# Leviticus 27:7 And if it be from sixty years old and above; if it be a male, then thy estimation shall be fifteen shekels, and for the female ten shekels.
# Numbers 7:88 And all the oxen for the sacrifice of the peace offerings were twenty and four bullocks, the rams sixty, the he goats sixty, the lambs of the first year sixty. This was the dedication of the altar, after that it was anointed.
# Deuteronomy 3:4 And we took all his cities at that time, there was not a city which we took not from them, threescore cities, all the region of Argob, the kingdom of Og in Bashan.
# Joshua 13:30 And their coast was from Mahanaim, all Bashan, all the kingdom of Og king of Bashan, and all the towns of Jair, which are in Bashan, threescore cities:
# 1 Kings 4:13 The son of Geber, in Ramothgilead; to him pertained the towns of Jair the son of Manasseh, which are in Gilead; to him also pertained the region of Argob, which is in Bashan, threescore great cities with walls and brasen bars:
# 1 Kings 4:22 And Solomon's provision for one day was thirty measures of fine flour, and threescore measures of meal,
# 1 Kings 6:2 And the house which king Solomon built for the LORD, the length thereof was threescore cubits, and the breadth thereof twenty cubits, and the height thereof thirty cubits.
# 2 Kings 25:19 And out of the city he took an officer that was set over the men of war, and five men of them that were in the king's presence, which were found in the city, and the principal scribe of the host, which mustered the people of the land, and threescore men of the people of the land that were found in the city:
# 1 Chronicles 2:21 And afterward Hezron went in to the daughter of Machir the father of Gilead, whom he married when he was threescore years old; and she bare him Segub.
# 1 Chronicles 2:23 And he took Geshur, and Aram, with the towns of Jair, from them, with Kenath, and the towns thereof, even threescore cities. All these belonged to the sons of Machir the father of Gilead.
# 2 Chronicles 3:3 Now these are the things wherein Solomon was instructed for the building of the house of God. The length by cubits after the first measure was threescore cubits, and the breadth twenty cubits.
# 2 Chronicles 11:21 And Rehoboam loved Maachah the daughter of Absalom above all his wives and his concubines: (for he took eighteen wives, and threescore concubines; and begat twenty and eight sons, and threescore daughters.)
# Ezra 6:3 In the first year of Cyrus the king the same Cyrus the king made a decree concerning the house of God at Jerusalem, Let the house be builded, the place where they offered sacrifices, and let the foundations thereof be strongly laid; the height thereof threescore cubits, and the breadth thereof threescore cubits;
# Ezra 8:13 And of the last sons of Adonikam, whose names are these, Eliphelet, Jeiel, and Shemaiah, and with them threescore males.
# Psalms 90:10 The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away.
# Song of Solomon 3:7 Behold his bed, which is Solomon's; threescore valiant men are about it, of the valiant of Israel.
# Song of Solomon 6:8 There are threescore queens, and fourscore concubines, and virgins without number.
# Jeremiah 52:25 He took also out of the city an eunuch, which had the charge of the men of war; and seven men of them that were near the king's person, which were found in the city; and the principal scribe of the host, who mustered the people of the land; and threescore men of the people of the land, that were found in the midst of the city.
# Ezekiel 40:14 He made also posts of threescore cubits, even unto the post of the court round about the gate.
# Daniel 3:1 Nebuchadnezzar the king made an image of gold, whose height was threescore cubits, and the breadth thereof six cubits: he set it up in the plain of Dura, in the province of Babylon.
# Matthew 13:23 But he that received seed into the good ground is he that heareth the word, and understandeth it; which also beareth fruit, and bringeth forth, some an hundredfold, some sixty, some thirty.
# Mark 4:8 And other fell on good ground, and did yield fruit that sprang up and increased; and brought forth, some thirty, and some sixty, and some an hundred.
# Mark 4:20 And these are they which are sown on good ground; such as hear the word, and receive it, and bring forth fruit, some thirtyfold, some sixty, and some an hundred.
# Luke 24:13 And, behold, two of them went that same day to a village called Emmaus, which was from Jerusalem about threescore furlongs.
# 1 Timothy 5:9 Let not a widow be taken into the number under threescore years old, having been the wife of one man.
# >>> 
# >>> Ezra.bookn()
# 15
# >>> 
