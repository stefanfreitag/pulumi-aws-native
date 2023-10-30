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
    'GetAccessPolicyResult',
    'AwaitableGetAccessPolicyResult',
    'get_access_policy',
    'get_access_policy_output',
]

@pulumi.output_type
class GetAccessPolicyResult:
    def __init__(__self__, access_policy_arn=None, access_policy_id=None, access_policy_identity=None, access_policy_permission=None, access_policy_resource=None):
        if access_policy_arn and not isinstance(access_policy_arn, str):
            raise TypeError("Expected argument 'access_policy_arn' to be a str")
        pulumi.set(__self__, "access_policy_arn", access_policy_arn)
        if access_policy_id and not isinstance(access_policy_id, str):
            raise TypeError("Expected argument 'access_policy_id' to be a str")
        pulumi.set(__self__, "access_policy_id", access_policy_id)
        if access_policy_identity and not isinstance(access_policy_identity, dict):
            raise TypeError("Expected argument 'access_policy_identity' to be a dict")
        pulumi.set(__self__, "access_policy_identity", access_policy_identity)
        if access_policy_permission and not isinstance(access_policy_permission, str):
            raise TypeError("Expected argument 'access_policy_permission' to be a str")
        pulumi.set(__self__, "access_policy_permission", access_policy_permission)
        if access_policy_resource and not isinstance(access_policy_resource, dict):
            raise TypeError("Expected argument 'access_policy_resource' to be a dict")
        pulumi.set(__self__, "access_policy_resource", access_policy_resource)

    @property
    @pulumi.getter(name="accessPolicyArn")
    def access_policy_arn(self) -> Optional[str]:
        """
        The ARN of the access policy.
        """
        return pulumi.get(self, "access_policy_arn")

    @property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[str]:
        """
        The ID of the access policy.
        """
        return pulumi.get(self, "access_policy_id")

    @property
    @pulumi.getter(name="accessPolicyIdentity")
    def access_policy_identity(self) -> Optional['outputs.AccessPolicyIdentity']:
        """
        The identity for this access policy. Choose either a user or a group but not both.
        """
        return pulumi.get(self, "access_policy_identity")

    @property
    @pulumi.getter(name="accessPolicyPermission")
    def access_policy_permission(self) -> Optional[str]:
        """
        The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.
        """
        return pulumi.get(self, "access_policy_permission")

    @property
    @pulumi.getter(name="accessPolicyResource")
    def access_policy_resource(self) -> Optional['outputs.AccessPolicyResource']:
        """
        The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.
        """
        return pulumi.get(self, "access_policy_resource")


class AwaitableGetAccessPolicyResult(GetAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPolicyResult(
            access_policy_arn=self.access_policy_arn,
            access_policy_id=self.access_policy_id,
            access_policy_identity=self.access_policy_identity,
            access_policy_permission=self.access_policy_permission,
            access_policy_resource=self.access_policy_resource)


def get_access_policy(access_policy_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPolicyResult:
    """
    Resource schema for AWS::IoTSiteWise::AccessPolicy


    :param str access_policy_id: The ID of the access policy.
    """
    __args__ = dict()
    __args__['accessPolicyId'] = access_policy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotsitewise:getAccessPolicy', __args__, opts=opts, typ=GetAccessPolicyResult).value

    return AwaitableGetAccessPolicyResult(
        access_policy_arn=pulumi.get(__ret__, 'access_policy_arn'),
        access_policy_id=pulumi.get(__ret__, 'access_policy_id'),
        access_policy_identity=pulumi.get(__ret__, 'access_policy_identity'),
        access_policy_permission=pulumi.get(__ret__, 'access_policy_permission'),
        access_policy_resource=pulumi.get(__ret__, 'access_policy_resource'))


@_utilities.lift_output_func(get_access_policy)
def get_access_policy_output(access_policy_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPolicyResult]:
    """
    Resource schema for AWS::IoTSiteWise::AccessPolicy


    :param str access_policy_id: The ID of the access policy.
    """
    ...
