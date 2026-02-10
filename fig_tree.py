class FigTree:
    """A class representing a fig fruit tree."""
    
    def __init__(self, age=0, height=0.0):
        """
        Initialize a fig tree.
        
        Args:
            age (int): Age of the tree in years
            height (float): Height of the tree in meters
        """
        self.age = age
        self.height = height
        self.fruit_count = 0
        self.is_mature = age >= 3
    
    def grow(self, years=1):
        """
        Grow the tree by specified number of years.
        
        Args:
            years (int): Number of years to grow
        """
        self.age += years
        self.height += years * 0.5
        self.is_mature = self.age >= 3
    
    def produce_fruit(self):
        """Produce figs if the tree is mature."""
        if self.is_mature:
            self.fruit_count += 10
            return f"The fig tree produced 10 figs! Total: {self.fruit_count}"
        else:
            return "The fig tree is too young to produce fruit."
    
    def harvest(self):
        """Harvest all figs from the tree."""
        if self.fruit_count > 0:
            harvested = self.fruit_count
            self.fruit_count = 0
            return f"Harvested {harvested} figs!"
        else:
            return "No figs to harvest."
    
    def __str__(self):
        """String representation of the fig tree."""
        return f"Fig Tree: Age={self.age} years, Height={self.height:.1f}m, Fruits={self.fruit_count}, Mature={self.is_mature}"


def main():
    """Demonstrate the fig tree functionality."""
    print("=== Fig Fruit Tree Simulation ===\n")
    
    # Create a new fig tree
    tree = FigTree(age=1, height=0.5)
    print(f"Created: {tree}")
    print()
    
    # Grow the tree
    print("Growing the tree for 2 years...")
    tree.grow(2)
    print(f"After growing: {tree}")
    print()
    
    # Try to produce fruit
    print(tree.produce_fruit())
    print(f"Current state: {tree}")
    print()
    
    # Grow more and produce more fruit
    print("Growing for 1 more year...")
    tree.grow(1)
    print(tree.produce_fruit())
    print()
    
    # Harvest the fruit
    print(tree.harvest())
    print(f"After harvest: {tree}")


if __name__ == "__main__":
    main()
