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
    'GetCustomMetricResult',
    'AwaitableGetCustomMetricResult',
    'get_custom_metric',
    'get_custom_metric_output',
]

@pulumi.output_type
class GetCustomMetricResult:
    def __init__(__self__, display_name=None, metric_arn=None, tags=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if metric_arn and not isinstance(metric_arn, str):
            raise TypeError("Expected argument 'metric_arn' to be a str")
        pulumi.set(__self__, "metric_arn", metric_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="metricArn")
    def metric_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) of the custom metric.
        """
        return pulumi.get(self, "metric_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CustomMetricTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetCustomMetricResult(GetCustomMetricResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomMetricResult(
            display_name=self.display_name,
            metric_arn=self.metric_arn,
            tags=self.tags)


def get_custom_metric(metric_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomMetricResult:
    """
    A custom metric published by your devices to Device Defender.


    :param str metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.
    """
    __args__ = dict()
    __args__['metricName'] = metric_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getCustomMetric', __args__, opts=opts, typ=GetCustomMetricResult).value

    return AwaitableGetCustomMetricResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        metric_arn=pulumi.get(__ret__, 'metric_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_custom_metric)
def get_custom_metric_output(metric_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomMetricResult]:
    """
    A custom metric published by your devices to Device Defender.


    :param str metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.
    """
    ...
