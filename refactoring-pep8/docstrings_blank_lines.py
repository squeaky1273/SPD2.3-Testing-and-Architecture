"""
by Kami Bigdely
Docstrings and blank lines
"""
class OnBoardTemperatureSensor:
    """Sense the temperature."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        """Initialize."""
        pass
    def read_voltage(self):
        """Set voltage to specific integer."""
        return 2.7
    def get_temperature(self):
        """Get temperature of voltage."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

class CarbonMonoxideSensor:
    """"Sense the Carbon Monoxide."""
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        """Initialize sensor temperature."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
    def get_carbon_monoxide_level(self):
        """Get carbon monoxide level."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    def read_sensor_voltage(self):
        """Read current voltage."""
        # In real life, it should read from hardware.
        return 2.3
    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Convert voltage."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature

class DisplayUnit:
    """Display the units."""
    def __init__(self):
        """Initialize the string."""
        self.string = ''
    def display(self,msg):
        """Print a message."""
        print(msg)
class CarbonMonoxideDevice:
    """State the Carbon Monoxide level."""
    def __init__(self, co_sensor, display_unit):
        """Initialize the units."""
        self.carbon_monoxide_sensor = co_sensor
        self.display_unit = display_unit
    def display(self):
        """Display the CO level."""
        msg = 'Carbon Monoxide Level is : ' +  str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
