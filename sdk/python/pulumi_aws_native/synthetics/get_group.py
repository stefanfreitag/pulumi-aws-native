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
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    def __init__(__self__, id=None, resource_arns=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_arns and not isinstance(resource_arns, list):
            raise TypeError("Expected argument 'resource_arns' to be a list")
        pulumi.set(__self__, "resource_arns", resource_arns)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of the group.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_arns")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            id=self.id,
            resource_arns=self.resource_arns,
            tags=self.tags)


def get_group(name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    Resource Type definition for AWS::Synthetics::Group


    :param str name: Name of the group.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:synthetics:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        id=pulumi.get(__ret__, 'id'),
        resource_arns=pulumi.get(__ret__, 'resource_arns'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_group)
def get_group_output(name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    Resource Type definition for AWS::Synthetics::Group


    :param str name: Name of the group.
    """
    ...
