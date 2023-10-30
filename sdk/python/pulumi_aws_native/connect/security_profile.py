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

__all__ = ['SecurityProfileArgs', 'SecurityProfile']

@pulumi.input_type
class SecurityProfileArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 allowed_access_control_tags: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_profile_name: Optional[pulumi.Input[str]] = None,
                 tag_restricted_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]] = None):
        """
        The set of arguments for constructing a SecurityProfile resource.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]] allowed_access_control_tags: The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        :param pulumi.Input[str] description: The description of the security profile.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: Permissions assigned to the security profile.
        :param pulumi.Input[str] security_profile_name: The name of the security profile.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tag_restricted_resources: The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]] tags: The tags used to organize, track, or control access for this resource.
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        if allowed_access_control_tags is not None:
            pulumi.set(__self__, "allowed_access_control_tags", allowed_access_control_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if security_profile_name is not None:
            pulumi.set(__self__, "security_profile_name", security_profile_name)
        if tag_restricted_resources is not None:
            pulumi.set(__self__, "tag_restricted_resources", tag_restricted_resources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter(name="allowedAccessControlTags")
    def allowed_access_control_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]]:
        """
        The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        """
        return pulumi.get(self, "allowed_access_control_tags")

    @allowed_access_control_tags.setter
    def allowed_access_control_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]]):
        pulumi.set(self, "allowed_access_control_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the security profile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Permissions assigned to the security profile.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="securityProfileName")
    def security_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security profile.
        """
        return pulumi.get(self, "security_profile_name")

    @security_profile_name.setter
    def security_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_profile_name", value)

    @property
    @pulumi.getter(name="tagRestrictedResources")
    def tag_restricted_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        """
        return pulumi.get(self, "tag_restricted_resources")

    @tag_restricted_resources.setter
    def tag_restricted_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tag_restricted_resources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]]:
        """
        The tags used to organize, track, or control access for this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)


class SecurityProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_access_control_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_profile_name: Optional[pulumi.Input[str]] = None,
                 tag_restricted_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::SecurityProfile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]] allowed_access_control_tags: The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        :param pulumi.Input[str] description: The description of the security profile.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: Permissions assigned to the security profile.
        :param pulumi.Input[str] security_profile_name: The name of the security profile.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tag_restricted_resources: The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]] tags: The tags used to organize, track, or control access for this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::SecurityProfile

        :param str resource_name: The name of the resource.
        :param SecurityProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_access_control_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_profile_name: Optional[pulumi.Input[str]] = None,
                 tag_restricted_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityProfileTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityProfileArgs.__new__(SecurityProfileArgs)

            __props__.__dict__["allowed_access_control_tags"] = allowed_access_control_tags
            __props__.__dict__["description"] = description
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["security_profile_name"] = security_profile_name
            __props__.__dict__["tag_restricted_resources"] = tag_restricted_resources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["security_profile_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["instance_arn", "security_profile_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SecurityProfile, __self__).__init__(
            'aws-native:connect:SecurityProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityProfile':
        """
        Get an existing SecurityProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityProfileArgs.__new__(SecurityProfileArgs)

        __props__.__dict__["allowed_access_control_tags"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["security_profile_arn"] = None
        __props__.__dict__["security_profile_name"] = None
        __props__.__dict__["tag_restricted_resources"] = None
        __props__.__dict__["tags"] = None
        return SecurityProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedAccessControlTags")
    def allowed_access_control_tags(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityProfileTag']]]:
        """
        The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        """
        return pulumi.get(self, "allowed_access_control_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the security profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Permissions assigned to the security profile.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="securityProfileArn")
    def security_profile_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the security profile.
        """
        return pulumi.get(self, "security_profile_arn")

    @property
    @pulumi.getter(name="securityProfileName")
    def security_profile_name(self) -> pulumi.Output[str]:
        """
        The name of the security profile.
        """
        return pulumi.get(self, "security_profile_name")

    @property
    @pulumi.getter(name="tagRestrictedResources")
    def tag_restricted_resources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        """
        return pulumi.get(self, "tag_restricted_resources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityProfileTag']]]:
        """
        The tags used to organize, track, or control access for this resource.
        """
        return pulumi.get(self, "tags")

