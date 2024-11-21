def ispalindrome(string):
    leftpose=0
    rightpose=len(string)-1
    while rightpose>=leftpose:
        if not string[leftpose]==string[rightpose]:
            return False
        leftpose+=1
        rightpose-=1
    return True
print("is this a palindrome")
print(ispalindrome ("madam"))