#Currency Conversion
#https://www.codewars.com/kata/5a5c118380eba8a53d0000ce

def convert_my_dollars(usd, currency):
  dollars = 0
  vowels = ['A','E','I','O','U']
  if currency[0] not in vowels:
      dollars = usd*int(str(CONVERSION_RATES[currency]),2)
  else:
      dollars = usd*CONVERSION_RATES[currency]
  return 'You now have {} of {}.'.format(dollars, currency)
