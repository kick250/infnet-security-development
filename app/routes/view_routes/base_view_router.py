from routes.base_router import BaseRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


class BaseViewRouter(BaseRouter):
    def __init__(self, prefix, tags):
        super().__init__(f"/view{prefix}", tags, default_response_class=HTMLResponse)
        self.__prefix = prefix
        self.__templates = Jinja2Templates(directory=f"templates")

    def _add_route(self, path, handler_method, methods, response_class=HTMLResponse):
        self._add_api_route(path, handler_method, methods, response_class=response_class)

    def _render_template(self, request, name, context={}):
        template = f"{self.__prefix}/{name}"
        return self.__templates.TemplateResponse(
            request=request, name=template, context=context
        )