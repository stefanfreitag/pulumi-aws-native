# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetTopicRuleDestinationResult',
    'AwaitableGetTopicRuleDestinationResult',
    'get_topic_rule_destination',
    'get_topic_rule_destination_output',
]

@pulumi.output_type
class GetTopicRuleDestinationResult:
    def __init__(__self__, arn=None, status=None, status_reason=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        pulumi.set(__self__, "status_reason", status_reason)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def status(self) -> Optional['TopicRuleDestinationStatus']:
        """
        The status of the TopicRuleDestination.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[str]:
        """
        The reasoning for the current status of the TopicRuleDestination.
        """
        return pulumi.get(self, "status_reason")


class AwaitableGetTopicRuleDestinationResult(GetTopicRuleDestinationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicRuleDestinationResult(
            arn=self.arn,
            status=self.status,
            status_reason=self.status_reason)


def get_topic_rule_destination(arn: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicRuleDestinationResult:
    """
    Resource Type definition for AWS::IoT::TopicRuleDestination


    :param str arn: Amazon Resource Name (ARN).
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getTopicRuleDestination', __args__, opts=opts, typ=GetTopicRuleDestinationResult).value

    return AwaitableGetTopicRuleDestinationResult(
        arn=pulumi.get(__ret__, 'arn'),
        status=pulumi.get(__ret__, 'status'),
        status_reason=pulumi.get(__ret__, 'status_reason'))


@_utilities.lift_output_func(get_topic_rule_destination)
def get_topic_rule_destination_output(arn: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicRuleDestinationResult]:
    """
    Resource Type definition for AWS::IoT::TopicRuleDestination


    :param str arn: Amazon Resource Name (ARN).
    """
    ...
