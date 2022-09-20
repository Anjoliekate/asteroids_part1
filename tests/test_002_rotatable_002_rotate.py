"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import rotatable

class TestRotatableRotate( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 100
        self.expected_y = 200
        self.expected_dx = 1.5
        self.expected_dy = -2.5
        self.expected_rotation = 90
        self.expected_world_width = 600
        self.expected_world_height = 400

        self.constructed_obj = rotatable.Rotatable( self.expected_x, self.expected_y, self.expected_dx, self.expected_dy, self.expected_rotation, self.expected_world_width, self.expected_world_height )

        return

    def tearDown( self ):
        return

    def test001_rotatesPositive( self ):
        rotation = 17.5
        expected_rotation = self.expected_rotation + rotation
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return

    def test002_rotatesNegative( self ):
        rotation = -17.5
        expected_rotation = self.expected_rotation + rotation
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return

    def test003_rotatesPast360To0( self ):
        rotation = 271
        expected_rotation = 1
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return

    def test004_rotatesPast0To360( self ):
        rotation = -91
        expected_rotation = 359
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return

    def test005_rotateAllows0Degrees( self ):
        rotation = -90
        expected_rotation = 0
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return

    def test006_rotateDoesNotAllow360Degrees( self ):
        rotation = 270
        expected_rotation = 0
        self.constructed_obj.rotate( rotation )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestRotatableRotate )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
