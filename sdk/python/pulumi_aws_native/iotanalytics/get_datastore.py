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
from .. import outputs as _root_outputs

__all__ = [
    'GetDatastoreResult',
    'AwaitableGetDatastoreResult',
    'get_datastore',
    'get_datastore_output',
]

@pulumi.output_type
class GetDatastoreResult:
    def __init__(__self__, datastore_partitions=None, datastore_storage=None, file_format_configuration=None, id=None, retention_period=None, tags=None):
        if datastore_partitions and not isinstance(datastore_partitions, dict):
            raise TypeError("Expected argument 'datastore_partitions' to be a dict")
        pulumi.set(__self__, "datastore_partitions", datastore_partitions)
        if datastore_storage and not isinstance(datastore_storage, dict):
            raise TypeError("Expected argument 'datastore_storage' to be a dict")
        pulumi.set(__self__, "datastore_storage", datastore_storage)
        if file_format_configuration and not isinstance(file_format_configuration, dict):
            raise TypeError("Expected argument 'file_format_configuration' to be a dict")
        pulumi.set(__self__, "file_format_configuration", file_format_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if retention_period and not isinstance(retention_period, dict):
            raise TypeError("Expected argument 'retention_period' to be a dict")
        pulumi.set(__self__, "retention_period", retention_period)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datastorePartitions")
    def datastore_partitions(self) -> Optional['outputs.DatastorePartitions']:
        return pulumi.get(self, "datastore_partitions")

    @property
    @pulumi.getter(name="datastoreStorage")
    def datastore_storage(self) -> Optional['outputs.DatastoreStorage']:
        return pulumi.get(self, "datastore_storage")

    @property
    @pulumi.getter(name="fileFormatConfiguration")
    def file_format_configuration(self) -> Optional['outputs.DatastoreFileFormatConfiguration']:
        return pulumi.get(self, "file_format_configuration")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional['outputs.DatastoreRetentionPeriod']:
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetDatastoreResult(GetDatastoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatastoreResult(
            datastore_partitions=self.datastore_partitions,
            datastore_storage=self.datastore_storage,
            file_format_configuration=self.file_format_configuration,
            id=self.id,
            retention_period=self.retention_period,
            tags=self.tags)


def get_datastore(datastore_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatastoreResult:
    """
    Resource Type definition for AWS::IoTAnalytics::Datastore
    """
    __args__ = dict()
    __args__['datastoreName'] = datastore_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotanalytics:getDatastore', __args__, opts=opts, typ=GetDatastoreResult).value

    return AwaitableGetDatastoreResult(
        datastore_partitions=pulumi.get(__ret__, 'datastore_partitions'),
        datastore_storage=pulumi.get(__ret__, 'datastore_storage'),
        file_format_configuration=pulumi.get(__ret__, 'file_format_configuration'),
        id=pulumi.get(__ret__, 'id'),
        retention_period=pulumi.get(__ret__, 'retention_period'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_datastore)
def get_datastore_output(datastore_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatastoreResult]:
    """
    Resource Type definition for AWS::IoTAnalytics::Datastore
    """
    ...
