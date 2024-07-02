def dec_to_base(num,base):  
    base_num = ""
    while num > 0:
        dig = int(num%base)
        if dig < 10:
            base_num = base_num + str(dig)
        else:
            base_num = base_num + chr(ord('A')+dig-10)  
        num = num // base
    base_num = base_num[::-1]  #To reverse the string
    return base_num
	
print(dec_to_base(10,2))