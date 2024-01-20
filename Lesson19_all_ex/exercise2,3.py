# write a getter and setter for the temperature attribute. use the @property
# decorator for the getter and the @attribute.setter for setter
# if the temperature is less than 0 or greater than 100 raise a ValueError
class TemperatureSensor:
    def __init__(self,temperature=0):
        self.__temperature = temperature
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self,new_temperature):
        if 0 <= new_temperature <=100:
            self.__temperature = new_temperature
        else:    
            raise ValueError("Error")

t = TemperatureSensor()
t.temperature = 90
print(t.temperature)