#Assignment3, Part B
menu_items = ['ravioli', 'beef stew', 'steamed vegetables', 'lobster mac and cheese']
print("Here is the plan for tomorrow's menu: ")
print(*menu_items)
suggestion = input("Please add a suggestion for tomorrow's menu: ")
print(suggestion)
menu_items.append(suggestion)
print("Here is tomorrow's full menu: ")
print(*menu_items)
