# Trying to implement the luhn algorithim

userCreditCardNo=input("Please enter your credit card no: ")

def validateCreditCard():
    #Remove the dashes and reverse the string
    creditCardNo=userCreditCardNo.replace("-","")
    creditCardNo=creditCardNo[::-1]
    
    total=0
    result=None
    
    for i in range(len(creditCardNo)):
        digit=int(creditCardNo[i])
        
        if i % 2 == 1:
            digit*=2
            
        if digit>9:
            digit-=9
            
        total+=digit
        
    if total % 2 == 0:
        result='The credit Card number you have provided is valid'
    else:
        result='The credit card number you have provided is invalid'
        
    return result
        

print(validateCreditCard())