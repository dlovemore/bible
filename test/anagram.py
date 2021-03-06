# >>> from bible import *
# >>> P=itertools.permutations
# >>> help(P)
# Help on class permutations in module itertools:
# 
# class permutations(builtins.object)
#  |  permutations(iterable[, r]) --> permutations object
#  |  
#  |  Return successive r-length permutations of elements in the iterable.
#  |  
#  |  permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
#  |  
#  |  Methods defined here:
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __next__(self, /)
#  |      Implement next(self).
#  |  
#  |  __reduce__(...)
#  |      Return state information for pickling.
#  |  
#  |  __setstate__(...)
#  |      Set state information for unpickling.
#  |  
#  |  __sizeof__(...)
#  |      Returns size in memory, in bytes.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
# 
# >>> P(range(5),5)
# <itertools.permutations object at 0xb62816f0>
# >>> list(_)
# [(0, 1, 2, 3, 4), (0, 1, 2, 4, 3), (0, 1, 3, 2, 4), (0, 1, 3, 4, 2), (0, 1, 4, 2, 3), (0, 1, 4, 3, 2), (0, 2, 1, 3, 4), (0, 2, 1, 4, 3), (0, 2, 3, 1, 4), (0, 2, 3, 4, 1), (0, 2, 4, 1, 3), (0, 2, 4, 3, 1), (0, 3, 1, 2, 4), (0, 3, 1, 4, 2), (0, 3, 2, 1, 4), (0, 3, 2, 4, 1), (0, 3, 4, 1, 2), (0, 3, 4, 2, 1), (0, 4, 1, 2, 3), (0, 4, 1, 3, 2), (0, 4, 2, 1, 3), (0, 4, 2, 3, 1), (0, 4, 3, 1, 2), (0, 4, 3, 2, 1), (1, 0, 2, 3, 4), (1, 0, 2, 4, 3), (1, 0, 3, 2, 4), (1, 0, 3, 4, 2), (1, 0, 4, 2, 3), (1, 0, 4, 3, 2), (1, 2, 0, 3, 4), (1, 2, 0, 4, 3), (1, 2, 3, 0, 4), (1, 2, 3, 4, 0), (1, 2, 4, 0, 3), (1, 2, 4, 3, 0), (1, 3, 0, 2, 4), (1, 3, 0, 4, 2), (1, 3, 2, 0, 4), (1, 3, 2, 4, 0), (1, 3, 4, 0, 2), (1, 3, 4, 2, 0), (1, 4, 0, 2, 3), (1, 4, 0, 3, 2), (1, 4, 2, 0, 3), (1, 4, 2, 3, 0), (1, 4, 3, 0, 2), (1, 4, 3, 2, 0), (2, 0, 1, 3, 4), (2, 0, 1, 4, 3), (2, 0, 3, 1, 4), (2, 0, 3, 4, 1), (2, 0, 4, 1, 3), (2, 0, 4, 3, 1), (2, 1, 0, 3, 4), (2, 1, 0, 4, 3), (2, 1, 3, 0, 4), (2, 1, 3, 4, 0), (2, 1, 4, 0, 3), (2, 1, 4, 3, 0), (2, 3, 0, 1, 4), (2, 3, 0, 4, 1), (2, 3, 1, 0, 4), (2, 3, 1, 4, 0), (2, 3, 4, 0, 1), (2, 3, 4, 1, 0), (2, 4, 0, 1, 3), (2, 4, 0, 3, 1), (2, 4, 1, 0, 3), (2, 4, 1, 3, 0), (2, 4, 3, 0, 1), (2, 4, 3, 1, 0), (3, 0, 1, 2, 4), (3, 0, 1, 4, 2), (3, 0, 2, 1, 4), (3, 0, 2, 4, 1), (3, 0, 4, 1, 2), (3, 0, 4, 2, 1), (3, 1, 0, 2, 4), (3, 1, 0, 4, 2), (3, 1, 2, 0, 4), (3, 1, 2, 4, 0), (3, 1, 4, 0, 2), (3, 1, 4, 2, 0), (3, 2, 0, 1, 4), (3, 2, 0, 4, 1), (3, 2, 1, 0, 4), (3, 2, 1, 4, 0), (3, 2, 4, 0, 1), (3, 2, 4, 1, 0), (3, 4, 0, 1, 2), (3, 4, 0, 2, 1), (3, 4, 1, 0, 2), (3, 4, 1, 2, 0), (3, 4, 2, 0, 1), (3, 4, 2, 1, 0), (4, 0, 1, 2, 3), (4, 0, 1, 3, 2), (4, 0, 2, 1, 3), (4, 0, 2, 3, 1), (4, 0, 3, 1, 2), (4, 0, 3, 2, 1), (4, 1, 0, 2, 3), (4, 1, 0, 3, 2), (4, 1, 2, 0, 3), (4, 1, 2, 3, 0), (4, 1, 3, 0, 2), (4, 1, 3, 2, 0), (4, 2, 0, 1, 3), (4, 2, 0, 3, 1), (4, 2, 1, 0, 3), (4, 2, 1, 3, 0), (4, 2, 3, 0, 1), (4, 2, 3, 1, 0), (4, 3, 0, 1, 2), (4, 3, 0, 2, 1), (4, 3, 1, 0, 2), (4, 3, 1, 2, 0), (4, 3, 2, 0, 1), (4, 3, 2, 1, 0)]
# >>> list(range(5))
# [0, 1, 2, 3, 4]
# >>> list(P(range(5)))
# [(0, 1, 2, 3, 4), (0, 1, 2, 4, 3), (0, 1, 3, 2, 4), (0, 1, 3, 4, 2), (0, 1, 4, 2, 3), (0, 1, 4, 3, 2), (0, 2, 1, 3, 4), (0, 2, 1, 4, 3), (0, 2, 3, 1, 4), (0, 2, 3, 4, 1), (0, 2, 4, 1, 3), (0, 2, 4, 3, 1), (0, 3, 1, 2, 4), (0, 3, 1, 4, 2), (0, 3, 2, 1, 4), (0, 3, 2, 4, 1), (0, 3, 4, 1, 2), (0, 3, 4, 2, 1), (0, 4, 1, 2, 3), (0, 4, 1, 3, 2), (0, 4, 2, 1, 3), (0, 4, 2, 3, 1), (0, 4, 3, 1, 2), (0, 4, 3, 2, 1), (1, 0, 2, 3, 4), (1, 0, 2, 4, 3), (1, 0, 3, 2, 4), (1, 0, 3, 4, 2), (1, 0, 4, 2, 3), (1, 0, 4, 3, 2), (1, 2, 0, 3, 4), (1, 2, 0, 4, 3), (1, 2, 3, 0, 4), (1, 2, 3, 4, 0), (1, 2, 4, 0, 3), (1, 2, 4, 3, 0), (1, 3, 0, 2, 4), (1, 3, 0, 4, 2), (1, 3, 2, 0, 4), (1, 3, 2, 4, 0), (1, 3, 4, 0, 2), (1, 3, 4, 2, 0), (1, 4, 0, 2, 3), (1, 4, 0, 3, 2), (1, 4, 2, 0, 3), (1, 4, 2, 3, 0), (1, 4, 3, 0, 2), (1, 4, 3, 2, 0), (2, 0, 1, 3, 4), (2, 0, 1, 4, 3), (2, 0, 3, 1, 4), (2, 0, 3, 4, 1), (2, 0, 4, 1, 3), (2, 0, 4, 3, 1), (2, 1, 0, 3, 4), (2, 1, 0, 4, 3), (2, 1, 3, 0, 4), (2, 1, 3, 4, 0), (2, 1, 4, 0, 3), (2, 1, 4, 3, 0), (2, 3, 0, 1, 4), (2, 3, 0, 4, 1), (2, 3, 1, 0, 4), (2, 3, 1, 4, 0), (2, 3, 4, 0, 1), (2, 3, 4, 1, 0), (2, 4, 0, 1, 3), (2, 4, 0, 3, 1), (2, 4, 1, 0, 3), (2, 4, 1, 3, 0), (2, 4, 3, 0, 1), (2, 4, 3, 1, 0), (3, 0, 1, 2, 4), (3, 0, 1, 4, 2), (3, 0, 2, 1, 4), (3, 0, 2, 4, 1), (3, 0, 4, 1, 2), (3, 0, 4, 2, 1), (3, 1, 0, 2, 4), (3, 1, 0, 4, 2), (3, 1, 2, 0, 4), (3, 1, 2, 4, 0), (3, 1, 4, 0, 2), (3, 1, 4, 2, 0), (3, 2, 0, 1, 4), (3, 2, 0, 4, 1), (3, 2, 1, 0, 4), (3, 2, 1, 4, 0), (3, 2, 4, 0, 1), (3, 2, 4, 1, 0), (3, 4, 0, 1, 2), (3, 4, 0, 2, 1), (3, 4, 1, 0, 2), (3, 4, 1, 2, 0), (3, 4, 2, 0, 1), (3, 4, 2, 1, 0), (4, 0, 1, 2, 3), (4, 0, 1, 3, 2), (4, 0, 2, 1, 3), (4, 0, 2, 3, 1), (4, 0, 3, 1, 2), (4, 0, 3, 2, 1), (4, 1, 0, 2, 3), (4, 1, 0, 3, 2), (4, 1, 2, 0, 3), (4, 1, 2, 3, 0), (4, 1, 3, 0, 2), (4, 1, 3, 2, 0), (4, 2, 0, 1, 3), (4, 2, 0, 3, 1), (4, 2, 1, 0, 3), (4, 2, 1, 3, 0), (4, 2, 3, 0, 1), (4, 2, 3, 1, 0), (4, 3, 0, 1, 2), (4, 3, 0, 2, 1), (4, 3, 1, 0, 2), (4, 3, 1, 2, 0), (4, 3, 2, 0, 1), (4, 3, 2, 1, 0)]
# >>> set.intersection({1,2,3},{3,4,5,1})
# {1, 3}
# >>> 
# >>> 
# >>> words=set([w.lower() for w in bible.words()])
# >>> list(P('HTsOg'))
# [('H', 'T', 's', 'O', 'g'), ('H', 'T', 's', 'g', 'O'), ('H', 'T', 'O', 's', 'g'), ('H', 'T', 'O', 'g', 's'), ('H', 'T', 'g', 's', 'O'), ('H', 'T', 'g', 'O', 's'), ('H', 's', 'T', 'O', 'g'), ('H', 's', 'T', 'g', 'O'), ('H', 's', 'O', 'T', 'g'), ('H', 's', 'O', 'g', 'T'), ('H', 's', 'g', 'T', 'O'), ('H', 's', 'g', 'O', 'T'), ('H', 'O', 'T', 's', 'g'), ('H', 'O', 'T', 'g', 's'), ('H', 'O', 's', 'T', 'g'), ('H', 'O', 's', 'g', 'T'), ('H', 'O', 'g', 'T', 's'), ('H', 'O', 'g', 's', 'T'), ('H', 'g', 'T', 's', 'O'), ('H', 'g', 'T', 'O', 's'), ('H', 'g', 's', 'T', 'O'), ('H', 'g', 's', 'O', 'T'), ('H', 'g', 'O', 'T', 's'), ('H', 'g', 'O', 's', 'T'), ('T', 'H', 's', 'O', 'g'), ('T', 'H', 's', 'g', 'O'), ('T', 'H', 'O', 's', 'g'), ('T', 'H', 'O', 'g', 's'), ('T', 'H', 'g', 's', 'O'), ('T', 'H', 'g', 'O', 's'), ('T', 's', 'H', 'O', 'g'), ('T', 's', 'H', 'g', 'O'), ('T', 's', 'O', 'H', 'g'), ('T', 's', 'O', 'g', 'H'), ('T', 's', 'g', 'H', 'O'), ('T', 's', 'g', 'O', 'H'), ('T', 'O', 'H', 's', 'g'), ('T', 'O', 'H', 'g', 's'), ('T', 'O', 's', 'H', 'g'), ('T', 'O', 's', 'g', 'H'), ('T', 'O', 'g', 'H', 's'), ('T', 'O', 'g', 's', 'H'), ('T', 'g', 'H', 's', 'O'), ('T', 'g', 'H', 'O', 's'), ('T', 'g', 's', 'H', 'O'), ('T', 'g', 's', 'O', 'H'), ('T', 'g', 'O', 'H', 's'), ('T', 'g', 'O', 's', 'H'), ('s', 'H', 'T', 'O', 'g'), ('s', 'H', 'T', 'g', 'O'), ('s', 'H', 'O', 'T', 'g'), ('s', 'H', 'O', 'g', 'T'), ('s', 'H', 'g', 'T', 'O'), ('s', 'H', 'g', 'O', 'T'), ('s', 'T', 'H', 'O', 'g'), ('s', 'T', 'H', 'g', 'O'), ('s', 'T', 'O', 'H', 'g'), ('s', 'T', 'O', 'g', 'H'), ('s', 'T', 'g', 'H', 'O'), ('s', 'T', 'g', 'O', 'H'), ('s', 'O', 'H', 'T', 'g'), ('s', 'O', 'H', 'g', 'T'), ('s', 'O', 'T', 'H', 'g'), ('s', 'O', 'T', 'g', 'H'), ('s', 'O', 'g', 'H', 'T'), ('s', 'O', 'g', 'T', 'H'), ('s', 'g', 'H', 'T', 'O'), ('s', 'g', 'H', 'O', 'T'), ('s', 'g', 'T', 'H', 'O'), ('s', 'g', 'T', 'O', 'H'), ('s', 'g', 'O', 'H', 'T'), ('s', 'g', 'O', 'T', 'H'), ('O', 'H', 'T', 's', 'g'), ('O', 'H', 'T', 'g', 's'), ('O', 'H', 's', 'T', 'g'), ('O', 'H', 's', 'g', 'T'), ('O', 'H', 'g', 'T', 's'), ('O', 'H', 'g', 's', 'T'), ('O', 'T', 'H', 's', 'g'), ('O', 'T', 'H', 'g', 's'), ('O', 'T', 's', 'H', 'g'), ('O', 'T', 's', 'g', 'H'), ('O', 'T', 'g', 'H', 's'), ('O', 'T', 'g', 's', 'H'), ('O', 's', 'H', 'T', 'g'), ('O', 's', 'H', 'g', 'T'), ('O', 's', 'T', 'H', 'g'), ('O', 's', 'T', 'g', 'H'), ('O', 's', 'g', 'H', 'T'), ('O', 's', 'g', 'T', 'H'), ('O', 'g', 'H', 'T', 's'), ('O', 'g', 'H', 's', 'T'), ('O', 'g', 'T', 'H', 's'), ('O', 'g', 'T', 's', 'H'), ('O', 'g', 's', 'H', 'T'), ('O', 'g', 's', 'T', 'H'), ('g', 'H', 'T', 's', 'O'), ('g', 'H', 'T', 'O', 's'), ('g', 'H', 's', 'T', 'O'), ('g', 'H', 's', 'O', 'T'), ('g', 'H', 'O', 'T', 's'), ('g', 'H', 'O', 's', 'T'), ('g', 'T', 'H', 's', 'O'), ('g', 'T', 'H', 'O', 's'), ('g', 'T', 's', 'H', 'O'), ('g', 'T', 's', 'O', 'H'), ('g', 'T', 'O', 'H', 's'), ('g', 'T', 'O', 's', 'H'), ('g', 's', 'H', 'T', 'O'), ('g', 's', 'H', 'O', 'T'), ('g', 's', 'T', 'H', 'O'), ('g', 's', 'T', 'O', 'H'), ('g', 's', 'O', 'H', 'T'), ('g', 's', 'O', 'T', 'H'), ('g', 'O', 'H', 'T', 's'), ('g', 'O', 'H', 's', 'T'), ('g', 'O', 'T', 'H', 's'), ('g', 'O', 'T', 's', 'H'), ('g', 'O', 's', 'H', 'T'), ('g', 'O', 's', 'T', 'H')]
# >>> [''.join(x) for x in _]
# ['HTsOg', 'HTsgO', 'HTOsg', 'HTOgs', 'HTgsO', 'HTgOs', 'HsTOg', 'HsTgO', 'HsOTg', 'HsOgT', 'HsgTO', 'HsgOT', 'HOTsg', 'HOTgs', 'HOsTg', 'HOsgT', 'HOgTs', 'HOgsT', 'HgTsO', 'HgTOs', 'HgsTO', 'HgsOT', 'HgOTs', 'HgOsT', 'THsOg', 'THsgO', 'THOsg', 'THOgs', 'THgsO', 'THgOs', 'TsHOg', 'TsHgO', 'TsOHg', 'TsOgH', 'TsgHO', 'TsgOH', 'TOHsg', 'TOHgs', 'TOsHg', 'TOsgH', 'TOgHs', 'TOgsH', 'TgHsO', 'TgHOs', 'TgsHO', 'TgsOH', 'TgOHs', 'TgOsH', 'sHTOg', 'sHTgO', 'sHOTg', 'sHOgT', 'sHgTO', 'sHgOT', 'sTHOg', 'sTHgO', 'sTOHg', 'sTOgH', 'sTgHO', 'sTgOH', 'sOHTg', 'sOHgT', 'sOTHg', 'sOTgH', 'sOgHT', 'sOgTH', 'sgHTO', 'sgHOT', 'sgTHO', 'sgTOH', 'sgOHT', 'sgOTH', 'OHTsg', 'OHTgs', 'OHsTg', 'OHsgT', 'OHgTs', 'OHgsT', 'OTHsg', 'OTHgs', 'OTsHg', 'OTsgH', 'OTgHs', 'OTgsH', 'OsHTg', 'OsHgT', 'OsTHg', 'OsTgH', 'OsgHT', 'OsgTH', 'OgHTs', 'OgHsT', 'OgTHs', 'OgTsH', 'OgsHT', 'OgsTH', 'gHTsO', 'gHTOs', 'gHsTO', 'gHsOT', 'gHOTs', 'gHOsT', 'gTHsO', 'gTHOs', 'gTsHO', 'gTsOH', 'gTOHs', 'gTOsH', 'gsHTO', 'gsHOT', 'gsTHO', 'gsTOH', 'gsOHT', 'gsOTH', 'gOHTs', 'gOHsT', 'gOTHs', 'gOTsH', 'gOsHT', 'gOsTH']
# >>> [''.join(x).lower() for x in _]
# ['htsog', 'htsgo', 'htosg', 'htogs', 'htgso', 'htgos', 'hstog', 'hstgo', 'hsotg', 'hsogt', 'hsgto', 'hsgot', 'hotsg', 'hotgs', 'hostg', 'hosgt', 'hogts', 'hogst', 'hgtso', 'hgtos', 'hgsto', 'hgsot', 'hgots', 'hgost', 'thsog', 'thsgo', 'thosg', 'thogs', 'thgso', 'thgos', 'tshog', 'tshgo', 'tsohg', 'tsogh', 'tsgho', 'tsgoh', 'tohsg', 'tohgs', 'toshg', 'tosgh', 'toghs', 'togsh', 'tghso', 'tghos', 'tgsho', 'tgsoh', 'tgohs', 'tgosh', 'shtog', 'shtgo', 'shotg', 'shogt', 'shgto', 'shgot', 'sthog', 'sthgo', 'stohg', 'stogh', 'stgho', 'stgoh', 'sohtg', 'sohgt', 'sothg', 'sotgh', 'soght', 'sogth', 'sghto', 'sghot', 'sgtho', 'sgtoh', 'sgoht', 'sgoth', 'ohtsg', 'ohtgs', 'ohstg', 'ohsgt', 'ohgts', 'ohgst', 'othsg', 'othgs', 'otshg', 'otsgh', 'otghs', 'otgsh', 'oshtg', 'oshgt', 'osthg', 'ostgh', 'osght', 'osgth', 'oghts', 'oghst', 'ogths', 'ogtsh', 'ogsht', 'ogsth', 'ghtso', 'ghtos', 'ghsto', 'ghsot', 'ghots', 'ghost', 'gthso', 'gthos', 'gtsho', 'gtsoh', 'gtohs', 'gtosh', 'gshto', 'gshot', 'gstho', 'gstoh', 'gsoht', 'gsoth', 'gohts', 'gohst', 'goths', 'gotsh', 'gosht', 'gosth']
# >>> set.intersection(words,_)
# {'ghost'}
# >>> 
# >>> 
# >>> 
