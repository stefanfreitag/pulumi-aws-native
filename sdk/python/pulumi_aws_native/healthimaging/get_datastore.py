# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetDatastoreResult',
    'AwaitableGetDatastoreResult',
    'get_datastore',
    'get_datastore_output',
]

@pulumi.output_type
class GetDatastoreResult:
    def __init__(__self__, created_at=None, datastore_arn=None, datastore_id=None, datastore_status=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if datastore_arn and not isinstance(datastore_arn, str):
            raise TypeError("Expected argument 'datastore_arn' to be a str")
        pulumi.set(__self__, "datastore_arn", datastore_arn)
        if datastore_id and not isinstance(datastore_id, str):
            raise TypeError("Expected argument 'datastore_id' to be a str")
        pulumi.set(__self__, "datastore_id", datastore_id)
        if datastore_status and not isinstance(datastore_status, str):
            raise TypeError("Expected argument 'datastore_status' to be a str")
        pulumi.set(__self__, "datastore_status", datastore_status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="datastoreArn")
    def datastore_arn(self) -> Optional[str]:
        return pulumi.get(self, "datastore_arn")

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[str]:
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter(name="datastoreStatus")
    def datastore_status(self) -> Optional['DatastoreStatus']:
        return pulumi.get(self, "datastore_status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        return pulumi.get(self, "updated_at")


class AwaitableGetDatastoreResult(GetDatastoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatastoreResult(
            created_at=self.created_at,
            datastore_arn=self.datastore_arn,
            datastore_id=self.datastore_id,
            datastore_status=self.datastore_status,
            updated_at=self.updated_at)


def get_datastore(datastore_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatastoreResult:
    """
    Definition of AWS::HealthImaging::Datastore Resource Type
    """
    __args__ = dict()
    __args__['datastoreId'] = datastore_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:healthimaging:getDatastore', __args__, opts=opts, typ=GetDatastoreResult).value

    return AwaitableGetDatastoreResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        datastore_arn=pulumi.get(__ret__, 'datastore_arn'),
        datastore_id=pulumi.get(__ret__, 'datastore_id'),
        datastore_status=pulumi.get(__ret__, 'datastore_status'),
        updated_at=pulumi.get(__ret__, 'updated_at'))


@_utilities.lift_output_func(get_datastore)
def get_datastore_output(datastore_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatastoreResult]:
    """
    Definition of AWS::HealthImaging::Datastore Resource Type
    """
    ...
