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
from ._inputs import *

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 bundle_id: pulumi.Input[str],
                 directory_id: pulumi.Input[str],
                 user_name: pulumi.Input[str],
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceTagArgs']]]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input['WorkspacePropertiesArgs']] = None):
        """
        The set of arguments for constructing a Workspace resource.
        """
        WorkspaceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bundle_id=bundle_id,
            directory_id=directory_id,
            user_name=user_name,
            root_volume_encryption_enabled=root_volume_encryption_enabled,
            tags=tags,
            user_volume_encryption_enabled=user_volume_encryption_enabled,
            volume_encryption_key=volume_encryption_key,
            workspace_properties=workspace_properties,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bundle_id: pulumi.Input[str],
             directory_id: pulumi.Input[str],
             user_name: pulumi.Input[str],
             root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceTagArgs']]]] = None,
             user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
             volume_encryption_key: Optional[pulumi.Input[str]] = None,
             workspace_properties: Optional[pulumi.Input['WorkspacePropertiesArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bundle_id", bundle_id)
        _setter("directory_id", directory_id)
        _setter("user_name", user_name)
        if root_volume_encryption_enabled is not None:
            _setter("root_volume_encryption_enabled", root_volume_encryption_enabled)
        if tags is not None:
            _setter("tags", tags)
        if user_volume_encryption_enabled is not None:
            _setter("user_volume_encryption_enabled", user_volume_encryption_enabled)
        if volume_encryption_key is not None:
            _setter("volume_encryption_key", volume_encryption_key)
        if workspace_properties is not None:
            _setter("workspace_properties", workspace_properties)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "root_volume_encryption_enabled")

    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "root_volume_encryption_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "user_volume_encryption_enabled")

    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "user_volume_encryption_enabled", value)

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume_encryption_key")

    @volume_encryption_key.setter
    def volume_encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_encryption_key", value)

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> Optional[pulumi.Input['WorkspacePropertiesArgs']]:
        return pulumi.get(self, "workspace_properties")

    @workspace_properties.setter
    def workspace_properties(self, value: Optional[pulumi.Input['WorkspacePropertiesArgs']]):
        pulumi.set(self, "workspace_properties", value)


warnings.warn("""Workspace is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Workspace(pulumi.CustomResource):
    warnings.warn("""Workspace is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceTagArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspacePropertiesArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WorkSpaces::Workspace

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WorkSpaces::Workspace

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WorkspaceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceTagArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspacePropertiesArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Workspace is deprecated: Workspace is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            if bundle_id is None and not opts.urn:
                raise TypeError("Missing required property 'bundle_id'")
            __props__.__dict__["bundle_id"] = bundle_id
            if directory_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_id'")
            __props__.__dict__["directory_id"] = directory_id
            __props__.__dict__["root_volume_encryption_enabled"] = root_volume_encryption_enabled
            __props__.__dict__["tags"] = tags
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["user_volume_encryption_enabled"] = user_volume_encryption_enabled
            __props__.__dict__["volume_encryption_key"] = volume_encryption_key
            if workspace_properties is not None and not isinstance(workspace_properties, WorkspacePropertiesArgs):
                workspace_properties = workspace_properties or {}
                def _setter(key, value):
                    workspace_properties[key] = value
                WorkspacePropertiesArgs._configure(_setter, **workspace_properties)
            __props__.__dict__["workspace_properties"] = workspace_properties
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["user_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Workspace, __self__).__init__(
            'aws-native:workspaces:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["bundle_id"] = None
        __props__.__dict__["directory_id"] = None
        __props__.__dict__["root_volume_encryption_enabled"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_name"] = None
        __props__.__dict__["user_volume_encryption_enabled"] = None
        __props__.__dict__["volume_encryption_key"] = None
        __props__.__dict__["workspace_properties"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "root_volume_encryption_enabled")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.WorkspaceTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "user_volume_encryption_enabled")

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "volume_encryption_key")

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> pulumi.Output[Optional['outputs.WorkspaceProperties']]:
        return pulumi.get(self, "workspace_properties")

