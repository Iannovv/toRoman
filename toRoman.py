def toRoman(num):
    
    m = ["","M","MM","MMM"]
    c = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    x = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    i = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    if (num < 1) or (num >3999):
        raise Exception("Podaj liczbe z przedzialu 1-3999")
    if not type(num) is int:
        raise TypeError("Podaj liczbe, nie slowo")

    M = m[num // 1000]
    C = c[(num % 1000) // 100]
    X = x[(num % 100) // 10]
    I = i[num % 10]
    
    return (M+C+X+I)
    
while True:    
    y = int(input("Podaj liczbe: "))
    print(toRoman(y))
