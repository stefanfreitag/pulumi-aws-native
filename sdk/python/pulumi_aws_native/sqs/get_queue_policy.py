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
    'GetQueuePolicyResult',
    'AwaitableGetQueuePolicyResult',
    'get_queue_policy',
    'get_queue_policy_output',
]

@pulumi.output_type
class GetQueuePolicyResult:
    def __init__(__self__, id=None, policy_document=None, queues=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)
        if queues and not isinstance(queues, list):
            raise TypeError("Expected argument 'queues' to be a list")
        pulumi.set(__self__, "queues", queues)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        """
        A policy document that contains the permissions for the specified SQS queues. For more information about SQS policies, see [Using custom policies with the access policy language](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies.html) in the *Developer Guide*.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter
    def queues(self) -> Optional[Sequence[str]]:
        """
        The URLs of the queues to which you want to add the policy. You can use the ``Ref`` function to specify an ``AWS::SQS::Queue`` resource.
        """
        return pulumi.get(self, "queues")


class AwaitableGetQueuePolicyResult(GetQueuePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueuePolicyResult(
            id=self.id,
            policy_document=self.policy_document,
            queues=self.queues)


def get_queue_policy(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueuePolicyResult:
    """
    The ``AWS::SQS::QueuePolicy`` type applies a policy to SQS queues. For an example snippet, see [Declaring an policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sqs-policy) in the *User Guide*.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sqs:getQueuePolicy', __args__, opts=opts, typ=GetQueuePolicyResult).value

    return AwaitableGetQueuePolicyResult(
        id=pulumi.get(__ret__, 'id'),
        policy_document=pulumi.get(__ret__, 'policy_document'),
        queues=pulumi.get(__ret__, 'queues'))


@_utilities.lift_output_func(get_queue_policy)
def get_queue_policy_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueuePolicyResult]:
    """
    The ``AWS::SQS::QueuePolicy`` type applies a policy to SQS queues. For an example snippet, see [Declaring an policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sqs-policy) in the *User Guide*.
    """
    ...
