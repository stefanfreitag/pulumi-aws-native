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
    'GetEnclaveCertificateIamRoleAssociationResult',
    'AwaitableGetEnclaveCertificateIamRoleAssociationResult',
    'get_enclave_certificate_iam_role_association',
    'get_enclave_certificate_iam_role_association_output',
]

@pulumi.output_type
class GetEnclaveCertificateIamRoleAssociationResult:
    def __init__(__self__, certificate_s3_bucket_name=None, certificate_s3_object_key=None, encryption_kms_key_id=None):
        if certificate_s3_bucket_name and not isinstance(certificate_s3_bucket_name, str):
            raise TypeError("Expected argument 'certificate_s3_bucket_name' to be a str")
        pulumi.set(__self__, "certificate_s3_bucket_name", certificate_s3_bucket_name)
        if certificate_s3_object_key and not isinstance(certificate_s3_object_key, str):
            raise TypeError("Expected argument 'certificate_s3_object_key' to be a str")
        pulumi.set(__self__, "certificate_s3_object_key", certificate_s3_object_key)
        if encryption_kms_key_id and not isinstance(encryption_kms_key_id, str):
            raise TypeError("Expected argument 'encryption_kms_key_id' to be a str")
        pulumi.set(__self__, "encryption_kms_key_id", encryption_kms_key_id)

    @property
    @pulumi.getter(name="certificateS3BucketName")
    def certificate_s3_bucket_name(self) -> Optional[str]:
        """
        The name of the Amazon S3 bucket to which the certificate was uploaded.
        """
        return pulumi.get(self, "certificate_s3_bucket_name")

    @property
    @pulumi.getter(name="certificateS3ObjectKey")
    def certificate_s3_object_key(self) -> Optional[str]:
        """
        The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored.
        """
        return pulumi.get(self, "certificate_s3_object_key")

    @property
    @pulumi.getter(name="encryptionKmsKeyId")
    def encryption_kms_key_id(self) -> Optional[str]:
        """
        The ID of the AWS KMS CMK used to encrypt the private key of the certificate.
        """
        return pulumi.get(self, "encryption_kms_key_id")


class AwaitableGetEnclaveCertificateIamRoleAssociationResult(GetEnclaveCertificateIamRoleAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnclaveCertificateIamRoleAssociationResult(
            certificate_s3_bucket_name=self.certificate_s3_bucket_name,
            certificate_s3_object_key=self.certificate_s3_object_key,
            encryption_kms_key_id=self.encryption_kms_key_id)


def get_enclave_certificate_iam_role_association(certificate_arn: Optional[str] = None,
                                                 role_arn: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnclaveCertificateIamRoleAssociationResult:
    """
    Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.


    :param str certificate_arn: The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.
    :param str role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.
    """
    __args__ = dict()
    __args__['certificateArn'] = certificate_arn
    __args__['roleArn'] = role_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getEnclaveCertificateIamRoleAssociation', __args__, opts=opts, typ=GetEnclaveCertificateIamRoleAssociationResult).value

    return AwaitableGetEnclaveCertificateIamRoleAssociationResult(
        certificate_s3_bucket_name=pulumi.get(__ret__, 'certificate_s3_bucket_name'),
        certificate_s3_object_key=pulumi.get(__ret__, 'certificate_s3_object_key'),
        encryption_kms_key_id=pulumi.get(__ret__, 'encryption_kms_key_id'))


@_utilities.lift_output_func(get_enclave_certificate_iam_role_association)
def get_enclave_certificate_iam_role_association_output(certificate_arn: Optional[pulumi.Input[str]] = None,
                                                        role_arn: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnclaveCertificateIamRoleAssociationResult]:
    """
    Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.


    :param str certificate_arn: The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.
    :param str role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.
    """
    ...
