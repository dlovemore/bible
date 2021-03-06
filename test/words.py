# >>> from bible import *
# >>> from primes import *
# <2>:1: ModuleNotFoundError: No module named 'primes'
# >>> from search import *
# >>> tri(29)
# 435
# >>> p(b.Ecc[7:])
# Ecclesiastes 7
# 1 A good name is better than precious ointment; and the day of death than the day of one's birth.
# 2 It is better to go to the house of mourning, than to go to the house of feasting: for that is the end of all men; and the living will lay it to his heart.
# 3 Sorrow is better than laughter: for by the sadness of the countenance the heart is made better.
# 4 The heart of the wise is in the house of mourning; but the heart of fools is in the house of mirth.
# 5 It is better to hear the rebuke of the wise, than for a man to hear the song of fools.
# 6 For as the crackling of thorns under a pot, so is the laughter of the fool: this also is vanity.
# 7 Surely oppression maketh a wise man mad; and a gift destroyeth the heart.
# 8 Better is the end of a thing than the beginning thereof: and the patient in spirit is better than the proud in spirit.
# 9 Be not hasty in thy spirit to be angry: for anger resteth in the bosom of fools.
# 10 Say not thou, What is the cause that the former days were better than these? for thou dost not enquire wisely concerning this.
# 11 Wisdom is good with an inheritance: and by it there is profit to them that see the sun.
# 12 For wisdom is a defence, and money is a defence: but the excellency of knowledge is, that wisdom giveth life to them that have it.
# 13 Consider the work of God: for who can make that straight, which he hath made crooked?
# 14 In the day of prosperity be joyful, but in the day of adversity consider: God also hath set the one over against the other, to the end that man should find nothing after him.
# 15 All things have I seen in the days of my vanity: there is a just man that perisheth in his righteousness, and there is a wicked man that prolongeth his life in his wickedness.
# 16 Be not righteous over much; neither make thyself over wise: why shouldest thou destroy thyself?
# 17 Be not over much wicked, neither be thou foolish: why shouldest thou die before thy time?
# 18 It is good that thou shouldest take hold of this; yea, also from this withdraw not thine hand: for he that feareth God shall come forth of them all.
# 19 Wisdom strengtheneth the wise more than ten mighty men which are in the city.
# 20 For there is not a just man upon earth, that doeth good, and sinneth not.
# 21 Also take no heed unto all words that are spoken; lest thou hear thy servant curse thee:
# 22 For oftentimes also thine own heart knoweth that thou thyself likewise hast cursed others.
# 23 All this have I proved by wisdom: I said, I will be wise; but it was far from me.
# 24 That which is far off, and exceeding deep, who can find it out?
# 25 I applied mine heart to know, and to search, and to seek out wisdom, and the reason of things, and to know the wickedness of folly, even of foolishness and madness:
# 26 And I find more bitter than death the woman, whose heart is snares and nets, and her hands as bands: whoso pleaseth God shall escape from her; but the sinner shall be taken by her.
# 27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# 28 Which yet my soul seeketh, but I find not: one man among a thousand have I found; but a woman among all those have I not found.
# 29 Lo, this only have I found, that God hath made man upright; but they have sought out many inventions.
# >>> tell('lord jesus christ')
# lord jesus christ  =
#  49    74    77   200
# >>> 
# >>> tell('Passover of the Lamb of God')
# Passover of the Lamb of God  =
#   115    21  33  28  21  26 244
# >>> tell('the pass over')
# the pass over  =
#  33  55   60  148
# >>> bw=set(b.ws())
# >>> len(bw)
# 13821
# >>> bw=set((s.lower() for s in bible.words()))
# >>> len(bw)
# 27646
# >>> 
# >>> bw=set((s.lower() for s in bible.ws()))
# >>> len(bw)
# 12848
# >>> ns(_)
# [2, 2, 2, 2, 11, 73] [1, 1, 1, 1, 5, 21]
# >>> 176*73
# 12848
# >>> 
# >>> bw=set((s.strip("'") for s in bw))
# >>> len(bw)
# 12786
# >>> 12848-12786
# 62
# >>> 
# >>> ns(_)
# [2, 3, 2131] [1, 2, 321]
# >>> 
# >>> sorted(bw)[:100]
# ['a', 'aaron', "aaron's", 'aaronites', 'abaddon', 'abagtha', 'abana', 'abarim', 'abase', 'abased', 'abasing', 'abated', 'abba', 'abda', 'abdeel', 'abdi', 'abdiel', 'abdon', 'abednego', 'abel', 'abelbethmaachah', 'abelmaim', 'abelmeholah', 'abelmizraim', 'abelshittim', 'abez', 'abhor', 'abhorred', 'abhorrest', 'abhorreth', 'abhorring', 'abi', 'abia', 'abiah', 'abialbon', 'abiasaph', 'abiathar', "abiathar's", 'abib', 'abida', 'abidah', 'abidan', 'abide', 'abideth', 'abiding', 'abiel', 'abiezer', 'abiezrite', 'abiezrites', 'abigail', 'abihail', 'abihu', 'abihud', 'abijah', 'abijam', 'abilene', 'ability', 'abimael', 'abimelech', "abimelech's", 'abinadab', 'abinoam', 'abiram', 'abishag', 'abishai', 'abishalom', 'abishua', 'abishur', 'abital', 'abitub', 'abiud', 'abjects', 'able', 'abner', "abner's", 'aboard', 'abode', 'abodest', 'abolish', 'abolished', 'abominable', 'abominably', 'abomination', 'abominations', 'abound', 'abounded', 'aboundeth', 'abounding', 'about', 'above', 'abraham', "abraham's", 'abram', "abram's", 'abroad', 'absalom', 'absalom!', "absalom's", 'absence', 'absent']
# >>> wn=[(count(w), w) for w in bw]
# >>> 
# >>> 
# >>> pf(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/home/pi/bible/primes.py", line 84, in pf
#     return collections.Counter(factors(n))
#   File "/home/pi/bible/primes.py", line 71, in factors
#     for p in (prime(j) for j in range(1,n)):
# TypeError: 'list' object cannot be interpreted as an integer
# >>> 
# >>> 
