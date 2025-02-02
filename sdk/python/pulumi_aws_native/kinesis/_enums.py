# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'StreamEncryptionEncryptionType',
    'StreamModeDetailsStreamMode',
]


class StreamEncryptionEncryptionType(str, Enum):
    """
    The encryption type to use. The only valid value is KMS. 
    """
    KMS = "KMS"


class StreamModeDetailsStreamMode(str, Enum):
    """
    The mode of the stream
    """
    ON_DEMAND = "ON_DEMAND"
    PROVISIONED = "PROVISIONED"
