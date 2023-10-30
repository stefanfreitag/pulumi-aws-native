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

__all__ = ['CachePolicyArgs', 'CachePolicy']

@pulumi.input_type
class CachePolicyArgs:
    def __init__(__self__, *,
                 cache_policy_config: pulumi.Input['CachePolicyConfigArgs']):
        """
        The set of arguments for constructing a CachePolicy resource.
        """
        pulumi.set(__self__, "cache_policy_config", cache_policy_config)

    @property
    @pulumi.getter(name="cachePolicyConfig")
    def cache_policy_config(self) -> pulumi.Input['CachePolicyConfigArgs']:
        return pulumi.get(self, "cache_policy_config")

    @cache_policy_config.setter
    def cache_policy_config(self, value: pulumi.Input['CachePolicyConfigArgs']):
        pulumi.set(self, "cache_policy_config", value)


class CachePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_policy_config: Optional[pulumi.Input[pulumi.InputType['CachePolicyConfigArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudFront::CachePolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CachePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudFront::CachePolicy

        :param str resource_name: The name of the resource.
        :param CachePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CachePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_policy_config: Optional[pulumi.Input[pulumi.InputType['CachePolicyConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CachePolicyArgs.__new__(CachePolicyArgs)

            if cache_policy_config is None and not opts.urn:
                raise TypeError("Missing required property 'cache_policy_config'")
            __props__.__dict__["cache_policy_config"] = cache_policy_config
            __props__.__dict__["last_modified_time"] = None
        super(CachePolicy, __self__).__init__(
            'aws-native:cloudfront:CachePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CachePolicy':
        """
        Get an existing CachePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CachePolicyArgs.__new__(CachePolicyArgs)

        __props__.__dict__["cache_policy_config"] = None
        __props__.__dict__["last_modified_time"] = None
        return CachePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cachePolicyConfig")
    def cache_policy_config(self) -> pulumi.Output['outputs.CachePolicyConfig']:
        return pulumi.get(self, "cache_policy_config")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modified_time")

