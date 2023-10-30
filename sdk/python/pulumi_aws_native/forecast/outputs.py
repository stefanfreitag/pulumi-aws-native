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
    'DatasetAttributesItemProperties',
    'DatasetGroupTag',
    'EncryptionConfigProperties',
    'SchemaProperties',
    'TagsItemProperties',
]

@pulumi.output_type
class DatasetAttributesItemProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attributeName":
            suggest = "attribute_name"
        elif key == "attributeType":
            suggest = "attribute_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DatasetAttributesItemProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DatasetAttributesItemProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DatasetAttributesItemProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attribute_name: Optional[str] = None,
                 attribute_type: Optional['DatasetAttributesItemPropertiesAttributeType'] = None):
        """
        :param str attribute_name: Name of the dataset field
        :param 'DatasetAttributesItemPropertiesAttributeType' attribute_type: Data type of the field
        """
        if attribute_name is not None:
            pulumi.set(__self__, "attribute_name", attribute_name)
        if attribute_type is not None:
            pulumi.set(__self__, "attribute_type", attribute_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[str]:
        """
        Name of the dataset field
        """
        return pulumi.get(self, "attribute_name")

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional['DatasetAttributesItemPropertiesAttributeType']:
        """
        Data type of the field
        """
        return pulumi.get(self, "attribute_type")


@pulumi.output_type
class DatasetGroupTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class EncryptionConfigProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyArn":
            suggest = "kms_key_arn"
        elif key == "roleArn":
            suggest = "role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionConfigProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionConfigProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionConfigProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key_arn: Optional[str] = None,
                 role_arn: Optional[str] = None):
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[str]:
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")


@pulumi.output_type
class SchemaProperties(dict):
    def __init__(__self__, *,
                 attributes: Optional[Sequence['outputs.DatasetAttributesItemProperties']] = None):
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Sequence['outputs.DatasetAttributesItemProperties']]:
        return pulumi.get(self, "attributes")


@pulumi.output_type
class TagsItemProperties(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


