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
from ._inputs import *

__all__ = ['EmailIdentityArgs', 'EmailIdentity']

@pulumi.input_type
class EmailIdentityArgs:
    def __init__(__self__, *,
                 email_identity: pulumi.Input[str],
                 configuration_set_attributes: Optional[pulumi.Input['EmailIdentityConfigurationSetAttributesArgs']] = None,
                 dkim_attributes: Optional[pulumi.Input['EmailIdentityDkimAttributesArgs']] = None,
                 dkim_signing_attributes: Optional[pulumi.Input['EmailIdentityDkimSigningAttributesArgs']] = None,
                 feedback_attributes: Optional[pulumi.Input['EmailIdentityFeedbackAttributesArgs']] = None,
                 mail_from_attributes: Optional[pulumi.Input['EmailIdentityMailFromAttributesArgs']] = None):
        """
        The set of arguments for constructing a EmailIdentity resource.
        :param pulumi.Input[str] email_identity: The email address or domain to verify.
        """
        pulumi.set(__self__, "email_identity", email_identity)
        if configuration_set_attributes is not None:
            pulumi.set(__self__, "configuration_set_attributes", configuration_set_attributes)
        if dkim_attributes is not None:
            pulumi.set(__self__, "dkim_attributes", dkim_attributes)
        if dkim_signing_attributes is not None:
            pulumi.set(__self__, "dkim_signing_attributes", dkim_signing_attributes)
        if feedback_attributes is not None:
            pulumi.set(__self__, "feedback_attributes", feedback_attributes)
        if mail_from_attributes is not None:
            pulumi.set(__self__, "mail_from_attributes", mail_from_attributes)

    @property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Input[str]:
        """
        The email address or domain to verify.
        """
        return pulumi.get(self, "email_identity")

    @email_identity.setter
    def email_identity(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_identity", value)

    @property
    @pulumi.getter(name="configurationSetAttributes")
    def configuration_set_attributes(self) -> Optional[pulumi.Input['EmailIdentityConfigurationSetAttributesArgs']]:
        return pulumi.get(self, "configuration_set_attributes")

    @configuration_set_attributes.setter
    def configuration_set_attributes(self, value: Optional[pulumi.Input['EmailIdentityConfigurationSetAttributesArgs']]):
        pulumi.set(self, "configuration_set_attributes", value)

    @property
    @pulumi.getter(name="dkimAttributes")
    def dkim_attributes(self) -> Optional[pulumi.Input['EmailIdentityDkimAttributesArgs']]:
        return pulumi.get(self, "dkim_attributes")

    @dkim_attributes.setter
    def dkim_attributes(self, value: Optional[pulumi.Input['EmailIdentityDkimAttributesArgs']]):
        pulumi.set(self, "dkim_attributes", value)

    @property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> Optional[pulumi.Input['EmailIdentityDkimSigningAttributesArgs']]:
        return pulumi.get(self, "dkim_signing_attributes")

    @dkim_signing_attributes.setter
    def dkim_signing_attributes(self, value: Optional[pulumi.Input['EmailIdentityDkimSigningAttributesArgs']]):
        pulumi.set(self, "dkim_signing_attributes", value)

    @property
    @pulumi.getter(name="feedbackAttributes")
    def feedback_attributes(self) -> Optional[pulumi.Input['EmailIdentityFeedbackAttributesArgs']]:
        return pulumi.get(self, "feedback_attributes")

    @feedback_attributes.setter
    def feedback_attributes(self, value: Optional[pulumi.Input['EmailIdentityFeedbackAttributesArgs']]):
        pulumi.set(self, "feedback_attributes", value)

    @property
    @pulumi.getter(name="mailFromAttributes")
    def mail_from_attributes(self) -> Optional[pulumi.Input['EmailIdentityMailFromAttributesArgs']]:
        return pulumi.get(self, "mail_from_attributes")

    @mail_from_attributes.setter
    def mail_from_attributes(self, value: Optional[pulumi.Input['EmailIdentityMailFromAttributesArgs']]):
        pulumi.set(self, "mail_from_attributes", value)


class EmailIdentity(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_set_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityConfigurationSetAttributesArgs']]] = None,
                 dkim_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityDkimAttributesArgs']]] = None,
                 dkim_signing_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityDkimSigningAttributesArgs']]] = None,
                 email_identity: Optional[pulumi.Input[str]] = None,
                 feedback_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityFeedbackAttributesArgs']]] = None,
                 mail_from_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityMailFromAttributesArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SES::EmailIdentity

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email_identity: The email address or domain to verify.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailIdentityArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SES::EmailIdentity

        :param str resource_name: The name of the resource.
        :param EmailIdentityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailIdentityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_set_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityConfigurationSetAttributesArgs']]] = None,
                 dkim_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityDkimAttributesArgs']]] = None,
                 dkim_signing_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityDkimSigningAttributesArgs']]] = None,
                 email_identity: Optional[pulumi.Input[str]] = None,
                 feedback_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityFeedbackAttributesArgs']]] = None,
                 mail_from_attributes: Optional[pulumi.Input[pulumi.InputType['EmailIdentityMailFromAttributesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EmailIdentityArgs.__new__(EmailIdentityArgs)

            __props__.__dict__["configuration_set_attributes"] = configuration_set_attributes
            __props__.__dict__["dkim_attributes"] = dkim_attributes
            __props__.__dict__["dkim_signing_attributes"] = dkim_signing_attributes
            if email_identity is None and not opts.urn:
                raise TypeError("Missing required property 'email_identity'")
            __props__.__dict__["email_identity"] = email_identity
            __props__.__dict__["feedback_attributes"] = feedback_attributes
            __props__.__dict__["mail_from_attributes"] = mail_from_attributes
            __props__.__dict__["dkim_dns_token_name1"] = None
            __props__.__dict__["dkim_dns_token_name2"] = None
            __props__.__dict__["dkim_dns_token_name3"] = None
            __props__.__dict__["dkim_dns_token_value1"] = None
            __props__.__dict__["dkim_dns_token_value2"] = None
            __props__.__dict__["dkim_dns_token_value3"] = None
        super(EmailIdentity, __self__).__init__(
            'aws-native:ses:EmailIdentity',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EmailIdentity':
        """
        Get an existing EmailIdentity resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EmailIdentityArgs.__new__(EmailIdentityArgs)

        __props__.__dict__["configuration_set_attributes"] = None
        __props__.__dict__["dkim_attributes"] = None
        __props__.__dict__["dkim_dns_token_name1"] = None
        __props__.__dict__["dkim_dns_token_name2"] = None
        __props__.__dict__["dkim_dns_token_name3"] = None
        __props__.__dict__["dkim_dns_token_value1"] = None
        __props__.__dict__["dkim_dns_token_value2"] = None
        __props__.__dict__["dkim_dns_token_value3"] = None
        __props__.__dict__["dkim_signing_attributes"] = None
        __props__.__dict__["email_identity"] = None
        __props__.__dict__["feedback_attributes"] = None
        __props__.__dict__["mail_from_attributes"] = None
        return EmailIdentity(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configurationSetAttributes")
    def configuration_set_attributes(self) -> pulumi.Output[Optional['outputs.EmailIdentityConfigurationSetAttributes']]:
        return pulumi.get(self, "configuration_set_attributes")

    @property
    @pulumi.getter(name="dkimAttributes")
    def dkim_attributes(self) -> pulumi.Output[Optional['outputs.EmailIdentityDkimAttributes']]:
        return pulumi.get(self, "dkim_attributes")

    @property
    @pulumi.getter(name="dkimDNSTokenName1")
    def dkim_dns_token_name1(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_name1")

    @property
    @pulumi.getter(name="dkimDNSTokenName2")
    def dkim_dns_token_name2(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_name2")

    @property
    @pulumi.getter(name="dkimDNSTokenName3")
    def dkim_dns_token_name3(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_name3")

    @property
    @pulumi.getter(name="dkimDNSTokenValue1")
    def dkim_dns_token_value1(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_value1")

    @property
    @pulumi.getter(name="dkimDNSTokenValue2")
    def dkim_dns_token_value2(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_value2")

    @property
    @pulumi.getter(name="dkimDNSTokenValue3")
    def dkim_dns_token_value3(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dkim_dns_token_value3")

    @property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> pulumi.Output[Optional['outputs.EmailIdentityDkimSigningAttributes']]:
        return pulumi.get(self, "dkim_signing_attributes")

    @property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Output[str]:
        """
        The email address or domain to verify.
        """
        return pulumi.get(self, "email_identity")

    @property
    @pulumi.getter(name="feedbackAttributes")
    def feedback_attributes(self) -> pulumi.Output[Optional['outputs.EmailIdentityFeedbackAttributes']]:
        return pulumi.get(self, "feedback_attributes")

    @property
    @pulumi.getter(name="mailFromAttributes")
    def mail_from_attributes(self) -> pulumi.Output[Optional['outputs.EmailIdentityMailFromAttributes']]:
        return pulumi.get(self, "mail_from_attributes")

