"""
Examples of generator functions using
enhancements in PEP342 illustrating
the yield expression and the ability to send()
"""

def countdown(counter):
    """
    This countdown generator can be reset/changed by sending
    a new integer.
    """
    while counter > 0:
        new_value = yield counter
        if new_value is not None:
            counter = new_value
        counter =  counter - 1

def footrace():
    """
    The footrace generator will start over if it is sent
    a string 'fault'
    """
    while True:
        status = yield 'On your marks.'
        if status == 'fault':
            continue
        status = yield 'Set.'
        if status == 'fault':
            continue
        yield 'Go!'
        break
