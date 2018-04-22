def camel_to_snake(name):
    newstr = ""
    for k, i in enumerate(name):
        if(k == 0 and i.isupper()):
            i = i.lower()
        if(i.isupper()):
            i = "_" + i.lower()
        newstr += i
    print(newstr)
	
def snake_to_camel(name):
    newstr = ""
    k_pass = ""
    for k, i in enumerate(name):
        if(k == 0 and i.islower()):
            i = i.upper()
        if(i == "_"):
            i = name[k + 1].upper()
            k_pass = k + 1
        if(k_pass != k): newstr += i
    print(newstr)
	
camel_to_snake("CamelCase")
camel_to_snake("getUserId")
snake_to_camel("snake_case")
snake_to_camel("set_repository")