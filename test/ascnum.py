# >>> from bible import *
# >>> ascsum('BILL GATES')+3
# 666
# >>> ascsum('ASCII')
# 361
# >>> tell('Lord Jesus Christ',ascsum)
# Lord Jesus Christ  =
# 401   522   621   1544
# >>> tell('Jesus Christ',ascsum)
# Jesus Christ  =
#  522   621   1143
# >>> tell('JESUS CHRIST',ascsum)
# JESUS CHRIST  =
#  394   461   855
# >>> 
# >>> tell('LORD JESUS CHRIST',ascsum)
# LORD JESUS CHRIST  =
# 305   394   461   1160
# >>> pf(1160)
# Counter({2: 3, 5: 1, 29: 1})
# >>> 
# >>> Genesis[1:1].tell(ascsum)
#  In the beginning God created the heaven and the earth.  =
# 183 321    945    282   728   321  631   307 321  532   4571
# >>> npf(4571)
# {7: 4, 653: 119}
# >>> 7*pn(119)
# 4571
# >>> ord('I')
# 73
# >>> 
# >>> ord('.')
# 46
# >>> 4571-32
# 4539
# >>> 4571+46
# 4617
# >>> pf(_)
# Counter({3: 5, 19: 1})
