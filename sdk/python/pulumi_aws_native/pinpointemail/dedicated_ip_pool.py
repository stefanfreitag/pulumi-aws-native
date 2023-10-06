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

__all__ = ['DedicatedIpPoolArgs', 'DedicatedIpPool']

@pulumi.input_type
class DedicatedIpPoolArgs:
    def __init__(__self__, *,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedIpPoolTagsArgs']]]] = None):
        """
        The set of arguments for constructing a DedicatedIpPool resource.
        """
        DedicatedIpPoolArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pool_name=pool_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pool_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedIpPoolTagsArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if pool_name is not None:
            _setter("pool_name", pool_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedIpPoolTagsArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedIpPoolTagsArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""DedicatedIpPool is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DedicatedIpPool(pulumi.CustomResource):
    warnings.warn("""DedicatedIpPool is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedIpPoolTagsArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::PinpointEmail::DedicatedIpPool

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DedicatedIpPoolArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::PinpointEmail::DedicatedIpPool

        :param str resource_name: The name of the resource.
        :param DedicatedIpPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedIpPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DedicatedIpPoolArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedIpPoolTagsArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""DedicatedIpPool is deprecated: DedicatedIpPool is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DedicatedIpPoolArgs.__new__(DedicatedIpPoolArgs)

            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["pool_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DedicatedIpPool, __self__).__init__(
            'aws-native:pinpointemail:DedicatedIpPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DedicatedIpPool':
        """
        Get an existing DedicatedIpPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DedicatedIpPoolArgs.__new__(DedicatedIpPoolArgs)

        __props__.__dict__["pool_name"] = None
        __props__.__dict__["tags"] = None
        return DedicatedIpPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pool_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DedicatedIpPoolTags']]]:
        return pulumi.get(self, "tags")

