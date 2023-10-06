# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DomainServerSideEncryptionConfigurationArgs',
    'DomainTagArgs',
]

@pulumi.input_type
class DomainServerSideEncryptionConfigurationArgs:
    def __init__(__self__, *,
                 kms_key_id: pulumi.Input[str]):
        DomainServerSideEncryptionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kms_key_id=kms_key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kms_key_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("kms_key_id", kms_key_id)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "kms_key_id", value)


@pulumi.input_type
class DomainTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        DomainTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


