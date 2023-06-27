# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CampaignCompression',
    'CampaignDiagnosticsMode',
    'CampaignSpoolingMode',
    'CampaignStatus',
    'CampaignUpdateCampaignAction',
    'DecoderManifestCanNetworkInterfaceType',
    'DecoderManifestCanSignalDecoderType',
    'DecoderManifestManifestStatus',
    'DecoderManifestObdNetworkInterfaceType',
    'DecoderManifestObdSignalDecoderType',
    'ModelManifestManifestStatus',
    'VehicleAssociationBehavior',
]


class CampaignCompression(str, Enum):
    OFF = "OFF"
    SNAPPY = "SNAPPY"


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


class VehicleAssociationBehavior(str, Enum):
    CREATE_IOT_THING = "CreateIotThing"
    VALIDATE_IOT_THING_EXISTS = "ValidateIotThingExists"
