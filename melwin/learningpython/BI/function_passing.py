## function objects 

def num_digits(x): 
    return len(str(x)) 

def most_digits(L): 
    L = sorted(L, key=num_digits) 
    return L[-1] 

def largest_two_digit_even(L): 
    two_digit_numbers = [i for i in L if num_digits(i)==2] 
    evens = [i for i in two_digit_numbers if i%2==0] 
    evens.sort()
    return evens[-1] 

def best(L, criteria): 
    return criteria(L) 

def num_ones_in_binary(num):
    binary = bin(num)[2:]
    return binary.count('1')
        
def most_ones_in_binary(L):
    L = sorted(L, key=num_ones_in_binary)
    return L[-1]

L = [1, 76, 84, 95, 214, 1023, 511, 32] 

print(best(L, min)) # Prints 1 
print(best(L, largest_two_digit_even)) # Prints 84 
print(best(L, most_digits)) # Prints 1023
print(best(L, most_ones_in_binary))
