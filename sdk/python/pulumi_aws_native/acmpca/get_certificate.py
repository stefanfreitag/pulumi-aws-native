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
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    def __init__(__self__, arn=None, certificate=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the issued certificate.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def certificate(self) -> Optional[str]:
        """
        The issued certificate in base 64 PEM-encoded format.
        """
        return pulumi.get(self, "certificate")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            arn=self.arn,
            certificate=self.certificate)


def get_certificate(arn: Optional[str] = None,
                    certificate_authority_arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    A certificate issued via a private certificate authority


    :param str arn: The ARN of the issued certificate.
    :param str certificate_authority_arn: The Amazon Resource Name (ARN) for the private CA to issue the certificate.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['certificateAuthorityArn'] = certificate_authority_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:acmpca:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        arn=pulumi.get(__ret__, 'arn'),
        certificate=pulumi.get(__ret__, 'certificate'))


@_utilities.lift_output_func(get_certificate)
def get_certificate_output(arn: Optional[pulumi.Input[str]] = None,
                           certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    A certificate issued via a private certificate authority


    :param str arn: The ARN of the issued certificate.
    :param str certificate_authority_arn: The Amazon Resource Name (ARN) for the private CA to issue the certificate.
    """
    ...
