def is_criticality_balanced(temperature, neutrons_emmited):
    """
    
    Determines if a nuclear reactor is in a balanced criticality state.

    A reactor is considered balanced if:
    - The temperatura is below 800k.
    - The number of neutrons emitted is greater than 500.
    - The product of temperature and neutrons emitted is less than 500,00.

    Parameters:
    temperature (int or float): The reactor's temperature in Kelvin.
    neutrons_emitted (int): The number of neutrons emitted per second.

    Returns:
    bool: True if the reactor is balanced, False otherwise.    
    """

    return (
        temperature < 800 and 
        neutrons_emmited > 500 and
        temperature * neutrons_emmited < 500000
    )
    

def reactor_efficiency(voltage, current, theoretical_max_power): 
    """
    Evaluates the efficieency category of a reactor based on power output.

    The efficency is determined by the ratio of generated power to the theoretical maximum power,
    expressed as a percetage. THe function categorizes efficiency into four levels:
    - `green' : efficiency >= 80%
    - 'orange' : 60% <= efficiency < 80%
    - 'red': 30% <= efficiency < 60%
    - 'black' : efficiency < 30%
    """
    generated_power  = voltage * current
    efficiency = (generated_power/ theoretical_max_power)*100
    
    if efficiency >= 80:
        return 'green'
    if 60 <= efficiency< 80:
        return 'orange'
    if 30 <= efficiency < 60:
        return 'red'
    return 'black' 
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    Determines the reactor's safety status based on its operational output compared to a threshold.
    
    The safety levels are categorized as:
    - 'LOW': if the reactor output is below 90% of the threshold.
    - 'NORMAL': if the reactor output is within ±10% of the threshold.
    - 'DANGER': if the reactor output exceeds 110% of the threshold.
    
    Parameters:
    temperature (int or float): The reactor's temperature in Kelvin.
    neutrons_produced_per_second (int): The number of neutrons produced per second.
    threshold (int or float): The safety threshold for reactor output.
    
    Returns:
    str: Safety status ('LOW', 'NORMAL', or 'DANGER').
    """
    reactor_output = (temperature * neutrons_produced_per_second)

    if reactor_output < 0.9 * threshold:
        return 'LOW'
    if 0.9 * threshold <= reactor_output <= 1.1 * threshold:
        return 'NORMAL'
    return 'DANGER'