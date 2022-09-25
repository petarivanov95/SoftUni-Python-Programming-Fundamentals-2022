from forex_python.coverter import CurrencyRates

amount = int(input('Amount in GBP: '))
c = CurrencyRates
current_rate = c.get_rate('GBP','USD')
my_result = amount*current_rate

print(f'{amount} in GBP is {my_result} in USD')
