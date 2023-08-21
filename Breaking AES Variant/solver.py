from funcc import blockbyte, exp, convfunc
from pyfinite import ffield

psw = "msgjhgksjhilhofqjsjhikijmofkkrlh"

mr = {}
for i in range(16):
    j = format(i, '04b')
    mr[j] = chr(ord('f')+i)

m={}
for i in mr:
    j=mr[i]
    m[j]=list(i)

inputfile="inputs.txt"
outputfile="outputs.txt"


input = open(inputfile, 'r')
output = open(outputfile, 'r')
pex= [[] for i in range(8)]
pai=[[[] for i in range(8)] for j in range(8)]

fi = ffield.FField(7)
# Loop through the lines in the input and output files
for k, (iline, oline) in enumerate(zip(input.readlines(), output.readlines())):
    
    # Create empty lists for the input and output strings
    instr = []
    outstr = []
    
    # Loop through the words in the input line and append their block bytes to the instr list
    for inn in iline.strip().split(" "):
        instr.append(blockbyte(inn)[k])
    
    # Loop through the words in the output line and append their block bytes to the outstr list
    for outt in oline.strip().split(" "):
        outstr.append(blockbyte(outt)[k])
    
    # Loop through all possible values of i and j
    for i in range(1, 127):
        for j in range(1, 128):
            
            # Assume the result is correct until proven otherwise
            f = True
            
            # Loop through the input and output strings in parallel and check if the result is correct
            for iin, oout in zip(instr, outstr):
                if ord(oout) != exp(fi.Multiply(exp(fi.Multiply(exp(ord(iin), i), j), i), j), i):
                    f = False
                    break
            
            # If the result is correct, append the values of i and j to the corresponding lists in pex and pai
            if f:
                pex[k].append(i)
                pai[k][k].append(j)

input = open(inputfile, 'r')
output = open(outputfile, 'r')
for k, (iline, oline) in enumerate(zip(input.readlines(), output.readlines())):
    if k <= 6:
        instr = [blockbyte(inn)[k] for inn in iline.strip().split(" ")]
        outstr = [blockbyte(outt)[k+1] for outt in oline.strip().split(" ")]
        for i in range(1, 128):
            for a, b in zip(pex[k+1], pai[k+1][k+1]):
                for r, s in zip(pex[k], pai[k][k]):
                    is_valid = True
                    for iin, oout in zip(instr, outstr):
                        lhs = int(fi.Multiply(exp(fi.Multiply(exp(ord(iin), r), s), r), i))
                        rhs = int(fi.Multiply(exp(fi.Multiply(exp(ord(iin), r), i), a), b))
                        if ord(oout) != exp(lhs ^ rhs, a):
                            is_valid = False
                            break
                    if is_valid:
                        pex[k+1], pai[k+1][k+1] = [a], [b]
                        pex[k], pai[k][k], pai[k][k+1] = [r], [s], [i]

for numi in range(6):
    nuz = numi + 2
    
    expm = [e[0] for e in pex]
    linmat = [[pai[i][j][0] if pai[i][j] else 0 for j in range(8)] for i in range(8)]
    
    with open(inputfile, 'r') as input, open(outputfile, 'r') as output:
        for k, (iline, oline) in enumerate(zip(input.readlines(), output.readlines())):
            if k > (7 - nuz):
                continue
            instr = [blockbyte(i) for i in iline.strip().split(" ")]
            outstr = [blockbyte(i) for i in oline.strip().split(" ")]
            for i in range(1, 128):
                linmat[k][k + nuz] = i
                if all(convfunc(inps, linmat, expm)[k + nuz] == ord(outs[k + nuz]) for inps, outs in zip(instr, outstr)):
                    pai[k][k + nuz] = [i]


linmat = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        if(len(pai[i][j]) == 0):
             linmat[i][j] = 0
        else: linmat[i][j] = pai[i][j][0]

def passout(password):
    pw = blockbyte(password)
    out = ""
    for k in range(8):
        for ans in range(128):
            an = format(ans, '08b')
            cs = mr[an[:4]] + mr[an[4:]]
            inn = out + cs + (16 - len(out) - 2) * 'f'
            conv = convfunc(blockbyte(inn), linmat, expm)
            if ord(pw[k]) == conv[k]:
                out += cs
                break
    return out

print((blockbyte(passout(psw[:16]))+blockbyte(passout(psw[16:]))))
