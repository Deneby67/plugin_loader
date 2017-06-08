def parametrized(route_name):
    def layer(func):
        func.route_name = route_name
        return func
    return layer
