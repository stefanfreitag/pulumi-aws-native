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
from ._enums import *

__all__ = [
    'GetIdentitySourceResult',
    'AwaitableGetIdentitySourceResult',
    'get_identity_source',
    'get_identity_source_output',
]

@pulumi.output_type
class GetIdentitySourceResult:
    def __init__(__self__, configuration=None, details=None, identity_source_id=None, principal_entity_type=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if details and not isinstance(details, dict):
            raise TypeError("Expected argument 'details' to be a dict")
        pulumi.set(__self__, "details", details)
        if identity_source_id and not isinstance(identity_source_id, str):
            raise TypeError("Expected argument 'identity_source_id' to be a str")
        pulumi.set(__self__, "identity_source_id", identity_source_id)
        if principal_entity_type and not isinstance(principal_entity_type, str):
            raise TypeError("Expected argument 'principal_entity_type' to be a str")
        pulumi.set(__self__, "principal_entity_type", principal_entity_type)

    @property
    @pulumi.getter
    def configuration(self) -> Optional['outputs.IdentitySourceConfiguration']:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def details(self) -> Optional['outputs.IdentitySourceDetails']:
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="identitySourceId")
    def identity_source_id(self) -> Optional[str]:
        return pulumi.get(self, "identity_source_id")

    @property
    @pulumi.getter(name="principalEntityType")
    def principal_entity_type(self) -> Optional[str]:
        return pulumi.get(self, "principal_entity_type")


class AwaitableGetIdentitySourceResult(GetIdentitySourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentitySourceResult(
            configuration=self.configuration,
            details=self.details,
            identity_source_id=self.identity_source_id,
            principal_entity_type=self.principal_entity_type)


def get_identity_source(identity_source_id: Optional[str] = None,
                        policy_store_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentitySourceResult:
    """
    Definition of AWS::VerifiedPermissions::IdentitySource Resource Type
    """
    __args__ = dict()
    __args__['identitySourceId'] = identity_source_id
    __args__['policyStoreId'] = policy_store_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:verifiedpermissions:getIdentitySource', __args__, opts=opts, typ=GetIdentitySourceResult).value

    return AwaitableGetIdentitySourceResult(
        configuration=__ret__.configuration,
        details=__ret__.details,
        identity_source_id=__ret__.identity_source_id,
        principal_entity_type=__ret__.principal_entity_type)


@_utilities.lift_output_func(get_identity_source)
def get_identity_source_output(identity_source_id: Optional[pulumi.Input[str]] = None,
                               policy_store_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIdentitySourceResult]:
    """
    Definition of AWS::VerifiedPermissions::IdentitySource Resource Type
    """
    ...
