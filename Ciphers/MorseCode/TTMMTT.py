print('Instructions: ')
print('This Program for turn Text into Morse code or from Morce code to Text ')
print('Enter 1 for turn Text to Morce code ')
print('Enter 2 for turn Morce code to Text ')
print('----------------------------------------------------------------------')
while True:
    try:
        s = int(input('Please enter 1 or 2: '))
        if s == 1:
            import TTM
            ttm = TTM
            break
        elif s == 2:
            import MTT
            mmt = MTT
            break
        else:
            print('Wrong number!, Try again')
    except ValueError:
        print('Do not enter a letters!, Try again')
