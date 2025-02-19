
import time
text_E = input('Please enter the caesar cipher here: ')
text_u = str.upper(text_E)
for ke in range(27):
    key = ke
    D_C3 = {
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
        'Z': 26,
    }
    D_C_R2 = {value: key for (key, value) in D_C3.items()}
    print('The Text is:', end=' ')
    for i in range(1):
        for j in text_u:
            if j == ' ':
                print(' ', end='')
            else:
                k = (D_C3.get(j) - key) % 26
                if k == 0:
                    print('Z', end='')
                else:
                    k_p = D_C_R2.get(k)
                    print(k_p, end='')
    print(', The number of the key =', ke)
    #time.sleep(1)

