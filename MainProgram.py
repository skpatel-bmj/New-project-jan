# This is the main Python file.
# This Project develop by Sandeep Kumar Patel for Testing.

''' 
This python file are contains all the env and integration of all functional program files.
This Project are using .

'''

# Import all required library in python
import os
from time import sleep


# Import other file



def option1():
    print('\033[95m' + "*"*80 + '\033[0m')
    print("You selected Option B.")
    print('\033[95m' + "*"*80 + '\033[0m')
    go.GitOps_Main()

def option2():
    print('\033[95m' + "*"*80 + '\033[0m')
    print("You selected Option C.")
    print('\033[95m' + "*"*80 + '\033[0m')
    do.Docker_Main()
    
def option3():
    print('\033[95m' + "*"*80 + '\033[0m')
    print("You selected Option D.")
    print('\033[95m' + "*"*80 + '\033[0m')
    mo.Monitoring_Ops_Main()
    
# Main menu loop
while True:
    AMD.Top_Manu_Display()
    if lo.login():
        AMD.Top_Manu_Display()
        AMD.Main_file_Manu_Display()
        choice = input('\033[96m' + "Enter your choice: " + '\033[0m')

        if choice == 'A' or choice == 'a':
            # Clear screen
            os.system('py mange_user.py')
        
        elif choice == 'B' or choice == 'b':
            # Clear screen
            os.system('clear')
            option1()

        elif choice == 'C' or choice == 'c':
            # Clear screen
            os.system('clear')
            option2()    
        
        elif choice == 'D' or choice == 'd':
            # Clear screen
            os.system('clear')
            option3()
        
        # Quit Option
        elif choice == 'Q' or choice == 'q':
            print()
            print('\033[95m' + "*"*124 + '\033[0m')
            print('\033[92m' + "                     Thank You For Using this AI-Pro-DevOps Application" + '\033[0m')
            print('\033[96m' + "                     Goodbye !  " +  '\033[0m')
            print('\033[95m' + "*"*124 + '\033[0m')
            os.system('clear')
            exit()

        else:
            print("Invalid choice. Please try again.")  
