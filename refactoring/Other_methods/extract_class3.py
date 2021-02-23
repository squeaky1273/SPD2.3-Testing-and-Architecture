# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Cooking:
    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cooking_criteria_satisfied(self, time, temperature, 
                                        pressure, desired_state):
        return self.is_well_done(time, temperature, pressure, desired_state) or \
            self.is_medium(time, temperature, pressure, desired_state)


    def is_well_done(self, time, temperature, pressure, desired_state):    
        return desired_state == 'well-done' and  \
            self.get_cooking_progress(time, temperature, pressure) >= WELL_DONE


    def is_medium(self, time, temperature, pressure, desired_state):
        return desired_state == 'medium' and  \
            self.get_cooking_progress(time, temperature, pressure) >= MEDIUM

    def get_cooking_progress(self, time, temperature, pressure):
        return time * temperature * pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

c = Cooking(time, temp, pressure, desired_state)
if c.is_cooking_criteria_satisfied(time, temp, pressure, desired_state):
    print('cooking is done.')
else:
    print('ongoing cooking.')
