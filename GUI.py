#GUI

import SNClasses as snc
from SNClasses import profile as pf

users = {
    "user": ("pw","bio")
}
snc.cls()
title = "Welcome to Ianstagram!"
print("*"*len(title)+'\n'+title+'\n'+"*"*len(title))
mod = 0
while True:
    mod+=1
    if mod != 1:
        snc.cls()
    choice = input(f'1. New User\n2. Sign in\n(1/2): ')
    if choice in ('1',1):
        ut,p1,b1 = snc.CreateProfile()
        users[ut] = (p1,b1)
        break
    elif choice in ('2',2):
        print()
        break

while True:
    snc.cls()
    title = "Welcome to Ianstagram!"
    print("*"*len(title)+'\n'+title+'\n'+"*"*len(title))

    choicemain = input(f'1. View/Edit Profile\n(1,2): ')

    if choicemain in ('1',1):

        snc.cls()

        un = str(input("Enter User: "))
        up = str(input("Enter Password: "))

        newstr = users.keys()
        #print(newstr)
        if un in str(newstr):
            temp = users[un]
            temp1 = temp[0]
            if up == temp1:
                print(un)
                print(f'Bio: {temp[1]}')
        
        while True:
            edit_ch = input("Would you like to edit your profile? (y/n): ")
            if edit_ch in ('Y','y'):
                break
            elif edit_ch in ('N','n'):
                break
        
        if edit_ch in ('Y','y'):
            print(f'What would you like to edit?\n1. Username\n2. Password\n3. Bio')
            edit_ch2 = input('(1/2/3): ')
            if edit_ch2 in ('1',1):
                tempcurrent = input('Enter current username: ')
                tempuser = users[tempcurrent]
                mod = 0
                while mod == 0:
                    temppass = input('Enter current password: ')
                    if temppass == tempuser[0]:
                        mod += 1
                    else:
                        print("Incorrect password")
                        mod = 0
                print(tempuser)
                if temppass == tempuser[0]:
                    tempnew = input("Enter new username: ")
                    users[tempnew] = users[tempcurrent]
                    del users[tempcurrent]
                    print(users[tempnew])
                    print(users.keys())
                    input()