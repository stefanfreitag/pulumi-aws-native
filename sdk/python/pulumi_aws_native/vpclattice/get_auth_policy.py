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
    'GetAuthPolicyResult',
    'AwaitableGetAuthPolicyResult',
    'get_auth_policy',
    'get_auth_policy_output',
]

@pulumi.output_type
class GetAuthPolicyResult:
    def __init__(__self__, policy=None, state=None):
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def state(self) -> Optional['AuthPolicyState']:
        return pulumi.get(self, "state")


class AwaitableGetAuthPolicyResult(GetAuthPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthPolicyResult(
            policy=self.policy,
            state=self.state)


def get_auth_policy(resource_identifier: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthPolicyResult:
    """
    Creates or updates the auth policy.
    """
    __args__ = dict()
    __args__['resourceIdentifier'] = resource_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:vpclattice:getAuthPolicy', __args__, opts=opts, typ=GetAuthPolicyResult).value

    return AwaitableGetAuthPolicyResult(
        policy=pulumi.get(__ret__, 'policy'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_auth_policy)
def get_auth_policy_output(resource_identifier: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthPolicyResult]:
    """
    Creates or updates the auth policy.
    """
    ...
