import numpy as np

mr = {format(i, '04b'): chr(ord('f') + i) for i in range(16)}

with open('inputs.txt', 'w+') as f:
    for i in range(8):
        for j in range(128):
            pr = np.binary_repr(j, width=8)
            es = 'ff' * i + mr[pr[:4]] + mr[pr[4:]] + 'ff' * (8 - i - 1)
            f.write(f'{es} ')
        f.write('\n')