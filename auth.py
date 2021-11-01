#all in same class login 
    #create a read function {read heart file file} ---- returns users=[]
    #create a write function {}
    #login 
    #change password
    #check if user exist 
    #create new user
    
class Authentication:
    def __init__(self,Heart_file):
        self.Heart_file = Heart_file
        self.read_function()


    def read_function(self):
        #taking user details from heart file 
        Heart_file = open(self.Heart_file)

        self.user_detalis = Heart_file.read().split("__@__")

        return self.user_detalis

    def create_user(self,username_input,password_input):

        if username_input not in self.user_detalis and password_input not in self.user_detalis :
            self.user_detalis.append(username_input)
            self.user_detalis.append(password_input)
            print("User Profile Created")
            
            self.save_details()

            return True
        
        if username_input in self.user_detalis :
            print("This username is already in use ")
            return False

        
    
    def save_details(self):
        Heart_file = open(self.Heart_file,"w+")

        str = "__@__".join(self.user_detalis) 

        Heart_file.write(str)
        Heart_file.close()

    def login(self,username_input,password_input):
        #opening file from the system
        Heart_file = open(self.Heart_file,"r")
        
        #reading the opened file 
        data_ = Heart_file.read()

        #creating a list to hold all the data (user,password)
        listed_data = data_.split("__@__")

        #getting the position of the username in the list 
        user_pos = listed_data.index(username_input)
        #getting the position of the password in the list
        passw_pos = listed_data.index(password_input)
         
        #checking whether they are in a row or not 
        if user_pos == passw_pos - 1  and passw_pos % 2 == 0:
            print(f'WELCOME {username_input} TO ORGAN' )
            return True

        else:
            return False
        
        Heart_file.close()

    def change_password(self,username_input,oldpassword_input,newpassword_input):
        #opening file from the system
        Heart_file = open(self.Heart_file,"r")

        #now checking whether the user exist
        data_ = Heart_file.read()

        #getting all the index number for the username and the password
        listed_data = data_.split("__@__")

        #closing file 
        Heart_file.close()

        #taking index of all the arguments 
        old_password_index = listed_data.index(oldpassword_input)

        username_index = listed_data.index(username_input)

        if username_index == old_password_index - 1 and old_password_index % 2 == 0 :
        
            #taking the data in form of string
            old_data = listed_data[old_password_index]
            
            #replacing the data with another string 
            new_data = old_data.replace(old_data, newpassword_input)

            ##inserting the data in the place of privious data
            listed_data.insert(old_password_index, new_data)

            #again opening the file in write formate
            Heart_file = open(self.Heart_file,"w")

            #poping out the old data from the list[]
            listed_data.pop(old_password_index + 1)

            #pushing the data to the designated file 
            data_to_push = "__@__".join(listed_data)
            Heart_file.write(data_to_push)

            return True
            Heart_file.close()

        else:
            return False
        
            





        

        
    






