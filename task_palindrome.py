def is_palindrome(s):
    s = str(s)
    s = "".join(s.split())

    without_spaces_revers = []
    for i in s:
        without_spaces_revers.append(i)
    
    without_spaces_revers = without_spaces_revers[::-1]
    without_spaces_revers = "".join(without_spaces_revers)
	
    if(s.lower() != without_spaces_revers.lower()):
        return False
	
    return True
	
print(is_palindrome("49094"))
print(is_palindrome("Я бы изменил мир, но бог не дает исходники"))
print(is_palindrome("Сел в озере березов лес"))