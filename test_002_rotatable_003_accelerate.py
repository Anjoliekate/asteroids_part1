"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import rotatable

class TestRotatableAccelerate( unittest.TestCase ):

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

    def test001_splitsFirstQuadrant( self ):
        delta_velocity = 10.0
        rotation = 45.0
        expected_ddx = delta_velocity * math.sqrt( 2 ) / 2
        expected_ddy = delta_velocity * math.sqrt( 2 ) / 2
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test002_splitsSecondQuadrant( self ):
        delta_velocity = 10.0
        rotation = 120.0
        expected_ddx = - delta_velocity * 0.5
        expected_ddy = delta_velocity * math.sqrt( 3 ) / 2.0
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test003_splitsThirdQuadrant( self ):
        delta_velocity = 10.0
        rotation = 210.0
        expected_ddx = - delta_velocity * math.sqrt( 3 ) / 2.0
        expected_ddy = - delta_velocity * 0.5
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test004_splitsFourthQuadrant( self ):
        delta_velocity = 10.0
        rotation = 300.0
        expected_ddx =   delta_velocity * 0.5
        expected_ddy = - delta_velocity * math.sqrt( 3 ) / 2.0
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test005_splitsPositiveXAxis( self ):
        delta_velocity = 10.0
        rotation = 0.0
        expected_ddx =   delta_velocity
        expected_ddy =   0.0
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test006_splitsNegativeXAxis( self ):
        delta_velocity = 10.0
        rotation = 180.0
        expected_ddx = - delta_velocity
        expected_ddy =   0.0
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test007_splitsPositiveYAxis( self ):
        delta_velocity = 10.0
        rotation = 90.0
        expected_ddx =   0.0
        expected_ddy =   delta_velocity
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return

    def test008_splitsNegativeYAxis( self ):
        delta_velocity = 10.0
        rotation = 270.0
        expected_ddx =   0.0
        expected_ddy = - delta_velocity
        ( ddx, ddy ) = self.constructed_obj.splitDeltaVIntoXAndY( rotation, delta_velocity )
        self.assertAlmostEqual( ddx, expected_ddx )
        self.assertAlmostEqual( ddy, expected_ddy )
        return


    def test011_acceleratesFirstQuadrant( self ):
        delta_velocity = 10.0
        rotation = 45.0
        expected_dx = self.expected_dx + delta_velocity * math.sqrt( 2 ) / 2
        expected_dy = self.expected_dy + delta_velocity * math.sqrt( 2 ) / 2
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test012_acceleratesSecondQuadrant( self ):
        delta_velocity = 10.0
        rotation = 120.0
        expected_dx = self.expected_dx - delta_velocity * 0.5
        expected_dy = self.expected_dy + delta_velocity * math.sqrt( 3 ) / 2.0
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test013_acceleratesThirdQuadrant( self ):
        delta_velocity = 10.0
        rotation = 210.0
        expected_dx = self.expected_dx - delta_velocity * math.sqrt( 3 ) / 2.0
        expected_dy = self.expected_dy - delta_velocity * 0.5
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test014_acceleratesFourthQuadrant( self ):
        delta_velocity = 10.0
        rotation = 300.0
        expected_dx =  self.expected_dx +  delta_velocity * 0.5
        expected_dy = self.expected_dy - delta_velocity * math.sqrt( 3 ) / 2.0
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test015_acceleratesPositiveXAxis( self ):
        delta_velocity = 10.0
        rotation = 0.0
        expected_dx = self.expected_dx +   delta_velocity
        expected_dy = self.expected_dy +   0.0
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test016_acceleratesNegativeXAxis( self ):
        delta_velocity = 10.0
        rotation = 180.0
        expected_dx = self.expected_dx - delta_velocity
        expected_dy = self.expected_dy +   0.0
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test017_acceleratesPositiveYAxis( self ):
        delta_velocity = 10.0
        rotation = 90.0
        expected_dx =  self.expected_dx +  0.0
        expected_dy =  self.expected_dy +  delta_velocity
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return

    def test018_acceleratesNegativeYAxis( self ):
        delta_velocity = 10.0
        rotation = 270.0
        expected_dx = self.expected_dx +   0.0
        expected_dy = self.expected_dy - delta_velocity
        self.constructed_obj.rotate( rotation - self.constructed_obj.getRotation( ) )
        self.constructed_obj.accelerate( delta_velocity )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        return



def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestRotatableAccelerate )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )