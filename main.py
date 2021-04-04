# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, template_parameter='Hello, <name>!'):
    substring = 'Hello, <name>!'
    if substring in template_parameter:
        return f'{template_parameter[:7]}{name}!'
    else:
        return f'{template_parameter[:-7]}{name}!'

print(greet('Klaas'))
print(greet('Piet', "What's up, <name>!"))

def force(mass, body='earth'):
    d = {
        'sun': 274.0,
        'jupiter': 24.9,
        'neptune': 11.2, 
        'saturn': 10.4, 
        'earth': 9.8,
        'uranus': 8.9, 
        'venus': 8.9, 
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6, 
        'pluto': 0.6
    }
    f = mass * d[body]
    return f

print(force(mass=5.9736))
print(force(mass=1.8986, body='jupiter'))

def pull(m1, m2, d):
    gravity = (6.674 * (10 ** -11)) * ((m1*m2)/d ** 2)
    return gravity

print(pull(m1=10.0, m2=20.0, d=5.0))
