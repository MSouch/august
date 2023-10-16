def celcius_to_farenheit():
    faren = 25 * 9/5 + 32
    return(faren)

def farenheit_to_celcius():
    celcius = 5/9 * (82 - 32)
    return(celcius)

print(f"25 Celcius to Farenheit is: {celcius_to_farenheit()}, and 82 Farenheit to Celcius is: {farenheit_to_celcius()}")