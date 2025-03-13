def is_criticality_balanced(temperature, neutrons_emmited):

    if( temperature < 800 and neutrons_emmited > 500
       and temperature * neutrons_emmited < 500000):
        return True
    else:
        return False