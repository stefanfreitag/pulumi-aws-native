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
from ._enums import *
from ._inputs import *

__all__ = ['MapArgs', 'Map']

@pulumi.input_type
class MapArgs:
    def __init__(__self__, *,
                 configuration: pulumi.Input['MapConfigurationArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['MapPricingPlan']] = None):
        """
        The set of arguments for constructing a Map resource.
        """
        pulumi.set(__self__, "configuration", configuration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if map_name is not None:
            pulumi.set(__self__, "map_name", map_name)
        if pricing_plan is not None:
            pulumi.set(__self__, "pricing_plan", pricing_plan)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Input['MapConfigurationArgs']:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: pulumi.Input['MapConfigurationArgs']):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="mapName")
    def map_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "map_name")

    @map_name.setter
    def map_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "map_name", value)

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional[pulumi.Input['MapPricingPlan']]:
        return pulumi.get(self, "pricing_plan")

    @pricing_plan.setter
    def pricing_plan(self, value: Optional[pulumi.Input['MapPricingPlan']]):
        pulumi.set(self, "pricing_plan", value)


class Map(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['MapConfigurationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['MapPricingPlan']] = None,
                 __props__=None):
        """
        Definition of AWS::Location::Map Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Location::Map Resource Type

        :param str resource_name: The name of the resource.
        :param MapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['MapConfigurationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 pricing_plan: Optional[pulumi.Input['MapPricingPlan']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MapArgs.__new__(MapArgs)

            if configuration is None and not opts.urn:
                raise TypeError("Missing required property 'configuration'")
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["description"] = description
            __props__.__dict__["map_name"] = map_name
            __props__.__dict__["pricing_plan"] = pricing_plan
            __props__.__dict__["arn"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["data_source"] = None
            __props__.__dict__["map_arn"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["configuration", "description", "map_name", "pricing_plan"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Map, __self__).__init__(
            'aws-native:location:Map',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Map':
        """
        Get an existing Map resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MapArgs.__new__(MapArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_source"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["map_arn"] = None
        __props__.__dict__["map_name"] = None
        __props__.__dict__["pricing_plan"] = None
        __props__.__dict__["update_time"] = None
        return Map(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output['outputs.MapConfiguration']:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="mapArn")
    def map_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "map_arn")

    @property
    @pulumi.getter(name="mapName")
    def map_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "map_name")

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> pulumi.Output[Optional['MapPricingPlan']]:
        return pulumi.get(self, "pricing_plan")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "update_time")

