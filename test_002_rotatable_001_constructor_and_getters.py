"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import rotatable

class TestRotatableConstructorAndGetters( unittest.TestCase ):

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

    def test001_ConstructorSetsX( self ):
        self.assertEqual( self.constructed_obj.getX( ), self.expected_x )
        return

    def test002_ConstructorSetsY( self ):
        self.assertEqual( self.constructed_obj.getY( ), self.expected_y )
        return

    def test003_ConstructorSetsDX( self ):
        self.assertEqual( self.constructed_obj.getDX( ), self.expected_dx )
        return

    def test004_ConstructorSetsDY( self ):
        self.assertEqual( self.constructed_obj.getDY( ), self.expected_dy )
        return

    def test005_ConstructorSetsWorldWidth( self ):
        self.assertEqual( self.constructed_obj.getWorldWidth( ), self.expected_world_width )
        return

    def test006_ConstructorSetsWorldHeight( self ):
        self.assertEqual( self.constructed_obj.getWorldHeight( ), self.expected_world_height )
        return

    def test007_ConstructorSetsRotation( self ):
        self.assertEqual( self.constructed_obj.getRotation( ), self.expected_rotation )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestRotatableConstructorAndGetters )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )