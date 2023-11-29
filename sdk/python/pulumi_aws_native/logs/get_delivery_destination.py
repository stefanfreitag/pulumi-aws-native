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
    'GetDeliveryDestinationResult',
    'AwaitableGetDeliveryDestinationResult',
    'get_delivery_destination',
    'get_delivery_destination_output',
]

@pulumi.output_type
class GetDeliveryDestinationResult:
    def __init__(__self__, arn=None, delivery_destination_policy=None, delivery_destination_type=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if delivery_destination_policy and not isinstance(delivery_destination_policy, dict):
            raise TypeError("Expected argument 'delivery_destination_policy' to be a dict")
        pulumi.set(__self__, "delivery_destination_policy", delivery_destination_policy)
        if delivery_destination_type and not isinstance(delivery_destination_type, str):
            raise TypeError("Expected argument 'delivery_destination_type' to be a str")
        pulumi.set(__self__, "delivery_destination_type", delivery_destination_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The value of the Arn property for this object.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deliveryDestinationPolicy")
    def delivery_destination_policy(self) -> Optional[Any]:
        """
        IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 51200
        """
        return pulumi.get(self, "delivery_destination_policy")

    @property
    @pulumi.getter(name="deliveryDestinationType")
    def delivery_destination_type(self) -> Optional[str]:
        """
        The value of the DeliveryDestinationType property for this object.
        """
        return pulumi.get(self, "delivery_destination_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DeliveryDestinationTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDeliveryDestinationResult(GetDeliveryDestinationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeliveryDestinationResult(
            arn=self.arn,
            delivery_destination_policy=self.delivery_destination_policy,
            delivery_destination_type=self.delivery_destination_type,
            tags=self.tags)


def get_delivery_destination(name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeliveryDestinationResult:
    """
    Resource Type definition for AWS::Logs::DeliveryDestination


    :param str name: The unique name of the Delivery Destination.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getDeliveryDestination', __args__, opts=opts, typ=GetDeliveryDestinationResult).value

    return AwaitableGetDeliveryDestinationResult(
        arn=pulumi.get(__ret__, 'arn'),
        delivery_destination_policy=pulumi.get(__ret__, 'delivery_destination_policy'),
        delivery_destination_type=pulumi.get(__ret__, 'delivery_destination_type'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_delivery_destination)
def get_delivery_destination_output(name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeliveryDestinationResult]:
    """
    Resource Type definition for AWS::Logs::DeliveryDestination


    :param str name: The unique name of the Delivery Destination.
    """
    ...
