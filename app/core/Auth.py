from starlette.requests import Request

from app.core.context import REQUEST_CONTEXT

from fastapi import Header

from app.core.exc.exceptions import AuthException, PermissionException
from app.core.Response import Response
from app.curd.system.user import UserDao
from app.core.TokenAuth import UserToken
from app.core.Enums import DutyEnum


class Permission:

    def __init__(self, duty: int = DutyEnum.member.value):
        self.duty = duty

    async def __call__(self, token: str = Header(None)):
        print("权限认证开始")
        if not token:
            raise AuthException()
        try:
            user_info = UserToken.parse_token(token)
            if user_info.get("data_permission", 0) < self.duty:
                raise PermissionException()
            user = await UserDao.get_user_by_id(user_info['id'])
            if user is None:
                raise Exception("用户不存在")
            user_info = Response.model_to_dict(user, "password")
        except PermissionException as e:
            raise e
        except Exception as e:
            raise AuthException()
        return user_info


async def request_context(request: Request):
    """ 保存当前request对象到上下文中 """
    REQUEST_CONTEXT.set(request)
