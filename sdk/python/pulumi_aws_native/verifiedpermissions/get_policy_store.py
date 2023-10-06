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
    'GetPolicyStoreResult',
    'AwaitableGetPolicyStoreResult',
    'get_policy_store',
    'get_policy_store_output',
]

@pulumi.output_type
class GetPolicyStoreResult:
    def __init__(__self__, arn=None, policy_store_id=None, schema=None, validation_settings=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if policy_store_id and not isinstance(policy_store_id, str):
            raise TypeError("Expected argument 'policy_store_id' to be a str")
        pulumi.set(__self__, "policy_store_id", policy_store_id)
        if schema and not isinstance(schema, dict):
            raise TypeError("Expected argument 'schema' to be a dict")
        pulumi.set(__self__, "schema", schema)
        if validation_settings and not isinstance(validation_settings, dict):
            raise TypeError("Expected argument 'validation_settings' to be a dict")
        pulumi.set(__self__, "validation_settings", validation_settings)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> Optional[str]:
        return pulumi.get(self, "policy_store_id")

    @property
    @pulumi.getter
    def schema(self) -> Optional['outputs.PolicyStoreSchemaDefinition']:
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="validationSettings")
    def validation_settings(self) -> Optional['outputs.PolicyStoreValidationSettings']:
        return pulumi.get(self, "validation_settings")


class AwaitableGetPolicyStoreResult(GetPolicyStoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyStoreResult(
            arn=self.arn,
            policy_store_id=self.policy_store_id,
            schema=self.schema,
            validation_settings=self.validation_settings)


def get_policy_store(policy_store_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyStoreResult:
    """
    Definition of AWS::VerifiedPermissions::PolicyStore Resource Type
    """
    __args__ = dict()
    __args__['policyStoreId'] = policy_store_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:verifiedpermissions:getPolicyStore', __args__, opts=opts, typ=GetPolicyStoreResult).value

    return AwaitableGetPolicyStoreResult(
        arn=pulumi.get(__ret__, 'arn'),
        policy_store_id=pulumi.get(__ret__, 'policy_store_id'),
        schema=pulumi.get(__ret__, 'schema'),
        validation_settings=pulumi.get(__ret__, 'validation_settings'))


@_utilities.lift_output_func(get_policy_store)
def get_policy_store_output(policy_store_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyStoreResult]:
    """
    Definition of AWS::VerifiedPermissions::PolicyStore Resource Type
    """
    ...
