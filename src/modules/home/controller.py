from litestar import Controller, get, MediaType
from litestar.response import Template


class HomeController(Controller):
    path = "/"

    opt = {"exclude_from_auth": True}
    include_in_schema = False

    @get(path="/", sync_to_thread=False, media_type=MediaType.HTML)
    def index(self) -> Template:
        return Template(template_name="index.j2")
