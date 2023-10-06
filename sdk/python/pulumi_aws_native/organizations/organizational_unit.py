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

__all__ = ['OrganizationalUnitArgs', 'OrganizationalUnit']

@pulumi.input_type
class OrganizationalUnitArgs:
    def __init__(__self__, *,
                 parent_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationalUnitTagArgs']]]] = None):
        """
        The set of arguments for constructing a OrganizationalUnit resource.
        :param pulumi.Input[str] parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        :param pulumi.Input[str] name: The friendly name of this OU.
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationalUnitTagArgs']]] tags: A list of tags that you want to attach to the newly created OU.
        """
        OrganizationalUnitArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            parent_id=parent_id,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             parent_id: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationalUnitTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("parent_id", parent_id)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Input[str]:
        """
        The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name of this OU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationalUnitTagArgs']]]]:
        """
        A list of tags that you want to attach to the newly created OU.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationalUnitTagArgs']]]]):
        pulumi.set(self, "tags", value)


class OrganizationalUnit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationalUnitTagArgs']]]]] = None,
                 __props__=None):
        """
        You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The friendly name of this OU.
        :param pulumi.Input[str] parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationalUnitTagArgs']]]] tags: A list of tags that you want to attach to the newly created OU.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationalUnitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.

        :param str resource_name: The name of the resource.
        :param OrganizationalUnitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationalUnitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OrganizationalUnitArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OrganizationalUnitTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationalUnitArgs.__new__(OrganizationalUnitArgs)

            __props__.__dict__["name"] = name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["parent_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(OrganizationalUnit, __self__).__init__(
            'aws-native:organizations:OrganizationalUnit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationalUnit':
        """
        Get an existing OrganizationalUnit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationalUnitArgs.__new__(OrganizationalUnitArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent_id"] = None
        __props__.__dict__["tags"] = None
        return OrganizationalUnit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of this OU.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The friendly name of this OU.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.OrganizationalUnitTag']]]:
        """
        A list of tags that you want to attach to the newly created OU.
        """
        return pulumi.get(self, "tags")

