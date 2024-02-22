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

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 dashboard_definition: pulumi.Input[str],
                 dashboard_description: pulumi.Input[str],
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] dashboard_definition: The dashboard definition specified in a JSON literal.
        :param pulumi.Input[str] dashboard_description: A description for the dashboard.
        :param pulumi.Input[str] dashboard_name: A friendly name for the dashboard.
        :param pulumi.Input[str] project_id: The ID of the project in which to create the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of key-value pairs that contain metadata for the dashboard.
        """
        pulumi.set(__self__, "dashboard_definition", dashboard_definition)
        pulumi.set(__self__, "dashboard_description", dashboard_description)
        if dashboard_name is not None:
            pulumi.set(__self__, "dashboard_name", dashboard_name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dashboardDefinition")
    def dashboard_definition(self) -> pulumi.Input[str]:
        """
        The dashboard definition specified in a JSON literal.
        """
        return pulumi.get(self, "dashboard_definition")

    @dashboard_definition.setter
    def dashboard_definition(self, value: pulumi.Input[str]):
        pulumi.set(self, "dashboard_definition", value)

    @property
    @pulumi.getter(name="dashboardDescription")
    def dashboard_description(self) -> pulumi.Input[str]:
        """
        A description for the dashboard.
        """
        return pulumi.get(self, "dashboard_description")

    @dashboard_description.setter
    def dashboard_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "dashboard_description", value)

    @property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for the dashboard.
        """
        return pulumi.get(self, "dashboard_name")

    @dashboard_name.setter
    def dashboard_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which to create the dashboard.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the dashboard.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_definition: Optional[pulumi.Input[str]] = None,
                 dashboard_description: Optional[pulumi.Input[str]] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::IoTSiteWise::Dashboard

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_definition: The dashboard definition specified in a JSON literal.
        :param pulumi.Input[str] dashboard_description: A description for the dashboard.
        :param pulumi.Input[str] dashboard_name: A friendly name for the dashboard.
        :param pulumi.Input[str] project_id: The ID of the project in which to create the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A list of key-value pairs that contain metadata for the dashboard.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::IoTSiteWise::Dashboard

        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_definition: Optional[pulumi.Input[str]] = None,
                 dashboard_description: Optional[pulumi.Input[str]] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            if dashboard_definition is None and not opts.urn:
                raise TypeError("Missing required property 'dashboard_definition'")
            __props__.__dict__["dashboard_definition"] = dashboard_definition
            if dashboard_description is None and not opts.urn:
                raise TypeError("Missing required property 'dashboard_description'")
            __props__.__dict__["dashboard_description"] = dashboard_description
            __props__.__dict__["dashboard_name"] = dashboard_name
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["dashboard_arn"] = None
            __props__.__dict__["dashboard_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Dashboard, __self__).__init__(
            'aws-native:iotsitewise:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DashboardArgs.__new__(DashboardArgs)

        __props__.__dict__["dashboard_arn"] = None
        __props__.__dict__["dashboard_definition"] = None
        __props__.__dict__["dashboard_description"] = None
        __props__.__dict__["dashboard_id"] = None
        __props__.__dict__["dashboard_name"] = None
        __props__.__dict__["project_id"] = None
        __props__.__dict__["tags"] = None
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the dashboard.
        """
        return pulumi.get(self, "dashboard_arn")

    @property
    @pulumi.getter(name="dashboardDefinition")
    def dashboard_definition(self) -> pulumi.Output[str]:
        """
        The dashboard definition specified in a JSON literal.
        """
        return pulumi.get(self, "dashboard_definition")

    @property
    @pulumi.getter(name="dashboardDescription")
    def dashboard_description(self) -> pulumi.Output[str]:
        """
        A description for the dashboard.
        """
        return pulumi.get(self, "dashboard_description")

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> pulumi.Output[str]:
        """
        The ID of the dashboard.
        """
        return pulumi.get(self, "dashboard_id")

    @property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> pulumi.Output[str]:
        """
        A friendly name for the dashboard.
        """
        return pulumi.get(self, "dashboard_name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the project in which to create the dashboard.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of key-value pairs that contain metadata for the dashboard.
        """
        return pulumi.get(self, "tags")

