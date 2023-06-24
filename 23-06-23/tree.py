Families = {
    'rohith': {
        'dheeraj': {'Boxy', 'Rosy'},
        'koushik': {'pepsi'}
    },
    'akshay': {
        'abhay': {'Tony'},
        'abhinay': {'Hamster'},
        'druva': {'Hamster'}
    },
    'Carlos': {
        'Diego': 'Cat',
        'ferret': 'Fox'
    }
}

for parent, children in Families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(", and ".join([str(child) for child in children]))
