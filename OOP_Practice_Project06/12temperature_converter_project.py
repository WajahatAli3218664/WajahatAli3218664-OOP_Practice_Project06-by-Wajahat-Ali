#Static Methods
#Assignment 12:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
    """
    🌡️ TemperatureConverter class provides static methods
    for converting temperatures between different units.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Convert Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return (celsius * 9/5) + 32

# 🚀 Example usage
if __name__ == "__main__":
    celsius_temp = 0
    fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
    print(f"🌡️ {celsius_temp}°C is equal to {fahrenheit_temp}°F")
