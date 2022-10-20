#----      Мне было очень грустно смотреть, на код только для двоичной и восьмеричной, поэтому я сделал для всех систем счисления с основанием < 17

numbers = "0123456789abcdef"

def num_sys(basis, n):
    res = ''
    while n > 0:
        res += numbers[n % basis]
        n //=  basis
    return int(res[::-1])



print("Введите число")
n = int(input())



print("Введите целевую систему счисления (основание не больше 16)")
basis = int(input())



print(n, "->", num_sys(basis, n))
