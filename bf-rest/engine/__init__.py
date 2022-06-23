# When a request is incoming, it is matched to a ROUTE
# If no route found, return default error or custom-defined one
# If route found, the request is passed through any middleware and eventually mapped to controller
# The controller interfaces with the model to get any requested data(depending on default controller behaviour)
# The model talks to database and returns values