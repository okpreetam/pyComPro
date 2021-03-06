import unittest
import l444


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l444.Solution()
    
    def test_solution(self):
        grid = [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        got = self.s.minPathSum(grid)
        self.assertEqual(got, 7)

        grid = [
          [1,2,5],
          [3,2,1]
        ]
        got = self.s.minPathSum(grid)
        self.assertEqual(got, 6)
        grid = [
          [1,2,3],
          [3,5,6]
        ]
        got = self.s.minPathSum(grid)
        self.assertEqual(got, 12)
if __name__ == "__main__":
    unittest.main()
