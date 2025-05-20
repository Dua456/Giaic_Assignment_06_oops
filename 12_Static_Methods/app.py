
class TemperatureConverter:
    
    # Define a static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Convert Celsius to Fahrenheit using the formula: (C × 9/5) + 32
        return (c * 9/5) + 32    # Corrected 9/3 to 9/5 for accurate conversion

# Call the static method without creating an object
# Passing 10°C to convert it into Fahrenheit
print(TemperatureConverter.celsius_to_fahrenheit(10))  # Output will be: 50.0°F
