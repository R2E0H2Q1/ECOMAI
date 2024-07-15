#Input a decimal number for temperature from the user. If the temperature is greater than 30 print hot otherwise print normal. Solve by abbreviated printing of one line.
temp: float = float(input("Please enter the current temperature: "));
print("Today is Hot!" if temp > 30 else "The temperature is normal today!")
