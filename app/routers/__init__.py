from app.routers.system import user, project
from collections import namedtuple

Router = namedtuple('router', ['module', 'prefix', 'tags'])

router_list = [
    Router(module=user.router, prefix='/sys', tags=["用户模块"]),
    Router(module=project.router, prefix='/sys', tags=["项目管理"]),
    # Router(module=cases.router, prefix='/api/cases', tags=["用例模块"]),
    # Router(module=data.router, prefix='/api/data', tags=["数据统计"])
]
