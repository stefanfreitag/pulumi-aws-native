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
    'ChannelTagArgs',
    'PlaybackKeyPairTagArgs',
    'RecordingConfigurationDestinationConfigurationArgs',
    'RecordingConfigurationRenditionConfigurationArgs',
    'RecordingConfigurationS3DestinationConfigurationArgs',
    'RecordingConfigurationTagArgs',
    'RecordingConfigurationThumbnailConfigurationArgs',
    'StreamKeyTagArgs',
]

@pulumi.input_type
class ChannelTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        ChannelTagArgs._configure(
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


@pulumi.input_type
class PlaybackKeyPairTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        PlaybackKeyPairTagArgs._configure(
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


@pulumi.input_type
class RecordingConfigurationDestinationConfigurationArgs:
    def __init__(__self__, *,
                 s3: Optional[pulumi.Input['RecordingConfigurationS3DestinationConfigurationArgs']] = None):
        """
        Recording Destination Configuration.
        """
        RecordingConfigurationDestinationConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            s3=s3,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             s3: Optional[pulumi.Input['RecordingConfigurationS3DestinationConfigurationArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if s3 is not None:
            _setter("s3", s3)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['RecordingConfigurationS3DestinationConfigurationArgs']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['RecordingConfigurationS3DestinationConfigurationArgs']]):
        pulumi.set(self, "s3", value)


@pulumi.input_type
class RecordingConfigurationRenditionConfigurationArgs:
    def __init__(__self__, *,
                 rendition_selection: Optional[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionSelection']] = None,
                 renditions: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionsItem']]]] = None):
        """
        Rendition Configuration describes which renditions should be recorded for a stream.
        :param pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionSelection'] rendition_selection: Resolution Selection indicates which set of renditions are recorded for a stream.
        :param pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionsItem']]] renditions: Renditions indicates which renditions are recorded for a stream.
        """
        RecordingConfigurationRenditionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rendition_selection=rendition_selection,
            renditions=renditions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rendition_selection: Optional[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionSelection']] = None,
             renditions: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionsItem']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if rendition_selection is not None:
            _setter("rendition_selection", rendition_selection)
        if renditions is not None:
            _setter("renditions", renditions)

    @property
    @pulumi.getter(name="renditionSelection")
    def rendition_selection(self) -> Optional[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionSelection']]:
        """
        Resolution Selection indicates which set of renditions are recorded for a stream.
        """
        return pulumi.get(self, "rendition_selection")

    @rendition_selection.setter
    def rendition_selection(self, value: Optional[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionSelection']]):
        pulumi.set(self, "rendition_selection", value)

    @property
    @pulumi.getter
    def renditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionsItem']]]]:
        """
        Renditions indicates which renditions are recorded for a stream.
        """
        return pulumi.get(self, "renditions")

    @renditions.setter
    def renditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationRenditionConfigurationRenditionsItem']]]]):
        pulumi.set(self, "renditions", value)


@pulumi.input_type
class RecordingConfigurationS3DestinationConfigurationArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str]):
        """
        Recording S3 Destination Configuration.
        """
        RecordingConfigurationS3DestinationConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_name=bucket_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)


@pulumi.input_type
class RecordingConfigurationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        RecordingConfigurationTagArgs._configure(
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


@pulumi.input_type
class RecordingConfigurationThumbnailConfigurationArgs:
    def __init__(__self__, *,
                 recording_mode: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationRecordingMode']] = None,
                 resolution: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationResolution']] = None,
                 storage: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationThumbnailConfigurationStorageItem']]]] = None,
                 target_interval_seconds: Optional[pulumi.Input[int]] = None):
        """
        Recording Thumbnail Configuration.
        :param pulumi.Input['RecordingConfigurationThumbnailConfigurationRecordingMode'] recording_mode: Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.
        :param pulumi.Input['RecordingConfigurationThumbnailConfigurationResolution'] resolution: Resolution indicates the desired resolution of recorded thumbnails.
        :param pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationThumbnailConfigurationStorageItem']]] storage: Storage indicates the format in which thumbnails are recorded.
        :param pulumi.Input[int] target_interval_seconds: Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.
        """
        RecordingConfigurationThumbnailConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            recording_mode=recording_mode,
            resolution=resolution,
            storage=storage,
            target_interval_seconds=target_interval_seconds,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             recording_mode: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationRecordingMode']] = None,
             resolution: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationResolution']] = None,
             storage: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationThumbnailConfigurationStorageItem']]]] = None,
             target_interval_seconds: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if recording_mode is not None:
            _setter("recording_mode", recording_mode)
        if resolution is not None:
            _setter("resolution", resolution)
        if storage is not None:
            _setter("storage", storage)
        if target_interval_seconds is not None:
            _setter("target_interval_seconds", target_interval_seconds)

    @property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationRecordingMode']]:
        """
        Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.
        """
        return pulumi.get(self, "recording_mode")

    @recording_mode.setter
    def recording_mode(self, value: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationRecordingMode']]):
        pulumi.set(self, "recording_mode", value)

    @property
    @pulumi.getter
    def resolution(self) -> Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationResolution']]:
        """
        Resolution indicates the desired resolution of recorded thumbnails.
        """
        return pulumi.get(self, "resolution")

    @resolution.setter
    def resolution(self, value: Optional[pulumi.Input['RecordingConfigurationThumbnailConfigurationResolution']]):
        pulumi.set(self, "resolution", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationThumbnailConfigurationStorageItem']]]]:
        """
        Storage indicates the format in which thumbnails are recorded.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RecordingConfigurationThumbnailConfigurationStorageItem']]]]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter(name="targetIntervalSeconds")
    def target_interval_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.
        """
        return pulumi.get(self, "target_interval_seconds")

    @target_interval_seconds.setter
    def target_interval_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "target_interval_seconds", value)


@pulumi.input_type
class StreamKeyTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        StreamKeyTagArgs._configure(
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


