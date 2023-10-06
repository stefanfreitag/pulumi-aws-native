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
    'FhirDatastoreCreatedAt',
    'FhirDatastoreIdentityProviderConfiguration',
    'FhirDatastoreKmsEncryptionConfig',
    'FhirDatastorePreloadDataConfig',
    'FhirDatastoreSseConfiguration',
    'FhirDatastoreTag',
]

@pulumi.output_type
class FhirDatastoreCreatedAt(dict):
    """
    The time that a Data Store was created.
    """
    def __init__(__self__, *,
                 nanos: int,
                 seconds: str):
        """
        The time that a Data Store was created.
        :param int nanos: Nanoseconds.
        :param str seconds: Seconds since epoch.
        """
        FhirDatastoreCreatedAt._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            nanos=nanos,
            seconds=seconds,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             nanos: int,
             seconds: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("nanos", nanos)
        _setter("seconds", seconds)

    @property
    @pulumi.getter
    def nanos(self) -> int:
        """
        Nanoseconds.
        """
        return pulumi.get(self, "nanos")

    @property
    @pulumi.getter
    def seconds(self) -> str:
        """
        Seconds since epoch.
        """
        return pulumi.get(self, "seconds")


@pulumi.output_type
class FhirDatastoreIdentityProviderConfiguration(dict):
    """
    The identity provider configuration for the datastore
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authorizationStrategy":
            suggest = "authorization_strategy"
        elif key == "fineGrainedAuthorizationEnabled":
            suggest = "fine_grained_authorization_enabled"
        elif key == "idpLambdaArn":
            suggest = "idp_lambda_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FhirDatastoreIdentityProviderConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FhirDatastoreIdentityProviderConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FhirDatastoreIdentityProviderConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 authorization_strategy: 'FhirDatastoreIdentityProviderConfigurationAuthorizationStrategy',
                 fine_grained_authorization_enabled: Optional[bool] = None,
                 idp_lambda_arn: Optional[str] = None,
                 metadata: Optional[str] = None):
        """
        The identity provider configuration for the datastore
        :param 'FhirDatastoreIdentityProviderConfigurationAuthorizationStrategy' authorization_strategy: Type of Authorization Strategy. The two types of supported Authorization strategies are SMART_ON_FHIR_V1 and AWS_AUTH.
        :param bool fine_grained_authorization_enabled: Flag to indicate if fine-grained authorization will be enabled for the datastore
        :param str idp_lambda_arn: The Amazon Resource Name (ARN) of the Lambda function that will be used to decode the access token created by the authorization server.
        :param str metadata: The JSON metadata elements for identity provider configuration.
        """
        FhirDatastoreIdentityProviderConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            authorization_strategy=authorization_strategy,
            fine_grained_authorization_enabled=fine_grained_authorization_enabled,
            idp_lambda_arn=idp_lambda_arn,
            metadata=metadata,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             authorization_strategy: 'FhirDatastoreIdentityProviderConfigurationAuthorizationStrategy',
             fine_grained_authorization_enabled: Optional[bool] = None,
             idp_lambda_arn: Optional[str] = None,
             metadata: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("authorization_strategy", authorization_strategy)
        if fine_grained_authorization_enabled is not None:
            _setter("fine_grained_authorization_enabled", fine_grained_authorization_enabled)
        if idp_lambda_arn is not None:
            _setter("idp_lambda_arn", idp_lambda_arn)
        if metadata is not None:
            _setter("metadata", metadata)

    @property
    @pulumi.getter(name="authorizationStrategy")
    def authorization_strategy(self) -> 'FhirDatastoreIdentityProviderConfigurationAuthorizationStrategy':
        """
        Type of Authorization Strategy. The two types of supported Authorization strategies are SMART_ON_FHIR_V1 and AWS_AUTH.
        """
        return pulumi.get(self, "authorization_strategy")

    @property
    @pulumi.getter(name="fineGrainedAuthorizationEnabled")
    def fine_grained_authorization_enabled(self) -> Optional[bool]:
        """
        Flag to indicate if fine-grained authorization will be enabled for the datastore
        """
        return pulumi.get(self, "fine_grained_authorization_enabled")

    @property
    @pulumi.getter(name="idpLambdaArn")
    def idp_lambda_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Lambda function that will be used to decode the access token created by the authorization server.
        """
        return pulumi.get(self, "idp_lambda_arn")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[str]:
        """
        The JSON metadata elements for identity provider configuration.
        """
        return pulumi.get(self, "metadata")


