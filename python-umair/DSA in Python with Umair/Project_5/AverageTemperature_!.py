days = int(input('How many Days Temperature ? -> '))

temperature_List = []

for i in range(days):
    temperature = int(input(f'Day {i+1}\'s high temperature : '))
    temperature_List.append(temperature)

tempSum = sum(temperature_List)
AverageTemperature = tempSum / days
print(f'Average Temperature is {AverageTemperature}')

AboveAverageTemperatureDays = [i for i in temperature_List if i > AverageTemperature]

print(f'{len(AboveAverageTemperatureDays)} day(s) have temperatue above than Average')

