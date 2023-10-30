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
    'GetGraphResult',
    'AwaitableGetGraphResult',
    'get_graph',
    'get_graph_output',
]

@pulumi.output_type
class GetGraphResult:
    def __init__(__self__, arn=None, auto_enable_members=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_enable_members and not isinstance(auto_enable_members, bool):
            raise TypeError("Expected argument 'auto_enable_members' to be a bool")
        pulumi.set(__self__, "auto_enable_members", auto_enable_members)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Detective graph ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoEnableMembers")
    def auto_enable_members(self) -> Optional[bool]:
        """
        Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.
        """
        return pulumi.get(self, "auto_enable_members")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GraphTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetGraphResult(GetGraphResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGraphResult(
            arn=self.arn,
            auto_enable_members=self.auto_enable_members,
            tags=self.tags)


def get_graph(arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGraphResult:
    """
    Resource schema for AWS::Detective::Graph


    :param str arn: The Detective graph ARN
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:detective:getGraph', __args__, opts=opts, typ=GetGraphResult).value

    return AwaitableGetGraphResult(
        arn=pulumi.get(__ret__, 'arn'),
        auto_enable_members=pulumi.get(__ret__, 'auto_enable_members'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_graph)
def get_graph_output(arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGraphResult]:
    """
    Resource schema for AWS::Detective::Graph


    :param str arn: The Detective graph ARN
    """
    ...
