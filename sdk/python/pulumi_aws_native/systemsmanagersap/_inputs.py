# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ApplicationCredentialArgs',
]

@pulumi.input_type
class ApplicationCredentialArgs:
    def __init__(__self__, *,
                 credential_type: Optional[pulumi.Input['ApplicationCredentialCredentialType']] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None):
        if credential_type is not None:
            pulumi.set(__self__, "credential_type", credential_type)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if secret_id is not None:
            pulumi.set(__self__, "secret_id", secret_id)

    @property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> Optional[pulumi.Input['ApplicationCredentialCredentialType']]:
        return pulumi.get(self, "credential_type")

    @credential_type.setter
    def credential_type(self, value: Optional[pulumi.Input['ApplicationCredentialCredentialType']]):
        pulumi.set(self, "credential_type", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_id", value)


