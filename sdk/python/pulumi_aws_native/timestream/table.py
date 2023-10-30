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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 magnetic_store_write_properties: Optional[pulumi.Input['MagneticStoreWritePropertiesPropertiesArgs']] = None,
                 retention_properties: Optional[pulumi.Input['RetentionPropertiesPropertiesArgs']] = None,
                 schema: Optional[pulumi.Input['SchemaPropertiesArgs']] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] database_name: The name for the database which the table to be created belongs to.
        :param pulumi.Input['MagneticStoreWritePropertiesPropertiesArgs'] magnetic_store_write_properties: The properties that determine whether magnetic store writes are enabled.
        :param pulumi.Input['RetentionPropertiesPropertiesArgs'] retention_properties: The retention duration of the memory store and the magnetic store.
        :param pulumi.Input['SchemaPropertiesArgs'] schema: A Schema specifies the expected data model of the table.
        :param pulumi.Input[str] table_name: The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
        :param pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "database_name", database_name)
        if magnetic_store_write_properties is not None:
            pulumi.set(__self__, "magnetic_store_write_properties", magnetic_store_write_properties)
        if retention_properties is not None:
            pulumi.set(__self__, "retention_properties", retention_properties)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name for the database which the table to be created belongs to.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(self) -> Optional[pulumi.Input['MagneticStoreWritePropertiesPropertiesArgs']]:
        """
        The properties that determine whether magnetic store writes are enabled.
        """
        return pulumi.get(self, "magnetic_store_write_properties")

    @magnetic_store_write_properties.setter
    def magnetic_store_write_properties(self, value: Optional[pulumi.Input['MagneticStoreWritePropertiesPropertiesArgs']]):
        pulumi.set(self, "magnetic_store_write_properties", value)

    @property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(self) -> Optional[pulumi.Input['RetentionPropertiesPropertiesArgs']]:
        """
        The retention duration of the memory store and the magnetic store.
        """
        return pulumi.get(self, "retention_properties")

    @retention_properties.setter
    def retention_properties(self, value: Optional[pulumi.Input['RetentionPropertiesPropertiesArgs']]):
        pulumi.set(self, "retention_properties", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input['SchemaPropertiesArgs']]:
        """
        A Schema specifies the expected data model of the table.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input['SchemaPropertiesArgs']]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 magnetic_store_write_properties: Optional[pulumi.Input[pulumi.InputType['MagneticStoreWritePropertiesPropertiesArgs']]] = None,
                 retention_properties: Optional[pulumi.Input[pulumi.InputType['RetentionPropertiesPropertiesArgs']]] = None,
                 schema: Optional[pulumi.Input[pulumi.InputType['SchemaPropertiesArgs']]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::Timestream::Table resource creates a Timestream Table.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name for the database which the table to be created belongs to.
        :param pulumi.Input[pulumi.InputType['MagneticStoreWritePropertiesPropertiesArgs']] magnetic_store_write_properties: The properties that determine whether magnetic store writes are enabled.
        :param pulumi.Input[pulumi.InputType['RetentionPropertiesPropertiesArgs']] retention_properties: The retention duration of the memory store and the magnetic store.
        :param pulumi.Input[pulumi.InputType['SchemaPropertiesArgs']] schema: A Schema specifies the expected data model of the table.
        :param pulumi.Input[str] table_name: The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Timestream::Table resource creates a Timestream Table.

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 magnetic_store_write_properties: Optional[pulumi.Input[pulumi.InputType['MagneticStoreWritePropertiesPropertiesArgs']]] = None,
                 retention_properties: Optional[pulumi.Input[pulumi.InputType['RetentionPropertiesPropertiesArgs']]] = None,
                 schema: Optional[pulumi.Input[pulumi.InputType['SchemaPropertiesArgs']]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["magnetic_store_write_properties"] = magnetic_store_write_properties
            __props__.__dict__["retention_properties"] = retention_properties
            __props__.__dict__["schema"] = schema
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["database_name", "table_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Table, __self__).__init__(
            'aws-native:timestream:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TableArgs.__new__(TableArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["database_name"] = None
        __props__.__dict__["magnetic_store_write_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["retention_properties"] = None
        __props__.__dict__["schema"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["tags"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        The name for the database which the table to be created belongs to.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(self) -> pulumi.Output[Optional['outputs.MagneticStoreWritePropertiesProperties']]:
        """
        The properties that determine whether magnetic store writes are enabled.
        """
        return pulumi.get(self, "magnetic_store_write_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The table name exposed as a read-only attribute.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(self) -> pulumi.Output[Optional['outputs.RetentionPropertiesProperties']]:
        """
        The retention duration of the memory store and the magnetic store.
        """
        return pulumi.get(self, "retention_properties")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional['outputs.SchemaProperties']]:
        """
        A Schema specifies the expected data model of the table.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TableTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

