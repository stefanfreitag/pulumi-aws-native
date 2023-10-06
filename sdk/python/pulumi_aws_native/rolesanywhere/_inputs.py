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
    'CrlTagArgs',
    'ProfileTagArgs',
    'TrustAnchorNotificationSettingArgs',
    'TrustAnchorSourceData0PropertiesArgs',
    'TrustAnchorSourceData1PropertiesArgs',
    'TrustAnchorSourceArgs',
    'TrustAnchorTagArgs',
]

@pulumi.input_type
class CrlTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        CrlTagArgs._configure(
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
class ProfileTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        ProfileTagArgs._configure(
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
class TrustAnchorNotificationSettingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 event: pulumi.Input['TrustAnchorNotificationEvent'],
                 channel: Optional[pulumi.Input['TrustAnchorNotificationChannel']] = None,
                 threshold: Optional[pulumi.Input[float]] = None):
        TrustAnchorNotificationSettingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            event=event,
            channel=channel,
            threshold=threshold,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: pulumi.Input[bool],
             event: pulumi.Input['TrustAnchorNotificationEvent'],
             channel: Optional[pulumi.Input['TrustAnchorNotificationChannel']] = None,
             threshold: Optional[pulumi.Input[float]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enabled", enabled)
        _setter("event", event)
        if channel is not None:
            _setter("channel", channel)
        if threshold is not None:
            _setter("threshold", threshold)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def event(self) -> pulumi.Input['TrustAnchorNotificationEvent']:
        return pulumi.get(self, "event")

    @event.setter
    def event(self, value: pulumi.Input['TrustAnchorNotificationEvent']):
        pulumi.set(self, "event", value)

    @property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input['TrustAnchorNotificationChannel']]:
        return pulumi.get(self, "channel")

    @channel.setter
    def channel(self, value: Optional[pulumi.Input['TrustAnchorNotificationChannel']]):
        pulumi.set(self, "channel", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold", value)


@pulumi.input_type
class TrustAnchorSourceData0PropertiesArgs:
    def __init__(__self__, *,
                 x509_certificate_data: pulumi.Input[str]):
        TrustAnchorSourceData0PropertiesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            x509_certificate_data=x509_certificate_data,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             x509_certificate_data: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("x509_certificate_data", x509_certificate_data)

    @property
    @pulumi.getter(name="x509CertificateData")
    def x509_certificate_data(self) -> pulumi.Input[str]:
        return pulumi.get(self, "x509_certificate_data")

    @x509_certificate_data.setter
    def x509_certificate_data(self, value: pulumi.Input[str]):
        pulumi.set(self, "x509_certificate_data", value)


@pulumi.input_type
class TrustAnchorSourceData1PropertiesArgs:
    def __init__(__self__, *,
                 acm_pca_arn: pulumi.Input[str]):
        TrustAnchorSourceData1PropertiesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            acm_pca_arn=acm_pca_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             acm_pca_arn: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("acm_pca_arn", acm_pca_arn)

    @property
    @pulumi.getter(name="acmPcaArn")
    def acm_pca_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "acm_pca_arn")

    @acm_pca_arn.setter
    def acm_pca_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "acm_pca_arn", value)


@pulumi.input_type
class TrustAnchorSourceArgs:
    def __init__(__self__, *,
                 source_data: Optional[pulumi.Input[Union['TrustAnchorSourceData0PropertiesArgs', 'TrustAnchorSourceData1PropertiesArgs']]] = None,
                 source_type: Optional[pulumi.Input['TrustAnchorType']] = None):
        TrustAnchorSourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source_data=source_data,
            source_type=source_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source_data: Optional[pulumi.Input[Union['TrustAnchorSourceData0PropertiesArgs', 'TrustAnchorSourceData1PropertiesArgs']]] = None,
             source_type: Optional[pulumi.Input['TrustAnchorType']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if source_data is not None:
            _setter("source_data", source_data)
        if source_type is not None:
            _setter("source_type", source_type)

    @property
    @pulumi.getter(name="sourceData")
    def source_data(self) -> Optional[pulumi.Input[Union['TrustAnchorSourceData0PropertiesArgs', 'TrustAnchorSourceData1PropertiesArgs']]]:
        return pulumi.get(self, "source_data")

    @source_data.setter
    def source_data(self, value: Optional[pulumi.Input[Union['TrustAnchorSourceData0PropertiesArgs', 'TrustAnchorSourceData1PropertiesArgs']]]):
        pulumi.set(self, "source_data", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input['TrustAnchorType']]:
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input['TrustAnchorType']]):
        pulumi.set(self, "source_type", value)


@pulumi.input_type
class TrustAnchorTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        TrustAnchorTagArgs._configure(
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


