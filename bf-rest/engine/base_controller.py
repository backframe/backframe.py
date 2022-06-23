
class RestController:
    def __init__(self, name, fields, sub_resources) -> None:
        pass

    # GET /resource(s) -> Get all
    def index(self):
        pass

    # POST /resource(s) -> Add one
    def create(self):
        pass

    # GET /resource(s)/:id
    def show(self):
        pass

    # PUT,PATCH /resource(s)
    def update(self):
        pass

    # DELETE
    def delete(self):
        pass


# File structure
# server.py
# routes.py
# Specfile
# models/
#    |_ user.schema
#    |_ book.schema
# migrations/
# resources/
#    |_ user/
#    |    |_ user.controller.py
#    |    |_ user.model.py
#    |    |_ user.test.py
#    |_ book/
#         |_ book.controller.py
#         |_ book.model.py
#         |_ book.test.py



# Example structure of a controller
class UserController(RestController):
    pass

# everything would work out of the box, you would only need to touch the controller if you need to modify its default behaviour or extend it
# it would need to have the following methods:
# /api/v1/users/#index
# /api/v1/users/id/#show
# /api/v1/users/id/#edit
# /api/v1/users/id/#delete
# /api/v1/users/id/#put
# the above methods built by the framework by default, then after parsing the Specfile, add the rest
# /api/v1/users/name/{name}#show_by_name
# /api/v1/users/email/{email}#show_by_email
# /api/v1/users/orders/id#show_user_orders

# @controller("User")
# class UserController(BaseController):
#   def __init__(self, *args, **kwargs) -> None:
#       super().__init__(args, kwargs)


# routes.py ->
# routes = [
#   "/users", "UserController"
# ]