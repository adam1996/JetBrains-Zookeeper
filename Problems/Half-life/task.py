HALF_LIFE = 12
days = 0

initial_num_atoms = int(input())
result_num_atoms = int(input())


while(initial_num_atoms > result_num_atoms):
    initial_num_atoms /= 2
    days += HALF_LIFE

print(days)

