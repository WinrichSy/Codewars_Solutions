#Grasshopper - Debug
#https://www.codewars.com/kata/55cb854deb36f11f130000e1

def weather_info (temp):
    c = convertToCelsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")

def convertToCelsius (temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius
