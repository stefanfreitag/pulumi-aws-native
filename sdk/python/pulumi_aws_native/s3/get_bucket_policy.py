# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetBucketPolicyResult',
    'AwaitableGetBucketPolicyResult',
    'get_bucket_policy',
    'get_bucket_policy_output',
]

@pulumi.output_type
class GetBucketPolicyResult:
    def __init__(__self__, id=None, policy_document=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        return pulumi.get(self, "policy_document")


class AwaitableGetBucketPolicyResult(GetBucketPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketPolicyResult(
            id=self.id,
            policy_document=self.policy_document)


def get_bucket_policy(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketPolicyResult:
    """
    Resource Type definition for AWS::S3::BucketPolicy
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:s3:getBucketPolicy', __args__, opts=opts, typ=GetBucketPolicyResult).value

    return AwaitableGetBucketPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        policy_document=pulumi.get(__ret__, 'policy_document'))


@_utilities.lift_output_func(get_bucket_policy)
def get_bucket_policy_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketPolicyResult]:
    """
    Resource Type definition for AWS::S3::BucketPolicy
    """
    ...
