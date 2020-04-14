# >>> from search import *
## Alleged contradictions from http://www.answering-christianity.com/101_bible_contradictions.htm
## 1. Who incited David to count the fighting men of Israel?
## 
## God did (2 Samuel 24: 1)
## Satan did (I Chronicles 2 1:1)
# >>> p(b["2 Samuel"][24:1]|b["1 Chronicles"][21:1])
# 2 Samuel 24:1 And again the anger of the LORD was kindled against Israel, and he moved David against them to say, Go, number Israel and Judah.
# 1 Chronicles 21:1 And Satan stood up against Israel, and provoked David to number Israel.
## Even Satan is subject to the power of God.
## See book of Job...
## 
## 2. In that count how many fighting men were found in Israel?
## 
## Eight hundred thousand (2 Samuel 24:9)
## One million, one hundred thousand (I Chronicles 21:5)
# >>> p(b["2 Samuel"][24:9]|b["1 Chronicles"][21:5])
# 2 Samuel 24:9 And Joab gave up the sum of the number of the people unto the king: and there were in Israel eight hundred thousand valiant men that drew the sword; and the men of Judah were five hundred thousand men.
# 1 Chronicles 21:5 And Joab gave the sum of the number of the people unto David. And all they of Israel were a thousand thousand and an hundred thousand men that drew sword: and Judah was four hundred threescore and ten thousand men that drew sword.
## Read and understand
## In Israel:
## 800,000 valiant men that drew sword
## 1,100,000 men that drew sword
## So in Israel men that drew sword 800,000 were valiant, 300,000 non-valiant (valiant is a term indicating that they were trained soldiers as defined in 1 Chron 5:18).
# >>> p(b["1 Chron"][5:18])
# 1 Chronicles 5:18 The sons of Reuben, and the Gadites, and half the tribe of Manasseh, of valiant men, men able to bear buckler and sword, and to shoot with bow, and skilful in war, were four and forty thousand seven hundred and threescore, that went out to the war.
## So the valiant men are able to bear buckler and sword, shoot with a bow and skilful in war.
##
## In Judah:
##   500,000 men
##   470,000 men that drew sword
## In Judah there were 470,000 men trained with a sword, and 30,000 other men.
##
## 3. How many fighting men were found in Judah?
## 
## Five hundred thousand (2 Samuel 24:9)
## Four hundred and seventy thousand (I Chronicles 21:5)
## In Judah:
##   500,000 men
##   470,000 men that drew sword
## In Judah there were 470,000 men trained with a sword, and 30,000 men not trained with a sword.
##
# >>> 
## 4. God sent his prophet to threaten David with how many years of famine?
##
## Seven (2 Samuel 24:13)
## Three (I Chronicles 21:12)
# >>> p(b["2 Samuel"][24:13]|b["1 Chronicles"][21:12])
# 2 Samuel 24:13 So Gad came to David, and told him, and said unto him, Shall seven years of famine come unto thee in thy land? or wilt thou flee three months before thine enemies, while they pursue thee? or that there be three days' pestilence in thy land? now advise, and see what answer I shall return to him that sent me.
# 1 Chronicles 21:12 Either three years' famine; or three months to be destroyed before thy foes, while that the sword of thine enemies overtaketh thee; or else three days the sword of the LORD, even the pestilence, in the land, and the angel of the LORD destroying throughout all the coasts of Israel. Now therefore advise thyself what word I shall bring again to him that sent me.
## 5. How old was Ahaziah when he began to rule over Jerusalem?
## 
## Twenty-two (2 Kings 8:26)
## Forty-two (2 Chronicles 22:2)
## Both. See https://www.youtube.com/watch?v=t9ytCE-QdCA
## *Include transcript*
##
## 6. How old was Jehoiachin when he became king of Jerusalem?
##
## Eighteen (2 Kings 24:8)
## Eight (2 Chronicles 36:9)
# >>> p(b["2 Kings"][24:8]|(b["2 Chronicles"][36:5]-9))
# 2 Kings 24:8 Jehoiachin was eighteen years old when he began to reign, and he reigned in Jerusalem three months. And his mother's name was Nehushta, the daughter of Elnathan of Jerusalem.
# 2 Chronicles 36:5 Jehoiakim was twenty and five years old when he began to reign, and he reigned eleven years in Jerusalem: and he did that which was evil in the sight of the LORD his God.
# 2 Chronicles 36:6 Against him came up Nebuchadnezzar king of Babylon, and bound him in fetters, to carry him to Babylon.
# 2 Chronicles 36:7 Nebuchadnezzar also carried of the vessels of the house of the LORD to Babylon, and put them in his temple at Babylon.
# 2 Chronicles 36:8 Now the rest of the acts of Jehoiakim, and his abominations which he did, and that which was found in him, behold, they are written in the book of the kings of Israel and Judah: and Jehoiachin his son reigned in his stead.
# 2 Chronicles 36:9 Jehoiachin was eight years old when he began to reign, and he reigned three months and ten days in Jerusalem: and he did that which was evil in the sight of the LORD.
##
## 7. How long did he rule over Jerusalem?
## 
## Three months (2 Kings 24:8)
## Three months and ten days (2 Chronicles 36:9)
## One of these time periods is simply more precise than the other. Similarly the places where years are described are not exact to the length of a year.
##
## 8. The chief of the mighty men of David lifted up his spear and killed how many men at one time?
## 
## Eight hundred (2 Samuel 23:8)
## Three hundred (I Chronicles 11: 11)
# >>> p(b["2 Samuel"][23:8]|b["1 Chronicles"][11:11])
# 2 Samuel 23:8 These be the names of the mighty men whom David had: The Tachmonite that sat in the seat, chief among the captains; the same was Adino the Eznite: he lift up his spear against eight hundred, whom he slew at one time.
# 1 Chronicles 11:11 And this is the number of the mighty men whom David had; Jashobeam, an Hachmonite, the chief of the captains: he lifted up his spear against three hundred slain by him at one time.
## These are at completely different time periods. The second is just after David started ruling in Hebron. The first is at the end of his life some 40 years later.
##
## 9. When did David bring the Ark of the Covenant to Jerusalem? Before defeating the Philistines or after?
## 
## After (2 Samuel 5 and 6)
## Before (I Chronicles 13 and 14)
##
## 
## 10. How many pairs of clean animals did God tell Noah to take into the Ark?
## 
## Two (Genesis 6:19, 20)
## Seven (Genesis 7:2). But despite this last instruction only two pairs went into the ark (Genesis 7:8-9)
## 11. When David defeated the King of Zobah, how many horsemen did he capture?
## 
## One thousand and seven hundred (2 Samuel 8:4)
## Seven thousand (I Chronicles 18:4)
## 12. How many stalls for horses did Solomon have?
## 
## Forty thousand (I Kings 4:26)
## Four thousand (2 chronicles 9:25)
## 13. In what year of King Asa's reign did Baasha, King of Israel die?
## 
## Twenty-sixth year  (I Kings 15:33 - 16:8)
## Still alive in the thirty-sixth year (2 Chronicles 16:1)
## 14. How many overseers did Solomon appoint for the work of building the temple?
## 
## Three thousand six hundred (2 Chronicles 2:2)
## Three thousand three hundred (I Kings 5:16)
## 15. Solomon built a facility containing how many baths?
## 
## Two thousand (1 Kings 7:26)
## Over three thousand (2 Chronicles 4:5)
## 16. Of the Israelites who were freed from the Babylonian captivity, how many were the children of Pahrath-Moab?
## 
## Two thousand eight hundred and twelve (Ezra 2:6)
## Two thousand eight hundred and eighteen (Nehemiah 7:11)
## 17. How many were the children of Zattu?
## 
## Nine hundred and forty-five (Ezra 2:8)
## Eight hundred and forty-five (Nehemiah 7:13)
## 18. How many were the children of Azgad?
## 
## One thousand two hundred and twenty-two (Ezra 2:12)
## Two thousand three hundred and twenty-two (Nehemiah 7:17)
## 19. How many were the children of Adin?
## 
## Four hundred and fifty-four (Ezra 2:15)
## Six hundred and fifty-five (Nehemiah 7:20)
## 20. How many were the children of Hashum?
## 
## Two hundred and twenty-three (Ezra 2:19)
## Three hundred and twenty-eight (Nehemiah 7:22)
## 21. How many were the children of Bethel and Ai?
## 
## Two hundred and twenty-three (Ezra 2:28)
## One hundred and twenty-three (Nehemiah 7:32)
## 22. Ezra 2:64 and Nehemiah 7:66 agree that the total number of the whole assembly was 42,360. Yet the numbers do not add up to anything close. The totals obtained from each book is as follows:
## 
## 29,818 (Ezra)
## 31,089 (Nehemiah)
## 23. How many singers accompanied the assembly?
## 
## Two hundred (Ezra 2:65)
## Two hundred and forty-five (Nehemiah 7:67)
## 24. What was the name of King Abijahs mother?
## 
## Michaiah, daughter of Uriel of Gibeah (2 Chronicles 13:2)
## Maachah, daughter of Absalom (2 Chronicles 11:20) But Absalom had only one daughter whose name was Tamar (2 Samuel 14:27)
## 25. Did Joshua and the Israelites capture Jerusalem?
## 
## Yes (Joshua 10:23, 40)
## No (Joshua 15:63)
## 26. Who was the father of Joseph, husband of Mary?
## 
## Jacob (Matthew 1:16)
## Hell (Luke 3:23)
## 27. Jesus descended from which son of David?
## 
## Solomon (Matthew 1:6)
## Nathan(Luke3:31)
## 28. Who was the father of Shealtiel?
## 
## Jechoniah (Matthew 1:12)
## Neri (Luke 3:27)
## 29. Which son of Zerubbabel was an ancestor of Jesus Christ?
## 
## Abiud (Matthew 1: 13)
## Rhesa (Luke 3:27) But the seven sons of Zerubbabel are as follows: i.Meshullam, ii. Hananiah, iii. Hashubah, iv. Ohel, v.Berechiah, vi. Hasadiah, viii. Jushabhesed (I Chronicles 3:19, 20). The names Abiud and Rhesa do not fit in anyway.
## 30. Who was the father of Uzziah?
## 
## Joram (Matthew 1:8)
## Amaziah (2 Chronicles 26:1)
## 31. Who was the father of Jechoniah?
## 
## Josiah (Matthew 1:11)
## Jeholakim (I Chronicles 3:16)
## 32. How many generations were there from the Babylonian exile until Christ?
## 
## Matthew says fourteen (Matthew 1:17)
## But a careful count of the generations reveals only thirteen (see Matthew 1: 12-16)
## 33. Who was the father of Shelah?
## 
## Cainan (Luke 3:35-36)
## Arphaxad (Genesis II: 12)
## 34. Was John the Baptist Elijah who was to come?
## 
## Yes (Matthew II: 14, 17:10-13)
## No (John 1:19-21)
## 35. Would Jesus inherit Davids throne?
## 
## Yes. So said the angel (Luke 1:32)
## No, since he is a descendant of Jehoiakim (see Matthew 1: I 1, I Chronicles 3:16). And Jehoiakim was cursed by God so that none of his descendants can sit upon Davids throne (Jeremiah 36:30)
## 36. Jesus rode into Jerusalem on how many animals?
## 
## One - a colt (Mark 11:7; cf Luke 19:3 5). And they brought the colt to Jesus and threw their garments on it; and he sat upon it.
## Two - a colt and an ass (Matthew 21:7). They brought the ass and the colt and put their garments on them and he sat thereon.
## 37. How did Simon Peter find out that Jesus was the Christ?
## 
## By a revelation from heaven (Matthew 16:17)
## His brother Andrew told him (John 1:41)
## 38. Where did Jesus first meet Simon Peter and Andrew?
## 
## By the sea of Galilee (Matthew 4:18-22)
## On the banks of river Jordan (John 1:42). After that, Jesus decided to go to Galilee (John 1:43)
## 39. When Jesus met Jairus was Jairus daughter already dead?
## 
## Yes. Matthew 9:18 quotes him as saying, My daughter has just died.
## No. Mark 5:23 quotes him as saying, My little daughter is at the point of death.
## 40. Did Jesus allow his disciples to keep a staff on their journey?
## 
## Yes (Mark 6:8)
## No (Matthew 10:9; Luke 9:3)
## 41. Did Herod think that Jesus was John the Baptist?
## 
## Yes (Matthew 14:2; Mark 6:16)
## No (Luke 9:9)
## 42. Did John the Baptist recognize Jesus before his baptism?
## 
## Yes (Matthew 3:13-14)
## No (John 1:32,33)
## 43. Did John the Baptist recognize Jesus after his baptism?
## 
## Yes (John 1:32, 33)
## No (Matthew 11:2)
## 44. According to the Gospel of John, what did Jesus say about bearing his own witness?
## 
## If I bear witness to myself, my testimony is not true (John 5:3 1)
## Even if I do bear witness to myself, my testimony is true (John 8:14)
## 45. When Jesus entered Jerusalem did he cleanse the temple that same day?
## 
## Yes (Matthew 21:12)
## No. He went into the temple and looked around, but since it was very late he did nothing. Instead, he went to Bethany to spend the night and returned the next morning to cleanse the temple (Mark I 1:1- 17)
## 46. The Gospels say that Jesus cursed a fig tree. Did the tree wither at once?
## 
## Yes. (Matthew 21:19)
## No. It withered overnight (Mark II: 20)
## 47. Did Judas kiss Jesus?
## 
## Yes (Matthew 26:48-50)
## No. Judas could not get close enough to Jesus to kiss him (John 18:3-12)
## 48. What did Jesus say about Peters denial?
## 
## The cock will not crow till you have denied me three times (John 13:38)
## Before the cock crows twice you will deny me three times (Mark 14:30) . When the cock crowed once, the three denials were not yet complete (see Mark 14:72). Therefore prediction (a) failed.
## 49. Did Jesus bear his own cross?
## 
## Yes (John 19:17)
## No (Matthew 27:31-32)
## 50. Did Jesus die before the curtain of the temple was torn?
## 
## Yes (Matthew 27:50-51; Mark lS:37-38)
## No. After the curtain was torn, then Jesus crying with a loud voice, said, Father, into thy hands I commit my spirit! And having said this he breathed his last (Luke 23:45-46)
## 51. Did Jesus say anything secretly?
## 
## No. I have said nothing secretly (John 18:20)
## Yes. He did not speak to them without a parable, but privately to his own disciples he explained everything (Mark 4:34). The disciples asked him Why do you speak to them in parables? He said, To you it has been given to know the secrets of the kingdom of heaven, but to them it has not been given (Matthew 13: 1 0-11)
## 52. Where was Jesus at the sixth hour on the day of the crucifixion?
## 
## On the cross (Mark 15:23)
## In Pilates court (John 19:14)
## 53. The gospels say that two thieves were crucified along with Jesus. Did both thieves mock Jesus?
## 
## Yes (Mark 15:32)
## No. One of them mocked Jesus, the other defended Jesus (Luke 23:43)
## 54. Did Jesus ascend to Paradise the same day of the crucifixion?
## 
## Yes. He said to the thief who defended him, Today you will be with me in Paradise (Luke 23:43)
## No. He said to Mary Magdelene two days later, I have not yet ascended to the Father (John 20:17)
## 55. When Paul was on the road to Damascus he saw a light and heard a voice. Did those who were with him hear the voice?
## 
## Yes (Acts9:7)
## No (Acts22:9)
## 56. When Paul saw the light he fell to the ground. Did his traveling companions also fall to the ground?
## 
## Yes (Acts 26:14)
## No (Acts 9:7)
## 57. Did the voice spell out on the spot what Pauls duties were to be?
## 
## Yes (Acts 26:16-18)
## No. The voice commanded Paul to go into the city of Damascus and there he will be told what he must do. (Acts9:7;22: 10)
## 58. When the Israelites dwelt in Shittin they committed adultery with the daughters of Moab. God struck them with a plague. How many people died in that plague?
## 
## Twenty-four thousand (Numbers 25:1 and 9)
## Twenty-three thousand (I Corinthians 10:8)
## 59. How many members of the house of Jacob came to Egypt?
## 
## Seventy souls (Genesis 4 & 27)
## Seventy-five souls (Acts 7:14)
## 60. What did Judas do with the blood money he received for betraying Jesus?
## 
## He bought a field (Acts 1: 18)
## He threw all of it into the temple and went away. The priests could not put the blood money into the temple treasury, so they used it to buy a field to bury strangers (Matthew 27:5)
## 61. How did Judas die?
## 
## After he threw the money into the temple he went away and hanged himself (Matthew 27:5)
## After he bought the field with the price of his evil deed he fell headlong and burst open in the middle and all his bowels gushed out (Acts 1:18)
## 62. Why is the field called Field of Blood?
## 
## Because the priests bought it with the blood money (Matthew 27:8)
## Because of the bloody death of Judas therein (Acts 1:19)
## 63. Who is a ransom for whom?
## 
## The Son of Man came...to give his life as a ransom for many (Mark 10:45). Christ Jesus who gave himself as a ransom for all... (I Timothy 2:5-6)
##  The wicked is a ransom for the righteous, and the faithless for the upright (Proverbs 21:18)
## 64. Is the law of Moses useful?
## 
## Yes. All scripture is... profitable... (2 Timothy 3:16)
## No. . . . A former commandment is set aside because of its weakness and uselessness... (Hebrews 7:18)
## 65. What was the exact wording on the cross?
## 
## This is Jesus the King of the Jews (Matthew 27:37)
## The King of the Jews (Mark 15:26)
## This is the King of the Jews (Luke 23:38)
## Jesus of Nazareth, the King of the Jews (John 19:19)
## 66. Did Herod want to kill John the Baptist?
## 
## Yes (Matthew 14:5)
## No. It was Herodias, the wife of Herod who wanted to kill him. But Herod knew that he was a righteous man and kept him safe (Mark 6:20)
## 67. Who was the tenth disciple of Jesus in the list of twelve?
## 
## Thaddaeus (Matthew 10: 1-4; Mark 3:13 -19)
## Judas son of James is the corresponding name in Lukes gospel (Luke 6:12-16)
## 68. Jesus saw a man sitat the tax collectors office and called him to be his disciple. What was his name?
## 
## Matthew (Matthew 9:9)
## Levi (Mark 2:14; Luke 5:27)
## 69. Was Jesus crucified on the daytime before the Passover meal or the daytime after?
## 
## After (Mark 14:12-17)
## Before. Before the feast of the Passover (John 1) Judas went out at night (John 13:30). The other disciples thought he was going out to buy supplies to prepare for the Passover meal (John 13:29). When Jesus was arrested, the Jews did not enter Pilates judgment hail because they wanted to stay clean to eat the Passover (John 18:28). When the judgment was pronounced against Jesus, it was about the sixth hour on the day of Preparation for the Passover (John 19:14)
## 70. Did Jesus pray to The Father to prevent the crucifixion?
## 
## Yes. (Matthew 26:39; Mark 14:36; Luke 22:42)
## No. (John 12:27)
## 71. In the gospels which say that Jesus prayed to avoid the cross, how many times did he move away from his disciples to pray?
## 
## Three (Matthew 26:36-46 and Mark 14:32-42)
## One. No opening is left for another two times. (Luke 22:39-46)
## 72. Matthew and Mark agree that Jesus went away and prayed three times. What were the words of the second prayer?
## 
## Mark does not give the words but he says that the words were the same as the first prayer (Mark 14:3 9)
## Matthew gives us the words, and we can see that they are not the same as in the first (Matthew 26:42)
## 73. What did the centurion say when Jesus dies?
## 
## Certainly this man was innocent (Luke 23:47)
## Truly this man was the Son of God (Mark 15:39)
## 74. When Jesus said My God, my God, why hast thou forsaken Me ? in what language did he speak?
## 
## Hebrew: the words are Eloi, Eloi ..(Matthew 27:46)
## Aramaic: the words are Eloi, Eloi .. (Mark   15:34)
## 75. According to the gospels, what were the last words of Jesus before he died?
## 
## Father, into thy hands I commit my spirit! (Luke 23:46)
## "It is finished" (John 19:30)
## 76. When Jesus entered Capernaum he healed the slave of a centurion. Did the centurion come personally to request Jesus for this?
## 
## Yes (Matthew 8:5)
## No. He sent some elders of the Jews and his friends (Luke 7:3,6)
## 77.
## 
## Adam was told that if and when he eats the forbidden fruit he would die the same day (Genesis 2:17)
## Adam ate the fruit and went on to live to a ripe old age of 930 years (Genesis 5:5)
## 78.
## 
## God decided that the life-span of humans will be limited to 120 years (Genesis 6:3)
## Many people born after that lived longer than 120. Arpachshad lived 438 years. His son Shelah lived 433 years. His son Eber lived 464 years, etc. (Genesis 11:12-16)
## 79. Apart from Jesus did anyone else ascend to heaven?
## 
## No (John 3:13)
## Yes. And Elijah went up by a whirlwind into heaven (2 Kings 2:11)
## 80. Who was high priest when David went into the house of God and ate the consecrated bread?
## 
## Abiathar (Mark 2:26)
## Ahimelech, the father of Abiathar (I Samuel 1:1; 22:20)
## 81. Was Jesus body wrapped in spices before burial in accordance with Jewish burial customs?
## 
## Yes and his female disciples witnessed his burial (John 19:39-40)
## No. Jesus was simply wrapped in a linen shroud. Then the women bought and prepared spices so that they may go and anoint him [Jesus) (Mark 16: 1)
## 82. When did the women buy the spices?
## 
## After the Sabbath was past (Mark 16:1)
## Before the Sabbath. The women prepared spices and ointments. Then, on the Sabbath they rested according to the commandment (Luke 23:55 to 24:1)
## 83. At what time of day did the women visit the tomb?
## 
## Toward the dawn (Matthew 28: 1)
## When the sun had risen (Mark 16:2)
## 84. What was the purpose for which the women went to the tomb?
## 
## To anoint Jesus body with spices (Mark 16: 1; Luke 23:55 to 24: 1)
## To see the tomb. Nothing about spices here (Matthew 28: 1)
## For no specified reason. In this gospel the wrapping with spices had been done before the Sabbath (John 20: 1)
## 85. A large stone was placed at the entrance of the tomb. Where was the stone when the women arrived?
## 
## They saw that the stone was Rolled back (Mark 16:4) They found the stone rolled away from the tomb (Luke 24:2) They saw that the stone had been taken away from the tomb (John 20:1)
## As the women approached, an angel descended from heaven, rolled away the stone, and conversed with the women. Matthew made the women witness the spectacular rolling away of the stone (Matthew 28:1-6)
## 86. Did anyone tell the women what happened to Jesus body?
## 
## Yes. A young man in a white robe (Mark 16:5). Two men ... in dazzling apparel later described as angels (Luke 24:4 and 24:23). An angel - the one who rolled back the stone (Matthew 16:2). In each case the women were told that Jesus had risen from the dead (Matthew 28:7; Mark 16:6; Luke 24:5 footnote)
## No. Mary met no one and returned saying, They have taken the Lord out of the tomb, and we do not know where they have laid him (John 20:2)
## 87. When did Mary Magdelene first meet the resurrected Jesus? And how did she react?
## 
## Mary and the other women met Jesus on their way back from their first and only visit to the tomb. They took hold of his feet and worshipped him (Matthew 28:9)
## On her second visit to the tomb Mary met Jesus just outside the tomb. When she saw Jesus she did not recognize him. She mistook him for the gardener. She still thinks that Jesus body is laid to rest somewhere and she demands to know where. But when Jesus said her name she at once recognized him and called him Teacher. Jesus said to her, Do not hold me... (John 20:11 to 17)
## 88. What was Jesus instruction for his disciples?
## 
## Tell my brethren to go to Galilee, and there they will see me (Matthew 2 8: 10)
## Go to my brethren and say to them, I am ascending to my Father and your Father, to my God and your God (John 20:17)
## 89. When did the disciples return to Galilee?
## 
## Immediately, because when they saw Jesus in Galilee some doubted (Matthew 28:17). This period of uncertainty should not persist
## After at least 40 days. That evening the disciples were still in Jerusalem (Luke 24:3 3). Jesus appeared to them there and told them, stay in the city until you are clothed with power from on high (Luke 24:49). He was appearing to them during forty days (Acts 1:3), and charged them not to depart from Jerusalem, but to wait for the promise ... (Acts 1:4)
## 90. To whom did the Midianites sell Joseph?
## 
## To the Ishmaelites (Genesis 37:28)
## To Potiphar, an officer of Pharaoh (Genesis 37:36)
## 91. Who brought Joseph to Egypt?
## 
## The Ishmaelites bought Joseph and then took Joseph to Egypt (Genesis 37:28)
## The Midianites had sold him in Egypt (Genesis 37:36)
## Joseph said to his brothers I am your brother, Joseph, whom you sold into Egypt (Genesis 45:4)
## 92. Does God change his mind?
## 
## Yes. The word of the Lord came to Samuel: I repent that I have made Saul King... (I Samuel 15:10 to 11)
## No. God will not lie or repent; for he is not a man, that he should repent (I Samuel 15:29)
##          Yes. And the Lord repented that he had made Saul King over Israel (I Samuel 15:35). Notice that the above three quotes are all from the same chapter of the same book! In addition, the Bible shows that God repented on several other occasions:
## 
## i. The Lord was sorry that he made man (Genesis 6:6)
## 
## I am sorry that I have made them (Genesis 6:7)
## 
## ii. And the Lord repented of the evil which he thought to do to his people (Exodus 32:14).
## 
## iii. (Lots of other such references).
## 
## 93. The Bible says that for each miracle Moses and Aaron demonstrated the magicians did the same by their secret arts. Then comes the following feat:
## 
## Moses and Aaron converted all the available water into blood (Exodus 7:20-21)
## The magicians did the same (Exodus 7:22). This is impossible, since there would have been no water left to convert into blood.
## 94. Who killed Goliath?
## 
## David (I Samuel 17:23, 50)
## Elhanan (2 Samuel 21:19)
## 95. Who killed Saul?
## 
## Saul took his own sword and fell upon it.... Thus Saul died... (I Samuel 31:4-6)
## An Amalekite slew him (2 Samuel 1:1- 16)
## 96. Does every man sin?
## 
## Yes. There is no man who does not sin (I Kings 8:46; see also 2 Chronicles 6:36; Proverbs 20:9; Ecclesiastes 7:20; and I John 1:810)
## No. True Christians cannot possibly sin, because they are the children of God. Every one who believes that Jesus is the Christ is a child of God.. (I John 5:1). We should be called children of God; and so we are (I John 3: 1). He who loves is born of God (I John 4:7). No one born of God commits sin; for Gods nature abides in him, and he cannot sin because he is born of God (I John 3:9). But, then again, Yes! If we say we have no sin we deceive ourselves, and the truth is not in us (I John 1:8)
## 97. Who will bear whose burden?
## 
## Bear one anothers burdens, and so fulfill the law of Christ (Galatians 6:2)
## Each man will have to bear his own load (Galatians 6:5)
## 98. How many disciples did Jesus appear to after his resurrection?
## 
## Twelve (I Corinthians 15:5)
## Eleven (Matthew 27:3-5 and Acts 1:9-26, see also Matthew 28:16; Mark 16:14 footnote; Luke 24:9; Luke 24:3 3)
## 99. Where was Jesus three days after his baptism?
## 
## After his baptism, the spirit immediately drove him out into the wilderness. And he was in the wilderness forty days ... (Mark 1:12-13)
## Next day after the baptism, Jesus selected two disciples. Second day: Jesus went to Galilee - two more disciples. Third day: Jesus was at a wedding feast in Cana in Galilee (see John 1:35; 1:43; 2:1-11)
## 100. Was baby Jesus life threatened in Jerusalem?
## 
## Yes, so Joseph fled with him to Egypt and stayed there until Herod died (Matthew 2:13 23)
## No. The family fled nowhere. They calmly presented the child at the Jerusalem temple according to the Jewish customs and returned to Galilee (Luke 2:21-40)
## 101. When Jesus walked on water how did the disciples respond?
## 
## They worshipped him, saying, Truly you are the Son of God (Matthew 14:33)
## They were utterly astounded, for they did not understand about the loaves, but their hearts were hardened (Mark 6:51-52)
# >>> p(b.Matthew[14:33]|(b.Mark[6:51]-52))
# Matthew 14:33 Then they that were in the ship came and worshipped him, saying, Of a truth thou art the Son of God.
# Mark 6:51 And he went up unto them into the ship; and the wind ceased: and they were sore amazed in themselves beyond measure, and wondered.
# Mark 6:52 For they considered not the miracle of the loaves: for their heart was hardened.
# >>> 
