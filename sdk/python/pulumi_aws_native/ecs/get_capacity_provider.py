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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetCapacityProviderResult',
    'AwaitableGetCapacityProviderResult',
    'get_capacity_provider',
    'get_capacity_provider_output',
]

@pulumi.output_type
class GetCapacityProviderResult:
    def __init__(__self__, auto_scaling_group_provider=None, tags=None):
        if auto_scaling_group_provider and not isinstance(auto_scaling_group_provider, dict):
            raise TypeError("Expected argument 'auto_scaling_group_provider' to be a dict")
        pulumi.set(__self__, "auto_scaling_group_provider", auto_scaling_group_provider)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(self) -> Optional['outputs.CapacityProviderAutoScalingGroupProvider']:
        return pulumi.get(self, "auto_scaling_group_provider")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetCapacityProviderResult(GetCapacityProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityProviderResult(
            auto_scaling_group_provider=self.auto_scaling_group_provider,
            tags=self.tags)


def get_capacity_provider(name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityProviderResult:
    """
    Resource Type definition for AWS::ECS::CapacityProvider.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ecs:getCapacityProvider', __args__, opts=opts, typ=GetCapacityProviderResult).value

    return AwaitableGetCapacityProviderResult(
        auto_scaling_group_provider=pulumi.get(__ret__, 'auto_scaling_group_provider'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_capacity_provider)
def get_capacity_provider_output(name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityProviderResult]:
    """
    Resource Type definition for AWS::ECS::CapacityProvider.
    """
    ...
