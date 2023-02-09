a = input()
happy = a.count(':-)')
sad = a.count(':-(')

if happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
elif happy !=0 and sad !=0 and happy == sad:
    print('unsure')
else:
    print('none')
