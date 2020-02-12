def mdtable(t):
    r0=t[0]
    l=max(len(x) for x in t)
    if l=0: return ''
    t=[[r+[]*l][:l] for r in t]
    rr=[':-:']*l
    t=[t[0],[':-:']*l]+t[1:]
    t=['|'.join(r) for r in t]
    return '\n'.join(t)
