# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AssetAssetPropertyNotificationState',
    'AssetModelDataType',
    'AssetModelDataTypeSpec',
    'AssetModelTypeName',
]


class AssetAssetPropertyNotificationState(str, Enum):
    """
    The MQTT notification state (ENABLED or DISABLED) for this asset property.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AssetModelDataType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"
    STRUCT = "STRUCT"


class AssetModelDataTypeSpec(str, Enum):
    AWSALARM_STATE = "AWS/ALARM_STATE"


class AssetModelTypeName(str, Enum):
    MEASUREMENT = "Measurement"
    ATTRIBUTE = "Attribute"
    TRANSFORM = "Transform"
    METRIC = "Metric"
