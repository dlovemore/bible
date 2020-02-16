    >>> from bible import *
    >>> b/'five loaves'
    1 Samuel 21:3;Matthew 14:17,19;16:9;Mark 6:41;8:19;Luke 9:13,16 (8 verses)
    >>> p(_)
    1 Samuel 21:3 Now therefore what is under thine hand? give me five loaves of bread in mine hand, or what there is present.
    Matthew 14:17 And they say unto him, We have here but five loaves, and two fishes.
    Matthew 14:19 And he commanded the multitude to sit down on the grass, and took the five loaves, and the two fishes, and looking up to heaven, he blessed, and brake, and gave the loaves to his disciples, and the disciples to the multitude.
    Matthew 16:9 Do ye not yet understand, neither remember the five loaves of the five thousand, and how many baskets ye took up?
    Mark 6:41 And when he had taken the five loaves and the two fishes, he looked up to heaven, and blessed, and brake the loaves, and gave them to his disciples to set before them; and the two fishes divided he among them all.
    Mark 8:19 When I brake the five loaves among five thousand, how many baskets full of fragments took ye up? They say unto him, Twelve.
    Luke 9:13 But he said unto them, Give ye them to eat. And they said, We have no more but five loaves and two fishes; except we should go and buy meat for all this people.
    Luke 9:16 Then he took the five loaves and the two fishes, and looking up to heaven, he blessed them, and brake, and gave to the disciples to set before the multitude.
    >>> Mark[6]
    Mark 6:1-56 (56 verses)
    >>> Mark[6:41]
    Mark 6:41 And when he had taken the five loaves and the two fishes, he looked up to heaven, and blessed, and brake the loaves, and gave them to his disciples to set before them; and the two fishes divided he among them all.
    >>> _.vn()
    24449
    >>> p(ot.vc())
    23145
    >>> _-23145
    1304
    >>> Luke[9:16]
    Luke 9:16 Then he took the five loaves and the two fishes, and looking up to heaven, he blessed them, and brake, and gave to the disciples to set before the multitude.
    >>> _.vn()
    25318
    >>> _-23145
    2173
    >>> Matthew[14:7]
    Matthew 14:7 Whereupon he promised with an oath to give her whatsoever she would ask.
    >>> _.vn()
    23605
    >>> _-23145
    460
    >>> ISamuel[21:3].vn()
    7776
    >>> ISamuel[21]|p
    1 Samuel 21
    1 Then came David to Nob to Ahimelech the priest: and Ahimelech was afraid at the meeting of David, and said unto him, Why art thou alone, and no man with thee?
    2 And David said unto Ahimelech the priest, The king hath commanded me a business, and hath said unto me, Let no man know any thing of the business whereabout I send thee, and what I have commanded thee: and I have appointed my servants to such and such a place.
    3 Now therefore what is under thine hand? give me five loaves of bread in mine hand, or what there is present.
    4 And the priest answered David, and said, There is no common bread under mine hand, but there is hallowed bread; if the young men have kept themselves at least from women.
    5 And David answered the priest, and said unto him, Of a truth women have been kept from us about these three days, since I came out, and the vessels of the young men are holy, and the bread is in a manner common, yea, though it were sanctified this day in the vessel.
    6 So the priest gave him hallowed bread: for there was no bread there but the shewbread, that was taken from before the LORD, to put hot bread in the day when it was taken away.
    7 Now a certain man of the servants of Saul was there that day, detained before the LORD; and his name was Doeg, an Edomite, the chiefest of the herdmen that belonged to Saul.
    8 And David said unto Ahimelech, And is there not here under thine hand spear or sword? for I have neither brought my sword nor my weapons with me, because the king's business required haste.
    9 And the priest said, The sword of Goliath the Philistine, whom thou slewest in the valley of Elah, behold, it is here wrapped in a cloth behind the ephod: if thou wilt take that, take it: for there is no other save that here. And David said, There is none like that; give it me.
    10 And David arose and fled that day for fear of Saul, and went to Achish the king of Gath.
    11 And the servants of Achish said unto him, Is not this David the king of the land? did they not sing one to another of him in dances, saying, Saul hath slain his thousands, and David his ten thousands?
    12 And David laid up these words in his heart, and was sore afraid of Achish the king of Gath.
    13 And he changed his behaviour before them, and feigned himself mad in their hands, and scrabbled on the doors of the gate, and let his spittle fall down upon his beard.
    14 Then said Achish unto his servants, Lo, ye see the man is mad: wherefore then have ye brought him to me?
    15 Have I need of mad men, that ye have brought this fellow to play the mad man in my presence? shall this fellow come into my house?
    >>> span(7774,7788)
    range(7774, 7789)
    >>> b/'hallowed bread'
    1 Samuel 21:4 And the priest answered David, and said, There is no common bread under mine hand, but there is hallowed bread; if the young men have kept themselves at least from women.
    1 Samuel 21:6 So the priest gave him hallowed bread: for there was no bread there but the shewbread, that was taken from before the LORD, to put hot bread in the day when it was taken away.
    >>> b.verse(7777)
    1 Samuel 21:4 And the priest answered David, and said, There is no common bread under mine hand, but there is hallowed bread; if the young men have kept themselves at least from women.
    >>> sums('Samuel')
    (71, 476)
    >>> pf(476)
    Counter({2: 2, 7: 1, 17: 1})
    >>> 4*119
    476
    >>> 
    >>> 
    >>> 
    >>> 
    >>> b.verse(5060)
    Deuteronomy 5:6 I am the LORD thy God, which brought thee out of the land of Egypt, from the house of bondage.
    >>> 5060-5
    5055
    >>> bible[5][5]
    Deuteronomy 5:1-33 (33 verses)
    >>> bible.verse(5055)
    Deuteronomy 5:1 And Moses called all Israel, and said unto them, Hear, O Israel, the statutes and judgments which I speak in your ears this day, that ye may learn them, and keep, and do them.
    >>> 
    >>> Mark[6]
    Mark 6:1-56 (56 verses)
    >>> b/'seven loaves'
    Matthew 15:36;16:10;Mark 8:6 (3 verses)
    >>> p(_)
    Matthew 15:36 And he took the seven loaves and the fishes, and gave thanks, and brake them, and gave to his disciples, and the disciples to the multitude.
    Matthew 16:10 Neither the seven loaves of the four thousand, and how many baskets ye took up?
    Mark 8:6 And he commanded the people to sit down on the ground: and he took the seven loaves, and gave thanks, and brake, and gave to his disciples to set before them; and they did set them before the people.
    >>> b.verse(4000)
    Numbers 10:11 And it came to pass on the twentieth day of the second month, in the second year, that the cloud was taken up from off the tabernacle of the testimony.
    >>> b.verse(4012)
    Numbers 10:23 And over the host of the tribe of the children of Manasseh was Gamaliel the son of Pedahzur.
    >>> b.verse(4048)
    Numbers 11:23 And the LORD said unto Moses, Is the LORD's hand waxed short? thou shalt see now whether my word shall come to pass unto thee or not.
    >>> nt.verse(4048)
    Acts 8:16 (For as yet he was fallen upon none of them: only they were baptized in the name of the Lord Jesus.)
    >>> 
