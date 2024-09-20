from litestar import Litestar, Request, Response, Router
from litestar.config.cors import CORSConfig
from litestar.exceptions import HTTPException
from litestar_vite import ViteConfig, VitePlugin
from litestar.config.csrf import CSRFConfig
from litestar.config.compression import CompressionConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogPlugin
from litestar.logging.config import StructLoggingConfig
from litestar.plugins.structlog import StructlogConfig

from .config import Env
from .modules.home import home_router

logging_middleware_config: LoggingMiddlewareConfig = LoggingMiddlewareConfig(
    request_headers_to_obfuscate={"Authorization"},
    request_cookies_to_obfuscate={"csrftoken"},
    response_cookies_to_obfuscate={"csrftoken"},
    response_headers_to_obfuscate={"x-csrftoken"},
    logger_name="z_dashboard",
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


struct_log_cfg = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="always",
    ),
    middleware_logging_config=logging_middleware_config,
)

plugins: list = [
    VitePlugin(
        config=ViteConfig(
            template_dir="./templates/",
            use_server_lifespan=True,
            dev_mode=Env.DEV,
            is_react=True,
            run_command=["bun", "dev"],
            build_watch_command=["bun", "watch"],
            build_command=["bun", "build"],
            install_command=["bun", "i"],
        )
    ),
    StructlogPlugin(struct_log_cfg),
]

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

routers: list[Router] = [home_router]

app: Litestar = Litestar(
    debug=True,
    plugins=plugins,
    route_handlers=routers,
    exception_handlers={HTTPException: app_exception_handler},
    cors_config=cors_config,
    csrf_config=csrf_config,
    compression_config=compression_config,
)
