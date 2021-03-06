# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, template_parameter='Hello, <name>!'):
    return (template_parameter.replace("<name>", name))

print(greet('Klaas'))
print(greet('Piet', "What's up, <name>!"))
print(greet('Jan', "Whatup, <name> whatup?!"))

def force(mass, body='earth'):
    d = {
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15, 
        'saturn': 10.44, 
        'earth': 9.798,
        'uranus': 8.87, 
        'venus': 8.87, 
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62, 
        'pluto': 0.58
    }
    f = mass * round(d[body], 1)
    return f

print(force(mass=5.9736))
print(force(mass=1.8986, body='jupiter'))

def pull(m1, m2, d):
    gravity = (6.674 * (10 ** -11)) * ((m1*m2)/d ** 2)
    return gravity

print(pull(10.0, 20.0, 5.0))
