"""
Kevin Loaeza Luna
CSCI 332 Spring 2025
Programming Assignment #10
I acknowledge that I have worked on this assignment independently, except where
explicitly
noted and referenced. Any collaboration or use of external resources has been
properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by
the
university's academic integrity policy. I understand the importance the
consequences of
plagiarism.
"""

import unittest
from main import convex_hull_jarvis


class TestMathFunctions(unittest.TestCase):
    
    def test_example_from_prompt(self):
        points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (3, 0), (3, 3), (0, 3)])

    def test_square_with_inner_points(self):
        points = [(0, 0), (5, 0), (5, 5), (0, 5), (3, 3), (1, 3)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (5, 0), (5, 5), (0, 5)])

    def test_duplicates(self):
        points = [(0, 0), (0, 0), (1, 1), (1, 1), (1, 0), (1, 0), (0, 1), (0, 1)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (0, 0), (1, 0), (1, 0), (1, 1), (1, 1), (0, 1), (0, 1)])

    def test_all_collinear(self):
        points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def test_two_points(self):
        points = [(0, 0), (4, 4)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (4, 4)])       

    def test_single_point(self):
        points = [(0, 0)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0)])

    def test_triangle(self):
        points = [(0, 0), (0, 6), (3, 3)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (3, 3), (0, 6)])   

    def test_collinear_on_edges(self):
        points = [(0, 0), (0, 2), (2, 2), (2, 0), (1, 0)]
        self.assertEqual(convex_hull_jarvis(points), [(0, 0), (2, 0), (2, 2), (0, 2)])

if __name__ == "__main__":
    unittest.main()