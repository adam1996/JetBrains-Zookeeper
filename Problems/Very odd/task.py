# Find out if the result of dividing A by B is an odd number.

dividend = int(input())
divisor = int(input())

#No remainder for inputs when divided

result = dividend / divisor

print(result%2 > 0)
