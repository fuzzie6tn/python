def greet(input):
    if 'hello' in input:
        return 'hello, there '
    else:
        return 'i\'m not sure you mean '
    
greetings = greet('hello')
print('Hm.. '  + greetings)    