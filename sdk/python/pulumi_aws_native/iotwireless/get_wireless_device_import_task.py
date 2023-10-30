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
    'GetWirelessDeviceImportTaskResult',
    'AwaitableGetWirelessDeviceImportTaskResult',
    'get_wireless_device_import_task',
    'get_wireless_device_import_task_output',
]

@pulumi.output_type
class GetWirelessDeviceImportTaskResult:
    def __init__(__self__, arn=None, creation_date=None, destination_name=None, failed_imported_devices_count=None, id=None, initialized_imported_devices_count=None, onboarded_imported_devices_count=None, pending_imported_devices_count=None, sidewalk=None, status=None, status_reason=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if destination_name and not isinstance(destination_name, str):
            raise TypeError("Expected argument 'destination_name' to be a str")
        pulumi.set(__self__, "destination_name", destination_name)
        if failed_imported_devices_count and not isinstance(failed_imported_devices_count, int):
            raise TypeError("Expected argument 'failed_imported_devices_count' to be a int")
        pulumi.set(__self__, "failed_imported_devices_count", failed_imported_devices_count)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initialized_imported_devices_count and not isinstance(initialized_imported_devices_count, int):
            raise TypeError("Expected argument 'initialized_imported_devices_count' to be a int")
        pulumi.set(__self__, "initialized_imported_devices_count", initialized_imported_devices_count)
        if onboarded_imported_devices_count and not isinstance(onboarded_imported_devices_count, int):
            raise TypeError("Expected argument 'onboarded_imported_devices_count' to be a int")
        pulumi.set(__self__, "onboarded_imported_devices_count", onboarded_imported_devices_count)
        if pending_imported_devices_count and not isinstance(pending_imported_devices_count, int):
            raise TypeError("Expected argument 'pending_imported_devices_count' to be a int")
        pulumi.set(__self__, "pending_imported_devices_count", pending_imported_devices_count)
        if sidewalk and not isinstance(sidewalk, dict):
            raise TypeError("Expected argument 'sidewalk' to be a dict")
        pulumi.set(__self__, "sidewalk", sidewalk)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        pulumi.set(__self__, "status_reason", status_reason)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Arn for Wireless Device Import Task, Returned upon successful start.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        CreationDate for import task
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> Optional[str]:
        """
        Destination Name for import task
        """
        return pulumi.get(self, "destination_name")

    @property
    @pulumi.getter(name="failedImportedDevicesCount")
    def failed_imported_devices_count(self) -> Optional[int]:
        """
        Failed Imported Devices Count
        """
        return pulumi.get(self, "failed_imported_devices_count")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id for Wireless Device Import Task, Returned upon successful start.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initializedImportedDevicesCount")
    def initialized_imported_devices_count(self) -> Optional[int]:
        """
        Initialized Imported Devices Count
        """
        return pulumi.get(self, "initialized_imported_devices_count")

    @property
    @pulumi.getter(name="onboardedImportedDevicesCount")
    def onboarded_imported_devices_count(self) -> Optional[int]:
        """
        Onboarded Imported Devices Count
        """
        return pulumi.get(self, "onboarded_imported_devices_count")

    @property
    @pulumi.getter(name="pendingImportedDevicesCount")
    def pending_imported_devices_count(self) -> Optional[int]:
        """
        Pending Imported Devices Count
        """
        return pulumi.get(self, "pending_imported_devices_count")

    @property
    @pulumi.getter
    def sidewalk(self) -> Optional['outputs.SidewalkProperties']:
        """
        sidewalk contain file for created device and role
        """
        return pulumi.get(self, "sidewalk")

    @property
    @pulumi.getter
    def status(self) -> Optional['WirelessDeviceImportTaskStatus']:
        """
        Status for import task
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[str]:
        """
        StatusReason for import task
        """
        return pulumi.get(self, "status_reason")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WirelessDeviceImportTaskTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetWirelessDeviceImportTaskResult(GetWirelessDeviceImportTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWirelessDeviceImportTaskResult(
            arn=self.arn,
            creation_date=self.creation_date,
            destination_name=self.destination_name,
            failed_imported_devices_count=self.failed_imported_devices_count,
            id=self.id,
            initialized_imported_devices_count=self.initialized_imported_devices_count,
            onboarded_imported_devices_count=self.onboarded_imported_devices_count,
            pending_imported_devices_count=self.pending_imported_devices_count,
            sidewalk=self.sidewalk,
            status=self.status,
            status_reason=self.status_reason,
            tags=self.tags)


def get_wireless_device_import_task(id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWirelessDeviceImportTaskResult:
    """
    Wireless Device Import Tasks


    :param str id: Id for Wireless Device Import Task, Returned upon successful start.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotwireless:getWirelessDeviceImportTask', __args__, opts=opts, typ=GetWirelessDeviceImportTaskResult).value

    return AwaitableGetWirelessDeviceImportTaskResult(
        arn=pulumi.get(__ret__, 'arn'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        destination_name=pulumi.get(__ret__, 'destination_name'),
        failed_imported_devices_count=pulumi.get(__ret__, 'failed_imported_devices_count'),
        id=pulumi.get(__ret__, 'id'),
        initialized_imported_devices_count=pulumi.get(__ret__, 'initialized_imported_devices_count'),
        onboarded_imported_devices_count=pulumi.get(__ret__, 'onboarded_imported_devices_count'),
        pending_imported_devices_count=pulumi.get(__ret__, 'pending_imported_devices_count'),
        sidewalk=pulumi.get(__ret__, 'sidewalk'),
        status=pulumi.get(__ret__, 'status'),
        status_reason=pulumi.get(__ret__, 'status_reason'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_wireless_device_import_task)
def get_wireless_device_import_task_output(id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWirelessDeviceImportTaskResult]:
    """
    Wireless Device Import Tasks


    :param str id: Id for Wireless Device Import Task, Returned upon successful start.
    """
    ...
