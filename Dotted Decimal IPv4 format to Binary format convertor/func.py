def OctetToBin(octet):
    nums = [128, 64, 32, 16, 8, 4, 2, 1]
    octet = int(octet)
    binary = ''
    added = 0
    for num in nums:
        if added == octet:
            binary += '0'
        elif octet > num and added + num <= octet:
                added += num
                binary += '1'
        elif octet < num or added + num > octet:
                binary += '0'
        elif octet == num:
                binary += '1'
                added += num
    return binary
