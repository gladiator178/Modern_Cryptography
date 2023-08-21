from pyfinite import ffield

expon= [[-1]*128 for i in range(128)]
fi = ffield.FField(7)

def blockbyte(c):
    return "".join([chr(16*(ord(c[i]) - ord('f')) + ord(c[i+1]) - ord('f')) for i in range(0, len(c), 2)])

def exp(num, ex):
    if expon[num][ex] != -1:
        return expon[num][ex]
    if ex == 0:
        return 1
    elif ex == 1:
        return num
    inb = exp(num, ex >> 1)
    sq = fi.Multiply(inb, inb)
    out = sq if ex % 2 == 0 else fi.Multiply(num, sq)
    expon[num][ex] = out
    return out

def addVectors(p, q):
    return [int(a) ^ int(b) for a, b in zip(p, q)]

def scalarMultiplication (p, q):
    out = [0]*8
    for i, a in enumerate(p):
        out[i] = fi.Multiply(a, q)
    return out

def lineartrans (mt, li):
    out = [0]*8
    for row, elem in zip(mt, li):
        out = addVectors(scalarMultiplication(row, elem), out)
    return out

def convfunc (txt, mat, expm):
    txt = [ord(c) for c in txt]
    cip = [[0 for j in range (8)] for i in range(8)]
    for i, elem in enumerate(txt):
        cip[0][i] = exp(elem, expm[i])

    cip[1] = lineartrans(mat, cip[0])

    for i, elem in enumerate(cip[1]):
        cip[2][i] = exp(elem, expm[i])

    cip[3] = lineartrans(mat, cip[2])

    for i, elem in enumerate(cip[3]):
        cip[4][i] = exp(elem, expm[i])
    return cip[4]
