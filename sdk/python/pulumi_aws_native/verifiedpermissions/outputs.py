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
    'IdentitySourceCognitoUserPoolConfiguration',
    'IdentitySourceConfiguration',
    'IdentitySourceDetails',
    'PolicyDefinition',
    'PolicyStoreSchemaDefinition',
    'PolicyStoreValidationSettings',
]

@pulumi.output_type
class IdentitySourceCognitoUserPoolConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "userPoolArn":
            suggest = "user_pool_arn"
        elif key == "clientIds":
            suggest = "client_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentitySourceCognitoUserPoolConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentitySourceCognitoUserPoolConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentitySourceCognitoUserPoolConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 user_pool_arn: str,
                 client_ids: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "user_pool_arn", user_pool_arn)
        if client_ids is not None:
            pulumi.set(__self__, "client_ids", client_ids)

    @property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> str:
        return pulumi.get(self, "user_pool_arn")

    @property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "client_ids")


@pulumi.output_type
class IdentitySourceConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cognitoUserPoolConfiguration":
            suggest = "cognito_user_pool_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentitySourceConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentitySourceConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentitySourceConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cognito_user_pool_configuration: 'outputs.IdentitySourceCognitoUserPoolConfiguration'):
        pulumi.set(__self__, "cognito_user_pool_configuration", cognito_user_pool_configuration)

    @property
    @pulumi.getter(name="cognitoUserPoolConfiguration")
    def cognito_user_pool_configuration(self) -> 'outputs.IdentitySourceCognitoUserPoolConfiguration':
        return pulumi.get(self, "cognito_user_pool_configuration")


@pulumi.output_type
class IdentitySourceDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientIds":
            suggest = "client_ids"
        elif key == "discoveryUrl":
            suggest = "discovery_url"
        elif key == "openIdIssuer":
            suggest = "open_id_issuer"
        elif key == "userPoolArn":
            suggest = "user_pool_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentitySourceDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentitySourceDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentitySourceDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_ids: Optional[Sequence[str]] = None,
                 discovery_url: Optional[str] = None,
                 open_id_issuer: Optional['IdentitySourceOpenIdIssuer'] = None,
                 user_pool_arn: Optional[str] = None):
        if client_ids is not None:
            pulumi.set(__self__, "client_ids", client_ids)
        if discovery_url is not None:
            pulumi.set(__self__, "discovery_url", discovery_url)
        if open_id_issuer is not None:
            pulumi.set(__self__, "open_id_issuer", open_id_issuer)
        if user_pool_arn is not None:
            pulumi.set(__self__, "user_pool_arn", user_pool_arn)

    @property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "client_ids")

    @property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[str]:
        return pulumi.get(self, "discovery_url")

    @property
    @pulumi.getter(name="openIdIssuer")
    def open_id_issuer(self) -> Optional['IdentitySourceOpenIdIssuer']:
        return pulumi.get(self, "open_id_issuer")

    @property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> Optional[str]:
        return pulumi.get(self, "user_pool_arn")


@pulumi.output_type
class PolicyDefinition(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class PolicyStoreSchemaDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cedarJson":
            suggest = "cedar_json"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyStoreSchemaDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyStoreSchemaDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyStoreSchemaDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cedar_json: Optional[str] = None):
        if cedar_json is not None:
            pulumi.set(__self__, "cedar_json", cedar_json)

    @property
    @pulumi.getter(name="cedarJson")
    def cedar_json(self) -> Optional[str]:
        return pulumi.get(self, "cedar_json")


@pulumi.output_type
class PolicyStoreValidationSettings(dict):
    def __init__(__self__, *,
                 mode: 'PolicyStoreValidationMode'):
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> 'PolicyStoreValidationMode':
        return pulumi.get(self, "mode")


