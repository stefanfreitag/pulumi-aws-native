# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTopicInlinePolicyResult',
    'AwaitableGetTopicInlinePolicyResult',
    'get_topic_inline_policy',
    'get_topic_inline_policy_output',
]

@pulumi.output_type
class GetTopicInlinePolicyResult:
    def __init__(__self__, policy_document=None):
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        """
        A policy document that contains permissions to add to the specified SNS topics.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SNS::TopicInlinePolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy_document")


class AwaitableGetTopicInlinePolicyResult(GetTopicInlinePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicInlinePolicyResult(
            policy_document=self.policy_document)


def get_topic_inline_policy(topic_arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicInlinePolicyResult:
    """
    Schema for AWS::SNS::TopicInlinePolicy


    :param str topic_arn: The Amazon Resource Name (ARN) of the topic to which you want to add the policy.
    """
    __args__ = dict()
    __args__['topicArn'] = topic_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sns:getTopicInlinePolicy', __args__, opts=opts, typ=GetTopicInlinePolicyResult).value

    return AwaitableGetTopicInlinePolicyResult(
        policy_document=pulumi.get(__ret__, 'policy_document'))


@_utilities.lift_output_func(get_topic_inline_policy)
def get_topic_inline_policy_output(topic_arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicInlinePolicyResult]:
    """
    Schema for AWS::SNS::TopicInlinePolicy


    :param str topic_arn: The Amazon Resource Name (ARN) of the topic to which you want to add the policy.
    """
    ...
