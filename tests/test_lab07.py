"""Tests for Lab 07 (transit.py).

There are no example tests this time: the whole suite is yours.
Before you implement each function in transit.py, work here first.
For every function below: note one ordinary case and one boundary
or edge case as comments, write one test per case (a single assert
statement), run the tests in PyCharm to watch them fail, and only
then implement the function until your tests pass.

One caution: append_stop changes the network it receives, so tests for
it must build small networks of their own instead of using NETWORK.
"""

from transit import (
    NETWORK,
    routes_by_stop,
    requires_transfer,
    route_backup,
    append_stop,
    are_aliases,
    fare,
    fare_matches,
)


# ----------------------------------------------------------------------------
# Grouping the network: routes_by_stop(network)
# Returns a dict mapping each stop name to the list of route names that
# serve it, in the order those routes appear in the network.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Grouping the network: requires_transfer(network, stop_one, stop_two)
# Returns True when no single route serves both stops, or when either
# stop is not in the network.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Protecting and editing routes: route_backup(network, route)
# Returns a copy of the route's list of stops that can be modified
# without affecting the network.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Protecting and editing routes: append_stop(network, route, stop)
# Adds stop to the end of the route's list in the network itself and
# returns None. Build your own small networks for these tests.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Protecting and editing routes: are_aliases(network, route_one, route_two)
# Returns True only when both route names refer to the same list object.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Pricing a ride: fare(network, route)
# Returns the fare to ride the route, rounded to two decimal places.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Pricing a ride: fare_matches(network, route, paid)
# Returns True when paid is within one cent of the route's
# unrounded fare.
# Write your tests below.
# ----------------------------------------------------------------------------
