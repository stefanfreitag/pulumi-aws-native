# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OriginEndpointAdMarkerHls',
    'OriginEndpointCmafEncryptionMethod',
    'OriginEndpointContainerType',
    'OriginEndpointDrmSystem',
    'OriginEndpointPresetSpeke20Audio',
    'OriginEndpointPresetSpeke20Video',
    'OriginEndpointScteFilter',
    'OriginEndpointTsEncryptionMethod',
]


class OriginEndpointAdMarkerHls(str, Enum):
    DATERANGE = "DATERANGE"


class OriginEndpointCmafEncryptionMethod(str, Enum):
    CENC = "CENC"
    CBCS = "CBCS"


class OriginEndpointContainerType(str, Enum):
    TS = "TS"
    CMAF = "CMAF"


class OriginEndpointDrmSystem(str, Enum):
    CLEAR_KEY_AES128 = "CLEAR_KEY_AES_128"
    FAIRPLAY = "FAIRPLAY"
    PLAYREADY = "PLAYREADY"
    WIDEVINE = "WIDEVINE"


class OriginEndpointPresetSpeke20Audio(str, Enum):
    PRESET_AUDIO1 = "PRESET_AUDIO_1"
    PRESET_AUDIO2 = "PRESET_AUDIO_2"
    PRESET_AUDIO3 = "PRESET_AUDIO_3"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class OriginEndpointPresetSpeke20Video(str, Enum):
    PRESET_VIDEO1 = "PRESET_VIDEO_1"
    PRESET_VIDEO2 = "PRESET_VIDEO_2"
    PRESET_VIDEO3 = "PRESET_VIDEO_3"
    PRESET_VIDEO4 = "PRESET_VIDEO_4"
    PRESET_VIDEO5 = "PRESET_VIDEO_5"
    PRESET_VIDEO6 = "PRESET_VIDEO_6"
    PRESET_VIDEO7 = "PRESET_VIDEO_7"
    PRESET_VIDEO8 = "PRESET_VIDEO_8"
    SHARED = "SHARED"
    UNENCRYPTED = "UNENCRYPTED"


class OriginEndpointScteFilter(str, Enum):
    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK_ = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"
    PROGRAM = "PROGRAM"


class OriginEndpointTsEncryptionMethod(str, Enum):
    AES128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"
