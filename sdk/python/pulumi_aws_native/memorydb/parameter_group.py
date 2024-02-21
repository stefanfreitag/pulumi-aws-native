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

__all__ = ['ParameterGroupArgs', 'ParameterGroup']

@pulumi.input_type
class ParameterGroupArgs:
    def __init__(__self__, *,
                 family: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 parameter_group_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a ParameterGroup resource.
        :param pulumi.Input[str] family: The name of the parameter group family that this parameter group is compatible with.
        :param pulumi.Input[str] description: A description of the parameter group.
        :param pulumi.Input[str] parameter_group_name: The name of the parameter group.
        :param Any parameters: An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MemoryDB::ParameterGroup` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]] tags: An array of key-value pairs to apply to this parameter group.
        """
        pulumi.set(__self__, "family", family)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parameter_group_name is not None:
            pulumi.set(__self__, "parameter_group_name", parameter_group_name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[str]:
        """
        The name of the parameter group family that this parameter group is compatible with.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[str]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the parameter group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the parameter group.
        """
        return pulumi.get(self, "parameter_group_name")

    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_group_name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MemoryDB::ParameterGroup` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this parameter group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ParameterGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameter_group_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the parameter group.
        :param pulumi.Input[str] family: The name of the parameter group family that this parameter group is compatible with.
        :param pulumi.Input[str] parameter_group_name: The name of the parameter group.
        :param Any parameters: An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MemoryDB::ParameterGroup` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterGroupTagArgs']]]] tags: An array of key-value pairs to apply to this parameter group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ParameterGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.

        :param str resource_name: The name of the resource.
        :param ParameterGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ParameterGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameter_group_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ParameterGroupArgs.__new__(ParameterGroupArgs)

            __props__.__dict__["description"] = description
            if family is None and not opts.urn:
                raise TypeError("Missing required property 'family'")
            __props__.__dict__["family"] = family
            __props__.__dict__["parameter_group_name"] = parameter_group_name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["description", "family", "parameter_group_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ParameterGroup, __self__).__init__(
            'aws-native:memorydb:ParameterGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ParameterGroup':
        """
        Get an existing ParameterGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ParameterGroupArgs.__new__(ParameterGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["family"] = None
        __props__.__dict__["parameter_group_name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["tags"] = None
        return ParameterGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the parameter group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the parameter group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[str]:
        """
        The name of the parameter group family that this parameter group is compatible with.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[str]:
        """
        The name of the parameter group.
        """
        return pulumi.get(self, "parameter_group_name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MemoryDB::ParameterGroup` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ParameterGroupTag']]]:
        """
        An array of key-value pairs to apply to this parameter group.
        """
        return pulumi.get(self, "tags")

