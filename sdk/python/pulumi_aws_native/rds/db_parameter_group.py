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

__all__ = ['DbParameterGroupArgs', 'DbParameterGroup']

@pulumi.input_type
class DbParameterGroupArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 family: pulumi.Input[str],
                 db_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbParameterGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a DbParameterGroup resource.
        :param pulumi.Input[str] description: Provides the customer-specified description for this DB parameter group.
        :param pulumi.Input[str] family: The DB parameter group family name.
        :param pulumi.Input[str] db_parameter_group_name: Specifies the name of the DB parameter group
        :param Any parameters: An array of parameter names and values for the parameter update.
        :param pulumi.Input[Sequence[pulumi.Input['DbParameterGroupTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        DbParameterGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            family=family,
            db_parameter_group_name=db_parameter_group_name,
            parameters=parameters,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: pulumi.Input[str],
             family: pulumi.Input[str],
             db_parameter_group_name: Optional[pulumi.Input[str]] = None,
             parameters: Optional[Any] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DbParameterGroupTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        _setter("family", family)
        if db_parameter_group_name is not None:
            _setter("db_parameter_group_name", db_parameter_group_name)
        if parameters is not None:
            _setter("parameters", parameters)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Provides the customer-specified description for this DB parameter group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[str]:
        """
        The DB parameter group family name.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[str]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the DB parameter group
        """
        return pulumi.get(self, "db_parameter_group_name")

    @db_parameter_group_name.setter
    def db_parameter_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_parameter_group_name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        An array of parameter names and values for the parameter update.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DbParameterGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DbParameterGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DbParameterGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_parameter_group_name: Specifies the name of the DB parameter group
        :param pulumi.Input[str] description: Provides the customer-specified description for this DB parameter group.
        :param pulumi.Input[str] family: The DB parameter group family name.
        :param Any parameters: An array of parameter names and values for the parameter update.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbParameterGroupTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbParameterGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family

        :param str resource_name: The name of the resource.
        :param DbParameterGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbParameterGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DbParameterGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_parameter_group_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DbParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbParameterGroupArgs.__new__(DbParameterGroupArgs)

            __props__.__dict__["db_parameter_group_name"] = db_parameter_group_name
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if family is None and not opts.urn:
                raise TypeError("Missing required property 'family'")
            __props__.__dict__["family"] = family
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["db_parameter_group_name", "description", "family"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DbParameterGroup, __self__).__init__(
            'aws-native:rds:DbParameterGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbParameterGroup':
        """
        Get an existing DbParameterGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbParameterGroupArgs.__new__(DbParameterGroupArgs)

        __props__.__dict__["db_parameter_group_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["family"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["tags"] = None
        return DbParameterGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the name of the DB parameter group
        """
        return pulumi.get(self, "db_parameter_group_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Provides the customer-specified description for this DB parameter group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[str]:
        """
        The DB parameter group family name.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        An array of parameter names and values for the parameter update.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DbParameterGroupTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

