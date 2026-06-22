# test_ledgeredge.py
"""
Tests for LedgerEdge module.
"""

import unittest
from ledgeredge import LedgerEdge

class TestLedgerEdge(unittest.TestCase):
    """Test cases for LedgerEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerEdge()
        self.assertIsInstance(instance, LedgerEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
