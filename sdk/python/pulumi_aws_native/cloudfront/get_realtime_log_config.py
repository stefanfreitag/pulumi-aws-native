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
    'GetRealtimeLogConfigResult',
    'AwaitableGetRealtimeLogConfigResult',
    'get_realtime_log_config',
    'get_realtime_log_config_output',
]

@pulumi.output_type
class GetRealtimeLogConfigResult:
    def __init__(__self__, arn=None, end_points=None, fields=None, sampling_rate=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if end_points and not isinstance(end_points, list):
            raise TypeError("Expected argument 'end_points' to be a list")
        pulumi.set(__self__, "end_points", end_points)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if sampling_rate and not isinstance(sampling_rate, float):
            raise TypeError("Expected argument 'sampling_rate' to be a float")
        pulumi.set(__self__, "sampling_rate", sampling_rate)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="endPoints")
    def end_points(self) -> Optional[Sequence['outputs.RealtimeLogConfigEndPoint']]:
        return pulumi.get(self, "end_points")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[float]:
        return pulumi.get(self, "sampling_rate")


class AwaitableGetRealtimeLogConfigResult(GetRealtimeLogConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRealtimeLogConfigResult(
            arn=self.arn,
            end_points=self.end_points,
            fields=self.fields,
            sampling_rate=self.sampling_rate)


def get_realtime_log_config(arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRealtimeLogConfigResult:
    """
    Resource Type definition for AWS::CloudFront::RealtimeLogConfig
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getRealtimeLogConfig', __args__, opts=opts, typ=GetRealtimeLogConfigResult).value

    return AwaitableGetRealtimeLogConfigResult(
        arn=pulumi.get(__ret__, 'arn'),
        end_points=pulumi.get(__ret__, 'end_points'),
        fields=pulumi.get(__ret__, 'fields'),
        sampling_rate=pulumi.get(__ret__, 'sampling_rate'))


@_utilities.lift_output_func(get_realtime_log_config)
def get_realtime_log_config_output(arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRealtimeLogConfigResult]:
    """
    Resource Type definition for AWS::CloudFront::RealtimeLogConfig
    """
    ...
