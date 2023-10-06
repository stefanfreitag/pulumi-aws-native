# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AccountExpiryEventsConfigurationArgs',
    'CertificateDomainValidationOptionArgs',
    'CertificateTagArgs',
]

@pulumi.input_type
class AccountExpiryEventsConfigurationArgs:
    def __init__(__self__, *,
                 days_before_expiry: Optional[pulumi.Input[int]] = None):
        AccountExpiryEventsConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            days_before_expiry=days_before_expiry,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             days_before_expiry: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if days_before_expiry is not None:
            _setter("days_before_expiry", days_before_expiry)

    @property
    @pulumi.getter(name="daysBeforeExpiry")
    def days_before_expiry(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "days_before_expiry")

    @days_before_expiry.setter
    def days_before_expiry(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "days_before_expiry", value)


@pulumi.input_type
class CertificateDomainValidationOptionArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 validation_domain: Optional[pulumi.Input[str]] = None):
        CertificateDomainValidationOptionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_name=domain_name,
            hosted_zone_id=hosted_zone_id,
            validation_domain=validation_domain,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_name: pulumi.Input[str],
             hosted_zone_id: Optional[pulumi.Input[str]] = None,
             validation_domain: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("domain_name", domain_name)
        if hosted_zone_id is not None:
            _setter("hosted_zone_id", hosted_zone_id)
        if validation_domain is not None:
            _setter("validation_domain", validation_domain)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hosted_zone_id", value)

    @property
    @pulumi.getter(name="validationDomain")
    def validation_domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "validation_domain")

    @validation_domain.setter
    def validation_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_domain", value)


@pulumi.input_type
class CertificateTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        CertificateTagArgs._configure(
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


