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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['CaCertificateArgs', 'CaCertificate']

@pulumi.input_type
class CaCertificateArgs:
    def __init__(__self__, *,
                 ca_certificate_pem: pulumi.Input[str],
                 status: pulumi.Input['CaCertificateStatus'],
                 auto_registration_status: Optional[pulumi.Input['CaCertificateAutoRegistrationStatus']] = None,
                 certificate_mode: Optional[pulumi.Input['CaCertificateCertificateMode']] = None,
                 registration_config: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']] = None,
                 remove_auto_registration: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CaCertificate resource.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] verification_certificate_pem: The private key verification certificate.
        """
        pulumi.set(__self__, "ca_certificate_pem", ca_certificate_pem)
        pulumi.set(__self__, "status", status)
        if auto_registration_status is not None:
            pulumi.set(__self__, "auto_registration_status", auto_registration_status)
        if certificate_mode is not None:
            pulumi.set(__self__, "certificate_mode", certificate_mode)
        if registration_config is not None:
            pulumi.set(__self__, "registration_config", registration_config)
        if remove_auto_registration is not None:
            pulumi.set(__self__, "remove_auto_registration", remove_auto_registration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if verification_certificate_pem is not None:
            pulumi.set(__self__, "verification_certificate_pem", verification_certificate_pem)

    @property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ca_certificate_pem")

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: pulumi.Input[str]):
        pulumi.set(self, "ca_certificate_pem", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['CaCertificateStatus']:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['CaCertificateStatus']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="autoRegistrationStatus")
    def auto_registration_status(self) -> Optional[pulumi.Input['CaCertificateAutoRegistrationStatus']]:
        return pulumi.get(self, "auto_registration_status")

    @auto_registration_status.setter
    def auto_registration_status(self, value: Optional[pulumi.Input['CaCertificateAutoRegistrationStatus']]):
        pulumi.set(self, "auto_registration_status", value)

    @property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input['CaCertificateCertificateMode']]:
        return pulumi.get(self, "certificate_mode")

    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input['CaCertificateCertificateMode']]):
        pulumi.set(self, "certificate_mode", value)

    @property
    @pulumi.getter(name="registrationConfig")
    def registration_config(self) -> Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]:
        return pulumi.get(self, "registration_config")

    @registration_config.setter
    def registration_config(self, value: Optional[pulumi.Input['CaCertificateRegistrationConfigArgs']]):
        pulumi.set(self, "registration_config", value)

    @property
    @pulumi.getter(name="removeAutoRegistration")
    def remove_auto_registration(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "remove_auto_registration")

    @remove_auto_registration.setter
    def remove_auto_registration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_auto_registration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> Optional[pulumi.Input[str]]:
        """
        The private key verification certificate.
        """
        return pulumi.get(self, "verification_certificate_pem")

    @verification_certificate_pem.setter
    def verification_certificate_pem(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verification_certificate_pem", value)


class CaCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_registration_status: Optional[pulumi.Input['CaCertificateAutoRegistrationStatus']] = None,
                 ca_certificate_pem: Optional[pulumi.Input[str]] = None,
                 certificate_mode: Optional[pulumi.Input['CaCertificateCertificateMode']] = None,
                 registration_config: Optional[pulumi.Input[pulumi.InputType['CaCertificateRegistrationConfigArgs']]] = None,
                 remove_auto_registration: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input['CaCertificateStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Registers a CA Certificate in IoT.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] verification_certificate_pem: The private key verification certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CaCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Registers a CA Certificate in IoT.

        :param str resource_name: The name of the resource.
        :param CaCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CaCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_registration_status: Optional[pulumi.Input['CaCertificateAutoRegistrationStatus']] = None,
                 ca_certificate_pem: Optional[pulumi.Input[str]] = None,
                 certificate_mode: Optional[pulumi.Input['CaCertificateCertificateMode']] = None,
                 registration_config: Optional[pulumi.Input[pulumi.InputType['CaCertificateRegistrationConfigArgs']]] = None,
                 remove_auto_registration: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input['CaCertificateStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 verification_certificate_pem: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CaCertificateArgs.__new__(CaCertificateArgs)

            __props__.__dict__["auto_registration_status"] = auto_registration_status
            if ca_certificate_pem is None and not opts.urn:
                raise TypeError("Missing required property 'ca_certificate_pem'")
            __props__.__dict__["ca_certificate_pem"] = ca_certificate_pem
            __props__.__dict__["certificate_mode"] = certificate_mode
            __props__.__dict__["registration_config"] = registration_config
            __props__.__dict__["remove_auto_registration"] = remove_auto_registration
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["verification_certificate_pem"] = verification_certificate_pem
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["ca_certificate_pem", "certificate_mode", "verification_certificate_pem"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CaCertificate, __self__).__init__(
            'aws-native:iot:CaCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CaCertificate':
        """
        Get an existing CaCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CaCertificateArgs.__new__(CaCertificateArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_registration_status"] = None
        __props__.__dict__["ca_certificate_pem"] = None
        __props__.__dict__["certificate_mode"] = None
        __props__.__dict__["registration_config"] = None
        __props__.__dict__["remove_auto_registration"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["verification_certificate_pem"] = None
        return CaCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoRegistrationStatus")
    def auto_registration_status(self) -> pulumi.Output[Optional['CaCertificateAutoRegistrationStatus']]:
        return pulumi.get(self, "auto_registration_status")

    @property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ca_certificate_pem")

    @property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> pulumi.Output[Optional['CaCertificateCertificateMode']]:
        return pulumi.get(self, "certificate_mode")

    @property
    @pulumi.getter(name="registrationConfig")
    def registration_config(self) -> pulumi.Output[Optional['outputs.CaCertificateRegistrationConfig']]:
        return pulumi.get(self, "registration_config")

    @property
    @pulumi.getter(name="removeAutoRegistration")
    def remove_auto_registration(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "remove_auto_registration")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['CaCertificateStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> pulumi.Output[Optional[str]]:
        """
        The private key verification certificate.
        """
        return pulumi.get(self, "verification_certificate_pem")

