// -*- C++ -*-
//
// michael a.g. aïvázis
// orthologue
// (c) 1998-2016 all rights reserved
//

// configuration
#include <portinfo>
// externals
#include <iostream>
#include <pyre/journal.h>
#include <pyre/memory.h>
#include <pyre/geometry.h>

// main
int main() {
    // journal control
    // pyre::journal::debug_t debug("pyre.memory.direct");
    // debug.activate();

    // space
    typedef double cell_t;
    // shape
    typedef std::array<int, 3> rep_t;
    typedef pyre::geometry::index_t<rep_t> index_t;
    typedef pyre::geometry::order_t<rep_t> order_t;
    typedef pyre::geometry::tile_t<index_t, order_t> tile_t;
    // storage
    typedef pyre::memory::direct_t direct_t;
    // grid
    typedef pyre::geometry::grid_t<cell_t, tile_t, direct_t> grid_t;

    // make a channel
    pyre::journal::debug_t channel("pyre.geometry");

    // make a order
    tile_t::order_type order {2, 1, 0};
    // make a shape
    tile_t::index_type shape {6, 4, 2};
    // make a tile
    tile_t tile {shape, order};

    // the name of the file
    pyre::memory::uri_t name {"grid.dat"};
    // make it
    direct_t::create(name, sizeof(cell_t) * tile.size());
    // map it
    pyre::memory::direct_t storage {name, true};
    // make the grid
    grid_t grid {tile, std::move(storage)};

    // show me
    channel
        << pyre::journal::at(__HERE__)
        << grid[{1,1,1}]
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file