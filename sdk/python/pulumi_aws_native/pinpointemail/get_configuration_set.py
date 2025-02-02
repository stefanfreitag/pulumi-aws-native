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

__all__ = [
    'GetConfigurationSetResult',
    'AwaitableGetConfigurationSetResult',
    'get_configuration_set',
    'get_configuration_set_output',
]

@pulumi.output_type
class GetConfigurationSetResult:
    def __init__(__self__, delivery_options=None, id=None, reputation_options=None, sending_options=None, tags=None, tracking_options=None):
        if delivery_options and not isinstance(delivery_options, dict):
            raise TypeError("Expected argument 'delivery_options' to be a dict")
        pulumi.set(__self__, "delivery_options", delivery_options)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if reputation_options and not isinstance(reputation_options, dict):
            raise TypeError("Expected argument 'reputation_options' to be a dict")
        pulumi.set(__self__, "reputation_options", reputation_options)
        if sending_options and not isinstance(sending_options, dict):
            raise TypeError("Expected argument 'sending_options' to be a dict")
        pulumi.set(__self__, "sending_options", sending_options)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tracking_options and not isinstance(tracking_options, dict):
            raise TypeError("Expected argument 'tracking_options' to be a dict")
        pulumi.set(__self__, "tracking_options", tracking_options)

    @property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> Optional['outputs.ConfigurationSetDeliveryOptions']:
        return pulumi.get(self, "delivery_options")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> Optional['outputs.ConfigurationSetReputationOptions']:
        return pulumi.get(self, "reputation_options")

    @property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> Optional['outputs.ConfigurationSetSendingOptions']:
        return pulumi.get(self, "sending_options")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> Optional['outputs.ConfigurationSetTrackingOptions']:
        return pulumi.get(self, "tracking_options")


class AwaitableGetConfigurationSetResult(GetConfigurationSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationSetResult(
            delivery_options=self.delivery_options,
            id=self.id,
            reputation_options=self.reputation_options,
            sending_options=self.sending_options,
            tags=self.tags,
            tracking_options=self.tracking_options)


def get_configuration_set(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationSetResult:
    """
    Resource Type definition for AWS::PinpointEmail::ConfigurationSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpointemail:getConfigurationSet', __args__, opts=opts, typ=GetConfigurationSetResult).value

    return AwaitableGetConfigurationSetResult(
        delivery_options=pulumi.get(__ret__, 'delivery_options'),
        id=pulumi.get(__ret__, 'id'),
        reputation_options=pulumi.get(__ret__, 'reputation_options'),
        sending_options=pulumi.get(__ret__, 'sending_options'),
        tags=pulumi.get(__ret__, 'tags'),
        tracking_options=pulumi.get(__ret__, 'tracking_options'))


@_utilities.lift_output_func(get_configuration_set)
def get_configuration_set_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationSetResult]:
    """
    Resource Type definition for AWS::PinpointEmail::ConfigurationSet
    """
    ...
