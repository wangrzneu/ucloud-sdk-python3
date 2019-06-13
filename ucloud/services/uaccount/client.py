import typing

from ucloud.core.client import Client
from ucloud.core.transport import Transport
from ucloud.services.uaccount.schemas import apis


class UAccountClient(Client):
    def __init__(self, config: dict, transport: typing.Optional[Transport] = None):
        super(UAccountClient, self).__init__(config, transport)

    def get_user_info(self, req: dict = None) -> dict:
        """ GetUserInfo - 获取用户信息

        """
        req = apis.GetUserInfoRequestSchema().dumps(req or {})
        resp = self.invoke("GetUserInfo", req)
        return apis.GetUserInfoResponseSchema().loads(resp)

    def modify_project(self, req: dict = None) -> dict:
        """ ModifyProject - 修改项目

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        :param ProjectName: (Required) 新的项目名称
        """
        req = apis.ModifyProjectRequestSchema().dumps(req or {})
        resp = self.invoke("ModifyProject", req)
        return apis.ModifyProjectResponseSchema().loads(resp)

    def terminate_project(self, req: dict = None) -> dict:
        """ TerminateProject - 删除项目

        :param ProjectId: (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考[GetProjectList接口](../summary/get_project_list.html)
        """
        req = apis.TerminateProjectRequestSchema().dumps(req or {})
        resp = self.invoke("TerminateProject", req)
        return apis.TerminateProjectResponseSchema().loads(resp)

    def create_project(self, req: dict = None) -> dict:
        """ CreateProject - 创建项目

        :param ProjectName: (Required) 项目名称
        """
        req = apis.CreateProjectRequestSchema().dumps(req or {})
        resp = self.invoke("CreateProject", req)
        return apis.CreateProjectResponseSchema().loads(resp)

    def get_project_list(self, req: dict = None) -> dict:
        """ GetProjectList - 获取项目列表

        :param IsFinance: (Optional) 是否是财务账号(Yes: 是, No: 否)
        """
        req = apis.GetProjectListRequestSchema().dumps(req or {})
        resp = self.invoke("GetProjectList", req)
        return apis.GetProjectListResponseSchema().loads(resp)

    def get_region(self, req: dict = None) -> dict:
        """ GetRegion - 获取用户在各数据中心的权限等信息

        """
        req = apis.GetRegionRequestSchema().dumps(req or {})
        resp = self.invoke("GetRegion", req)
        return apis.GetRegionResponseSchema().loads(resp)
