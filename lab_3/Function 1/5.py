from itertools import permutations
def permut(input_string):
    permuteds = [''.join(p) for p in permutations(input_string)]
    
    
    for permuted in permuteds:
        print(permuted)


user_input = input("vvedite:")    
permut(user_input)