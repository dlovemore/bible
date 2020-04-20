import itertools
from mene import *
from func import *
from word2num import *
from bible import *

@aslist
def withoutrepeats(l):
    return [x for x,y in pairs(itertools.chain(l,[None])) if x!=y]

ns=word2num((Genesis[5:1]-31).text())
ns=[(x,y) if x+y==z else zz for x,y,z in inks(3,ns)]
names=withoutrepeats(re.findall(r'(?:name|begat) ([A-Z]\w*)',Genesis[5].text()))
def tl(ns, names):
    t=0
    for (x,y),name in zip(ns,names):
        print(' '*(t//10)+'*'*(x//10)+'+'*(y//10),name)
        t+=x
ns=word2num(Genesis[11:10:25].text())[1:]
ns=inks(2,ns)
names=withoutrepeats(re.findall(r'(?:name|begat) ([A-Z]\w*)',Genesis[11:10:25].text()))

# >>> from bible import *
# >>> from timeline import *
# >>> 
# >>> ns
# [(2, 500), (35, 403), (30, 403), (34, 430), (30, 209), (32, 207), (30, 200), (29, 119)]
# >>> len(_)
# 8
# >>> 
# >>> names
# ['Arphaxad', 'Salah', 'Eber', 'Peleg', 'Reu', 'Serug', 'Nahor', 'Terah']
# >>> len(_)
# 8
# >>> p(Genesis[11:9:26])
# Genesis 11
# 9 Therefore is the name of it called Babel; because the LORD did there confound the language of all the earth: and from thence did the LORD scatter them abroad upon the face of all the earth.
# 10 These are the generations of Shem: Shem was an hundred years old, and begat Arphaxad two years after the flood:
# 11 And Shem lived after he begat Arphaxad five hundred years, and begat sons and daughters.
# 12 And Arphaxad lived five and thirty years, and begat Salah:
# 13 And Arphaxad lived after he begat Salah four hundred and three years, and begat sons and daughters.
# 14 And Salah lived thirty years, and begat Eber:
# 15 And Salah lived after he begat Eber four hundred and three years, and begat sons and daughters.
# 16 And Eber lived four and thirty years, and begat Peleg:
# 17 And Eber lived after he begat Peleg four hundred and thirty years, and begat sons and daughters.
# 18 And Peleg lived thirty years, and begat Reu:
# 19 And Peleg lived after he begat Reu two hundred and nine years, and begat sons and daughters.
# 20 And Reu lived two and thirty years, and begat Serug:
# 21 And Reu lived after he begat Serug two hundred and seven years, and begat sons and daughters.
# 22 And Serug lived thirty years, and begat Nahor:
# 23 And Serug lived after he begat Nahor two hundred years, and begat sons and daughters.
# 24 And Nahor lived nine and twenty years, and begat Terah:
# 25 And Nahor lived after he begat Terah an hundred and nineteen years, and begat sons and daughters.
# 26 And Terah lived seventy years, and begat Abram, Nahor, and Haran.
# >>> ns
# [(2, 500), (35, 403), (30, 403), (34, 430), (30, 209), (32, 207), (30, 200), (29, 119)]
# >>> 
# >>> tl(ns, names)
# ++++++++++++++++++++++++++++++++++++++++++++++++++ Arphaxad
# ***++++++++++++++++++++++++++++++++++++++++ Salah
#    ***++++++++++++++++++++++++++++++++++++++++ Eber
#       ***+++++++++++++++++++++++++++++++++++++++++++ Peleg
#           ***++++++++++++++++++++ Reu
#              ***++++++++++++++++++++ Serug
#                 ***++++++++++++++++++++ Nahor
#                    **+++++++++++ Terah
# >>> 
# >>> word2num
# Func(functools.partial(<function aslist.<locals>.tolist at 0xb639f390>, <function word2num at 0xb639f348>))
# >>> wordnums
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'and': 0, 'hundred': 100, 'thousand': 1000, 'score': 20, 'twoscore': 40, 'threescore': 60, 'fourscore': 80, 'onefold': 1, 'twofold': 2, 'threefold': 3, 'fourfold': 4, 'fivefold': 5, 'sixfold': 6, 'sevenfold': 7, 'eightfold': 8, 'ninefold': 9, 'tenfold': 10, 'elevenfold': 11, 'twelvefold': 12, 'thirteenfold': 13, 'fourteenfold': 14, 'fifteenfold': 15, 'sixteenfold': 16, 'seventeenfold': 17, 'eighteenfold': 18, 'nineteenfold': 19, 'twentyfold': 20, 'thirtyfold': 30, 'fortyfold': 40, 'fiftyfold': 50, 'sixtyfold': 60, 'seventyfold': 70, 'eightyfold': 80, 'ninetyfold': 90, 'andfold': 0, 'hundredfold': 100, 'thousandfold': 1000, 'scorefold': 20, 'twoscorefold': 40, 'threescorefold': 60, 'fourscorefold': 80}
# >>> ns=word2num((Genesis[5:1]-31).text())
# >>> ns
# [130, 800, 930, 105, 807, 912, 90, 815, 905, 70, 840, 910, 65, 830, 895, 162, 800, 962, 65, 300, 365, 187, 782, 969, 182, 595, 777]
# >>> inks(3,_)
# [(130, 800, 930), (105, 807, 912), (90, 815, 905), (70, 840, 910), (65, 830, 895), (162, 800, 962), (65, 300, 365), (187, 782, 969), (182, 595, 777)]
# >>> [x for x in inks(3,ns)]
# [(130, 800, 930), (105, 807, 912), (90, 815, 905), (70, 840, 910), (65, 830, 895), (162, 800, 962), (65, 300, 365), (187, 782, 969), (182, 595, 777)]
# >>> t=0
# >>> names=withoutrepeats(re.findall(r'(?:name|begat) ([A-Z]\w*)',Genesis[5].text()))
# >>> for (x,y,z),name in zip(_,names):
# ...     print(' '*(t//10)+'*'*(x//10)+'+'*(y//10),name)
# ...     t+=x
# ... 
# *************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Adam
#              **********++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Seth
#                        *********+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Enos
#                                 *******++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Cainan
#                                        ******+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Mahalaleel
#                                               ****************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Jared
#                                                               ******++++++++++++++++++++++++++++++ Enoch
#                                                                     ******************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methuselah
#                                                                                        ******************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Lamech
# >>> 
# >>> 
# >>> p(Genesis[5])
# Genesis 5
# 1 This is the book of the generations of Adam. In the day that God created man, in the likeness of God made he him;
# 2 Male and female created he them; and blessed them, and called their name Adam, in the day when they were created.
# 3 And Adam lived an hundred and thirty years, and begat a son in his own likeness, and after his image; and called his name Seth:
# 4 And the days of Adam after he had begotten Seth were eight hundred years: and he begat sons and daughters:
# 5 And all the days that Adam lived were nine hundred and thirty years: and he died.
# 6 And Seth lived an hundred and five years, and begat Enos:
# 7 And Seth lived after he begat Enos eight hundred and seven years, and begat sons and daughters:
# 8 And all the days of Seth were nine hundred and twelve years: and he died.
# 9 And Enos lived ninety years, and begat Cainan:
# 10 And Enos lived after he begat Cainan eight hundred and fifteen years, and begat sons and daughters:
# 11 And all the days of Enos were nine hundred and five years: and he died.
# 12 And Cainan lived seventy years and begat Mahalaleel:
# 13 And Cainan lived after he begat Mahalaleel eight hundred and forty years, and begat sons and daughters:
# 14 And all the days of Cainan were nine hundred and ten years: and he died.
# 15 And Mahalaleel lived sixty and five years, and begat Jared:
# 16 And Mahalaleel lived after he begat Jared eight hundred and thirty years, and begat sons and daughters:
# 17 And all the days of Mahalaleel were eight hundred ninety and five years: and he died.
# 18 And Jared lived an hundred sixty and two years, and he begat Enoch:
# 19 And Jared lived after he begat Enoch eight hundred years, and begat sons and daughters:
# 20 And all the days of Jared were nine hundred sixty and two years: and he died.
# 21 And Enoch lived sixty and five years, and begat Methuselah:
# 22 And Enoch walked with God after he begat Methuselah three hundred years, and begat sons and daughters:
# 23 And all the days of Enoch were three hundred sixty and five years:
# 24 And Enoch walked with God: and he was not; for God took him.
# 25 And Methuselah lived an hundred eighty and seven years, and begat Lamech.
# 26 And Methuselah lived after he begat Lamech seven hundred eighty and two years, and begat sons and daughters:
# 27 And all the days of Methuselah were nine hundred sixty and nine years: and he died.
# 28 And Lamech lived an hundred eighty and two years, and begat a son:
# 29 And he called his name Noah, saying, This same shall comfort us concerning our work and toil of our hands, because of the ground which the LORD hath cursed.
# 30 And Lamech lived after he begat Noah five hundred ninety and five years, and begat sons and daughters:
# 31 And all the days of Lamech were seven hundred seventy and seven years: and he died.
# 32 And Noah was five hundred years old: and Noah begat Shem, Ham, and Japheth.
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 

# >>> b.chapter(777)
# Jeremiah 32:1-44 (44 verses)
# >>> p(_)
# Jeremiah 32
# 1 The word that came to Jeremiah from the LORD in the tenth year of Zedekiah king of Judah, which was the eighteenth year of Nebuchadrezzar.
# 2 For then the king of Babylon's army besieged Jerusalem: and Jeremiah the prophet was shut up in the court of the prison, which was in the king of Judah's house.
# 3 For Zedekiah king of Judah had shut him up, saying, Wherefore dost thou prophesy, and say, Thus saith the LORD, Behold, I will give this city into the hand of the king of Babylon, and he shall take it;
# 4 And Zedekiah king of Judah shall not escape out of the hand of the Chaldeans, but shall surely be delivered into the hand of the king of Babylon, and shall speak with him mouth to mouth, and his eyes shall behold his eyes;
# 5 And he shall lead Zedekiah to Babylon, and there shall he be until I visit him, saith the LORD: though ye fight with the Chaldeans, ye shall not prosper.
# 6 And Jeremiah said, The word of the LORD came unto me, saying,
# 7 Behold, Hanameel the son of Shallum thine uncle shall come unto thee saying, Buy thee my field that is in Anathoth: for the right of redemption is thine to buy it.
# 8 So Hanameel mine uncle's son came to me in the court of the prison according to the word of the LORD, and said unto me, Buy my field, I pray thee, that is in Anathoth, which is in the country of Benjamin: for the right of inheritance is thine, and the redemption is thine; buy it for thyself. Then I knew that this was the word of the LORD.
# 9 And I bought the field of Hanameel my uncle's son, that was in Anathoth, and weighed him the money, even seventeen shekels of silver.
# 10 And I subscribed the evidence, and sealed it, and took witnesses, and weighed him the money in the balances.
# 11 So I took the evidence of the purchase, both that which was sealed according to the law and custom, and that which was open:
# 12 And I gave the evidence of the purchase unto Baruch the son of Neriah, the son of Maaseiah, in the sight of Hanameel mine uncle's son, and in the presence of the witnesses that subscribed the book of the purchase, before all the Jews that sat in the court of the prison.
# 13 And I charged Baruch before them, saying,
# 14 Thus saith the LORD of hosts, the God of Israel; Take these evidences, this evidence of the purchase, both which is sealed, and this evidence which is open; and put them in an earthen vessel, that they may continue many days.
# 15 For thus saith the LORD of hosts, the God of Israel; Houses and fields and vineyards shall be possessed again in this land.
# 16 Now when I had delivered the evidence of the purchase unto Baruch the son of Neriah, I prayed unto the LORD, saying,
# 17 Ah Lord GOD! behold, thou hast made the heaven and the earth by thy great power and stretched out arm, and there is nothing too hard for thee:
# 18 Thou shewest lovingkindness unto thousands, and recompensest the iniquity of the fathers into the bosom of their children after them: the Great, the Mighty God, the LORD of hosts, is his name,
# 19 Great in counsel, and mighty in work: for thine eyes are open upon all the ways of the sons of men: to give every one according to his ways, and according to the fruit of his doings:
# 20 Which hast set signs and wonders in the land of Egypt, even unto this day, and in Israel, and among other men; and hast made thee a name, as at this day;
# 21 And hast brought forth thy people Israel out of the land of Egypt with signs, and with wonders, and with a strong hand, and with a stretched out arm, and with great terror;
# 22 And hast given them this land, which thou didst swear to their fathers to give them, a land flowing with milk and honey;
# 23 And they came in, and possessed it; but they obeyed not thy voice, neither walked in thy law; they have done nothing of all that thou commandedst them to do: therefore thou hast caused all this evil to come upon them:
# 24 Behold the mounts, they are come unto the city to take it; and the city is given into the hand of the Chaldeans, that fight against it, because of the sword, and of the famine, and of the pestilence: and what thou hast spoken is come to pass; and, behold, thou seest it.
# 25 And thou hast said unto me, O Lord GOD, Buy thee the field for money, and take witnesses; for the city is given into the hand of the Chaldeans.
# 26 Then came the word of the LORD unto Jeremiah, saying,
# 27 Behold, I am the LORD, the God of all flesh: is there any thing too hard for me?
# 28 Therefore thus saith the LORD; Behold, I will give this city into the hand of the Chaldeans, and into the hand of Nebuchadrezzar king of Babylon, and he shall take it:
# 29 And the Chaldeans, that fight against this city, shall come and set fire on this city, and burn it with the houses, upon whose roofs they have offered incense unto Baal, and poured out drink offerings unto other gods, to provoke me to anger.
# 30 For the children of Israel and the children of Judah have only done evil before me from their youth: for the children of Israel have only provoked me to anger with the work of their hands, saith the LORD.
# 31 For this city hath been to me as a provocation of mine anger and of my fury from the day that they built it even unto this day; that I should remove it from before my face,
# 32 Because of all the evil of the children of Israel and of the children of Judah, which they have done to provoke me to anger, they, their kings, their princes, their priests, and their prophets, and the men of Judah, and the inhabitants of Jerusalem.
# 33 And they have turned unto me the back, and not the face: though I taught them, rising up early and teaching them, yet they have not hearkened to receive instruction.
# 34 But they set their abominations in the house, which is called by my name, to defile it.
# 35 And they built the high places of Baal, which are in the valley of the son of Hinnom, to cause their sons and their daughters to pass through the fire unto Molech; which I commanded them not, neither came it into my mind, that they should do this abomination, to cause Judah to sin.
# 36 And now therefore thus saith the LORD, the God of Israel, concerning this city, whereof ye say, It shall be delivered into the hand of the king of Babylon by the sword, and by the famine, and by the pestilence;
# 37 Behold, I will gather them out of all countries, whither I have driven them in mine anger, and in my fury, and in great wrath; and I will bring them again unto this place, and I will cause them to dwell safely:
# 38 And they shall be my people, and I will be their God:
# 39 And I will give them one heart, and one way, that they may fear me for ever, for the good of them, and of their children after them:
# 40 And I will make an everlasting covenant with them, that I will not turn away from them, to do them good; but I will put my fear in their hearts, that they shall not depart from me.
# 41 Yea, I will rejoice over them to do them good, and I will plant them in this land assuredly with my whole heart and with my whole soul.
# 42 For thus saith the LORD; Like as I have brought all this great evil upon this people, so will I bring upon them all the good that I have promised them.
# 43 And fields shall be bought in this land, whereof ye say, It is desolate without man or beast; it is given into the hand of the Chaldeans.
# 44 Men shall buy fields for money, and subscribe evidences, and seal them, and take witnesses in the land of Benjamin, and in the places about Jerusalem, and in the cities of Judah, and in the cities of the mountains, and in the cities of the valley, and in the cities of the south: for I will cause their captivity to return, saith the LORD.
# >>> 
# >>>   
