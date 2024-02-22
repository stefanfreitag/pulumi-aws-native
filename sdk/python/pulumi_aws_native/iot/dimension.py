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
from ._enums import *

__all__ = ['DimensionArgs', 'Dimension']

@pulumi.input_type
class DimensionArgs:
    def __init__(__self__, *,
                 string_values: pulumi.Input[Sequence[pulumi.Input[str]]],
                 type: pulumi.Input['DimensionType'],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Dimension resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] string_values: Specifies the value or list of values for the dimension.
        :param pulumi.Input['DimensionType'] type: Specifies the type of the dimension.
        :param pulumi.Input[str] name: A unique identifier for the dimension.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Metadata that can be used to manage the dimension.
        """
        pulumi.set(__self__, "string_values", string_values)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="stringValues")
    def string_values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies the value or list of values for the dimension.
        """
        return pulumi.get(self, "string_values")

    @string_values.setter
    def string_values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "string_values", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['DimensionType']:
        """
        Specifies the type of the dimension.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['DimensionType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier for the dimension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Metadata that can be used to manage the dimension.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Dimension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 string_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 type: Optional[pulumi.Input['DimensionType']] = None,
                 __props__=None):
        """
        A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique identifier for the dimension.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] string_values: Specifies the value or list of values for the dimension.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Metadata that can be used to manage the dimension.
        :param pulumi.Input['DimensionType'] type: Specifies the type of the dimension.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DimensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.

        :param str resource_name: The name of the resource.
        :param DimensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DimensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 string_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 type: Optional[pulumi.Input['DimensionType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DimensionArgs.__new__(DimensionArgs)

            __props__.__dict__["name"] = name
            if string_values is None and not opts.urn:
                raise TypeError("Missing required property 'string_values'")
            __props__.__dict__["string_values"] = string_values
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Dimension, __self__).__init__(
            'aws-native:iot:Dimension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dimension':
        """
        Get an existing Dimension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DimensionArgs.__new__(DimensionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["string_values"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Dimension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN (Amazon resource name) of the created dimension.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        A unique identifier for the dimension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="stringValues")
    def string_values(self) -> pulumi.Output[Sequence[str]]:
        """
        Specifies the value or list of values for the dimension.
        """
        return pulumi.get(self, "string_values")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Metadata that can be used to manage the dimension.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['DimensionType']:
        """
        Specifies the type of the dimension.
        """
        return pulumi.get(self, "type")

