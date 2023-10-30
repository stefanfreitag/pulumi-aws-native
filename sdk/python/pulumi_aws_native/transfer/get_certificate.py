# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    def __init__(__self__, active_date=None, arn=None, certificate_id=None, description=None, inactive_date=None, not_after_date=None, not_before_date=None, serial=None, status=None, tags=None, type=None, usage=None):
        if active_date and not isinstance(active_date, str):
            raise TypeError("Expected argument 'active_date' to be a str")
        pulumi.set(__self__, "active_date", active_date)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if certificate_id and not isinstance(certificate_id, str):
            raise TypeError("Expected argument 'certificate_id' to be a str")
        pulumi.set(__self__, "certificate_id", certificate_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if inactive_date and not isinstance(inactive_date, str):
            raise TypeError("Expected argument 'inactive_date' to be a str")
        pulumi.set(__self__, "inactive_date", inactive_date)
        if not_after_date and not isinstance(not_after_date, str):
            raise TypeError("Expected argument 'not_after_date' to be a str")
        pulumi.set(__self__, "not_after_date", not_after_date)
        if not_before_date and not isinstance(not_before_date, str):
            raise TypeError("Expected argument 'not_before_date' to be a str")
        pulumi.set(__self__, "not_before_date", not_before_date)
        if serial and not isinstance(serial, str):
            raise TypeError("Expected argument 'serial' to be a str")
        pulumi.set(__self__, "serial", serial)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if usage and not isinstance(usage, str):
            raise TypeError("Expected argument 'usage' to be a str")
        pulumi.set(__self__, "usage", usage)

    @property
    @pulumi.getter(name="activeDate")
    def active_date(self) -> Optional[str]:
        """
        Specifies the active date for the certificate.
        """
        return pulumi.get(self, "active_date")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the agreement.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[str]:
        """
        A unique identifier for the certificate.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A textual description for the certificate.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inactiveDate")
    def inactive_date(self) -> Optional[str]:
        """
        Specifies the inactive date for the certificate.
        """
        return pulumi.get(self, "inactive_date")

    @property
    @pulumi.getter(name="notAfterDate")
    def not_after_date(self) -> Optional[str]:
        """
        Specifies the not after date for the certificate.
        """
        return pulumi.get(self, "not_after_date")

    @property
    @pulumi.getter(name="notBeforeDate")
    def not_before_date(self) -> Optional[str]:
        """
        Specifies the not before date for the certificate.
        """
        return pulumi.get(self, "not_before_date")

    @property
    @pulumi.getter
    def serial(self) -> Optional[str]:
        """
        Specifies Certificate's serial.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def status(self) -> Optional['CertificateStatus']:
        """
        A status description for the certificate.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CertificateTag']]:
        """
        Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional['CertificateType']:
        """
        Describing the type of certificate. With or without a private key.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def usage(self) -> Optional['CertificateUsage']:
        """
        Specifies the usage type for the certificate.
        """
        return pulumi.get(self, "usage")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            active_date=self.active_date,
            arn=self.arn,
            certificate_id=self.certificate_id,
            description=self.description,
            inactive_date=self.inactive_date,
            not_after_date=self.not_after_date,
            not_before_date=self.not_before_date,
            serial=self.serial,
            status=self.status,
            tags=self.tags,
            type=self.type,
            usage=self.usage)


def get_certificate(certificate_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Resource Type definition for AWS::Transfer::Certificate


    :param str certificate_id: A unique identifier for the certificate.
    """
    __args__ = dict()
    __args__['certificateId'] = certificate_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:transfer:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        active_date=pulumi.get(__ret__, 'active_date'),
        arn=pulumi.get(__ret__, 'arn'),
        certificate_id=pulumi.get(__ret__, 'certificate_id'),
        description=pulumi.get(__ret__, 'description'),
        inactive_date=pulumi.get(__ret__, 'inactive_date'),
        not_after_date=pulumi.get(__ret__, 'not_after_date'),
        not_before_date=pulumi.get(__ret__, 'not_before_date'),
        serial=pulumi.get(__ret__, 'serial'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        usage=pulumi.get(__ret__, 'usage'))


@_utilities.lift_output_func(get_certificate)
def get_certificate_output(certificate_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Resource Type definition for AWS::Transfer::Certificate


    :param str certificate_id: A unique identifier for the certificate.
    """
    ...
