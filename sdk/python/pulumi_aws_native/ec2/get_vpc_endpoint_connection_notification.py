# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVPCEndpointConnectionNotificationResult',
    'AwaitableGetVPCEndpointConnectionNotificationResult',
    'get_vpc_endpoint_connection_notification',
    'get_vpc_endpoint_connection_notification_output',
]

@pulumi.output_type
class GetVPCEndpointConnectionNotificationResult:
    def __init__(__self__, connection_events=None, connection_notification_arn=None, id=None):
        if connection_events and not isinstance(connection_events, list):
            raise TypeError("Expected argument 'connection_events' to be a list")
        pulumi.set(__self__, "connection_events", connection_events)
        if connection_notification_arn and not isinstance(connection_notification_arn, str):
            raise TypeError("Expected argument 'connection_notification_arn' to be a str")
        pulumi.set(__self__, "connection_notification_arn", connection_notification_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="connectionEvents")
    def connection_events(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "connection_events")

    @property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> Optional[str]:
        return pulumi.get(self, "connection_notification_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetVPCEndpointConnectionNotificationResult(GetVPCEndpointConnectionNotificationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVPCEndpointConnectionNotificationResult(
            connection_events=self.connection_events,
            connection_notification_arn=self.connection_notification_arn,
            id=self.id)


def get_vpc_endpoint_connection_notification(id: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVPCEndpointConnectionNotificationResult:
    """
    Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVPCEndpointConnectionNotification', __args__, opts=opts, typ=GetVPCEndpointConnectionNotificationResult).value

    return AwaitableGetVPCEndpointConnectionNotificationResult(
        connection_events=__ret__.connection_events,
        connection_notification_arn=__ret__.connection_notification_arn,
        id=__ret__.id)


@_utilities.lift_output_func(get_vpc_endpoint_connection_notification)
def get_vpc_endpoint_connection_notification_output(id: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVPCEndpointConnectionNotificationResult]:
    """
    Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
    """
    ...
