"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import asteroids, ship, rock

class TestAsteroidsShipActions( unittest.TestCase ):

    def setUp( self ):
        self.expected_rock_count = 10
        self.expected_object_count = 11
        self.expected_world_width = 800
        self.expected_world_height = 600
        self.constructed_obj = asteroids.Asteroids( self.expected_world_width, self.expected_world_height )

        return

    def tearDown( self ):
        return

    def test001_ShipTurnsLeft( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 13.1
        expected_rotation = original_rotation - rotate_amount
        if expected_rotation < 0.0:
            expected_rotation += 360.0

        self.constructed_obj.turnShipLeft( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return

    def test002_ShipTurnsLeftALot( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 359.0
        expected_rotation = original_rotation - rotate_amount
        if expected_rotation < 0.0:
            expected_rotation += 360.0

        self.constructed_obj.turnShipLeft( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return


    def test003_ShipTurnsLeftALittle( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 0.01
        expected_rotation = original_rotation - rotate_amount
        if expected_rotation < 0.0:
            expected_rotation += 360.0

        self.constructed_obj.turnShipLeft( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return

    def test004_ShipTurnsRight( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 13.1
        expected_rotation = original_rotation + rotate_amount
        if expected_rotation >= 360.0:
            expected_rotation -= 360.0

        self.constructed_obj.turnShipRight( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return

    def test005_ShipTurnsRightALot( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 359.0
        expected_rotation = original_rotation + rotate_amount
        if expected_rotation >= 360.0:
            expected_rotation -= 360.0

        self.constructed_obj.turnShipRight( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return


    def test006_ShipTurnsRightALittle( self ):
        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        rotate_amount = 0.01
        expected_rotation = original_rotation + rotate_amount
        if expected_rotation >= 360.0:
            expected_rotation -= 360.0

        self.constructed_obj.turnShipRight( rotate_amount )

        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )
        return

    def test011_ShipAccelerates( self ):
        # setup
        original_dx = self.constructed_obj.getShip( ).getDX( )
        original_dy = self.constructed_obj.getShip( ).getDY( )

        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        expected_rotation = 315.0
        rotate_amount = expected_rotation - original_rotation
        if rotate_amount > 0:
            self.constructed_obj.turnShipRight( rotate_amount )
        else:
            self.constructed_obj.turnShipLeft( -rotate_amount )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )

        delta_velocity = 10.0
        expected_dx = original_dx + math.sqrt( 2 ) * delta_velocity / 2.0
        expected_dy = original_dy - math.sqrt( 2 ) * delta_velocity / 2.0

        # stimulus
        self.constructed_obj.accelerateShip( delta_velocity )

        # check
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDY( ), expected_dy )
        return

    def test012_ShipAcceleratesALot( self ):
        # setup
        original_dx = self.constructed_obj.getShip( ).getDX( )
        original_dy = self.constructed_obj.getShip( ).getDY( )

        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        expected_rotation = 135.0
        rotate_amount = expected_rotation - original_rotation
        if rotate_amount > 0:
            self.constructed_obj.turnShipRight( rotate_amount )
        else:
            self.constructed_obj.turnShipLeft( -rotate_amount )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )

        delta_velocity = 60.0
        expected_dx = original_dx - math.sqrt( 2 ) * delta_velocity / 2.0
        expected_dy = original_dy + math.sqrt( 2 ) * delta_velocity / 2.0

        # stimulus
        self.constructed_obj.accelerateShip( delta_velocity )

        # check
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDY( ), expected_dy )
        return


    def test013_ShipAcceleratesALittle( self ):
        # setup
        original_dx = self.constructed_obj.getShip( ).getDX( )
        original_dy = self.constructed_obj.getShip( ).getDY( )

        original_rotation = self.constructed_obj.getShip( ).getRotation( )
        expected_rotation = 225.0
        rotate_amount = expected_rotation - original_rotation
        if rotate_amount > 0:
            self.constructed_obj.turnShipRight( rotate_amount )
        else:
            self.constructed_obj.turnShipLeft( -rotate_amount )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getRotation( ), expected_rotation )

        delta_velocity = 0.1
        expected_dx = original_dx - math.sqrt( 2 ) * delta_velocity / 2.0
        expected_dy = original_dy - math.sqrt( 2 ) * delta_velocity / 2.0

        # stimulus
        self.constructed_obj.accelerateShip( delta_velocity )

        # check
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getShip( ).getDY( ), expected_dy )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestAsteroidsShipActions )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
