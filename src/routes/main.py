from litestar import Router
from pathlib import Path
from litestar import Request, Response

from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.exceptions import ValidationException

from ..controllers import MainController


def router_handler_exception_handler(
    request: Request, exc: ValidationException
) -> Response:
    return Response(
        content={"error": "validation error", "path": request.url.path},
        status_code=400,
    )


mainController: Router = Router(
    path="/v1",
    route_handlers=[MainController],
    exception_handlers={ValidationException: router_handler_exception_handler},
)
