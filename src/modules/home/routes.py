from litestar import Router
from litestar import Request, Response

from litestar.exceptions import ValidationException

from .controller import HomeController


def router_handler_exception_handler(
    request: Request, exc: ValidationException
) -> Response:
    request.logger.error(1, f"{exc.msg=}")
    return Response(
        content={"error": "validation error", "path": request.url.path},
        status_code=400,
    )


home_router: Router = Router(
    path="/",
    route_handlers=[HomeController],
    exception_handlers={ValidationException: router_handler_exception_handler},
)
