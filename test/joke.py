>>> from bible import *
>>> for book in bible.books(): print(repr(book))
... 
Genesis 1:1-50:26 (1533 verses)
Exodus 1:1-40:38 (1213 verses)
Leviticus 1:1-27:34 (859 verses)
Numbers 1:1-36:13 (1288 verses)
Deuteronomy 1:1-34:12 (959 verses)
Joshua 1:1-24:33 (658 verses)
Judges 1:1-21:25 (618 verses)
Ruth 1:1-4:22 (85 verses)
1 Samuel 1:1-31:13 (810 verses)
2 Samuel 1:1-24:25 (695 verses)
1 Kings 1:1-22:53 (816 verses)
2 Kings 1:1-25:30 (719 verses)
1 Chronicles 1:1-29:30 (942 verses)
2 Chronicles 1:1-36:23 (822 verses)
Ezra 1:1-10:44 (280 verses)
Nehemiah 1:1-13:31 (406 verses)
Esther 1:1-10:3 (167 verses)
Job 1:1-42:17 (1070 verses)
Psalms 1:1-150:6 (2461 verses)
Proverbs 1:1-31:31 (915 verses)
Ecclesiastes 1:1-12:14 (222 verses)
Song of Solomon 1:1-8:14 (117 verses)
Isaiah 1:1-66:24 (1292 verses)
Jeremiah 1:1-52:34 (1364 verses)
Lamentations 1:1-5:22 (154 verses)
Ezekiel 1:1-48:35 (1273 verses)
Daniel 1:1-12:13 (357 verses)
Hosea 1:1-14:9 (197 verses)
Joel 1:1-3:21 (73 verses)
Amos 1:1-9:15 (146 verses)
Obadiah 1:1-21 (21 verses)
Jonah 1:1-4:11 (48 verses)
Micah 1:1-7:20 (105 verses)
Nahum 1:1-3:19 (47 verses)
Habakkuk 1:1-3:19 (56 verses)
Zephaniah 1:1-3:20 (53 verses)
Haggai 1:1-2:23 (38 verses)
Zechariah 1:1-14:21 (211 verses)
Malachi 1:1-4:6 (55 verses)
Matthew 1:1-28:20 (1071 verses)
Mark 1:1-16:20 (678 verses)
Luke 1:1-24:53 (1151 verses)
John 1:1-21:25 (879 verses)
Acts 1:1-28:31 (1007 verses)
Romans 1:1-16:27 (433 verses)
1 Corinthians 1:1-16:24 (437 verses)
2 Corinthians 1:1-13:14 (257 verses)
Galatians 1:1-6:18 (149 verses)
Ephesians 1:1-6:24 (155 verses)
Philippians 1:1-4:23 (104 verses)
Colossians 1:1-4:18 (95 verses)
1 Thessalonians 1:1-5:28 (89 verses)
2 Thessalonians 1:1-3:18 (47 verses)
1 Timothy 1:1-6:21 (113 verses)
2 Timothy 1:1-4:22 (83 verses)
Titus 1:1-3:15 (46 verses)
Philemon 1:1-25 (25 verses)
Hebrews 1:1-13:25 (303 verses)
James 1:1-5:20 (108 verses)
1 Peter 1:1-5:14 (105 verses)
2 Peter 1:1-3:18 (61 verses)
1 John 1:1-5:21 (105 verses)
2 John 1:1-13 (13 verses)
3 John 1:1-14 (14 verses)
Jude 1:1-25 (25 verses)
Revelation 1:1-22:21 (404 verses)
>>> 
>>> len(bible.books())
66
>>> [book.versecount() for book in bible.books()]
[1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55, 1071, 678, 1151, 879, 1007, 433, 437, 257, 149, 155, 104, 95, 89, 47, 113, 83, 46, 25, 303, 108, 105, 61, 105, 13, 14, 25, 404]
>>> sum(_)
31102
>>> bible
Genesis 1:1-Revelation 22:21 (31102 verses)
>>> sof(31102)
46656
>>> allfactors(31102)
[1, 2, 15551, 31102]
>>> sum(_)
46656
>>> 1+2+15551+31102
46656
>>> 6**6
46656
>>> b.midverse()
Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
>>> b.verse(15551,15552)
Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
>>> 
>>> b.midchapter()
Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.
>>> 
>>> min([chapter.versecount() for chapter in bible.chapters()])
2
>>> [len(book.chapters()) for book in bible.books()]
[50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
>>> max(_), sum(_)
(150, 1189)
>>> Psalms
Psalms 1:1-150:6 (2461 verses)
>>> len(Psalms.chapters())
150
>>> 31102/66/150
3.1416161616161618
>>> [book.versecount() for book in (Genesis-Job).books()]
[1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070]
>>> sum(_)
13940
>>> [chapter.versecount() for chapter in (Psalm[1:]-Psalm[102:]).chapters()]
[6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28]
>>> sum(_)
1610
>>> 13940+1610+1
15551
>>> 15551*2
31102
>>> # 1611 is the year the King James bible was first published.
>>> Psalms.verse(1611)
Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
>>> 
