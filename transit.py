NETWORK = {
    "Expo Line": [
        "Waterfront",
        "Burrard",
        "Commercial",
        "Metrotown",
    ],
    "Millennium Line": [
        "Commercial",
        "Brentwood",
        "Holdom",
    ],
    "Canada Line": [
        "Waterfront",
        "Yaletown",
        "Broadway",
    ],
    "99 B-Line": [
        "Commercial",
        "Broadway",
        "UBC",
    ],
    "SeaBus": [
        "Waterfront",
        "Lonsdale",
    ],
}

FARE_PER_HOP = 0.35


def routes_by_stop(network):
    pass


def requires_transfer(network, stop_one, stop_two):
    pass


def route_backup(network, route):
    pass


def append_stop(network, route, stop):
    pass


def are_aliases(network, route_one, route_two):
    pass


def fare(network, route):
    pass


def fare_matches(network, route, paid):
    pass


def main():
    """
    Demonstrate the Metro Vancouver transit network.
    """
    print("=== Metro Vancouver Transit Network ===")


if __name__ == "__main__":
    main()