@pulumi.output_type
class FhirDatastoreKmsEncryptionConfig(dict):
    """
    The customer-managed-key (CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cmkType":
            suggest = "cmk_type"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FhirDatastoreKmsEncryptionConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FhirDatastoreKmsEncryptionConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FhirDatastoreKmsEncryptionConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cmk_type: 'FhirDatastoreKmsEncryptionConfigCmkType',
                 kms_key_id: Optional[str] = None):
        """
        The customer-managed-key (CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
        :param 'FhirDatastoreKmsEncryptionConfigCmkType' cmk_type: The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
        :param str kms_key_id: The KMS encryption key id/alias used to encrypt the Data Store contents at rest.
        """
        FhirDatastoreKmsEncryptionConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cmk_type=cmk_type,
            kms_key_id=kms_key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cmk_type: 'FhirDatastoreKmsEncryptionConfigCmkType',
             kms_key_id: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cmk_type", cmk_type)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)

    @property
    @pulumi.getter(name="cmkType")
    def cmk_type(self) -> 'FhirDatastoreKmsEncryptionConfigCmkType':
        """
        The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
        """
        return pulumi.get(self, "cmk_type")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The KMS encryption key id/alias used to encrypt the Data Store contents at rest.
        """
        return pulumi.get(self, "kms_key_id")


@pulumi.output_type
class FhirDatastorePreloadDataConfig(dict):
    """
    The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "preloadDataType":
            suggest = "preload_data_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FhirDatastorePreloadDataConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FhirDatastorePreloadDataConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FhirDatastorePreloadDataConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 preload_data_type: 'FhirDatastorePreloadDataConfigPreloadDataType'):
        """
        The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
        :param 'FhirDatastorePreloadDataConfigPreloadDataType' preload_data_type: The type of preloaded data. Only Synthea preloaded data is supported.
        """
        FhirDatastorePreloadDataConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            preload_data_type=preload_data_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             preload_data_type: 'FhirDatastorePreloadDataConfigPreloadDataType',
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("preload_data_type", preload_data_type)

    @property
    @pulumi.getter(name="preloadDataType")
    def preload_data_type(self) -> 'FhirDatastorePreloadDataConfigPreloadDataType':
        """
        The type of preloaded data. Only Synthea preloaded data is supported.
        """
        return pulumi.get(self, "preload_data_type")


@pulumi.output_type
class FhirDatastoreSseConfiguration(dict):
    """
    The server-side encryption key configuration for a customer provided encryption key.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsEncryptionConfig":
            suggest = "kms_encryption_config"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FhirDatastoreSseConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FhirDatastoreSseConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FhirDatastoreSseConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_encryption_config: 'outputs.FhirDatastoreKmsEncryptionConfig'):
        """
        The server-side encryption key configuration for a customer provided encryption key.
        """
        FhirDatastoreSseConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kms_encryption_config=kms_encryption_config,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kms_encryption_config: 'outputs.FhirDatastoreKmsEncryptionConfig',
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("kms_encryption_config", kms_encryption_config)

    @property
    @pulumi.getter(name="kmsEncryptionConfig")
    def kms_encryption_config(self) -> 'outputs.FhirDatastoreKmsEncryptionConfig':
        return pulumi.get(self, "kms_encryption_config")


@pulumi.output_type
class FhirDatastoreTag(dict):
    """
    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        :param str key: The key of the tag.
        :param str value: The value of the tag.
        """
        FhirDatastoreTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the tag.
        """
        return pulumi.get(self, "value")


