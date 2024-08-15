ones = {0:'',1:'yek',2:'do',3:'se',4:'chahar',5:'panj',6:'shesh',7:'haft',8:'hasht',9:'noh'}
teens = {0:'',10:'dah',11:'yazdah',12:'davazdah',13:'sizdah',14:'chahardah',15:'panzdah',16:'shanzdah',17:'hefdah',18:'hejdah',19:'nozdah'}
tens = {0:'',2:'bist',3:'si',4:'chehel',5:'panjah',6:'shast',7:'haftad',8:'hashtad',9:'navad'}
hundreds = {0:'',1:'sad',2:'divist',3:'sisad',4:'chaharsad',5:'pansad',6:'sheshsad',7:'hafsad',8:'hashsad',9:'nohsad'}
thousands = {0:'',1:'hezar'}
millions = {0:'',1:'million'}
billions = {0:'',1:'milyard'}
trillions = {0:'',1:'tirilyard'}
quadrillions = {0:'',1:'quadrilyard'}
quintrillions = {0:'',1:'quintilyard'}
units = [ones,teens,tens,hundreds,thousands,millions,billions,trillions,quadrillions,quintrillions]
def digitCounter(n):
    count = 0
    while n>0:
        count += 1
        n //= 10
    return count
def spliter(n):
    numlist = []
    while n>0:
        numlist.append(n%1000)
        n //= 1000
    return numlist
def numberToString(n,unit=''):
    s = ''
    if n==0:
        return s
    nDigits = digitCounter(n)
    if nDigits == 3:
        s = tripleDigit(n)
    elif nDigits == 2:
        s = doubleDigit(n)
    else:
        s = ones[n]
    if unit=='': return s
    else: return (s + ' ' + unit)
def tripleDigit(n):
    s = ''
    r = n%100
    n = str(n)
    r1 = int(n[0]); r2 = int(n[1]); r3 = int(n[2])
    if r==0:
        s = hundreds[r1] 
    elif r<10:
        s = hundreds[r1] + ' o ' + ones[r3]
    elif r<20:
        s = hundreds[r1] + ' o ' + teens[r]
    elif r3!=0:
        s = hundreds[r1] + ' o ' + tens[r2] + ' o ' + ones[r3]
    else:
        s = hundreds[r1] + ' o ' + tens[r2] 
    return s
def doubleDigit(n):
    s = ''
    if n<20:
        s = teens[n]
    else:
        n = str(n)
        r1 = int(n[0]); r2 = int(n[1])
        if r2==0:
            s = tens[r1]
        else:
            s = tens[r1] + ' o ' + ones[r2]
    return s
def main():
    negative = False
    while True:
        try:
            n = int(input("enter a number: "))
        except Exception as error:
            print(error)
        else: break
    if n==0: 
        print('sefr')
        return
    if n<0:
        n = n*(-1)
        negative = True
    numberList = spliter(n)
    alphaNumber = []
    alphaNumber.append(numberToString(numberList[0]))
    del numberList[0]
    j = 4
    for i in numberList:
        alphaNumber.append(numberToString(i,units[j][1]))
        j += 1
    alphaNumber = alphaNumber[::-1]
    s = ''
    for k in alphaNumber:
        if len(k)>0:
            s += k + ' o '
    s = s[0:len(s)-2]
    if negative == True:
        print('manfie ' + s)
    else:
        print(s)
main()
