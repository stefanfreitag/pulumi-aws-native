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
from ._enums import *

__all__ = [
    'GetIdentityProviderResult',
    'AwaitableGetIdentityProviderResult',
    'get_identity_provider',
    'get_identity_provider_output',
]

@pulumi.output_type
class GetIdentityProviderResult:
    def __init__(__self__, identity_provider_arn=None, identity_provider_details=None, identity_provider_name=None, identity_provider_type=None):
        if identity_provider_arn and not isinstance(identity_provider_arn, str):
            raise TypeError("Expected argument 'identity_provider_arn' to be a str")
        pulumi.set(__self__, "identity_provider_arn", identity_provider_arn)
        if identity_provider_details and not isinstance(identity_provider_details, dict):
            raise TypeError("Expected argument 'identity_provider_details' to be a dict")
        pulumi.set(__self__, "identity_provider_details", identity_provider_details)
        if identity_provider_name and not isinstance(identity_provider_name, str):
            raise TypeError("Expected argument 'identity_provider_name' to be a str")
        pulumi.set(__self__, "identity_provider_name", identity_provider_name)
        if identity_provider_type and not isinstance(identity_provider_type, str):
            raise TypeError("Expected argument 'identity_provider_type' to be a str")
        pulumi.set(__self__, "identity_provider_type", identity_provider_type)

    @property
    @pulumi.getter(name="identityProviderArn")
    def identity_provider_arn(self) -> Optional[str]:
        return pulumi.get(self, "identity_provider_arn")

    @property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> Optional['outputs.IdentityProviderDetails']:
        return pulumi.get(self, "identity_provider_details")

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> Optional[str]:
        return pulumi.get(self, "identity_provider_name")

    @property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> Optional['IdentityProviderType']:
        return pulumi.get(self, "identity_provider_type")


class AwaitableGetIdentityProviderResult(GetIdentityProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityProviderResult(
            identity_provider_arn=self.identity_provider_arn,
            identity_provider_details=self.identity_provider_details,
            identity_provider_name=self.identity_provider_name,
            identity_provider_type=self.identity_provider_type)


def get_identity_provider(identity_provider_arn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityProviderResult:
    """
    Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type
    """
    __args__ = dict()
    __args__['identityProviderArn'] = identity_provider_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspacesweb:getIdentityProvider', __args__, opts=opts, typ=GetIdentityProviderResult).value

    return AwaitableGetIdentityProviderResult(
        identity_provider_arn=pulumi.get(__ret__, 'identity_provider_arn'),
        identity_provider_details=pulumi.get(__ret__, 'identity_provider_details'),
        identity_provider_name=pulumi.get(__ret__, 'identity_provider_name'),
        identity_provider_type=pulumi.get(__ret__, 'identity_provider_type'))


@_utilities.lift_output_func(get_identity_provider)
def get_identity_provider_output(identity_provider_arn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIdentityProviderResult]:
    """
    Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type
    """
    ...
