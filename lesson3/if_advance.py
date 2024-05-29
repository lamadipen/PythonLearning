nepai=['momo', 'chowmen', 'dalbhat']
italian=['pizza', 'pasta']
chinese=['fried rice', 'egg roll']

dish=input('Enter a food name: ')

if dish in nepai:
    print('Nepali Food')
elif dish in italian:
    print('Italian Food')
elif dish in chinese:
    print('Chinese Food')
else:
    print('No such food avaialbe')