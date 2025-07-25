#1.WAP:Take a list and add the numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

#2.WAP:Take a list and find the even numbers
numbers = [10, 22, 23, 24, 27, 69]
for num in numbers:
    if num%2 ==0:
        print(num)

#3.WAP:Count even and odd numbers from 1 to 10
even_count = 0
odd_count = 0
for i in range(1, 11):
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1
print('even_count:', even_count)
print('odd_count:', odd_count)

#4.SUM OF DIGITS OF A NUMBER EXAMPLE 12322 OUTPUT=10
num = 12322
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10
print("Sum of digits:", sum_digits)

#5.PRODUCT OF DIGITS OF A NUMBER EXAMPLE 123 OUTPUT=6
num = 123
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Product of digits:", product)