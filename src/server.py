from pathlib import Path

from litestar import Litestar, Request, Response, Router
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

from src.utils.env import Env

from .routes import mainController

logging_middleware_config: LoggingMiddlewareConfig = LoggingMiddlewareConfig(
    request_headers_to_obfuscate={"Authorization"},
    request_cookies_to_obfuscate={"csrftoken"},
    response_cookies_to_obfuscate={"csrftoken"},
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


plugins: list = [
    VitePlugin(
        config=ViteConfig(
            template_dir="./templates/",
            use_server_lifespan=True,
            dev_mode=Env().DEV,
        )
    ),
    StructlogPlugin(),
]

# jinja_config: TemplateConfig = TemplateConfig(
#     directory=Path("./templates"),
#     engine=JinjaTemplateEngine,
# )

cors_config: CORSConfig = CORSConfig(
    allow_origins=["*"],
    max_age=3600,
    allow_credentials=True,
    allow_headers=["*"],
)

compression_config: CompressionConfig = CompressionConfig(
    backend="gzip", gzip_compress_level=9
)

csrf_config: CSRFConfig = CSRFConfig(secret=Env.CSRF_KEY)

routers: list[Router] = [mainController]

app: Litestar = Litestar(
    debug=Env.DEV,
    plugins=plugins,
    route_handlers=routers,
    # template_config=jinja_config,
    exception_handlers={HTTPException: app_exception_handler},
    cors_config=cors_config,
    csrf_config=csrf_config,
    compression_config=compression_config,
    logging_config=logging_middleware_config,
    middleware=[logging_middleware_config.middleware],
)
