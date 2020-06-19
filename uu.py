#palindrome

print("Cześć abym mógł z tobą normalnie rozmawiać napisz mi swoje imię")
imię=input()

def palindrome(s): 
    return s == s[::-1] 

print("Ok,{} sprawdźmy czy znasz jakieś palindromy,to wyraz które brzmią tak samo od tyłu jaki o od przodu".format(imię))
s=input()
xyz = palindrome(s) 
    
   
    
if xyz:
        print("Dobrze {} czaisz bazuke".format(imię))
else:
        print("Ajć to nie to")

