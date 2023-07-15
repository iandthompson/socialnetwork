#GUI

import SNClasses as snc
from SNClasses import profile as pf

u,p,b = snc.CreateProfile()

NewUser = pf(u,p,b)
print(NewUser.bio)