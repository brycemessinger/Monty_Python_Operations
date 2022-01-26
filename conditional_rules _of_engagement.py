num_knights = int(input('How many knights?'))
day = input('Enter the day of the week')
print('You sent',num_knights, "knights on a ", day)
print('Course of action:')

if num_knights < 3 or day == 'Monday':
    print('Retreat!')
    # print('Raise the white flag!')
elif num_knights >= 10 and day == "Wednesday":
    print('Trojan Rabbit')
elif day == 'Tuesday':
    print('Taco Night')
else: print('Truce?')