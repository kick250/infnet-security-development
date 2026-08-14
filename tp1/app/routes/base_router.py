from fastapi import APIRouter, HTTPException

class BaseRouter:
    def __init__(self, prefix, tags):
        self.__router = APIRouter(prefix=prefix, tags=tags)

    @classmethod
    def get_router(cls):
        return cls().__router

    def _add_api_route(self, path, handler_method, methods):
        self.__router.add_api_route(path, handler_method, methods=methods)

    def _render_http_exception(self, status_code, detail):
        raise HTTPException(status_code=status_code, detail=detail)
