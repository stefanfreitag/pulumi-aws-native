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

__all__ = ['WalWorkspaceArgs', 'WalWorkspace']

@pulumi.input_type
class WalWorkspaceArgs:
    def __init__(__self__, *,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 wal_workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WalWorkspace resource.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] wal_workspace_name: The name of the emrwal container
        """
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if wal_workspace_name is not None:
            pulumi.set(__self__, "wal_workspace_name", wal_workspace_name)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="walWorkspaceName")
    def wal_workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the emrwal container
        """
        return pulumi.get(self, "wal_workspace_name")

    @wal_workspace_name.setter
    def wal_workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "wal_workspace_name", value)


class WalWorkspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 wal_workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EMR::WALWorkspace Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] wal_workspace_name: The name of the emrwal container
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WalWorkspaceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EMR::WALWorkspace Type

        :param str resource_name: The name of the resource.
        :param WalWorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WalWorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 wal_workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WalWorkspaceArgs.__new__(WalWorkspaceArgs)

            __props__.__dict__["tags"] = tags
            __props__.__dict__["wal_workspace_name"] = wal_workspace_name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["wal_workspace_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(WalWorkspace, __self__).__init__(
            'aws-native:emr:WalWorkspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WalWorkspace':
        """
        Get an existing WalWorkspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WalWorkspaceArgs.__new__(WalWorkspaceArgs)

        __props__.__dict__["tags"] = None
        __props__.__dict__["wal_workspace_name"] = None
        return WalWorkspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="walWorkspaceName")
    def wal_workspace_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the emrwal container
        """
        return pulumi.get(self, "wal_workspace_name")

