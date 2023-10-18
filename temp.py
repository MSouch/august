def celcius_to_farenheit():
    """Given a celcius value, return converted temp"""
    faren = 25 * 9/5 + 32
    return(faren)

def farenheit_to_celcius():
    """Given a farenheit value, return converted temp"""
    celcius = 5/9 * (82 - 32)
    return(celcius)

#just a silly little test commit

print(f"25 Celcius to Farenheit is: {celcius_to_farenheit()}, and 82 Farenheit to Celcius is: {farenheit_to_celcius()}")