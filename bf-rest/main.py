from typing import Sequence
from starlette.applications import Starlette
from starlette.routing import BaseRoute
from starlette.middleware import Middleware


class BackframeApp:
    def __init__(self) -> None:
        debug = self.is_debug()
        routes = self.get_routes()
        middleware = self.get_middleware()

        self._app = Starlette(
            routes,
            middleware,
            debug,
            exception_handlers=[],
        )

    def get_routes() -> Sequence[BaseRoute]:
        """ 
        Loads all routes configured for the app and returns them
        """
        return []

    def get_middleware() -> Sequence[Middleware]:
        """
        Loads all configured middleware and initializes them
        """
        return []

    def is_debug() -> bool:
        """
        Loads the environment variables checking whether debug mode is on or off
        """
        return True



