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
from ._enums import *

__all__ = [
    'GetFlowEntitlementResult',
    'AwaitableGetFlowEntitlementResult',
    'get_flow_entitlement',
    'get_flow_entitlement_output',
]

@pulumi.output_type
class GetFlowEntitlementResult:
    def __init__(__self__, description=None, encryption=None, entitlement_arn=None, entitlement_status=None, flow_arn=None, subscribers=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if entitlement_arn and not isinstance(entitlement_arn, str):
            raise TypeError("Expected argument 'entitlement_arn' to be a str")
        pulumi.set(__self__, "entitlement_arn", entitlement_arn)
        if entitlement_status and not isinstance(entitlement_status, str):
            raise TypeError("Expected argument 'entitlement_status' to be a str")
        pulumi.set(__self__, "entitlement_status", entitlement_status)
        if flow_arn and not isinstance(flow_arn, str):
            raise TypeError("Expected argument 'flow_arn' to be a str")
        pulumi.set(__self__, "flow_arn", flow_arn)
        if subscribers and not isinstance(subscribers, list):
            raise TypeError("Expected argument 'subscribers' to be a list")
        pulumi.set(__self__, "subscribers", subscribers)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the entitlement.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.FlowEntitlementEncryption']:
        """
        The type of encryption that will be used on the output that is associated with this entitlement.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="entitlementArn")
    def entitlement_arn(self) -> Optional[str]:
        """
        The ARN of the entitlement.
        """
        return pulumi.get(self, "entitlement_arn")

    @property
    @pulumi.getter(name="entitlementStatus")
    def entitlement_status(self) -> Optional['FlowEntitlementEntitlementStatus']:
        """
         An indication of whether the entitlement is enabled.
        """
        return pulumi.get(self, "entitlement_status")

    @property
    @pulumi.getter(name="flowArn")
    def flow_arn(self) -> Optional[str]:
        """
        The ARN of the flow.
        """
        return pulumi.get(self, "flow_arn")

    @property
    @pulumi.getter
    def subscribers(self) -> Optional[Sequence[str]]:
        """
        The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
        """
        return pulumi.get(self, "subscribers")


class AwaitableGetFlowEntitlementResult(GetFlowEntitlementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFlowEntitlementResult(
            description=self.description,
            encryption=self.encryption,
            entitlement_arn=self.entitlement_arn,
            entitlement_status=self.entitlement_status,
            flow_arn=self.flow_arn,
            subscribers=self.subscribers)


def get_flow_entitlement(entitlement_arn: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFlowEntitlementResult:
    """
    Resource schema for AWS::MediaConnect::FlowEntitlement


    :param str entitlement_arn: The ARN of the entitlement.
    """
    __args__ = dict()
    __args__['entitlementArn'] = entitlement_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediaconnect:getFlowEntitlement', __args__, opts=opts, typ=GetFlowEntitlementResult).value

    return AwaitableGetFlowEntitlementResult(
        description=pulumi.get(__ret__, 'description'),
        encryption=pulumi.get(__ret__, 'encryption'),
        entitlement_arn=pulumi.get(__ret__, 'entitlement_arn'),
        entitlement_status=pulumi.get(__ret__, 'entitlement_status'),
        flow_arn=pulumi.get(__ret__, 'flow_arn'),
        subscribers=pulumi.get(__ret__, 'subscribers'))


@_utilities.lift_output_func(get_flow_entitlement)
def get_flow_entitlement_output(entitlement_arn: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFlowEntitlementResult]:
    """
    Resource schema for AWS::MediaConnect::FlowEntitlement


    :param str entitlement_arn: The ARN of the entitlement.
    """
    ...
