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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 configuration: Optional[pulumi.Input[Sequence[pulumi.Input['GroupConfigurationItemArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_query: Optional[pulumi.Input['GroupResourceQueryArgs']] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[str] description: The description of the resource group
        :param pulumi.Input[str] name: The name of the resource group
        """
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_query is not None:
            pulumi.set(__self__, "resource_query", resource_query)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupConfigurationItemArgs']]]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupConfigurationItemArgs']]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the resource group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceQuery")
    def resource_query(self) -> Optional[pulumi.Input['GroupResourceQueryArgs']]:
        return pulumi.get(self, "resource_query")

    @resource_query.setter
    def resource_query(self, value: Optional[pulumi.Input['GroupResourceQueryArgs']]):
        pulumi.set(self, "resource_query", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupConfigurationItemArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_query: Optional[pulumi.Input[pulumi.InputType['GroupResourceQueryArgs']]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Schema for ResourceGroups::Group

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the resource group
        :param pulumi.Input[str] name: The name of the resource group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for ResourceGroups::Group

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GroupConfigurationItemArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_query: Optional[pulumi.Input[pulumi.InputType['GroupResourceQueryArgs']]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_query"] = resource_query
            __props__.__dict__["resources"] = resources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Group, __self__).__init__(
            'aws-native:resourcegroups:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupArgs.__new__(GroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_query"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["tags"] = None
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Resource Group ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[Sequence['outputs.GroupConfigurationItem']]]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the resource group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceQuery")
    def resource_query(self) -> pulumi.Output[Optional['outputs.GroupResourceQuery']]:
        return pulumi.get(self, "resource_query")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

