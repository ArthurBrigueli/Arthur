def sequencia_fibonacci(num):
    sequencia = []
    a = 0 
    b = 1

    while a <= num:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

def is_fibonacci(num):
    sequencia = sequencia_fibonacci(num)
    return num in sequencia, sequencia


num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
is_fibo, sequence = is_fibonacci(num)

if is_fibo:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

print(f"Sequência de Fibonacci até {num}: {sequence}")
