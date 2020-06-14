INTEREST_RATE = 7.1
number_of_years = 0

deposit = int(input())

while(deposit < 700000):
    deposit += deposit / 100 * INTEREST_RATE
    number_of_years += 1

print(number_of_years)
