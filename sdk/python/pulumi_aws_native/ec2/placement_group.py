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

__all__ = ['PlacementGroupArgs', 'PlacementGroup']

@pulumi.input_type
class PlacementGroupArgs:
    def __init__(__self__, *,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 spread_level: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]] = None):
        """
        The set of arguments for constructing a PlacementGroup resource.
        :param pulumi.Input[int] partition_count: The number of partitions. Valid only when **Strategy** is set to `partition`
        :param pulumi.Input[str] spread_level: The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread
        :param pulumi.Input[str] strategy: The placement strategy.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if partition_count is not None:
            pulumi.set(__self__, "partition_count", partition_count)
        if spread_level is not None:
            pulumi.set(__self__, "spread_level", spread_level)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of partitions. Valid only when **Strategy** is set to `partition`
        """
        return pulumi.get(self, "partition_count")

    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "partition_count", value)

    @property
    @pulumi.getter(name="spreadLevel")
    def spread_level(self) -> Optional[pulumi.Input[str]]:
        """
        The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread
        """
        return pulumi.get(self, "spread_level")

    @spread_level.setter
    def spread_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spread_level", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        The placement strategy.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]):
        pulumi.set(self, "tags", value)


class PlacementGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 spread_level: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::PlacementGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] partition_count: The number of partitions. Valid only when **Strategy** is set to `partition`
        :param pulumi.Input[str] spread_level: The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread
        :param pulumi.Input[str] strategy: The placement strategy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PlacementGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::PlacementGroup

        :param str resource_name: The name of the resource.
        :param PlacementGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlacementGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 spread_level: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlacementGroupArgs.__new__(PlacementGroupArgs)

            __props__.__dict__["partition_count"] = partition_count
            __props__.__dict__["spread_level"] = spread_level
            __props__.__dict__["strategy"] = strategy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["group_name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["partition_count", "spread_level", "strategy", "tags[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PlacementGroup, __self__).__init__(
            'aws-native:ec2:PlacementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PlacementGroup':
        """
        Get an existing PlacementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PlacementGroupArgs.__new__(PlacementGroupArgs)

        __props__.__dict__["group_name"] = None
        __props__.__dict__["partition_count"] = None
        __props__.__dict__["spread_level"] = None
        __props__.__dict__["strategy"] = None
        __props__.__dict__["tags"] = None
        return PlacementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        """
        The Group Name of Placement Group.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[Optional[int]]:
        """
        The number of partitions. Valid only when **Strategy** is set to `partition`
        """
        return pulumi.get(self, "partition_count")

    @property
    @pulumi.getter(name="spreadLevel")
    def spread_level(self) -> pulumi.Output[Optional[str]]:
        """
        The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread
        """
        return pulumi.get(self, "spread_level")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[Optional[str]]:
        """
        The placement strategy.
        """
        return pulumi.get(self, "strategy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.CreateOnlyTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

