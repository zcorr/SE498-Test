# SE498-Test

## Fig Fruit Tree

A simple Python implementation of a fig fruit tree simulation.

### Features

- Create and manage a fig tree
- Track tree age, height, and fruit production
- Trees become mature at 3 years old
- Produce and harvest figs

### Usage

Run the simulation:

```bash
python3 fig_tree.py
```

Or use the FigTree class in your own code:

```python
from fig_tree import FigTree

# Create a new fig tree
tree = FigTree(age=1, height=0.5)

# Grow the tree
tree.grow(years=2)

# Produce fruit
tree.produce_fruit()

# Harvest fruit
tree.harvest()
```

### Requirements

- Python 3.x