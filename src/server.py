from pathlib import Path

from litestar import Litestar, Request, Response
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.template.config import TemplateConfig
from litestar_vite import ViteConfig, VitePlugin
from litestar.config.csrf import CSRFConfig
from litestar.config.compression import CompressionConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogPlugin

from .routes import mainController

logging_middleware_config = LoggingMiddlewareConfig(
    request_headers_to_obfuscate={"Authorization"},
    response_headers_to_obfuscate={"x-csrftoken"},
    logger_name="[Z Dashboard]",
)


def app_exception_handler(request: Request, exc: HTTPException) -> Response:
    return Response(
        content={
            "error": "server error",
            "path": request.url.path,
            "detail": exc.detail,
            "status_code": exc.status_code,
        },
        status_code=500,
    )


app: Litestar = Litestar(
    plugins=[
        VitePlugin(config=ViteConfig(template_dir="./templates/")),
        StructlogPlugin(),
    ],
    route_handlers=[mainController],
    template_config=TemplateConfig(
        directory=Path("./templates"),
        engine=JinjaTemplateEngine,
    ),
    exception_handlers={HTTPException: app_exception_handler},
    cors_config=CORSConfig(
        allow_origins=["*"],
        max_age=3600,
        allow_credentials=True,
        allow_headers=["*"],
    ),
    csrf_config=CSRFConfig(secret="qsd"),
    compression_config=CompressionConfig(backend="gzip", gzip_compress_level=9),
    logging_config=logging_middleware_config,
    middleware=[logging_middleware_config.middleware],
)
