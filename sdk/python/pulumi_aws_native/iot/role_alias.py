# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RoleAliasArgs', 'RoleAlias']

@pulumi.input_type
class RoleAliasArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 credential_duration_seconds: Optional[pulumi.Input[int]] = None,
                 role_alias: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['RoleAliasTagArgs']]]] = None):
        """
        The set of arguments for constructing a RoleAlias resource.
        """
        RoleAliasArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role_arn=role_arn,
            credential_duration_seconds=credential_duration_seconds,
            role_alias=role_alias,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role_arn: pulumi.Input[str],
             credential_duration_seconds: Optional[pulumi.Input[int]] = None,
             role_alias: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['RoleAliasTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role_arn", role_arn)
        if credential_duration_seconds is not None:
            _setter("credential_duration_seconds", credential_duration_seconds)
        if role_alias is not None:
            _setter("role_alias", role_alias)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="credentialDurationSeconds")
    def credential_duration_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "credential_duration_seconds")

    @credential_duration_seconds.setter
    def credential_duration_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "credential_duration_seconds", value)

    @property
    @pulumi.getter(name="roleAlias")
    def role_alias(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_alias")

    @role_alias.setter
    def role_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_alias", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoleAliasTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoleAliasTagArgs']]]]):
        pulumi.set(self, "tags", value)


class RoleAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_duration_seconds: Optional[pulumi.Input[int]] = None,
                 role_alias: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleAliasTagArgs']]]]] = None,
                 __props__=None):
        """
        Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.

        :param str resource_name: The name of the resource.
        :param RoleAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RoleAliasArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_duration_seconds: Optional[pulumi.Input[int]] = None,
                 role_alias: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleAliasTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleAliasArgs.__new__(RoleAliasArgs)

            __props__.__dict__["credential_duration_seconds"] = credential_duration_seconds
            __props__.__dict__["role_alias"] = role_alias
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["role_alias_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["role_alias"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(RoleAlias, __self__).__init__(
            'aws-native:iot:RoleAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoleAlias':
        """
        Get an existing RoleAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoleAliasArgs.__new__(RoleAliasArgs)

        __props__.__dict__["credential_duration_seconds"] = None
        __props__.__dict__["role_alias"] = None
        __props__.__dict__["role_alias_arn"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return RoleAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="credentialDurationSeconds")
    def credential_duration_seconds(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "credential_duration_seconds")

    @property
    @pulumi.getter(name="roleAlias")
    def role_alias(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "role_alias")

    @property
    @pulumi.getter(name="roleAliasArn")
    def role_alias_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_alias_arn")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.RoleAliasTag']]]:
        return pulumi.get(self, "tags")

