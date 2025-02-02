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
    'GetRoleResult',
    'AwaitableGetRoleResult',
    'get_role',
    'get_role_output',
]

@pulumi.output_type
class GetRoleResult:
    def __init__(__self__, arn=None, assume_role_policy_document=None, description=None, managed_policy_arns=None, max_session_duration=None, permissions_boundary=None, policies=None, role_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if assume_role_policy_document and not isinstance(assume_role_policy_document, dict):
            raise TypeError("Expected argument 'assume_role_policy_document' to be a dict")
        pulumi.set(__self__, "assume_role_policy_document", assume_role_policy_document)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if managed_policy_arns and not isinstance(managed_policy_arns, list):
            raise TypeError("Expected argument 'managed_policy_arns' to be a list")
        pulumi.set(__self__, "managed_policy_arns", managed_policy_arns)
        if max_session_duration and not isinstance(max_session_duration, int):
            raise TypeError("Expected argument 'max_session_duration' to be a int")
        pulumi.set(__self__, "max_session_duration", max_session_duration)
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)
        if role_id and not isinstance(role_id, str):
            raise TypeError("Expected argument 'role_id' to be a str")
        pulumi.set(__self__, "role_id", role_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the role.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assumeRolePolicyDocument")
    def assume_role_policy_document(self) -> Optional[Any]:
        """
        The trust policy that is associated with this role.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::Role` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "assume_role_policy_document")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the role that you provide.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[Sequence[str]]:
        """
        A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role. 
        """
        return pulumi.get(self, "managed_policy_arns")

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[int]:
        """
        The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours. 
        """
        return pulumi.get(self, "max_session_duration")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> Optional[str]:
        """
        The ARN of the policy used to set the permissions boundary for the role.
        """
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter
    def policies(self) -> Optional[Sequence['outputs.RolePolicy']]:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM role. 
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[str]:
        """
        The stable and unique string identifying the role.
        """
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of tags that are attached to the role.
        """
        return pulumi.get(self, "tags")


class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            arn=self.arn,
            assume_role_policy_document=self.assume_role_policy_document,
            description=self.description,
            managed_policy_arns=self.managed_policy_arns,
            max_session_duration=self.max_session_duration,
            permissions_boundary=self.permissions_boundary,
            policies=self.policies,
            role_id=self.role_id,
            tags=self.tags)


def get_role(role_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleResult:
    """
    Resource Type definition for AWS::IAM::Role


    :param str role_name: A name for the IAM role, up to 64 characters in length.
    """
    __args__ = dict()
    __args__['roleName'] = role_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getRole', __args__, opts=opts, typ=GetRoleResult).value

    return AwaitableGetRoleResult(
        arn=pulumi.get(__ret__, 'arn'),
        assume_role_policy_document=pulumi.get(__ret__, 'assume_role_policy_document'),
        description=pulumi.get(__ret__, 'description'),
        managed_policy_arns=pulumi.get(__ret__, 'managed_policy_arns'),
        max_session_duration=pulumi.get(__ret__, 'max_session_duration'),
        permissions_boundary=pulumi.get(__ret__, 'permissions_boundary'),
        policies=pulumi.get(__ret__, 'policies'),
        role_id=pulumi.get(__ret__, 'role_id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_role)
def get_role_output(role_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleResult]:
    """
    Resource Type definition for AWS::IAM::Role


    :param str role_name: A name for the IAM role, up to 64 characters in length.
    """
    ...
