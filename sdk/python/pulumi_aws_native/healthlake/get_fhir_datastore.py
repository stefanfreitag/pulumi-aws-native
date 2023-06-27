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

__all__ = [
    'GetFHIRDatastoreResult',
    'AwaitableGetFHIRDatastoreResult',
    'get_fhir_datastore',
    'get_fhir_datastore_output',
]

@pulumi.output_type
class GetFHIRDatastoreResult:
    def __init__(__self__, created_at=None, datastore_arn=None, datastore_endpoint=None, datastore_id=None, datastore_status=None, tags=None):
        if created_at and not isinstance(created_at, dict):
            raise TypeError("Expected argument 'created_at' to be a dict")
        pulumi.set(__self__, "created_at", created_at)
        if datastore_arn and not isinstance(datastore_arn, str):
            raise TypeError("Expected argument 'datastore_arn' to be a str")
        pulumi.set(__self__, "datastore_arn", datastore_arn)
        if datastore_endpoint and not isinstance(datastore_endpoint, str):
            raise TypeError("Expected argument 'datastore_endpoint' to be a str")
        pulumi.set(__self__, "datastore_endpoint", datastore_endpoint)
        if datastore_id and not isinstance(datastore_id, str):
            raise TypeError("Expected argument 'datastore_id' to be a str")
        pulumi.set(__self__, "datastore_id", datastore_id)
        if datastore_status and not isinstance(datastore_status, str):
            raise TypeError("Expected argument 'datastore_status' to be a str")
        pulumi.set(__self__, "datastore_status", datastore_status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional['outputs.FHIRDatastoreCreatedAt']:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="datastoreArn")
    def datastore_arn(self) -> Optional[str]:
        return pulumi.get(self, "datastore_arn")

    @property
    @pulumi.getter(name="datastoreEndpoint")
    def datastore_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "datastore_endpoint")

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[str]:
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter(name="datastoreStatus")
    def datastore_status(self) -> Optional['FHIRDatastoreDatastoreStatus']:
        return pulumi.get(self, "datastore_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FHIRDatastoreTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetFHIRDatastoreResult(GetFHIRDatastoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFHIRDatastoreResult(
            created_at=self.created_at,
            datastore_arn=self.datastore_arn,
            datastore_endpoint=self.datastore_endpoint,
            datastore_id=self.datastore_id,
            datastore_status=self.datastore_status,
            tags=self.tags)


def get_fhir_datastore(datastore_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFHIRDatastoreResult:
    """
    HealthLake FHIR Datastore
    """
    __args__ = dict()
    __args__['datastoreId'] = datastore_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:healthlake:getFHIRDatastore', __args__, opts=opts, typ=GetFHIRDatastoreResult).value

    return AwaitableGetFHIRDatastoreResult(
        created_at=__ret__.created_at,
        datastore_arn=__ret__.datastore_arn,
        datastore_endpoint=__ret__.datastore_endpoint,
        datastore_id=__ret__.datastore_id,
        datastore_status=__ret__.datastore_status,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_fhir_datastore)
def get_fhir_datastore_output(datastore_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFHIRDatastoreResult]:
    """
    HealthLake FHIR Datastore
    """
    ...
