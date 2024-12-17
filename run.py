import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. กำหนด Input และ Output
temperature = ctrl.Antecedent(np.arange(16, 31, 1), 'temperature')  # อุณหภูมิ 16°C ถึง 30°C
humidity = ctrl.Antecedent(np.arange(20, 81, 1), 'humidity')        # ความชื้น 20% ถึง 80%
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')      # ความเร็วพัดลม 0% ถึง 100%

# 2. สร้าง Membership Functions
temperature['cool'] = fuzz.trimf(temperature.universe, [16, 16, 22])
temperature['comfortable'] = fuzz.trimf(temperature.universe, [20, 24, 28])
temperature['hot'] = fuzz.trimf(temperature.universe, [26, 30, 30])

humidity['low'] = fuzz.trimf(humidity.universe, [20, 20, 40])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trimf(humidity.universe, [60, 80, 80])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [60, 100, 100])

# 3. สร้างกฎ (Fuzzy Rules)
rule1 = ctrl.Rule(temperature['cool'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['comfortable'] & humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'] | humidity['high'], fan_speed['high'])

# 4. รวมกฎเข้าด้วยกัน
fan_speed_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_control)

# 5. ทดสอบการทำงาน
fan_speed_simulation.input['temperature'] = 27  # อุณหภูมิ 27°C
fan_speed_simulation.input['humidity'] = 65    # ความชื้น 65%

fan_speed_simulation.compute()

# 6. แสดงผล
print(f"Fan Speed: {fan_speed_simulation.output['fan_speed']:.2f}%")

temperature.view()
humidity.view()
fan_speed.view()
plt.show()


