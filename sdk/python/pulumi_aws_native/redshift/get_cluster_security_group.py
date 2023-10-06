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
    'GetClusterSecurityGroupResult',
    'AwaitableGetClusterSecurityGroupResult',
    'get_cluster_security_group',
    'get_cluster_security_group_output',
]

@pulumi.output_type
class GetClusterSecurityGroupResult:
    def __init__(__self__, id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ClusterSecurityGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetClusterSecurityGroupResult(GetClusterSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterSecurityGroupResult(
            id=self.id,
            tags=self.tags)


def get_cluster_security_group(id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterSecurityGroupResult:
    """
    Resource Type definition for AWS::Redshift::ClusterSecurityGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:redshift:getClusterSecurityGroup', __args__, opts=opts, typ=GetClusterSecurityGroupResult).value

    return AwaitableGetClusterSecurityGroupResult(
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_cluster_security_group)
def get_cluster_security_group_output(id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterSecurityGroupResult]:
    """
    Resource Type definition for AWS::Redshift::ClusterSecurityGroup
    """
    ...
