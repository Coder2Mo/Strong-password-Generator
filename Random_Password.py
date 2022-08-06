########################################################
''' Coded By : Coder2Mo
    Fb : https://facebook.com/mosh3eb
    Te : https://t.me/Mosh3_eb
    Wp : +201030191239 '''
########################################################

import string
import random

print(''' This program was Coded By : Coder2Mo
      
          Fb : https://facebook.com/mosh3eb
          Te : https://t.me/Mosh3_eb
          Wp : +201030191239 \n''')


if __name__ == "__main__":
    def R_gen():
        
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        ps_Len = int(input("\nEnter Password length :  "))

        s_List = []

        s_List.extend(list(s1))
        s_List.extend(list(s2))
        s_List.extend(list(s3))
        s_List.extend(list(s4))
        print("\nYour password : ", end = "")
        print("".join(random.sample(s_List, ps_Len)))
        while True:
            Restart = str(input("\nWould you like to Restart this program ? ( y / n ) : "))
            if 'y' in Restart:
                R_gen()
                break
            elif 'n' in Restart:
                print("\nProgram terminated , Goodbye")
                break
            else:
                print("\nInvalid input")
            
    R_gen()
    wait_less = input("\nEnter any key to Exit...")

        

