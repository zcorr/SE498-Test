"""Tests for the FigTree class."""
import unittest
from fig_tree import FigTree


class TestFigTree(unittest.TestCase):
    """Test cases for the FigTree class."""
    
    def test_initialization(self):
        """Test fig tree initialization."""
        tree = FigTree(age=2, height=1.0)
        self.assertEqual(tree.age, 2)
        self.assertEqual(tree.height, 1.0)
        self.assertEqual(tree.fruit_count, 0)
        self.assertFalse(tree.is_mature)
    
    def test_maturity(self):
        """Test fig tree maturity at 3 years."""
        young_tree = FigTree(age=2, height=1.0)
        self.assertFalse(young_tree.is_mature)
        
        mature_tree = FigTree(age=3, height=1.5)
        self.assertTrue(mature_tree.is_mature)
    
    def test_grow(self):
        """Test fig tree growth."""
        tree = FigTree(age=1, height=0.5)
        tree.grow(2)
        self.assertEqual(tree.age, 3)
        self.assertEqual(tree.height, 1.5)
        self.assertTrue(tree.is_mature)
    
    def test_produce_fruit_immature(self):
        """Test that immature trees don't produce fruit."""
        tree = FigTree(age=1, height=0.5)
        result = tree.produce_fruit()
        self.assertEqual(tree.fruit_count, 0)
        self.assertIn("too young", result)
    
    def test_produce_fruit_mature(self):
        """Test that mature trees produce fruit."""
        tree = FigTree(age=3, height=1.5)
        result = tree.produce_fruit()
        self.assertEqual(tree.fruit_count, 10)
        self.assertIn("produced 10 figs", result)
        
        # Produce more fruit
        tree.produce_fruit()
        self.assertEqual(tree.fruit_count, 20)
    
    def test_harvest(self):
        """Test harvesting figs."""
        tree = FigTree(age=3, height=1.5)
        tree.produce_fruit()
        tree.produce_fruit()
        
        result = tree.harvest()
        self.assertIn("Harvested 20 figs", result)
        self.assertEqual(tree.fruit_count, 0)
    
    def test_harvest_empty(self):
        """Test harvesting when no fruit available."""
        tree = FigTree(age=3, height=1.5)
        result = tree.harvest()
        self.assertIn("No figs", result)
        self.assertEqual(tree.fruit_count, 0)
    
    def test_str_representation(self):
        """Test string representation of the tree."""
        tree = FigTree(age=3, height=1.5)
        str_repr = str(tree)
        self.assertIn("Age=3", str_repr)
        self.assertIn("Height=1.5m", str_repr)
        self.assertIn("Fruits=0", str_repr)
        self.assertIn("Mature=True", str_repr)


if __name__ == "__main__":
    unittest.main()
