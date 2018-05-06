def dec2bin(number):
    return univers_conv_from_dec(number, 2)


def dec2oct(number):
    return univers_conv_from_dec(number, 8)
    
   
def dec2hex(number):
    return univers_conv_from_dec(number, 16)
   
  
def bin2dec(number):
    return univers_conv_to_dec(number, 2)


def oct2dec(number):
    return univers_conv_to_dec(number, 8)

    
def hex2dec(number):
    return univers_conv_to_dec(number, 16)
    
    
def univers_conv_from_dec(number, sis):
    list = []
    while number > 0:
        x = number % sis
        number /= sis
        list.insert(0, str(x))
        
        number = int(number)
        
    return "".join(list)
    
    
def univers_conv_to_dec(number, sis):
    lim = len(number)
    result = 0
    for k, v in enumerate(range(lim, 0, -1)):
        num = ord(number[k]) if number[k].isalpha() else number[k]
        result += int(num) * sis**(v-1)
        
    return result
    