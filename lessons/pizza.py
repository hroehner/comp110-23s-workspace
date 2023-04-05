"""Define Pizza class!"""

class Pizza: 

    # attributes 
    size: str # "small or large"
    toppings: int # number of toppings
    gluten_free: bool 

    def __init__(self, size_input: str, topping_input: int, gluten_free_input: bool):
        self.size = size_input
        self.topping = topping_input 
        self.gluten_free = gluten_free_input
        # it actually returns self 

    def price(self) -> float: 
        """Calculate and return the cost of pizza"""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else: 
            cost = 5.0 
        # charge .75 per topping
        cost += .75 * self.topping
        # charge $1 for gluten free 
        if self.gluten_free:
            cost += 1.0 
        return cost 
    
    def add_toppings(self, num_toppings: int) -> None: 
        """Add a certain number of toppings!"""
        self.toppings += num_toppings