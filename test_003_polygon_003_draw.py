"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import polygon

class TestPolygonDraw( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 100
        self.expected_y = 200
        self.expected_dx = 1.5
        self.expected_dy = -2.5
        self.expected_rotation = 90
        self.expected_world_width = 600
        self.expected_world_height = 400

        self.constructed_obj = polygon.Polygon( self.expected_x, self.expected_y, self.expected_dx, self.expected_dy, self.expected_rotation, self.expected_world_width, self.expected_world_height )

        return

    def tearDown( self ):
        return

    def test001_polygonHasDraw( self ):
        self.assertEqual( hasattr( self.constructed_obj, 'draw' ), True )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestPolygonDraw )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
