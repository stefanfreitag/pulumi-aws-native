# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CampaignCompression',
    'CampaignDataFormat',
    'CampaignDiagnosticsMode',
    'CampaignSpoolingMode',
    'CampaignStatus',
    'CampaignStorageCompressionFormat',
    'CampaignTriggerMode',
    'CampaignUpdateCampaignAction',
    'DecoderManifestCanNetworkInterfaceType',
    'DecoderManifestCanSignalDecoderType',
    'DecoderManifestManifestStatus',
    'DecoderManifestObdNetworkInterfaceType',
    'DecoderManifestObdSignalDecoderType',
    'ModelManifestManifestStatus',
    'SignalCatalogNodeDataType',
    'VehicleAssociationBehavior',
]


class CampaignCompression(str, Enum):
    OFF = "OFF"
    SNAPPY = "SNAPPY"


class CampaignDataFormat(str, Enum):
    JSON = "JSON"
    PARQUET = "PARQUET"


class CampaignDiagnosticsMode(str, Enum):
    OFF = "OFF"
    SEND_ACTIVE_DTCS = "SEND_ACTIVE_DTCS"


class CampaignSpoolingMode(str, Enum):
    OFF = "OFF"
    TO_DISK = "TO_DISK"


class CampaignStatus(str, Enum):
    CREATING = "CREATING"
    WAITING_FOR_APPROVAL = "WAITING_FOR_APPROVAL"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"


class CampaignStorageCompressionFormat(str, Enum):
    NONE = "NONE"
    GZIP = "GZIP"


class CampaignTriggerMode(str, Enum):
    ALWAYS = "ALWAYS"
    RISING_EDGE = "RISING_EDGE"


class CampaignUpdateCampaignAction(str, Enum):
    APPROVE = "APPROVE"
    SUSPEND = "SUSPEND"
    RESUME = "RESUME"
    UPDATE = "UPDATE"


class DecoderManifestCanNetworkInterfaceType(str, Enum):
    CAN_INTERFACE = "CAN_INTERFACE"


class DecoderManifestCanSignalDecoderType(str, Enum):
    CAN_SIGNAL = "CAN_SIGNAL"


class DecoderManifestManifestStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"


class DecoderManifestObdNetworkInterfaceType(str, Enum):
    OBD_INTERFACE = "OBD_INTERFACE"


class DecoderManifestObdSignalDecoderType(str, Enum):
    OBD_SIGNAL = "OBD_SIGNAL"


class ModelManifestManifestStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"


class SignalCatalogNodeDataType(str, Enum):
    INT8 = "INT8"
    UINT8 = "UINT8"
    INT16 = "INT16"
    UINT16 = "UINT16"
    INT32 = "INT32"
    UINT32 = "UINT32"
    INT64 = "INT64"
    UINT64 = "UINT64"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    UNIX_TIMESTAMP = "UNIX_TIMESTAMP"
    INT8_ARRAY = "INT8_ARRAY"
    UINT8_ARRAY = "UINT8_ARRAY"
    INT16_ARRAY = "INT16_ARRAY"
    UINT16_ARRAY = "UINT16_ARRAY"
    INT32_ARRAY = "INT32_ARRAY"
    UINT32_ARRAY = "UINT32_ARRAY"
    INT64_ARRAY = "INT64_ARRAY"
    UINT64_ARRAY = "UINT64_ARRAY"
    BOOLEAN_ARRAY = "BOOLEAN_ARRAY"
    FLOAT_ARRAY = "FLOAT_ARRAY"
    DOUBLE_ARRAY = "DOUBLE_ARRAY"
    STRING_ARRAY = "STRING_ARRAY"
    UNIX_TIMESTAMP_ARRAY = "UNIX_TIMESTAMP_ARRAY"
    UNKNOWN = "UNKNOWN"


class VehicleAssociationBehavior(str, Enum):
    CREATE_IOT_THING = "CreateIotThing"
    VALIDATE_IOT_THING_EXISTS = "ValidateIotThingExists"
