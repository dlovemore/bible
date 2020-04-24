from auto import *
from search import *
from kjv import kjv

b=bible=Sel(kjv)

Genesis=b.Genesis
Exodus=b.Exodus
Leviticus=b.Leviticus
Numbers=b.Numbers
Deuteronomy=b.Deuteronomy
Joshua=b.Joshua
Judges=b.Judges
Ruth=b.Ruth
ISamuel=b['1 Samuel']
IISamuel=b['2 Samuel']
IKings=b['1 Kings']
IIKings=b['2 Kings']
IChronicles=b['1 Chronicles']
IIChronicles=b['2 Chronicles']
Ezra=b.Ezra
Nehemiah=b.Nehemiah
Esther=b.Esther
Job=b.Job
Psalm=Psalms=b.Psalms
Proverb=Proverbs=b.Proverbs
Ecclesiastes=b.Ecclesiastes
Song=Solomon=Songs=b.Song
Isaiah=b.Isaiah
Jeremiah=b.Jeremiah
Lamentations=b.Lamentations
Ezekiel=b.Ezekiel
Daniel=b.Daniel
Hosea=b.Hosea
Joel=b.Joel
Amos=b.Amos
Obadiah=b.Obadiah
Jonah=b.Jonah
Micah=b.Micah
Nahum=b.Nahum
Habakkuk=b.Habakkuk
Zephaniah=b.Zephaniah
Haggai=b.Haggai
Zechariah=b.Zechariah
Malachi=b.Malachi
Matthew=b.Matthew
Mark=b.Mark
Luke=b.Luke
John=b.John
Acts=b.Acts
Romans=b.Romans
ICorinthians=b['1 Corinthians']
IICorinthains=b['2 Corinthians']
Galatians=b.Galatians
Ephesians=b.Ephesians
Philippians=b.Philippians
Colossians=b.Colossians
IThessalonians=b['1 Thessalonians']
IIThessalonians=b['2 Thessalonians']
ITimothy=b['1 Timothy']
IITimothy=b['2 Timothy']
Titus=b.Titus
Philemon=b.Philemon
IPeter=b['1 Peter']
IIPeter=b['2 Peter']
Hebrews=b.Hebrews
James=b.James
IJohn=b['1 John']
IIJohn=b['2 John']
IIIJohn=b['3 John']
Jude=b.Jude
Revelation=b.Revelation

five=b[1]-b[5]
OT=ot=Genesis-Malachi
NT=nt=Matthew-Revelation

def show(s):
    print(f'{s} = {eval(s, globals())}')
