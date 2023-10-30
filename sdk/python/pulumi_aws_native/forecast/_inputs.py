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
    'DatasetAttributesItemPropertiesArgs',
    'DatasetGroupTagArgs',
    'EncryptionConfigPropertiesArgs',
    'SchemaPropertiesArgs',
    'TagsItemPropertiesArgs',
]

@pulumi.input_type
class DatasetAttributesItemPropertiesArgs:
    def __init__(__self__, *,
                 attribute_name: Optional[pulumi.Input[str]] = None,
                 attribute_type: Optional[pulumi.Input['DatasetAttributesItemPropertiesAttributeType']] = None):
        """
        :param pulumi.Input[str] attribute_name: Name of the dataset field
        :param pulumi.Input['DatasetAttributesItemPropertiesAttributeType'] attribute_type: Data type of the field
        """
        if attribute_name is not None:
            pulumi.set(__self__, "attribute_name", attribute_name)
        if attribute_type is not None:
            pulumi.set(__self__, "attribute_type", attribute_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the dataset field
        """
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[pulumi.Input['DatasetAttributesItemPropertiesAttributeType']]:
        """
        Data type of the field
        """
        return pulumi.get(self, "attribute_type")

    @attribute_type.setter
    def attribute_type(self, value: Optional[pulumi.Input['DatasetAttributesItemPropertiesAttributeType']]):
        pulumi.set(self, "attribute_type", value)


@pulumi.input_type
class DatasetGroupTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EncryptionConfigPropertiesArgs:
    def __init__(__self__, *,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None):
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)


@pulumi.input_type
class SchemaPropertiesArgs:
    def __init__(__self__, *,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetAttributesItemPropertiesArgs']]]] = None):
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatasetAttributesItemPropertiesArgs']]]]:
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetAttributesItemPropertiesArgs']]]]):
        pulumi.set(self, "attributes", value)


@pulumi.input_type
class TagsItemPropertiesArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

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


