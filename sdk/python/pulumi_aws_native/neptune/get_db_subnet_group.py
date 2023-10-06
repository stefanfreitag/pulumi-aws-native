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
    'GetDbSubnetGroupResult',
    'AwaitableGetDbSubnetGroupResult',
    'get_db_subnet_group',
    'get_db_subnet_group_output',
]

@pulumi.output_type
class GetDbSubnetGroupResult:
    def __init__(__self__, db_subnet_group_description=None, id=None, subnet_ids=None, tags=None):
        if db_subnet_group_description and not isinstance(db_subnet_group_description, str):
            raise TypeError("Expected argument 'db_subnet_group_description' to be a str")
        pulumi.set(__self__, "db_subnet_group_description", db_subnet_group_description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> Optional[str]:
        return pulumi.get(self, "db_subnet_group_description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DbSubnetGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDbSubnetGroupResult(GetDbSubnetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbSubnetGroupResult(
            db_subnet_group_description=self.db_subnet_group_description,
            id=self.id,
            subnet_ids=self.subnet_ids,
            tags=self.tags)


def get_db_subnet_group(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbSubnetGroupResult:
    """
    Resource Type definition for AWS::Neptune::DBSubnetGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:neptune:getDbSubnetGroup', __args__, opts=opts, typ=GetDbSubnetGroupResult).value

    return AwaitableGetDbSubnetGroupResult(
        db_subnet_group_description=pulumi.get(__ret__, 'db_subnet_group_description'),
        id=pulumi.get(__ret__, 'id'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_db_subnet_group)
def get_db_subnet_group_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbSubnetGroupResult]:
    """
    Resource Type definition for AWS::Neptune::DBSubnetGroup
    """
    ...
