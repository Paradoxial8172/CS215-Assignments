
# #Formula for next term: Fn = Fn-1 + Fn-2
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
    
def main(nterms: int) -> list:
    if nterms <= 0:
        raise ValueError("Value must be greater than 0.")     
    else:
        fib_seq = []
        for i in range(nterms+1):
            fib_seq.append(fib(i))

    fib_seq.pop(0)
    return fib_seq

def odd_even(sequence: list) -> dict:
    even_num = 0
    odd_num = 0
    for num in sequence:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    return {
        "Odd Numbers": odd_num,
        "Even Numbers": even_num
    }

    
user_input = int(input("Input a number of terms you wish to be implemented into the fibonacci sequence: "))
print(main(user_input))
print("Number of terms: {a}".format(a=user_input))
print(odd_even(main(user_input)))
