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

__all__ = [
    'GetGroupMembershipResult',
    'AwaitableGetGroupMembershipResult',
    'get_group_membership',
    'get_group_membership_output',
]

@pulumi.output_type
class GetGroupMembershipResult:
    def __init__(__self__, group_id=None, member_id=None, membership_id=None):
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if member_id and not isinstance(member_id, dict):
            raise TypeError("Expected argument 'member_id' to be a dict")
        pulumi.set(__self__, "member_id", member_id)
        if membership_id and not isinstance(membership_id, str):
            raise TypeError("Expected argument 'membership_id' to be a str")
        pulumi.set(__self__, "membership_id", membership_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        The unique identifier for a group in the identity store.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional['outputs.GroupMembershipMemberId']:
        """
        An object containing the identifier of a group member.
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> Optional[str]:
        """
        The identifier for a GroupMembership in the identity store.
        """
        return pulumi.get(self, "membership_id")


class AwaitableGetGroupMembershipResult(GetGroupMembershipResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupMembershipResult(
            group_id=self.group_id,
            member_id=self.member_id,
            membership_id=self.membership_id)


def get_group_membership(identity_store_id: Optional[str] = None,
                         membership_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupMembershipResult:
    """
    Resource Type Definition for AWS:IdentityStore::GroupMembership


    :param str identity_store_id: The globally unique identifier for the identity store.
    :param str membership_id: The identifier for a GroupMembership in the identity store.
    """
    __args__ = dict()
    __args__['identityStoreId'] = identity_store_id
    __args__['membershipId'] = membership_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:identitystore:getGroupMembership', __args__, opts=opts, typ=GetGroupMembershipResult).value

    return AwaitableGetGroupMembershipResult(
        group_id=pulumi.get(__ret__, 'group_id'),
        member_id=pulumi.get(__ret__, 'member_id'),
        membership_id=pulumi.get(__ret__, 'membership_id'))


@_utilities.lift_output_func(get_group_membership)
def get_group_membership_output(identity_store_id: Optional[pulumi.Input[str]] = None,
                                membership_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupMembershipResult]:
    """
    Resource Type Definition for AWS:IdentityStore::GroupMembership


    :param str identity_store_id: The globally unique identifier for the identity store.
    :param str membership_id: The identifier for a GroupMembership in the identity store.
    """
    ...
