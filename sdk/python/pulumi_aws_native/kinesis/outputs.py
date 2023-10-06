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
    'StreamEncryption',
    'StreamModeDetails',
    'StreamTag',
]

@pulumi.output_type
class StreamEncryption(dict):
    """
    When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionType":
            suggest = "encryption_type"
        elif key == "keyId":
            suggest = "key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StreamEncryption. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StreamEncryption.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StreamEncryption.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption_type: 'StreamEncryptionEncryptionType',
                 key_id: str):
        """
        When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption.
        :param 'StreamEncryptionEncryptionType' encryption_type: The encryption type to use. The only valid value is KMS. 
        :param str key_id: The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.
        """
        StreamEncryption._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encryption_type=encryption_type,
            key_id=key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encryption_type: 'StreamEncryptionEncryptionType',
             key_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("encryption_type", encryption_type)
        _setter("key_id", key_id)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> 'StreamEncryptionEncryptionType':
        """
        The encryption type to use. The only valid value is KMS. 
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        """
        The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.
        """
        return pulumi.get(self, "key_id")


@pulumi.output_type
class StreamModeDetails(dict):
    """
    When specified, enables or updates the mode of stream. Default is PROVISIONED.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "streamMode":
            suggest = "stream_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StreamModeDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StreamModeDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StreamModeDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stream_mode: 'StreamModeDetailsStreamMode'):
        """
        When specified, enables or updates the mode of stream. Default is PROVISIONED.
        :param 'StreamModeDetailsStreamMode' stream_mode: The mode of the stream
        """
        StreamModeDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            stream_mode=stream_mode,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             stream_mode: 'StreamModeDetailsStreamMode',
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("stream_mode", stream_mode)

    @property
    @pulumi.getter(name="streamMode")
    def stream_mode(self) -> 'StreamModeDetailsStreamMode':
        """
        The mode of the stream
        """
        return pulumi.get(self, "stream_mode")


@pulumi.output_type
class StreamTag(dict):
    """
    An arbitrary set of tags (key-value pairs) to associate with the Kinesis stream.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        An arbitrary set of tags (key-value pairs) to associate with the Kinesis stream.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        StreamTag._configure(
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
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that is 0 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


