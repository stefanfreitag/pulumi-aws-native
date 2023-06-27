# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ResolverConfigArgs', 'ResolverConfig']

@pulumi.input_type
class ResolverConfigArgs:
    def __init__(__self__, *,
                 autodefined_reverse_flag: pulumi.Input['ResolverConfigAutodefinedReverseFlag'],
                 resource_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ResolverConfig resource.
        :param pulumi.Input['ResolverConfigAutodefinedReverseFlag'] autodefined_reverse_flag: Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
        :param pulumi.Input[str] resource_id: ResourceId
        """
        pulumi.set(__self__, "autodefined_reverse_flag", autodefined_reverse_flag)
        pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> pulumi.Input['ResolverConfigAutodefinedReverseFlag']:
        """
        Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
        """
        return pulumi.get(self, "autodefined_reverse_flag")

    @autodefined_reverse_flag.setter
    def autodefined_reverse_flag(self, value: pulumi.Input['ResolverConfigAutodefinedReverseFlag']):
        pulumi.set(self, "autodefined_reverse_flag", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)


class ResolverConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autodefined_reverse_flag: Optional[pulumi.Input['ResolverConfigAutodefinedReverseFlag']] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::ResolverConfig.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ResolverConfigAutodefinedReverseFlag'] autodefined_reverse_flag: Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
        :param pulumi.Input[str] resource_id: ResourceId
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResolverConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::ResolverConfig.

        :param str resource_name: The name of the resource.
        :param ResolverConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autodefined_reverse_flag: Optional[pulumi.Input['ResolverConfigAutodefinedReverseFlag']] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverConfigArgs.__new__(ResolverConfigArgs)

            if autodefined_reverse_flag is None and not opts.urn:
                raise TypeError("Missing required property 'autodefined_reverse_flag'")
            __props__.__dict__["autodefined_reverse_flag"] = autodefined_reverse_flag
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["autodefined_reverse"] = None
            __props__.__dict__["owner_id"] = None
        super(ResolverConfig, __self__).__init__(
            'aws-native:route53resolver:ResolverConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResolverConfig':
        """
        Get an existing ResolverConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResolverConfigArgs.__new__(ResolverConfigArgs)

        __props__.__dict__["autodefined_reverse"] = None
        __props__.__dict__["autodefined_reverse_flag"] = None
        __props__.__dict__["owner_id"] = None
        __props__.__dict__["resource_id"] = None
        return ResolverConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autodefinedReverse")
    def autodefined_reverse(self) -> pulumi.Output['ResolverConfigAutodefinedReverse']:
        """
        ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
        """
        return pulumi.get(self, "autodefined_reverse")

    @property
    @pulumi.getter(name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> pulumi.Output['ResolverConfigAutodefinedReverseFlag']:
        """
        Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
        """
        return pulumi.get(self, "autodefined_reverse_flag")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        AccountId
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

