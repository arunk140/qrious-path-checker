import run
import unittest

class TestRun(unittest.TestCase):
    def test_findStartAndEndCoords(self):
        self.assertEqual(run.findStartAndEndCoords([['s', 'e']]), ((0, 0), (0, 1)))

    def test_getMazeSymbol(self):
        self.assertEqual(run.getMazeSymbol([['s', 'e']], (0, 0)), 's')
        self.assertEqual(run.getMazeSymbol([['s', 'e']], (0, 1)), 'e')

    def test_splitAndTrimMaze(self):
        self.assertEqual(run.splitAndTrimMaze('s..\n..e'), [['s', '.', '.'], ['.', '.', 'e']])
        self.assertEqual(run.splitAndTrimMaze('.....'), [['.', '.', '.', '.', '.']])

    def test_findNextPath(self):
        self.assertEqual(run.findNextPath([['s', 'e']], (0, 0), (0, 1), []), [(0, 0), (0, 1)])
        self.assertEqual(run.findNextPath([['s', '.', '.', 'e']], (0, 0), (0, 3), []), [(0, 0), (0, 1), (0, 2), (0, 3)])

    def test_solvable(self):
        self.assertTrue(run.solvable('s e'))
        self.assertFalse(run.solvable('s x e'))
    
if __name__ == '__main__':
    unittest.main()