def encode(lst, rot=0):
    new_lst = ""

    for i in lst:
        if(i.isalpha()):
            code = abc(ord(i), rot, "+")
            i = chr(code())
        new_lst += i

    print(new_lst)
	
def decode(lst, rot=0):
    new_lst = ""
    for i in lst:
        if(i.isalpha()):
            code = abc(ord(i), rot, "-")
            i = chr(code())
        new_lst += i

    print(new_lst)
	
def abc(a, rot, sign):
    numb1 = list(range(65, 91))
    numb2 = list(range(97, 123))
	
    if(a in numb1):
        numb = numb1
    else:
        numb = numb2
		
    def plus():
        if(numb[len(numb) - 1] >= a + rot):
            return a + rot
        
        return numb[a + rot - numb[len(numb) - 1] - 1]
		
    def minus():
        if(numb[len(numb) - 1] >= a - rot and numb[0] <= a - rot):
            return a - rot
        
        return numb[len(numb) - (numb[0] - (a - rot))]

    if(sign == "+"):
        return plus
    else:
        return minus

encode("Hello, Python3!", 1)
decode("Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg.", 13)
encode("There is no programming language, no matter how structured, that will prevent programmers from making bad programs.", 25)