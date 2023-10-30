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

__all__ = ['CalculatedAttributeDefinitionArgs', 'CalculatedAttributeDefinition']

@pulumi.input_type
class CalculatedAttributeDefinitionArgs:
    def __init__(__self__, *,
                 attribute_details: pulumi.Input['CalculatedAttributeDefinitionAttributeDetailsArgs'],
                 calculated_attribute_name: pulumi.Input[str],
                 domain_name: pulumi.Input[str],
                 statistic: pulumi.Input['CalculatedAttributeDefinitionStatistic'],
                 conditions: Optional[pulumi.Input['CalculatedAttributeDefinitionConditionsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedAttributeDefinitionTagArgs']]]] = None):
        """
        The set of arguments for constructing a CalculatedAttributeDefinition resource.
        """
        pulumi.set(__self__, "attribute_details", attribute_details)
        pulumi.set(__self__, "calculated_attribute_name", calculated_attribute_name)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "statistic", statistic)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="attributeDetails")
    def attribute_details(self) -> pulumi.Input['CalculatedAttributeDefinitionAttributeDetailsArgs']:
        return pulumi.get(self, "attribute_details")

    @attribute_details.setter
    def attribute_details(self, value: pulumi.Input['CalculatedAttributeDefinitionAttributeDetailsArgs']):
        pulumi.set(self, "attribute_details", value)

    @property
    @pulumi.getter(name="calculatedAttributeName")
    def calculated_attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "calculated_attribute_name")

    @calculated_attribute_name.setter
    def calculated_attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "calculated_attribute_name", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def statistic(self) -> pulumi.Input['CalculatedAttributeDefinitionStatistic']:
        return pulumi.get(self, "statistic")

    @statistic.setter
    def statistic(self, value: pulumi.Input['CalculatedAttributeDefinitionStatistic']):
        pulumi.set(self, "statistic", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['CalculatedAttributeDefinitionConditionsArgs']]:
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['CalculatedAttributeDefinitionConditionsArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedAttributeDefinitionTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedAttributeDefinitionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CalculatedAttributeDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_details: Optional[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionAttributeDetailsArgs']]] = None,
                 calculated_attribute_name: Optional[pulumi.Input[str]] = None,
                 conditions: Optional[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionConditionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 statistic: Optional[pulumi.Input['CalculatedAttributeDefinitionStatistic']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionTagArgs']]]]] = None,
                 __props__=None):
        """
        A calculated attribute definition for Customer Profiles

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CalculatedAttributeDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A calculated attribute definition for Customer Profiles

        :param str resource_name: The name of the resource.
        :param CalculatedAttributeDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CalculatedAttributeDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_details: Optional[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionAttributeDetailsArgs']]] = None,
                 calculated_attribute_name: Optional[pulumi.Input[str]] = None,
                 conditions: Optional[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionConditionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 statistic: Optional[pulumi.Input['CalculatedAttributeDefinitionStatistic']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CalculatedAttributeDefinitionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CalculatedAttributeDefinitionArgs.__new__(CalculatedAttributeDefinitionArgs)

            if attribute_details is None and not opts.urn:
                raise TypeError("Missing required property 'attribute_details'")
            __props__.__dict__["attribute_details"] = attribute_details
            if calculated_attribute_name is None and not opts.urn:
                raise TypeError("Missing required property 'calculated_attribute_name'")
            __props__.__dict__["calculated_attribute_name"] = calculated_attribute_name
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if statistic is None and not opts.urn:
                raise TypeError("Missing required property 'statistic'")
            __props__.__dict__["statistic"] = statistic
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_updated_at"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["calculated_attribute_name", "domain_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CalculatedAttributeDefinition, __self__).__init__(
            'aws-native:customerprofiles:CalculatedAttributeDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CalculatedAttributeDefinition':
        """
        Get an existing CalculatedAttributeDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CalculatedAttributeDefinitionArgs.__new__(CalculatedAttributeDefinitionArgs)

        __props__.__dict__["attribute_details"] = None
        __props__.__dict__["calculated_attribute_name"] = None
        __props__.__dict__["conditions"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["last_updated_at"] = None
        __props__.__dict__["statistic"] = None
        __props__.__dict__["tags"] = None
        return CalculatedAttributeDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attributeDetails")
    def attribute_details(self) -> pulumi.Output['outputs.CalculatedAttributeDefinitionAttributeDetails']:
        return pulumi.get(self, "attribute_details")

    @property
    @pulumi.getter(name="calculatedAttributeName")
    def calculated_attribute_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "calculated_attribute_name")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Optional['outputs.CalculatedAttributeDefinitionConditions']]:
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The timestamp of when the calculated attribute definition was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[str]:
        """
        The timestamp of when the calculated attribute definition was most recently edited.
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def statistic(self) -> pulumi.Output['CalculatedAttributeDefinitionStatistic']:
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CalculatedAttributeDefinitionTag']]]:
        return pulumi.get(self, "tags")

