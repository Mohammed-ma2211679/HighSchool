try:

    print('Enter 1 for turn text to caesar cipher')
    print('Enter 2 for turn caesar cipher to text')
    print('---------------------------------------')
    choice = int(input('Please enter 1 or 2: '))
    # the code that turn text to caesar cipher
    if choice == 1:
        key = int(input('Enter the key of Cipher: '))
        D_C2 = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }
        D_C_R = {value: key for (key, value) in D_C2.items()}
        text_E = input('Please enter the text here: ')
        text_u = str.upper(text_E)
        print('The Cipher is:', end=' ')
        for i in range(1):
            for j in text_u:
                if j == ' ':
                    print(' ', end='')
                else:
                    k = (D_C2.get(j) + key) % 26
                    if k == 0:
                        print('Z', end='')
                    else:
                        k_p = D_C_R.get(k)
                        print(k_p, end='')

    # the code that turn caesar cipher to text is in caesar_C_R
    elif choice == 2:
        import caesar_C_R

    else:
        print('Do not enter an another number')

except Exception as e:
    print('Error:', e)

finally:
    print('')
    print('Thank you for using my program <3')
    input('Press Enter to end...')
# End of the Program
