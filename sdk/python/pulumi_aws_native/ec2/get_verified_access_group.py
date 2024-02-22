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
    'GetVerifiedAccessGroupResult',
    'AwaitableGetVerifiedAccessGroupResult',
    'get_verified_access_group',
    'get_verified_access_group_output',
]

@pulumi.output_type
class GetVerifiedAccessGroupResult:
    def __init__(__self__, creation_time=None, description=None, last_updated_time=None, owner=None, policy_document=None, policy_enabled=None, sse_specification=None, tags=None, verified_access_group_arn=None, verified_access_group_id=None, verified_access_instance_id=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if policy_document and not isinstance(policy_document, str):
            raise TypeError("Expected argument 'policy_document' to be a str")
        pulumi.set(__self__, "policy_document", policy_document)
        if policy_enabled and not isinstance(policy_enabled, bool):
            raise TypeError("Expected argument 'policy_enabled' to be a bool")
        pulumi.set(__self__, "policy_enabled", policy_enabled)
        if sse_specification and not isinstance(sse_specification, dict):
            raise TypeError("Expected argument 'sse_specification' to be a dict")
        pulumi.set(__self__, "sse_specification", sse_specification)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if verified_access_group_arn and not isinstance(verified_access_group_arn, str):
            raise TypeError("Expected argument 'verified_access_group_arn' to be a str")
        pulumi.set(__self__, "verified_access_group_arn", verified_access_group_arn)
        if verified_access_group_id and not isinstance(verified_access_group_id, str):
            raise TypeError("Expected argument 'verified_access_group_id' to be a str")
        pulumi.set(__self__, "verified_access_group_id", verified_access_group_id)
        if verified_access_instance_id and not isinstance(verified_access_instance_id, str):
            raise TypeError("Expected argument 'verified_access_instance_id' to be a str")
        pulumi.set(__self__, "verified_access_instance_id", verified_access_instance_id)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        Time this Verified Access Group was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the AWS Verified Access group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        Time this Verified Access Group was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def owner(self) -> Optional[str]:
        """
        The AWS account number that owns the group.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[str]:
        """
        The AWS Verified Access policy document.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> Optional[bool]:
        """
        The status of the Verified Access policy.
        """
        return pulumi.get(self, "policy_enabled")

    @property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional['outputs.VerifiedAccessGroupSseSpecification']:
        """
        The configuration options for customer provided KMS encryption.
        """
        return pulumi.get(self, "sse_specification")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verifiedAccessGroupArn")
    def verified_access_group_arn(self) -> Optional[str]:
        """
        The ARN of the Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_arn")

    @property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> Optional[str]:
        """
        The ID of the AWS Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_id")

    @property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> Optional[str]:
        """
        The ID of the AWS Verified Access instance.
        """
        return pulumi.get(self, "verified_access_instance_id")


class AwaitableGetVerifiedAccessGroupResult(GetVerifiedAccessGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVerifiedAccessGroupResult(
            creation_time=self.creation_time,
            description=self.description,
            last_updated_time=self.last_updated_time,
            owner=self.owner,
            policy_document=self.policy_document,
            policy_enabled=self.policy_enabled,
            sse_specification=self.sse_specification,
            tags=self.tags,
            verified_access_group_arn=self.verified_access_group_arn,
            verified_access_group_id=self.verified_access_group_id,
            verified_access_instance_id=self.verified_access_instance_id)


def get_verified_access_group(verified_access_group_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVerifiedAccessGroupResult:
    """
    The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.


    :param str verified_access_group_id: The ID of the AWS Verified Access group.
    """
    __args__ = dict()
    __args__['verifiedAccessGroupId'] = verified_access_group_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVerifiedAccessGroup', __args__, opts=opts, typ=GetVerifiedAccessGroupResult).value

    return AwaitableGetVerifiedAccessGroupResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        owner=pulumi.get(__ret__, 'owner'),
        policy_document=pulumi.get(__ret__, 'policy_document'),
        policy_enabled=pulumi.get(__ret__, 'policy_enabled'),
        sse_specification=pulumi.get(__ret__, 'sse_specification'),
        tags=pulumi.get(__ret__, 'tags'),
        verified_access_group_arn=pulumi.get(__ret__, 'verified_access_group_arn'),
        verified_access_group_id=pulumi.get(__ret__, 'verified_access_group_id'),
        verified_access_instance_id=pulumi.get(__ret__, 'verified_access_instance_id'))


@_utilities.lift_output_func(get_verified_access_group)
def get_verified_access_group_output(verified_access_group_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVerifiedAccessGroupResult]:
    """
    The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.


    :param str verified_access_group_id: The ID of the AWS Verified Access group.
    """
    ...
