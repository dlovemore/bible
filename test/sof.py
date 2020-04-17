>>> from bible import *
>>> sof(11)
12
>>> sof(12)
28
>>> sof(26)
42
>>> 14*3
42
>>> sof(33)
48
>>> sums('woman')
(66, 651)
>>> b/'this is my body'
Matthew 26:26;Mark 14:22;Luke 22:19;1 Corinthians 11:24 (4 verses)
>>> p(_)
Matthew 26:26 And as they were eating, Jesus took bread, and blessed it, and brake it, and gave it to the disciples, and said, Take, eat; this is my body.
Mark 14:22 And as they did eat, Jesus took bread, and blessed, and brake it, and gave to them, and said, Take, eat: this is my body.
Luke 22:19 And he took bread, and gave thanks, and brake it, and gave unto them, saying, This is my body which is given for you: this do in remembrance of me.
1 Corinthians 11:24 And when he had given thanks, he brake it, and said, Take, eat: this is my body, which is broken for you: this do in remembrance of me.
>>> b/'bread of life'
John 6:35 And Jesus said unto them, I am the bread of life: he that cometh to me shall never hunger; and he that believeth on me shall never thirst.
John 6:48 I am that bread of life.
>>> sof(66)
144
>>> pf(651)
Counter({3: 1, 7: 1, 31: 1})
>>> 21*31
651
>>> count('man')+2*count('dna')
66
>>> sof(39), sof(27)
(56, 40)
>>> sof(1189)
1260
>>> sof(31102)
46656
>>> [sof(x) for x in range(152)]
[0, 1, 3, 4, 7, 6, 12, 8, 15, 13, 18, 12, 28, 14, 24, 24, 31, 18, 39, 20, 42, 32, 36, 24, 60, 31, 42, 40, 56, 30, 72, 32, 63, 48, 54, 48, 91, 38, 60, 56, 90, 42, 96, 44, 84, 78, 72, 48, 124, 57, 93, 72, 98, 54, 120, 72, 120, 80, 90, 60, 168, 62, 96, 104, 127, 84, 144, 68, 126, 96, 144, 72, 195, 74, 114, 124, 140, 96, 168, 80, 186, 121, 126, 84, 224, 108, 132, 120, 180, 90, 234, 112, 168, 128, 144, 120, 252, 98, 171, 156, 217, 102, 216, 104, 210, 192, 162, 108, 280, 110, 216, 152, 248, 114, 240, 144, 210, 182, 180, 144, 360, 133, 186, 168, 224, 156, 312, 128, 255, 176, 252, 132, 336, 160, 204, 240, 270, 138, 288, 140, 336, 192, 216, 168, 403, 180, 222, 228, 266, 150, 372, 152]
>>> sorted(set(_))
[0, 1, 3, 4, 6, 7, 8, 12, 13, 14, 15, 18, 20, 24, 28, 30, 31, 32, 36, 38, 39, 40, 42, 44, 48, 54, 56, 57, 60, 62, 63, 68, 72, 74, 78, 80, 84, 90, 91, 93, 96, 98, 102, 104, 108, 110, 112, 114, 120, 121, 124, 126, 127, 128, 132, 133, 138, 140, 144, 150, 152, 156, 160, 162, 168, 171, 176, 180, 182, 186, 192, 195, 204, 210, 216, 217, 222, 224, 228, 234, 240, 248, 252, 255, 266, 270, 280, 288, 312, 336, 360, 372, 403]
>>> nsof(368)
[367]
>>> np(367)
73
>>> 
>>> nsof(144)
[66, 70, 94, 115, 119]
>>> nsof(1260)
[520, 580, 608, 664, 716, 754, 838, 1157, 1189, 1259]
>>> nsof(930)
[464, 488, 725, 929]
>>> [17490, 19410, 22578, 24610, 24910, 25466, 25910, 26554, 26818, 27285, 29342, 29733, 29762, 31102, 31535, 32043, 32997, 33985, 35585, 36635, 37985, 39697, 41393, 41837, 42347, 44047, 45637, 45739, 45937, 46117]
[17490, 19410, 22578, 24610, 24910, 25466, 25910, 26554, 26818, 27285, 29342, 29733, 29762, 31102, 31535, 32043, 32997, 33985, 35585, 36635, 37985, 39697, 41393, 41837, 42347, 44047, 45637, 45739, 45937, 46117]
>>> p(sum(b.verses(*_[:14]), b.verse(0)))
Ecclesiastes 9:14 There was a little city, and few men within it; and there came a great king against it, and besieged it, and built great bulwarks against it:
Jeremiah 19:2 And go forth unto the valley of the son of Hinnom, which is by the entry of the east gate, and proclaim there the words that I shall tell thee,
Jonah 4:9 And God said to Jonah, Doest thou well to be angry for the gourd? And he said, I do well to be angry, even unto death.
Mark 10:21 Then Jesus beholding him loved him, and said unto him, One thing thou lackest: go thy way, sell whatsoever thou hast, and give to the poor, and thou shalt have treasure in heaven: and come, take up the cross, and follow me.
Luke 1:16 And many of the children of Israel shall he turn to the Lord their God.
Luke 12:6 Are not five sparrows sold for two farthings, and not one of them is forgotten before God?
Luke 22:45 And when he rose up from prayer, and was come to his disciples, he found them sleeping for sorrow,
John 11:30 Now Jesus was not yet come into the town, but was in that place where Martha met him.
John 18:32 That the saying of Jesus might be fulfilled, which he spake, signifying what death he should die.
Acts 10:25 And as Peter was coming in, Cornelius met him, and fell down at his feet, and worshipped him.
Ephesians 6:4 And, ye fathers, provoke not your children to wrath: but bring them up in the nurture and admonition of the Lord.
1 Timothy 3:1 This is a true saying, If a man desire the office of a bishop, he desireth a good work.
1 Timothy 4:14 Neglect not the gift that is in thee, which was given thee by prophecy, with the laying on of the hands of the presbytery.
Revelation 22:21 The grace of our Lord Jesus Christ be with you all. Amen.
>>> 
>>> nsof(103)
[]
>>> nsof(117)
[]
>>> nsof(23)
[]
>>> nsof(26)
[]
>>> nsof(69)
[]
>>> nsof(74)
[73]
>>> nsof(77)
[]
>>> nsof(151)
[]
>>> nsof(676)
[]
>>> nsof(515)
[]
>>> sums('king')
(41, 86)
>>> nsof(41)
[]
>>> nsof(86)
[]
>>> nsof(19)
[]
>>> nsof(118)
[]
>>> nsof(108)
[85, 107]
>>> nsof(113)
[]
>>> nsof(100)
[]
>>> nsof(200)
[199]
>>> nsof(60)
[24, 38, 59]
>>> nsof(40)
[27]
>>> nsof(930)
[464, 488, 725, 929]
>>> for i in _: print(repr(b.chapter(i)))
... 
Job 28:1-28 (28 verses)
Psalms 10:1-18 (18 verses)
Isaiah 46:1-13 (13 verses)
Malachi 4:1-6 (6 verses)
>>> 
>>> tell('Genes is')
Genes is
  50 +28=78
>>> tell('Genes man')
Genes man
  50 + 28=78
>>> 
>>> 
>>> 
>>> 
