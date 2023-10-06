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

__all__ = ['DbSubnetGroupArgs', 'DbSubnetGroup']

@pulumi.input_type
class DbSubnetGroupArgs:
    def __init__(__self__, *,
                 db_subnet_group_description: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbSubnetGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a DbSubnetGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['DbSubnetGroupTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        DbSubnetGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            db_subnet_group_description=db_subnet_group_description,
            subnet_ids=subnet_ids,
            db_subnet_group_name=db_subnet_group_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             db_subnet_group_description: pulumi.Input[str],
             subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             db_subnet_group_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbSubnetGroupTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("db_subnet_group_description", db_subnet_group_description)
        _setter("subnet_ids", subnet_ids)
        if db_subnet_group_name is not None:
            _setter("db_subnet_group_name", db_subnet_group_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "db_subnet_group_description")

    @db_subnet_group_description.setter
    def db_subnet_group_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_subnet_group_description", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_subnet_group_name")

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_subnet_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DbSubnetGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DbSubnetGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DbSubnetGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbSubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::RDS::DBSubnetGroup resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbSubnetGroupTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbSubnetGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::RDS::DBSubnetGroup resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region.

        :param str resource_name: The name of the resource.
        :param DbSubnetGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbSubnetGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DbSubnetGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 db_subnet_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbSubnetGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbSubnetGroupArgs.__new__(DbSubnetGroupArgs)

            if db_subnet_group_description is None and not opts.urn:
                raise TypeError("Missing required property 'db_subnet_group_description'")
            __props__.__dict__["db_subnet_group_description"] = db_subnet_group_description
            __props__.__dict__["db_subnet_group_name"] = db_subnet_group_name
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["db_subnet_group_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DbSubnetGroup, __self__).__init__(
            'aws-native:rds:DbSubnetGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbSubnetGroup':
        """
        Get an existing DbSubnetGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbSubnetGroupArgs.__new__(DbSubnetGroupArgs)

        __props__.__dict__["db_subnet_group_description"] = None
        __props__.__dict__["db_subnet_group_name"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        return DbSubnetGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "db_subnet_group_description")

    @property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "db_subnet_group_name")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DbSubnetGroupTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

