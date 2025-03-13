def is_criticality_balanced(temperature, neutrons_emmited):

    if( temperature < 800 and neutrons_emmited > 500
       and temperature * neutrons_emmited < 500000):
        return True
    else:
        return False
    

def reactor_efficiency(voltage, current, theoretical_max_power):

    generated_power  = voltage * current
    efficiency = (generated_power/ theoretical_max_power)*100

    if efficiency >= 80:
        return 'green'
    elif 60 <= efficiency< 80:
        return 'orange'
    elif 30 <= efficiency < 60:
        return 'red'
    else:
        return 'black' 
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):

    reactor_output = (temperature * neutrons_produced_per_second)

    if reactor_output < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= reactor_output <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'