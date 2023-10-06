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
    'GetStudioSessionMappingResult',
    'AwaitableGetStudioSessionMappingResult',
    'get_studio_session_mapping',
    'get_studio_session_mapping_output',
]

@pulumi.output_type
class GetStudioSessionMappingResult:
    def __init__(__self__, session_policy_arn=None):
        if session_policy_arn and not isinstance(session_policy_arn, str):
            raise TypeError("Expected argument 'session_policy_arn' to be a str")
        pulumi.set(__self__, "session_policy_arn", session_policy_arn)

    @property
    @pulumi.getter(name="sessionPolicyArn")
    def session_policy_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles.
        """
        return pulumi.get(self, "session_policy_arn")


class AwaitableGetStudioSessionMappingResult(GetStudioSessionMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStudioSessionMappingResult(
            session_policy_arn=self.session_policy_arn)


def get_studio_session_mapping(identity_name: Optional[str] = None,
                               identity_type: Optional['StudioSessionMappingIdentityType'] = None,
                               studio_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStudioSessionMappingResult:
    """
    An example resource schema demonstrating some basic constructs and validation rules.


    :param str identity_name: The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.
    :param 'StudioSessionMappingIdentityType' identity_type: Specifies whether the identity to map to the Studio is a user or a group.
    :param str studio_id: The ID of the Amazon EMR Studio to which the user or group will be mapped.
    """
    __args__ = dict()
    __args__['identityName'] = identity_name
    __args__['identityType'] = identity_type
    __args__['studioId'] = studio_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:emr:getStudioSessionMapping', __args__, opts=opts, typ=GetStudioSessionMappingResult).value

    return AwaitableGetStudioSessionMappingResult(
        session_policy_arn=pulumi.get(__ret__, 'session_policy_arn'))


@_utilities.lift_output_func(get_studio_session_mapping)
def get_studio_session_mapping_output(identity_name: Optional[pulumi.Input[str]] = None,
                                      identity_type: Optional[pulumi.Input['StudioSessionMappingIdentityType']] = None,
                                      studio_id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStudioSessionMappingResult]:
    """
    An example resource schema demonstrating some basic constructs and validation rules.


    :param str identity_name: The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.
    :param 'StudioSessionMappingIdentityType' identity_type: Specifies whether the identity to map to the Studio is a user or a group.
    :param str studio_id: The ID of the Amazon EMR Studio to which the user or group will be mapped.
    """
    ...
