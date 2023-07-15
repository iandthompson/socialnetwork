class profile:
    def __init__(self, username, password, bio):
        self.user = username
        self.pw = password
        self.bio = bio

def CreateProfile():
    user = input("Enter a username: ")
    pw = input("Enter a password | make it complex ;): ")
    bio = input("Write bio: ")

    
    return user,pw,bio

def showuser():
    u,p,b = CreateProfile()

    NewUser = profile(u,p,b)
    print(NewUser.bio)






