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
    'GetLogDeliveryConfigurationResult',
    'AwaitableGetLogDeliveryConfigurationResult',
    'get_log_delivery_configuration',
    'get_log_delivery_configuration_output',
]

@pulumi.output_type
class GetLogDeliveryConfigurationResult:
    def __init__(__self__, id=None, log_configurations=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_configurations and not isinstance(log_configurations, list):
            raise TypeError("Expected argument 'log_configurations' to be a list")
        pulumi.set(__self__, "log_configurations", log_configurations)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(self) -> Optional[Sequence['outputs.LogDeliveryConfigurationLogConfiguration']]:
        return pulumi.get(self, "log_configurations")


class AwaitableGetLogDeliveryConfigurationResult(GetLogDeliveryConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogDeliveryConfigurationResult(
            id=self.id,
            log_configurations=self.log_configurations)


def get_log_delivery_configuration(id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogDeliveryConfigurationResult:
    """
    Resource Type definition for AWS::Cognito::LogDeliveryConfiguration
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getLogDeliveryConfiguration', __args__, opts=opts, typ=GetLogDeliveryConfigurationResult).value

    return AwaitableGetLogDeliveryConfigurationResult(
        id=pulumi.get(__ret__, 'id'),
        log_configurations=pulumi.get(__ret__, 'log_configurations'))


@_utilities.lift_output_func(get_log_delivery_configuration)
def get_log_delivery_configuration_output(id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogDeliveryConfigurationResult]:
    """
    Resource Type definition for AWS::Cognito::LogDeliveryConfiguration
    """
    ...
