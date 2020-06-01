#Subtract the Sum
#https://www.codewars.com/kata/56c5847f27be2c3db20009c3

kiwi = 'kiwi'
pear = 'pear'
banana = 'banana'
melon = 'melon'
pineapple = 'pineapple'
cucumber = 'cucumber'
apple = 'apple'
orange = 'orange'
cherry = 'cherry'
grape = 'grape'

fruits = [kiwi,pear,kiwi,banana,melon,banana,melon,pineapple,apple,pineapple,cucumber,pineapple,
          cucumber,orange,grape,orange,grape,apple,grape,cherry,pear,cherry,pear,kiwi,banana,kiwi,
          apple,melon,banana,melon,pineapple,melon,pineapple,cucumber,orange,apple,orange,grape,orange,
          grape,cherry,pear,cherry,pear,apple,pear,kiwi,banana,kiwi,banana,melon,pineapple,melon,apple,
          cucumber,pineapple,cucumber,orange,cucumber,orange,grape,cherry,apple,cherry,pear,cherry,pear,kiwi,
          pear,kiwi,banana,apple,banana,melon,pineapple,melon,pineapple,cucumber,pineapple,cucumber,apple,grape,
          orange,grape,cherry,grape,cherry,pear,cherry,apple,kiwi,banana,kiwi,banana,melon,banana,melon,
          pineapple,apple,pineapple]
def subtract_sum(number):
    number -= sum([int(i) for i in str(number)])
    while(number>100):
        total = sum([int(i) for i in str(number)])
        number -= total

    return fruits[number-1]
