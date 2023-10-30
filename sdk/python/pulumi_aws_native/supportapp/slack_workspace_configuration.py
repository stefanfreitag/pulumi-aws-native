# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SlackWorkspaceConfigurationArgs', 'SlackWorkspaceConfiguration']

@pulumi.input_type
class SlackWorkspaceConfigurationArgs:
    def __init__(__self__, *,
                 team_id: pulumi.Input[str],
                 version_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SlackWorkspaceConfiguration resource.
        :param pulumi.Input[str] team_id: The team ID in Slack, which uniquely identifies a workspace.
        :param pulumi.Input[str] version_id: An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
        """
        pulumi.set(__self__, "team_id", team_id)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        The team ID in Slack, which uniquely identifies a workspace.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[str]]:
        """
        An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_id", value)


class SlackWorkspaceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] team_id: The team ID in Slack, which uniquely identifies a workspace.
        :param pulumi.Input[str] version_id: An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SlackWorkspaceConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.

        :param str resource_name: The name of the resource.
        :param SlackWorkspaceConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SlackWorkspaceConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SlackWorkspaceConfigurationArgs.__new__(SlackWorkspaceConfigurationArgs)

            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["version_id"] = version_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["team_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SlackWorkspaceConfiguration, __self__).__init__(
            'aws-native:supportapp:SlackWorkspaceConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SlackWorkspaceConfiguration':
        """
        Get an existing SlackWorkspaceConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SlackWorkspaceConfigurationArgs.__new__(SlackWorkspaceConfigurationArgs)

        __props__.__dict__["team_id"] = None
        __props__.__dict__["version_id"] = None
        return SlackWorkspaceConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The team ID in Slack, which uniquely identifies a workspace.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[Optional[str]]:
        """
        An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
        """
        return pulumi.get(self, "version_id")

