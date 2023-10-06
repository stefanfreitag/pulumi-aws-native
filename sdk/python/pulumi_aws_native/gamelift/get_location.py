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
    'GetLocationResult',
    'AwaitableGetLocationResult',
    'get_location',
    'get_location_output',
]

@pulumi.output_type
class GetLocationResult:
    def __init__(__self__, location_arn=None, tags=None):
        if location_arn and not isinstance(location_arn, str):
            raise TypeError("Expected argument 'location_arn' to be a str")
        pulumi.set(__self__, "location_arn", location_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[str]:
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LocationTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocationResult(GetLocationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationResult(
            location_arn=self.location_arn,
            tags=self.tags)


def get_location(location_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationResult:
    """
    The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.
    """
    __args__ = dict()
    __args__['locationName'] = location_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getLocation', __args__, opts=opts, typ=GetLocationResult).value

    return AwaitableGetLocationResult(
        location_arn=pulumi.get(__ret__, 'location_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_location)
def get_location_output(location_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationResult]:
    """
    The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.
    """
    ...
