from dna import *
class AD(dict):
    def __getattr__(self,k):
        return self[k]
    def __setattr__(self,k,v):
        self[k]=v

wheat=AD({'bps':14547261565,'name':'triticum aestivum'})
barley=AD({'bps':4834432680, 'name':'hordeum vulgare'})

# >>> from bible import *
# >>> from wheat import *
# >>> from dna import *
# >>> wheat.bps
# 14547261565
# >>> AY
# 3088286401
# >>> wheat.bps/(AY)
# 4.710463887121847
# >>> math.pi*3/2
# 4.71238898038469
# >>> wheat.bps/(AY)*2/3
# 3.1403092580812313
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tell(wheat.name,lsum,osum,ssum)
# triticum aestivum
#    8    +   8    = 16
#   113   +  110   =223
#   851   +  1055  =1906
# >>> 22*3
# 66
# >>> 1906,osum('dna'),6
# (1906, 19, 6)
# >>> Luke.vi(223)
# Luke 5:9 For he was astonished, and all that were with him, at the draught of the fishes which they had taken:
# >>> 
# >>> 
# >>> John[6:10].vn()-John.vn()+1
# 223
# >>> John[6:10]
# John 6:10 And Jesus said, Make the men sit down. Now there was much grass in the place. So the men sat down, in number about five thousand.
# >>> _.tell(lsum,osum,ssum)
# And Jesus said, Make the men sit down. Now there was much grass in the place.  So the men sat down, in number about five thousand.
#  3 +  5  +  4  + 4  + 3 + 3 + 3 +  4  + 3 +  5  + 3 + 4  +  5  +2 + 3 +  5   + 2 + 3 + 3 + 3 +  4  +2 +  6   +  5  + 4  +    8    = 99
#  19+  74 +  33 + 30 + 33+ 32+ 48+  56 + 52+  56 + 43+ 45 +  64 +23+ 33+  37  + 34+ 33+ 32+ 40+  56 +23+  73  +  59 + 42 +   102   =1172
#  55+ 515 + 114 + 66 +213+ 95+309+ 614 +610+ 308 +601+351 + 298 +59+213+ 109  +160+213+ 95+301+ 614 +59+ 487  + 563 +420 +   723   =8165
# >>> 
# >>> 
# >>> tell('grass')
# g r  a s  s
# 7+18+1+19+19=64
# >>> tell('g dna dna dna')
# g dna dna dna
# 7+ 19+ 19+ 19=64
# >>> wheat.bps/barley.bps
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'wheat' is not defined
# >>> Revelation[6:6]
# Revelation 6:6 And I heard a voice in the midst of the four beasts say, A measure of wheat for a penny, and three measures of barley for a penny; and see thou hurt not the oil and the wine.
# >>> _.tell()
# And I heard a voice in the midst of the four beasts say, A measure of wheat for a penny, and three measures of barley for a penny; and see thou hurt not the oil and the wine.
#  19+9+  36 +1+  54 +23+ 33+  65 +21+ 33+ 60 +  66  + 45 +1+   82  +21+  57 + 39+1+  74  + 19+  56 +  101   +21+  63  + 39+1+  74  + 19+ 29+ 64 + 67 + 49+ 33+ 36+ 19+ 33+  51 =1514
# >>> 
# >>> osum('wheat'),3*osum('dna')
# (57, 57)
# >>> sums('wheat')
# (57, 714)
# >>> sums('barley')
# (63, 828)
# >>> sums('grass')
# (64, 298)
# >>> tell('sev en times nine')
# sev en times nine
#  46+19+  66 + 42 =173
# >>> tell('times and laws',osum,ssum)
# times and laws
#   66 + 19+ 55 =140
#  354 + 55+631 =1040
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> npp(10501)
# 22
# >>> math.sqrt(10501/1064)
# 3.141553899307736
# >>> pf(1064)
# Counter({2: 3, 7: 1, 19: 1})
# >>> math.pi**2*1123
# 11083.565742423349
# >>> math.pi**2*1189
# 11734.959632895247
# >>> 
# >>> 
# >>> tell('spelta')
# s  p  e l  t  a
# 19+16+5+12+20+1=73
# >>> tell('einkorn')
# e i n  k  o  r  n
# 5+9+14+11+15+18+14=86
# >>> 
# >>> 223+73
# 296
# >>> tell('triticum aestivum')
# triticum aestivum
#   113   +  110   =223
# >>> Genesis[1:1].tell()
# In the beginning God created the heaven and the earth.
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# >>> 23+33,81+26,56+33,55+19,33+52
# (56, 107, 89, 74, 85)
# >>> 
# >>> tell("the hitchhiker's guide to the galaxy",lsum,osum,ssum)
# the hitchhiker's guide  to the galaxy
#  3 +     11     +  5  + 2 + 3 +  6   = 30
#  33+    118     +  46 + 35+ 33+  70  =335
# 213+    460     + 325 +260+213+ 1339 =2810
# >>> tell('hhgg')
# h h g g
# 8+8+7+7=30
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
