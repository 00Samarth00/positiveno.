#THIS PROGRAM FINDS THE POSITIVE NOS. FROM THE LIST OF 5 NUMBERS.

def pos_(n1):
    return n1 if n1>=0 else ''
    

l1=[]
while(True):
    for i in range(0,5):
        x=eval(input('ENTER VALUE {} IN LIST:'.format(i+1)))
        l1.append(x)
    print('GIVEN NUMBERS:-',l1)
    print('THE POSITIVE NUMBERS OUT OF THESE ARE:')
    for q in range(0,5):
        print(pos_(l1[q]))


    con_=input('DO YOU WANT TO USE ANOTHER LIST OF NUMBERS?(Y/N)').casefold()
    
    if(con_=='yes' or con_=='y'):
        continue
    elif(con_=='no' or con_=='n'):
        break




