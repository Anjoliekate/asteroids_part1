"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import asteroids, ship, rock

class TestAsteroidsEvolve( unittest.TestCase ):

    def setUp( self ):
        self.expected_rock_count = 10
        self.expected_object_count = 11
        self.expected_world_width = 800
        self.expected_world_height = 600
        self.constructed_obj = asteroids.Asteroids( self.expected_world_width, self.expected_world_height )

        return

    def getAllStats( self ):
        s = self.constructed_obj.getShip( )
        ship_stats = s.getX( ), s.getY( ), s.getDX( ), s.getDY( ), s.getRotation( )

        rock_stats = [ ]
        for r in self.constructed_obj.getRocks( ):
            stats = r.getX( ), r.getY( ), r.getDX( ), r.getDY( ), r.getRotation( ), r.getSpinRate( )
            rock_stats.append( stats )

        return ship_stats, rock_stats


    def tearDown( self ):
        return

    def test001_ShipMoves( self ):
        # setup
        dt = 0.1
        self.constructed_obj.turnShipLeft( 15.0 )
        self.constructed_obj.accelerateShip( 7.0 )
        original_stats = self.getAllStats( )

        # stimulus
        self.constructed_obj.evolve( dt )

        # check
        evolved_stats = self.getAllStats( )

        original_ship_x, original_ship_y, original_ship_dx, original_ship_dy, original_ship_rotation = original_stats[ 0 ]
        ship_x, ship_y, ship_dx, ship_dy, ship_rotation = evolved_stats[ 0 ]

        self.assertNotEqual( ship_x, original_ship_x )
        self.assertNotEqual( ship_y, original_ship_y )
        self.assertEqual( ship_dx, original_ship_dx )
        self.assertEqual( ship_dy, original_ship_dy )
        self.assertEqual( ship_rotation, original_ship_rotation )

        return

    def test002_RocksMoveAndRotate( self ):
        # setup
        dt = 0.1
        original_stats = self.getAllStats( )

        # stimulus
        self.constructed_obj.evolve( dt )

        # check
        evolved_stats = self.getAllStats( )

        for i in range( len( self.constructed_obj.getRocks( ) ) ):

            original_rock_x, original_rock_y, original_rock_dx, original_rock_dy, original_rock_rotation, original_rock_spin_rate = original_stats[ 1 ][ i ]
            rock_x, rock_y, rock_dx, rock_dy, rock_rotation, rock_spin_rate = evolved_stats[ 1 ][ i ]

            self.assertNotEqual( rock_x, original_rock_x )
            self.assertNotEqual( rock_y, original_rock_y )
            self.assertEqual( rock_dx, original_rock_dx )
            self.assertEqual( rock_dy, original_rock_dy )
            self.assertNotEqual( rock_rotation, original_rock_rotation )
            self.assertEqual( rock_spin_rate, original_rock_spin_rate )

        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestAsteroidsEvolve )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )