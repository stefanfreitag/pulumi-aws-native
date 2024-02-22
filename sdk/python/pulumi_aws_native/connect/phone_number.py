# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['PhoneNumberArgs', 'PhoneNumber']

@pulumi.input_type
class PhoneNumberArgs:
    def __init__(__self__, *,
                 target_arn: pulumi.Input[str],
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 source_phone_number_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PhoneNumber resource.
        :param pulumi.Input[str] target_arn: The ARN of the target the phone number is claimed to.
        :param pulumi.Input[str] country_code: The phone number country code.
        :param pulumi.Input[str] description: The description of the phone number.
        :param pulumi.Input[str] prefix: The phone number prefix.
        :param pulumi.Input[str] source_phone_number_arn: The source phone number arn.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: One or more tags.
        :param pulumi.Input[str] type: The phone number type
        """
        pulumi.set(__self__, "target_arn", target_arn)
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if source_phone_number_arn is not None:
            pulumi.set(__self__, "source_phone_number_arn", source_phone_number_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the target the phone number is claimed to.
        """
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_arn", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number country code.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the phone number.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number prefix.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="sourcePhoneNumberArn")
    def source_phone_number_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The source phone number arn.
        """
        return pulumi.get(self, "source_phone_number_arn")

    @source_phone_number_arn.setter
    def source_phone_number_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_phone_number_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class PhoneNumber(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 source_phone_number_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::PhoneNumber

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] country_code: The phone number country code.
        :param pulumi.Input[str] description: The description of the phone number.
        :param pulumi.Input[str] prefix: The phone number prefix.
        :param pulumi.Input[str] source_phone_number_arn: The source phone number arn.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: One or more tags.
        :param pulumi.Input[str] target_arn: The ARN of the target the phone number is claimed to.
        :param pulumi.Input[str] type: The phone number type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PhoneNumberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::PhoneNumber

        :param str resource_name: The name of the resource.
        :param PhoneNumberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PhoneNumberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 source_phone_number_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PhoneNumberArgs.__new__(PhoneNumberArgs)

            __props__.__dict__["country_code"] = country_code
            __props__.__dict__["description"] = description
            __props__.__dict__["prefix"] = prefix
            __props__.__dict__["source_phone_number_arn"] = source_phone_number_arn
            __props__.__dict__["tags"] = tags
            if target_arn is None and not opts.urn:
                raise TypeError("Missing required property 'target_arn'")
            __props__.__dict__["target_arn"] = target_arn
            __props__.__dict__["type"] = type
            __props__.__dict__["address"] = None
            __props__.__dict__["phone_number_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["country_code", "prefix", "source_phone_number_arn", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PhoneNumber, __self__).__init__(
            'aws-native:connect:PhoneNumber',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PhoneNumber':
        """
        Get an existing PhoneNumber resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PhoneNumberArgs.__new__(PhoneNumberArgs)

        __props__.__dict__["address"] = None
        __props__.__dict__["country_code"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["phone_number_arn"] = None
        __props__.__dict__["prefix"] = None
        __props__.__dict__["source_phone_number_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_arn"] = None
        __props__.__dict__["type"] = None
        return PhoneNumber(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The phone number e164 address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Output[Optional[str]]:
        """
        The phone number country code.
        """
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the phone number.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="phoneNumberArn")
    def phone_number_arn(self) -> pulumi.Output[str]:
        """
        The phone number ARN
        """
        return pulumi.get(self, "phone_number_arn")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The phone number prefix.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="sourcePhoneNumberArn")
    def source_phone_number_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The source phone number arn.
        """
        return pulumi.get(self, "source_phone_number_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the target the phone number is claimed to.
        """
        return pulumi.get(self, "target_arn")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The phone number type
        """
        return pulumi.get(self, "type")

