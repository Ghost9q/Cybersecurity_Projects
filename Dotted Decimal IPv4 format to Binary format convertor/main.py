from func import OctetToBin

while True:
    decimal = input('enter an ip address in decimal notation (enter q to quit): ')
    if decimal == 'q':
        break

    binary = ''
    octet1 = ''
    octet2 = ''
    octet3 = ''
    octet4 = ''

    count = 0
    for digit in decimal:
        if digit == '.':
            break
        octet1 += digit
        count+=1

    for digit in decimal[count+1:]:
        if digit == '.':
            break
        octet2 += digit
        count+=1

    for digit in decimal[count +2:]:
        if digit == '.':
            break
        octet3 += digit
        count+=1


    for digit in decimal[count +3:]:
        if digit == '.':
            break
        octet4 += digit
        count+=1
    # this is one way of doing it using a built-in function of python
    # binary = f'{format(int(octet1), '08b')}.{format(int(octet2), '08b')}.{format(int(octet3), '08b')}.{format(int(octet4), '08b')}'

    # but i wrote a function for my self so i am gonna use that :)
    binary = f'{OctetToBin(int(octet1))}.{OctetToBin(int(octet2))}.{OctetToBin(int(octet3))}.{OctetToBin(int(octet4))}'
    print(f'Binary: {binary}')
