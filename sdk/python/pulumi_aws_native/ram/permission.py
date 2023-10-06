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

__all__ = ['PermissionArgs', 'Permission']

@pulumi.input_type
class PermissionArgs:
    def __init__(__self__, *,
                 policy_template: Any,
                 resource_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionTagArgs']]]] = None):
        """
        The set of arguments for constructing a Permission resource.
        :param Any policy_template: Policy template for the permission.
        :param pulumi.Input[str] resource_type: The resource type this permission can be used with.
        :param pulumi.Input[str] name: The name of the permission.
        """
        PermissionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_template=policy_template,
            resource_type=resource_type,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_template: Any,
             resource_type: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_template", policy_template)
        _setter("resource_type", resource_type)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="policyTemplate")
    def policy_template(self) -> Any:
        """
        Policy template for the permission.
        """
        return pulumi.get(self, "policy_template")

    @policy_template.setter
    def policy_template(self, value: Any):
        pulumi.set(self, "policy_template", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        The resource type this permission can be used with.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the permission.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Permission(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_template: Optional[Any] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource type definition for AWS::RAM::Permission

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the permission.
        :param Any policy_template: Policy template for the permission.
        :param pulumi.Input[str] resource_type: The resource type this permission can be used with.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource type definition for AWS::RAM::Permission

        :param str resource_name: The name of the resource.
        :param PermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PermissionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_template: Optional[Any] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PermissionArgs.__new__(PermissionArgs)

            __props__.__dict__["name"] = name
            if policy_template is None and not opts.urn:
                raise TypeError("Missing required property 'policy_template'")
            __props__.__dict__["policy_template"] = policy_template
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["is_resource_type_default"] = None
            __props__.__dict__["permission_type"] = None
            __props__.__dict__["version"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "policy_template", "resource_type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Permission, __self__).__init__(
            'aws-native:ram:Permission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Permission':
        """
        Get an existing Permission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PermissionArgs.__new__(PermissionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["is_resource_type_default"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permission_type"] = None
        __props__.__dict__["policy_template"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version"] = None
        return Permission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="isResourceTypeDefault")
    def is_resource_type_default(self) -> pulumi.Output[bool]:
        """
        Set to true to use this as the default permission.
        """
        return pulumi.get(self, "is_resource_type_default")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the permission.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "permission_type")

    @property
    @pulumi.getter(name="policyTemplate")
    def policy_template(self) -> pulumi.Output[Any]:
        """
        Policy template for the permission.
        """
        return pulumi.get(self, "policy_template")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The resource type this permission can be used with.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PermissionTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the permission.
        """
        return pulumi.get(self, "version")

