# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDbSecurityGroupResult',
    'AwaitableGetDbSecurityGroupResult',
    'get_db_security_group',
    'get_db_security_group_output',
]

@pulumi.output_type
class GetDbSecurityGroupResult:
    def __init__(__self__, db_security_group_ingress=None, id=None, tags=None):
        if db_security_group_ingress and not isinstance(db_security_group_ingress, list):
            raise TypeError("Expected argument 'db_security_group_ingress' to be a list")
        pulumi.set(__self__, "db_security_group_ingress", db_security_group_ingress)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dbSecurityGroupIngress")
    def db_security_group_ingress(self) -> Optional[Sequence['outputs.DbSecurityGroupIngress']]:
        return pulumi.get(self, "db_security_group_ingress")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DbSecurityGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDbSecurityGroupResult(GetDbSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbSecurityGroupResult(
            db_security_group_ingress=self.db_security_group_ingress,
            id=self.id,
            tags=self.tags)


def get_db_security_group(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbSecurityGroupResult:
    """
    Resource Type definition for AWS::RDS::DBSecurityGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getDbSecurityGroup', __args__, opts=opts, typ=GetDbSecurityGroupResult).value

    return AwaitableGetDbSecurityGroupResult(
        db_security_group_ingress=pulumi.get(__ret__, 'db_security_group_ingress'),
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_db_security_group)
def get_db_security_group_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbSecurityGroupResult]:
    """
    Resource Type definition for AWS::RDS::DBSecurityGroup
    """
    ...
