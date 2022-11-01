def isValid( s: str) -> bool:
    if len(s) %2 != 0:
        return False
    while True:
        if '[]' in s:
            s = s.replace('[]', '')
        elif '{}' in s:
            s = s.replace('{}', '')
        elif '()' in s:
            s = s.replace('()', '')
        else:
            break
    if s:
        return False
    else:
        return True        
print(isValid('()'))

