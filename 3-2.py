num = int(input("Enter a four-digit positive integer \n" ))
print(num)
digit1 = int(num / 1000)
digit2 = int(num / 100 % 10)
digit3 = int(num / 10 % 10)
digit4 = int(num % 10)
print(digit1)
print(digit2)
print(digit3)
print(digit4)
print ("The product of numbers =", digit1 * digit2 * digit3 * digit4)
order = [digit1, digit2, digit3, digit4]
print ('Numbers in ascending order =', sorted(order))
revers = (str(digit4) + str(digit3) + str(digit2) + str(digit1))
print('The number is in reverse order =', revers)
