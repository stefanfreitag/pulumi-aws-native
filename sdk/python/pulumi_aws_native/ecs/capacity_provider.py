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
from ._enums import *
from ._inputs import *

__all__ = ['CapacityProviderArgs', 'CapacityProvider']

@pulumi.input_type
class CapacityProviderArgs:
    def __init__(__self__, *,
                 auto_scaling_group_provider: pulumi.Input['CapacityProviderAutoScalingGroupProviderArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityProviderTagArgs']]]] = None):
        """
        The set of arguments for constructing a CapacityProvider resource.
        """
        CapacityProviderArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auto_scaling_group_provider=auto_scaling_group_provider,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auto_scaling_group_provider: pulumi.Input['CapacityProviderAutoScalingGroupProviderArgs'],
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityProviderTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("auto_scaling_group_provider", auto_scaling_group_provider)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(self) -> pulumi.Input['CapacityProviderAutoScalingGroupProviderArgs']:
        return pulumi.get(self, "auto_scaling_group_provider")

    @auto_scaling_group_provider.setter
    def auto_scaling_group_provider(self, value: pulumi.Input['CapacityProviderAutoScalingGroupProviderArgs']):
        pulumi.set(self, "auto_scaling_group_provider", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CapacityProviderTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityProviderTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CapacityProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_group_provider: Optional[pulumi.Input[pulumi.InputType['CapacityProviderAutoScalingGroupProviderArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityProviderTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ECS::CapacityProvider.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapacityProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ECS::CapacityProvider.

        :param str resource_name: The name of the resource.
        :param CapacityProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CapacityProviderArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_group_provider: Optional[pulumi.Input[pulumi.InputType['CapacityProviderAutoScalingGroupProviderArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityProviderTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityProviderArgs.__new__(CapacityProviderArgs)

            if auto_scaling_group_provider is not None and not isinstance(auto_scaling_group_provider, CapacityProviderAutoScalingGroupProviderArgs):
                auto_scaling_group_provider = auto_scaling_group_provider or {}
                def _setter(key, value):
                    auto_scaling_group_provider[key] = value
                CapacityProviderAutoScalingGroupProviderArgs._configure(_setter, **auto_scaling_group_provider)
            if auto_scaling_group_provider is None and not opts.urn:
                raise TypeError("Missing required property 'auto_scaling_group_provider'")
            __props__.__dict__["auto_scaling_group_provider"] = auto_scaling_group_provider
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["auto_scaling_group_provider.auto_scaling_group_arn", "name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CapacityProvider, __self__).__init__(
            'aws-native:ecs:CapacityProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CapacityProvider':
        """
        Get an existing CapacityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapacityProviderArgs.__new__(CapacityProviderArgs)

        __props__.__dict__["auto_scaling_group_provider"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return CapacityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScalingGroupProvider")
    def auto_scaling_group_provider(self) -> pulumi.Output['outputs.CapacityProviderAutoScalingGroupProvider']:
        return pulumi.get(self, "auto_scaling_group_provider")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CapacityProviderTag']]]:
        return pulumi.get(self, "tags")

