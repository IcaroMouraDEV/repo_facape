def convert_celsius_in_fahrenheit() -> None:  # converter grau celsius em grau fahrenhiet
    
    celsius = int(input('digite a temperatura em °C: '))
    fahrenheit = (9 * celsius) / 5 + 32

    print(
        f'''{celsius}°C são {fahrenheit}°F'''
    )


convert_celsius_in_fahrenheit()
