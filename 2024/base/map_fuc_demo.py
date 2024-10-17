people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = {'phone': 'phone number','address': 'Address'}
name = input("Enter your name: ")
request = input('phone(p) or address(a)? ')

# Get the requested information
key = request.strip().lower()

if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print(f"{name}'s {label} is {result}")
