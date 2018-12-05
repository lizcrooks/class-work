def make_sandwich(*toppings):
    """Print the list of toppings for each sandwich."""
    print("\nMaking a sandwich with the following items:"
    for topping in toppings:
        print("- " + topping)
    
make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('tuna')
make_sandwich('cheese whiz', 'grilled onions', 'steak', 'mushrooms')