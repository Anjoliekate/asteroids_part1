"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import movable

class TestMovableMove( unittest.TestCase ):

    def setUp( self ):
        return

    def tearDown( self ):
        return

    def test001_movableMovesPositive( self ):
        # setup
        x = 100
        y = 200
        dx = 1.5
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test002_movableMovesNegative( self ):
        # setup
        x = 100
        y = 200
        dx = -1.5
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test003_movableMovesPositiveNegative( self ):
        # setup
        x = 100
        y = 200
        dx = 1.5
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test004_movableMovesNegativePositive( self ):
        # setup
        x = 100
        y = 200
        dx = -1.5
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test010_movableMoveWrapsLeft( self ):
        # setup
        x = 1
        y = 200
        dx = -3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = world_width - 0.5
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test011_movableMoveWrapsRight( self ):
        # setup
        x = 599
        y = 200
        dx = 3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = 0.5
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test012_movableMoveWrapsTop( self ):
        # setup
        x = 200
        y = 1
        dx = -3.0
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = world_height - 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test013_movableMoveWrapsBottom( self ):
        # setup
        x = 200
        y = 399
        dx = 3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return


    def test014_movableMoveWrapsTopLeft( self ):
        # setup
        x = 1
        y = 1
        dx = -3.0
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = world_width - 0.5
        expected_y = world_height - 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test015_movableMoveWrapsTopRight( self ):
        # setup
        x = 599
        y = 1
        dx = 3.0
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = 0.5
        expected_y = world_height - 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return


    def test016_movableMoveWrapsBottomRight( self ):
        # setup
        x = 599
        y = 399
        dx = 3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = 0.5
        expected_y = 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test017_movableMoveWrapsBottomLeft( self ):
        # setup
        x = 1
        y = 399
        dx = -3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = world_width - 0.5
        expected_y = 0.25
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return


    def test020_movableMoveAllowsXEqual0( self ):
        # setup
        x = 0.5
        y = 200
        dx = -1.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = 0.0
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test021_movableMoveDoesNotAllowXEqualWorldWidth( self ):
        # setup
        x = 599.5
        y = 200
        dx = 1.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = 0.0
        expected_y = y + dt * dy
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return

    def test022_movableMoveAllowsYEqual0( self ):
        # setup
        x = 200
        y = 1.25
        dx = -3.0
        dy = -2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = 0.0
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return


    def test023_movableMoveDoesNotAllowYEqualWorldHeight( self ):
        # setup
        x = 200
        y = 398.75
        dx = -3.0
        dy = 2.5
        world_width = 600
        world_height = 400
        obj = movable.Movable( x, y, dx, dy, world_width, world_height )

        # stimulus
        dt = 0.5
        expected_x = x + dt * dx
        expected_y = 0.0
        expected_dx = dx
        expected_dy = dy
        expected_world_width = world_width
        expected_world_height = world_height
        obj.move( dt )

        # verification
        self.assertAlmostEqual( obj.getX( ), expected_x )
        self.assertAlmostEqual( obj.getY( ), expected_y )
        self.assertEqual( obj.getDX( ), expected_dx )
        self.assertEqual( obj.getDY( ), expected_dy )
        self.assertEqual( obj.getWorldWidth( ), expected_world_width )
        self.assertEqual( obj.getWorldHeight( ), expected_world_height )
        return


def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestMovableMove )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
