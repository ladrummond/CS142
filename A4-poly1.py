
# print_poly(a,e) takes two input arrays a, e representing the integer coefficients 
# exponentials of the polynomial, respectively. It outputs a string with a
# the input polynomial written in an special formated.  
# For instance: 3x^2 + 5x - 10  is output as 3x^(2)+5x^(1)-10x^(0).
# p(x) = a1*x^e1 + a2*x^e2 + . . . ak*x^e^k
# ai is an array of k-integer coefficients, and 0 <= ai <= c_max,
# ei is an array of k-integer exponentials, and 0 <= ei <= e_max
# returns the
def print_poly(a,e):
    w = ''
    for i in range(len(a)):
        if a[i] > 0:
            if w:
                w += '+'+str(a[i])+'x^('+str(e[i])+')'
            else:
                w += str(a[i])+'x^('+str(e[i])+')'
        elif a[i] < 0:
            w += str(a[i])+'x^('+str(e[i])+')'
        print(w)
    return w

# poly(a,e) computes the integer roots of a polynomial
# p(x) = a1*x^e1 + a2*x^e2 + . . . ak*x^e^k
# ai is an array of k-integer coefficients, and 0 <= ai <= c_max,
# ei is an array of k-integer exponentials, and 0 <= ei <= e_max.
# It returns a string with either an error or the roots of the polynomial 
# it also returns whether poly1 accepts or rejects the string.
def poly1(a, e):
    if len(a) != len(e):
        w = 'the number of coefficients and exponents do not match'
        decide = 'reject'
    else:
        # generate a printable string w with the polynomial
        w = print_poly(a,e)
        # coefficient with the largest absolute value
        c_max = max([abs(y) for y in a ])
        # c1 is the coefficient of the highest order term
        e_max, i = max((abs(v),i) for i,v in enumerate(e))
        c1 = abs(a[i])
        # count how many terms are in the polynomial a_i not = 0
        k = sum([1 for i in a if i != 0])
        #compute bound b = +/- k*c_max/c1
        b = k*c_max//c1
        roots = []
        for x in range(b*-1, b+1,1):
            p = 0
            for i in range(len(a)):
                p += a[i]*(x**(e[i]))
            if p == 0:
                roots.append(x)
        if roots:
            
            sroots = [str(i) for i in roots] 
            sroots = ','.join(sroots)
            w += ' <integer roots:'+sroots+'>'
          
            decide = 'accept'
        else:
            w += ' has no integer roots found'
            decide = 'reject'
    return decide, w 
