from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import Depends
from auth import AuthService

class BaseRouter:
    def __init__(self, prefix, tags, default_response_class=JSONResponse):
        self.__router = APIRouter(prefix=prefix, tags=tags, default_response_class=default_response_class)

    @classmethod
    def get_router(cls):
        return cls().__router

    def _add_api_route(self, path, handler_method, methods, response_class=JSONResponse, authenticated=True):
        self.__router.add_api_route(
            path,
            handler_method,
            methods=methods,
            response_class=response_class,
            dependencies=self.__get_dependencies(authenticated)
        )

    def _render_http_exception(self, status_code, detail):
        raise HTTPException(status_code=status_code, detail=detail)

    def __get_dependencies(self, authenticated=True):
        if authenticated:
            return [Depends(AuthService.get_active_user)]

        return None