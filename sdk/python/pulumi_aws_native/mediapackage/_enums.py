# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OriginEndpointAdsOnDeliveryRestrictions',
    'OriginEndpointDashPackageAdTriggersItem',
    'OriginEndpointDashPackageManifestLayout',
    'OriginEndpointDashPackagePeriodTriggersItem',
    'OriginEndpointDashPackageProfile',
    'OriginEndpointDashPackageSegmentTemplateFormat',
    'OriginEndpointDashPackageUtcTiming',
    'OriginEndpointHlsEncryptionEncryptionMethod',
    'OriginEndpointHlsManifestAdMarkers',
    'OriginEndpointHlsManifestAdTriggersItem',
    'OriginEndpointHlsManifestPlaylistType',
    'OriginEndpointHlsPackageAdMarkers',
    'OriginEndpointHlsPackageAdTriggersItem',
    'OriginEndpointHlsPackagePlaylistType',
    'OriginEndpointOrigination',
    'OriginEndpointStreamSelectionStreamOrder',
    'PackagingConfigurationDashManifestManifestLayout',
    'PackagingConfigurationDashManifestProfile',
    'PackagingConfigurationDashPackageSegmentTemplateFormat',
    'PackagingConfigurationHlsEncryptionEncryptionMethod',
    'PackagingConfigurationHlsManifestAdMarkers',
    'PackagingConfigurationStreamSelectionStreamOrder',
]


class OriginEndpointAdsOnDeliveryRestrictions(str, Enum):
    """
    This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad.  Choosing "NONE" means no SCTE-35 messages become ads.  Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads.  Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads.  Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads.  Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    """
    NONE = "NONE"
    RESTRICTED = "RESTRICTED"
    UNRESTRICTED = "UNRESTRICTED"
    BOTH = "BOTH"


class OriginEndpointDashPackageAdTriggersItem(str, Enum):
    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK_ = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"


class OriginEndpointDashPackageManifestLayout(str, Enum):
    """
    Determines the position of some tags in the Media Presentation Description (MPD).  When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation.  When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    """
    FULL = "FULL"
    COMPACT = "COMPACT"


class OriginEndpointDashPackagePeriodTriggersItem(str, Enum):
    ADS = "ADS"


class OriginEndpointDashPackageProfile(str, Enum):
    """
    The Dynamic Adaptive Streaming over HTTP (DASH) profile type.  When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    """
    NONE = "NONE"
    HBBTV15 = "HBBTV_1_5"


class OriginEndpointDashPackageSegmentTemplateFormat(str, Enum):
    """
    Determines the type of SegmentTemplate included in the Media Presentation Description (MPD).  When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs.  When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    """
    NUMBER_WITH_TIMELINE = "NUMBER_WITH_TIMELINE"
    TIME_WITH_TIMELINE = "TIME_WITH_TIMELINE"
    NUMBER_WITH_DURATION = "NUMBER_WITH_DURATION"


class OriginEndpointDashPackageUtcTiming(str, Enum):
    """
    Determines the type of UTCTiming included in the Media Presentation Description (MPD)
    """
    HTTP_ISO = "HTTP-ISO"
    HTTP_HEAD = "HTTP-HEAD"
    NONE = "NONE"


class OriginEndpointHlsEncryptionEncryptionMethod(str, Enum):
    """
    The encryption method to use.
    """
    AES128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


class OriginEndpointHlsManifestAdMarkers(str, Enum):
    """
    This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source. "DATERANGE" inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.
    """
    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"
    DATERANGE = "DATERANGE"


class OriginEndpointHlsManifestAdTriggersItem(str, Enum):
    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK_ = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"


class OriginEndpointHlsManifestPlaylistType(str, Enum):
    """
    The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    """
    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class OriginEndpointHlsPackageAdMarkers(str, Enum):
    """
    This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source. "DATERANGE" inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.
    """
    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"
    DATERANGE = "DATERANGE"


class OriginEndpointHlsPackageAdTriggersItem(str, Enum):
    SPLICE_INSERT = "SPLICE_INSERT"
    BREAK_ = "BREAK"
    PROVIDER_ADVERTISEMENT = "PROVIDER_ADVERTISEMENT"
    DISTRIBUTOR_ADVERTISEMENT = "DISTRIBUTOR_ADVERTISEMENT"
    PROVIDER_PLACEMENT_OPPORTUNITY = "PROVIDER_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_PLACEMENT_OPPORTUNITY"
    PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY = "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"
    DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY = "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"


class OriginEndpointHlsPackagePlaylistType(str, Enum):
    """
    The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    """
    NONE = "NONE"
    EVENT = "EVENT"
    VOD = "VOD"


class OriginEndpointOrigination(str, Enum):
    """
    Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
    """
    ALLOW = "ALLOW"
    DENY = "DENY"


class OriginEndpointStreamSelectionStreamOrder(str, Enum):
    """
    A directive that determines the order of streams in the output.
    """
    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"


class PackagingConfigurationDashManifestManifestLayout(str, Enum):
    """
    Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    """
    FULL = "FULL"
    COMPACT = "COMPACT"


class PackagingConfigurationDashManifestProfile(str, Enum):
    """
    The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    """
    NONE = "NONE"
    HBBTV15 = "HBBTV_1_5"


class PackagingConfigurationDashPackageSegmentTemplateFormat(str, Enum):
    """
    Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    """
    NUMBER_WITH_TIMELINE = "NUMBER_WITH_TIMELINE"
    TIME_WITH_TIMELINE = "TIME_WITH_TIMELINE"
    NUMBER_WITH_DURATION = "NUMBER_WITH_DURATION"


class PackagingConfigurationHlsEncryptionEncryptionMethod(str, Enum):
    """
    The encryption method to use.
    """
    AES128 = "AES_128"
    SAMPLE_AES = "SAMPLE_AES"


class PackagingConfigurationHlsManifestAdMarkers(str, Enum):
    """
    This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    """
    NONE = "NONE"
    SCTE35_ENHANCED = "SCTE35_ENHANCED"
    PASSTHROUGH = "PASSTHROUGH"


class PackagingConfigurationStreamSelectionStreamOrder(str, Enum):
    """
    A directive that determines the order of streams in the output.
    """
    ORIGINAL = "ORIGINAL"
    VIDEO_BITRATE_ASCENDING = "VIDEO_BITRATE_ASCENDING"
    VIDEO_BITRATE_DESCENDING = "VIDEO_BITRATE_DESCENDING"
