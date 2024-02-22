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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['DatastoreArgs', 'Datastore']

@pulumi.input_type
class DatastoreArgs:
    def __init__(__self__, *,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 datastore_partitions: Optional[pulumi.Input['DatastorePartitionsArgs']] = None,
                 datastore_storage: Optional[pulumi.Input['DatastoreStorageArgs']] = None,
                 file_format_configuration: Optional[pulumi.Input['DatastoreFileFormatConfigurationArgs']] = None,
                 retention_period: Optional[pulumi.Input['DatastoreRetentionPeriodArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Datastore resource.
        """
        if datastore_name is not None:
            pulumi.set(__self__, "datastore_name", datastore_name)
        if datastore_partitions is not None:
            pulumi.set(__self__, "datastore_partitions", datastore_partitions)
        if datastore_storage is not None:
            pulumi.set(__self__, "datastore_storage", datastore_storage)
        if file_format_configuration is not None:
            pulumi.set(__self__, "file_format_configuration", file_format_configuration)
        if retention_period is not None:
            pulumi.set(__self__, "retention_period", retention_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "datastore_name")

    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore_name", value)

    @property
    @pulumi.getter(name="datastorePartitions")
    def datastore_partitions(self) -> Optional[pulumi.Input['DatastorePartitionsArgs']]:
        return pulumi.get(self, "datastore_partitions")

    @datastore_partitions.setter
    def datastore_partitions(self, value: Optional[pulumi.Input['DatastorePartitionsArgs']]):
        pulumi.set(self, "datastore_partitions", value)

    @property
    @pulumi.getter(name="datastoreStorage")
    def datastore_storage(self) -> Optional[pulumi.Input['DatastoreStorageArgs']]:
        return pulumi.get(self, "datastore_storage")

    @datastore_storage.setter
    def datastore_storage(self, value: Optional[pulumi.Input['DatastoreStorageArgs']]):
        pulumi.set(self, "datastore_storage", value)

    @property
    @pulumi.getter(name="fileFormatConfiguration")
    def file_format_configuration(self) -> Optional[pulumi.Input['DatastoreFileFormatConfigurationArgs']]:
        return pulumi.get(self, "file_format_configuration")

    @file_format_configuration.setter
    def file_format_configuration(self, value: Optional[pulumi.Input['DatastoreFileFormatConfigurationArgs']]):
        pulumi.set(self, "file_format_configuration", value)

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input['DatastoreRetentionPeriodArgs']]:
        return pulumi.get(self, "retention_period")

    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input['DatastoreRetentionPeriodArgs']]):
        pulumi.set(self, "retention_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Datastore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 datastore_partitions: Optional[pulumi.Input[pulumi.InputType['DatastorePartitionsArgs']]] = None,
                 datastore_storage: Optional[pulumi.Input[pulumi.InputType['DatastoreStorageArgs']]] = None,
                 file_format_configuration: Optional[pulumi.Input[pulumi.InputType['DatastoreFileFormatConfigurationArgs']]] = None,
                 retention_period: Optional[pulumi.Input[pulumi.InputType['DatastoreRetentionPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IoTAnalytics::Datastore

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatastoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IoTAnalytics::Datastore

        :param str resource_name: The name of the resource.
        :param DatastoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatastoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 datastore_partitions: Optional[pulumi.Input[pulumi.InputType['DatastorePartitionsArgs']]] = None,
                 datastore_storage: Optional[pulumi.Input[pulumi.InputType['DatastoreStorageArgs']]] = None,
                 file_format_configuration: Optional[pulumi.Input[pulumi.InputType['DatastoreFileFormatConfigurationArgs']]] = None,
                 retention_period: Optional[pulumi.Input[pulumi.InputType['DatastoreRetentionPeriodArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatastoreArgs.__new__(DatastoreArgs)

            __props__.__dict__["datastore_name"] = datastore_name
            __props__.__dict__["datastore_partitions"] = datastore_partitions
            __props__.__dict__["datastore_storage"] = datastore_storage
            __props__.__dict__["file_format_configuration"] = file_format_configuration
            __props__.__dict__["retention_period"] = retention_period
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["datastore_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Datastore, __self__).__init__(
            'aws-native:iotanalytics:Datastore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Datastore':
        """
        Get an existing Datastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatastoreArgs.__new__(DatastoreArgs)

        __props__.__dict__["datastore_name"] = None
        __props__.__dict__["datastore_partitions"] = None
        __props__.__dict__["datastore_storage"] = None
        __props__.__dict__["file_format_configuration"] = None
        __props__.__dict__["retention_period"] = None
        __props__.__dict__["tags"] = None
        return Datastore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "datastore_name")

    @property
    @pulumi.getter(name="datastorePartitions")
    def datastore_partitions(self) -> pulumi.Output[Optional['outputs.DatastorePartitions']]:
        return pulumi.get(self, "datastore_partitions")

    @property
    @pulumi.getter(name="datastoreStorage")
    def datastore_storage(self) -> pulumi.Output[Optional['outputs.DatastoreStorage']]:
        return pulumi.get(self, "datastore_storage")

    @property
    @pulumi.getter(name="fileFormatConfiguration")
    def file_format_configuration(self) -> pulumi.Output[Optional['outputs.DatastoreFileFormatConfiguration']]:
        return pulumi.get(self, "file_format_configuration")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional['outputs.DatastoreRetentionPeriod']]:
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

