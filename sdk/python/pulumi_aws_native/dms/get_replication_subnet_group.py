# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetReplicationSubnetGroupResult',
    'AwaitableGetReplicationSubnetGroupResult',
    'get_replication_subnet_group',
    'get_replication_subnet_group_output',
]

@pulumi.output_type
class GetReplicationSubnetGroupResult:
    def __init__(__self__, id=None, replication_subnet_group_description=None, subnet_ids=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if replication_subnet_group_description and not isinstance(replication_subnet_group_description, str):
            raise TypeError("Expected argument 'replication_subnet_group_description' to be a str")
        pulumi.set(__self__, "replication_subnet_group_description", replication_subnet_group_description)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> Optional[str]:
        return pulumi.get(self, "replication_subnet_group_description")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ReplicationSubnetGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetReplicationSubnetGroupResult(GetReplicationSubnetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationSubnetGroupResult(
            id=self.id,
            replication_subnet_group_description=self.replication_subnet_group_description,
            subnet_ids=self.subnet_ids,
            tags=self.tags)


def get_replication_subnet_group(id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationSubnetGroupResult:
    """
    Resource Type definition for AWS::DMS::ReplicationSubnetGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:dms:getReplicationSubnetGroup', __args__, opts=opts, typ=GetReplicationSubnetGroupResult).value

    return AwaitableGetReplicationSubnetGroupResult(
        id=__ret__.id,
        replication_subnet_group_description=__ret__.replication_subnet_group_description,
        subnet_ids=__ret__.subnet_ids,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_replication_subnet_group)
def get_replication_subnet_group_output(id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationSubnetGroupResult]:
    """
    Resource Type definition for AWS::DMS::ReplicationSubnetGroup
    """
    ...
