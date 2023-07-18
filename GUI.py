#GUI

import SNClasses as snc
from SNClasses import profile as pf

users = {
    "user": ("pw","bio")
}
friends = {
    "user": ("list friends")
}
messages = {
    "user": ("all messages")
}
blocks = {
    "user": ("blocked users")
}
snc.cls()
title = "Welcome to Ianstagram!"
print("*"*len(title)+'\n'+title+'\n'+"*"*len(title))
mod = 0
while True:
    mod+=1
    if mod != 1:
        snc.cls()
    choice = input(f'1. New User\n2. Press any key to continue if you already have an account\n(1/2): ')
    if choice in ('1',1):
        ut,p1,b1 = snc.CreateProfile()
        users[ut] = (p1,b1)
        friends[ut] = ()
        messages[ut] = ()
        blocks[ut] = ()
        #break
    elif choice in ('2',2):
        print()
        #break

    while True:
        snc.cls()
        title = "Welcome to Ianstagram!"
        print("*"*len(title)+'\n'+title+'\n'+"*"*len(title))

        choicemain = input(f'1. View/Edit Profile\n2. Add/Remove Friends\n3. View Friends\n4. Send/Check Messages\n5. Back to Sign Up Page\n(1,2): ')

        if choicemain in ('1',1):

            snc.cls()
            while True:
                un = str(input("Enter User: "))
                if un in users.keys():
                    break
                else:
                    continue
            while True:
                up = str(input("Enter Password: "))

                newstr = users.keys()
                #print(newstr)
                if un in str(newstr):
                    temp = users[un]
                    temp1 = temp[0]
                    if up == temp1:
                        print(un)
                        print(f'Bio: {temp[1]}')
                        break
                    else: 
                        continue
            
            while True:
                edit_ch = input("Would you like to edit your profile? (y/n): ")
            
                if edit_ch in ('Y','y'):
                    print(f'What would you like to edit?\n1. Username\n2. Password\n3. Bio')
                    edit_ch2 = input('(1/2/3): ')
                    if edit_ch2 in ('1',1):
                        mod = 0
                        while mod == 0:
                            tempcurrent = input('Enter current username: ')
                            if tempcurrent in users.keys():
                                mod +=1
                            else:
                                mod = 0
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
                            #print(users[tempnew])
                            #print(users.keys())
                            input("Enter any key to continue: ")
                            snc.cls()
                            continue
                    if edit_ch2 in ('2',2):
                        mod = 0
                        while mod == 0:
                            tempcurrent = input('Enter current username: ')
                            if tempcurrent in users.keys():
                                mod +=1
                            else:
                                mod = 0
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
                            tempnew = input("Enter new passsword: ")
                            k = list(tempuser)
                            k[0] = tempnew
                            users[tempcurrent] = k
                            #del users[tempcurrent]
                            #print(users[tempnew])
                            print(users)
                            input("Enter any key to continue: ")
                            snc.cls()
                            continue
                    if edit_ch2 in ('3',3):
                        mod = 0
                        while mod == 0:
                            tempcurrent = input('Enter current username: ')
                            if tempcurrent in users.keys():
                                mod +=1
                            else:
                                mod = 0
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
                            tempnew = input("Enter new bio: ")
                            k = list(tempuser)
                            k[1] = tempnew
                            users[tempcurrent] = k
                            #del users[tempcurrent]
                            #print(users[tempnew])
                            print(users)
                            input("Enter any key to continue: ")
                            snc.cls()
                            continue
                    
                    break
                elif edit_ch in ('N','n'):
                    break
        elif choicemain in ('2',2):
            snc.cls()
            print("Would you like to add or remove friends?\n1. Add\n2. Remove")
            while True:
                a_r = input("(1/2): ")
                if a_r in ('1',1,'2',2):
                    break
                else:
                    continue
            if a_r in ('1',1):
                while True:
                    tempuser = input("Enter current username: ")
                    if tempuser in users.keys():
                        break
                    else: 
                        continue
                while True:
                    temppass = input("Enter password: ")
                    k = users[tempuser]
                    if k[0] == temppass:
                        break
                    else:
                        continue
            # print(friends[tempuser])
                if friends[tempuser] == ():
                    print("You have no friends")
                else:
                    print(f'Friends = {friends[tempuser]}')
                newfriend = input("Enter the username of the user you would like to add: ")
                if newfriend in users.keys() and newfriend not in friends[tempuser]:
                    k = list(friends[tempuser])
                    k.append(newfriend)
                    friends[tempuser] = k
                    print(f'Friends = {friends[tempuser]}')
                    input("Enter any key to continue ")
                else:
                    print("User does not exist or is already your friend")
                    input("Enter any key to continue ")
            elif a_r in ('2',2):
                while True:
                    tempuser = input("Enter current username: ")
                    if tempuser in users.keys():
                        break
                    else: 
                        continue
                while True:
                    temppass = input("Enter password: ")
                    k = users[tempuser]
                    if k[0] == temppass:
                        break
                    else:
                        continue
                if friends[tempuser] == ():
                    print("You have no friends, so you cannot remove any friends")
                else:
                    print(f'Friends = {friends[tempuser]}')
                    while True:
                        remfriend = input("Enter the username of the user you would like to remove as a friend: ")
                        if remfriend in friends[tempuser]:
                            break
                        else:
                            continue
                    k = list(friends[tempuser])
                    k.remove(remfriend)
                    friends[tempuser] = k
                    print(f'Friends = {friends[tempuser]}')
                    input("Enter any key to continue ")
        elif choicemain in ('3',3):
            snc.cls()
            while True:
                tempuser = input("Enter current username: ")
                if tempuser in users.keys():
                    break
                else:
                    continue
            print(f'Friends = {friends[tempuser]}')
            input("Enter any key to continue ")
        elif choicemain in ('4',4):
            snc.cls()
            while True:
                tempuser = input("Enter current username: ")
                if tempuser in users.keys():
                    break
                else:
                    continue
            while True:
                temppass = input("Enter current password: ")
                k = users[tempuser]
                if k[0] == temppass:
                    break
                else:
                    continue
            if friends[tempuser] == ():
                print("You have no friends to message")
                input("Enter any key to continue")
            else:
                print(f'Friends: {friends[tempuser]}')
                mess_ch = input("1. Send Messages\n2. Check Messages\n3. Block users\n(1/2/3): ")
                if mess_ch in ('1',1):
                    while True:
                        recipient = input("Enter the username of the user you would like to message: ")
                        if tempuser in blocks[recipient]:
                            print("This user has blocked you, thus disallowing you from messaging them")
                            input("Enter any key to continue ")
                            break
                        if recipient in friends[tempuser]:
                            message = input("Write message here: ")
                            k = list(messages[recipient])
                            k.append(message)
                            messages[recipient] = k
                            break
                        else:
                            
                            input("Enter any key to continue")
                            continue
                elif mess_ch in ('2',2):
                    while True:
                        tempuser = input("Enter current username: ")
                        if tempuser in users.keys():
                            break
                        else:
                            continue
                    while True:
                        temppass = input("Enter password: ")
                        k = users[tempuser]
                        if temppass == k[0]:
                            break
                        else:
                            continue
                    print(f'All messages: {messages[tempuser]}')
                    input("Enter any key to continue: ")
                elif mess_ch in ('3',3):
                    while True:
                        b_user = input("Enter the username of the user you would like to block: ")
                        if b_user in friends[tempuser] and b_user not in blocks[tempuser]:
                            k = list(blocks[tempuser])
                            k.append(b_user)
                            blocks[tempuser] = k
                            input("Enter any key to continue ")
                            break

        elif choicemain in ('5',5):
            break