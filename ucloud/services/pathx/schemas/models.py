""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class GlobalSSHAreaSchema(schema.ResponseSchema):
    """ GlobalSSHArea - GlobalSSH覆盖地区,包括关联的UCloud机房信息
    """

    fields = {
        "Area": fields.Str(required=True, load_from="Area"),
        "AreaCode": fields.Str(required=True, load_from="AreaCode"),
        "RegionSet": fields.List(fields.Str()),
    }


class GlobalSSHInfoSchema(schema.ResponseSchema):
    """ GlobalSSHInfo - GlobalSSH实例信息
    """

    fields = {
        "AcceleratingDomain": fields.Str(
            required=True, load_from="AcceleratingDomain"
        ),
        "Area": fields.Str(required=True, load_from="Area"),
        "ChargeType": fields.Str(required=True, load_from="ChargeType"),
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ExpireTime": fields.Int(required=True, load_from="ExpireTime"),
        "InstanceId": fields.Str(required=True, load_from="InstanceId"),
        "Port": fields.Int(required=True, load_from="Port"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "TargetIP": fields.Str(required=True, load_from="TargetIP"),
    }