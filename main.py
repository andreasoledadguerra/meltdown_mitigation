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
    
