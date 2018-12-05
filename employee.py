class Employee():
    """Info about employees."""
    
    def __init__(self, first_name, last_name, salary):
        """Collect info about employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Give employee a raise."""
        self.salary += amount
        