class password:
    passwd="myclass"
    def login(self):

        p=input("Enter the password")
        if self.passwd==p:
            print("login successful")
        else:
            print("Invalid Password")

    def reset(self):
        r_p=input

