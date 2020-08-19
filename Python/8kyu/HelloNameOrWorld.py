#Hello, Name or World!
#https://www.codewars.com/kata/57e3f79c9cb119374600046b

def hello(name=''):
    if name == '': return 'Hello, World!'
    return "Hello, {}!".format(name.title())
