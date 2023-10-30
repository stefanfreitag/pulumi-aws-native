# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetCertificateAuthorityActivationResult',
    'AwaitableGetCertificateAuthorityActivationResult',
    'get_certificate_authority_activation',
    'get_certificate_authority_activation_output',
]

@pulumi.output_type
class GetCertificateAuthorityActivationResult:
    def __init__(__self__, complete_certificate_chain=None, status=None):
        if complete_certificate_chain and not isinstance(complete_certificate_chain, str):
            raise TypeError("Expected argument 'complete_certificate_chain' to be a str")
        pulumi.set(__self__, "complete_certificate_chain", complete_certificate_chain)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="completeCertificateChain")
    def complete_certificate_chain(self) -> Optional[str]:
        """
        The complete certificate chain, including the Certificate Authority certificate.
        """
        return pulumi.get(self, "complete_certificate_chain")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the Certificate Authority.
        """
        return pulumi.get(self, "status")


class AwaitableGetCertificateAuthorityActivationResult(GetCertificateAuthorityActivationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateAuthorityActivationResult(
            complete_certificate_chain=self.complete_certificate_chain,
            status=self.status)


def get_certificate_authority_activation(certificate_authority_arn: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateAuthorityActivationResult:
    """
    Used to install the certificate authority certificate and update the certificate authority status.


    :param str certificate_authority_arn: Arn of the Certificate Authority.
    """
    __args__ = dict()
    __args__['certificateAuthorityArn'] = certificate_authority_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:acmpca:getCertificateAuthorityActivation', __args__, opts=opts, typ=GetCertificateAuthorityActivationResult).value

    return AwaitableGetCertificateAuthorityActivationResult(
        complete_certificate_chain=pulumi.get(__ret__, 'complete_certificate_chain'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_certificate_authority_activation)
def get_certificate_authority_activation_output(certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateAuthorityActivationResult]:
    """
    Used to install the certificate authority certificate and update the certificate authority status.


    :param str certificate_authority_arn: Arn of the Certificate Authority.
    """
    ...
