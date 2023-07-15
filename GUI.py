#GUI

import SNClasses as snc
from SNClasses import profile as pf

newuser = pf.snc.CreateProfile()

print(f'{pf.user}\nPW: {"*"*len(pf.pw)}')