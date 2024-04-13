

print('Tell me your name')
x = input()
print('Hello ' + x)
print()
print('How old are you?')
y = input()
print("Are you " + y + " years old? That's old!")
print()
print('What is your occupation?\n')
z = input()
print('Do you like your job?')
t = input()
for n in z:
    if t == 'yes':
        print('Ok, then you are one of the lucky ones!')
        break
else:
    print('Too bad!\n')
print()
    
    
try:
    a = (int(input('Now a new game!\nPick a number for A:')))
    print('Thanks for that!')
except ValueError: 
        print('Sorry, I need a real number. Try again:')
    
        a = (int(input('Now pick a number for A:')))
        print('Thanks for that!') 
print()

try:
    b = (int(input('Now pick a number for B:')))
    print()
    print('Oh, you are good at this!')
except ValueError:
    print('Sorry, I need a real number. Try again:')
    
    b = (int(input('Now pick a number for B:')))
    print('Good choice!  That is one of my favorite numbers!')  
print()
try:
    c = (int(input('Ok, now one more time, pick a number for C:')))
    print('Thanks! Your brain has worked hard!')
    print()
except ValueError:
    print('Sorry, I need a real number. \nTry again:')
    
    c = (int(input('Now pick a number for C:')))
    print('You go girrrl!')  
    print()
if b == a or c == b or a == c:
    print('Are you trying to trick me? \nYou picked the same numbers.\n\n\nBut I forgive you, goodbye.') 
    
elif b > a:
    print("Oh look! B is larger than A")
elif c > a:
    print('Oh cool! C is larger than A')
elif b > c:
    print('Wow! B is larger that C') 



