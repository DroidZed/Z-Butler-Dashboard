from litestar import Litestar, Request, Response, Router
from litestar.config.cors import CORSConfig
from litestar.exceptions import HTTPException
from litestar_vite import ViteConfig, VitePlugin
from litestar.config.csrf import CSRFConfig
from litestar.logging import LoggingConfig
from litestar.config.compression import CompressionConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogPlugin

from .config import Env
from .modules.home import home_router

logging_middleware_config: LoggingMiddlewareConfig = LoggingMiddlewareConfig(
    # request_headers_to_obfuscate={"Authorization"},
    # request_cookies_to_obfuscate={"csrftoken"},
    # response_cookies_to_obfuscate={"csrftoken"},
    # response_headers_to_obfuscate={"x-csrftoken"},
    logger_name="z_dashboard",
)

logging_cfg = LoggingConfig()


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


"""
Default port to use for Vite server.
    run_command: list[str] = field(default_factory=lambda: ["npm", "run", "dev"])
    Default command to use for running Vite.
    build_watch_command: list[str] = field(default_factory=lambda: ["npm", "run", "watch"])
    Default command to use for dev building with Vite.
    build_command: list[str] = field(default_factory=lambda: ["npm", "run", "build"])
    Default command to use for building with Vite.
    install_command: list[str] = field(default_factory=lambda: ["npm", "install"])
"""

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
    StructlogPlugin(),
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
    logging_config=logging_cfg,
    middleware=[logging_middleware_config.middleware],
)
