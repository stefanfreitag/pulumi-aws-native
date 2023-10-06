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

__all__ = ['FilterArgs', 'Filter']

@pulumi.input_type
class FilterArgs:
    def __init__(__self__, *,
                 filter_action: pulumi.Input['FilterAction'],
                 filter_criteria: pulumi.Input['FilterCriteriaArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Filter resource.
        :param pulumi.Input['FilterAction'] filter_action: Findings filter action.
        :param pulumi.Input['FilterCriteriaArgs'] filter_criteria: Findings filter criteria.
        :param pulumi.Input[str] description: Findings filter description.
        :param pulumi.Input[str] name: Findings filter name.
        """
        FilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filter_action=filter_action,
            filter_criteria=filter_criteria,
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filter_action: pulumi.Input['FilterAction'],
             filter_criteria: pulumi.Input['FilterCriteriaArgs'],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("filter_action", filter_action)
        _setter("filter_criteria", filter_criteria)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> pulumi.Input['FilterAction']:
        """
        Findings filter action.
        """
        return pulumi.get(self, "filter_action")

    @filter_action.setter
    def filter_action(self, value: pulumi.Input['FilterAction']):
        pulumi.set(self, "filter_action", value)

    @property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> pulumi.Input['FilterCriteriaArgs']:
        """
        Findings filter criteria.
        """
        return pulumi.get(self, "filter_criteria")

    @filter_criteria.setter
    def filter_criteria(self, value: pulumi.Input['FilterCriteriaArgs']):
        pulumi.set(self, "filter_criteria", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Findings filter description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Findings filter name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Filter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter_action: Optional[pulumi.Input['FilterAction']] = None,
                 filter_criteria: Optional[pulumi.Input[pulumi.InputType['FilterCriteriaArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Inspector Filter resource schema

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Findings filter description.
        :param pulumi.Input['FilterAction'] filter_action: Findings filter action.
        :param pulumi.Input[pulumi.InputType['FilterCriteriaArgs']] filter_criteria: Findings filter criteria.
        :param pulumi.Input[str] name: Findings filter name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Inspector Filter resource schema

        :param str resource_name: The name of the resource.
        :param FilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FilterArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter_action: Optional[pulumi.Input['FilterAction']] = None,
                 filter_criteria: Optional[pulumi.Input[pulumi.InputType['FilterCriteriaArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FilterArgs.__new__(FilterArgs)

            __props__.__dict__["description"] = description
            if filter_action is None and not opts.urn:
                raise TypeError("Missing required property 'filter_action'")
            __props__.__dict__["filter_action"] = filter_action
            if filter_criteria is not None and not isinstance(filter_criteria, FilterCriteriaArgs):
                filter_criteria = filter_criteria or {}
                def _setter(key, value):
                    filter_criteria[key] = value
                FilterCriteriaArgs._configure(_setter, **filter_criteria)
            if filter_criteria is None and not opts.urn:
                raise TypeError("Missing required property 'filter_criteria'")
            __props__.__dict__["filter_criteria"] = filter_criteria
            __props__.__dict__["name"] = name
            __props__.__dict__["arn"] = None
        super(Filter, __self__).__init__(
            'aws-native:inspectorv2:Filter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Filter':
        """
        Get an existing Filter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FilterArgs.__new__(FilterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["filter_action"] = None
        __props__.__dict__["filter_criteria"] = None
        __props__.__dict__["name"] = None
        return Filter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Findings filter ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Findings filter description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> pulumi.Output['FilterAction']:
        """
        Findings filter action.
        """
        return pulumi.get(self, "filter_action")

    @property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> pulumi.Output['outputs.FilterCriteria']:
        """
        Findings filter criteria.
        """
        return pulumi.get(self, "filter_criteria")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Findings filter name.
        """
        return pulumi.get(self, "name")

