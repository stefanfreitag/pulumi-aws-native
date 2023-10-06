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

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 role_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 duration_seconds: Optional[pulumi.Input[float]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 require_instance_properties: Optional[pulumi.Input[bool]] = None,
                 session_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileTagArgs']]]] = None):
        """
        The set of arguments for constructing a Profile resource.
        """
        ProfileArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role_arns=role_arns,
            duration_seconds=duration_seconds,
            enabled=enabled,
            managed_policy_arns=managed_policy_arns,
            name=name,
            require_instance_properties=require_instance_properties,
            session_policy=session_policy,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
             duration_seconds: Optional[pulumi.Input[float]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             require_instance_properties: Optional[pulumi.Input[bool]] = None,
             session_policy: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role_arns", role_arns)
        if duration_seconds is not None:
            _setter("duration_seconds", duration_seconds)
        if enabled is not None:
            _setter("enabled", enabled)
        if managed_policy_arns is not None:
            _setter("managed_policy_arns", managed_policy_arns)
        if name is not None:
            _setter("name", name)
        if require_instance_properties is not None:
            _setter("require_instance_properties", require_instance_properties)
        if session_policy is not None:
            _setter("session_policy", session_policy)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="roleArns")
    def role_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "role_arns")

    @role_arns.setter
    def role_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "role_arns", value)

    @property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "duration_seconds")

    @duration_seconds.setter
    def duration_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "duration_seconds", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "managed_policy_arns")

    @managed_policy_arns.setter
    def managed_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "managed_policy_arns", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="requireInstanceProperties")
    def require_instance_properties(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_instance_properties")

    @require_instance_properties.setter
    def require_instance_properties(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_instance_properties", value)

    @property
    @pulumi.getter(name="sessionPolicy")
    def session_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "session_policy")

    @session_policy.setter
    def session_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProfileTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duration_seconds: Optional[pulumi.Input[float]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 require_instance_properties: Optional[pulumi.Input[bool]] = None,
                 role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 session_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::RolesAnywhere::Profile Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::RolesAnywhere::Profile Resource Type

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProfileArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 duration_seconds: Optional[pulumi.Input[float]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 require_instance_properties: Optional[pulumi.Input[bool]] = None,
                 role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 session_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            __props__.__dict__["duration_seconds"] = duration_seconds
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["managed_policy_arns"] = managed_policy_arns
            __props__.__dict__["name"] = name
            __props__.__dict__["require_instance_properties"] = require_instance_properties
            if role_arns is None and not opts.urn:
                raise TypeError("Missing required property 'role_arns'")
            __props__.__dict__["role_arns"] = role_arns
            __props__.__dict__["session_policy"] = session_policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["profile_arn"] = None
            __props__.__dict__["profile_id"] = None
        super(Profile, __self__).__init__(
            'aws-native:rolesanywhere:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProfileArgs.__new__(ProfileArgs)

        __props__.__dict__["duration_seconds"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["managed_policy_arns"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["profile_arn"] = None
        __props__.__dict__["profile_id"] = None
        __props__.__dict__["require_instance_properties"] = None
        __props__.__dict__["role_arns"] = None
        __props__.__dict__["session_policy"] = None
        __props__.__dict__["tags"] = None
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "duration_seconds")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "managed_policy_arns")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileArn")
    def profile_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "profile_arn")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter(name="requireInstanceProperties")
    def require_instance_properties(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "require_instance_properties")

    @property
    @pulumi.getter(name="roleArns")
    def role_arns(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "role_arns")

    @property
    @pulumi.getter(name="sessionPolicy")
    def session_policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "session_policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ProfileTag']]]:
        return pulumi.get(self, "tags")

