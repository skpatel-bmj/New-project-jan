import os


def test():
    os.system('clear')
    print()
    print('\033[95m' + "*"*124 + '\033[0m')
    print()
    print('       function start......!!')
    print('       function End......!!')
    print('       thank you for using this program......!!')
    print()
    print('\033[95m' + "*"*124 + '\033[0m')

test()

def feedback_fun():
    print()
    print('\033[95m' + "*"*124 + '\033[0m')
    feedback = input("Plz Enter you feed back :- ")
    print('\033[95m' + "*"*124 + '\033[0m')
    print('your feedback display : - ',feedback)
    

feedback_fun()