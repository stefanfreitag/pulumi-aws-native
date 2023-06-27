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

__all__ = [
    'GetFleetResult',
    'AwaitableGetFleetResult',
    'get_fleet',
    'get_fleet_output',
]

@pulumi.output_type
class GetFleetResult:
    def __init__(__self__, compute_capacity=None, description=None, disconnect_timeout_in_seconds=None, display_name=None, domain_join_info=None, enable_default_internet_access=None, iam_role_arn=None, id=None, idle_disconnect_timeout_in_seconds=None, image_arn=None, image_name=None, instance_type=None, max_concurrent_sessions=None, max_user_duration_in_seconds=None, platform=None, session_script_s3_location=None, stream_view=None, tags=None, usb_device_filter_strings=None, vpc_config=None):
        if compute_capacity and not isinstance(compute_capacity, dict):
            raise TypeError("Expected argument 'compute_capacity' to be a dict")
        pulumi.set(__self__, "compute_capacity", compute_capacity)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disconnect_timeout_in_seconds and not isinstance(disconnect_timeout_in_seconds, int):
            raise TypeError("Expected argument 'disconnect_timeout_in_seconds' to be a int")
        pulumi.set(__self__, "disconnect_timeout_in_seconds", disconnect_timeout_in_seconds)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if domain_join_info and not isinstance(domain_join_info, dict):
            raise TypeError("Expected argument 'domain_join_info' to be a dict")
        pulumi.set(__self__, "domain_join_info", domain_join_info)
        if enable_default_internet_access and not isinstance(enable_default_internet_access, bool):
            raise TypeError("Expected argument 'enable_default_internet_access' to be a bool")
        pulumi.set(__self__, "enable_default_internet_access", enable_default_internet_access)
        if iam_role_arn and not isinstance(iam_role_arn, str):
            raise TypeError("Expected argument 'iam_role_arn' to be a str")
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idle_disconnect_timeout_in_seconds and not isinstance(idle_disconnect_timeout_in_seconds, int):
            raise TypeError("Expected argument 'idle_disconnect_timeout_in_seconds' to be a int")
        pulumi.set(__self__, "idle_disconnect_timeout_in_seconds", idle_disconnect_timeout_in_seconds)
        if image_arn and not isinstance(image_arn, str):
            raise TypeError("Expected argument 'image_arn' to be a str")
        pulumi.set(__self__, "image_arn", image_arn)
        if image_name and not isinstance(image_name, str):
            raise TypeError("Expected argument 'image_name' to be a str")
        pulumi.set(__self__, "image_name", image_name)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if max_concurrent_sessions and not isinstance(max_concurrent_sessions, int):
            raise TypeError("Expected argument 'max_concurrent_sessions' to be a int")
        pulumi.set(__self__, "max_concurrent_sessions", max_concurrent_sessions)
        if max_user_duration_in_seconds and not isinstance(max_user_duration_in_seconds, int):
            raise TypeError("Expected argument 'max_user_duration_in_seconds' to be a int")
        pulumi.set(__self__, "max_user_duration_in_seconds", max_user_duration_in_seconds)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if session_script_s3_location and not isinstance(session_script_s3_location, dict):
            raise TypeError("Expected argument 'session_script_s3_location' to be a dict")
        pulumi.set(__self__, "session_script_s3_location", session_script_s3_location)
        if stream_view and not isinstance(stream_view, str):
            raise TypeError("Expected argument 'stream_view' to be a str")
        pulumi.set(__self__, "stream_view", stream_view)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if usb_device_filter_strings and not isinstance(usb_device_filter_strings, list):
            raise TypeError("Expected argument 'usb_device_filter_strings' to be a list")
        pulumi.set(__self__, "usb_device_filter_strings", usb_device_filter_strings)
        if vpc_config and not isinstance(vpc_config, dict):
            raise TypeError("Expected argument 'vpc_config' to be a dict")
        pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter(name="computeCapacity")
    def compute_capacity(self) -> Optional['outputs.FleetComputeCapacity']:
        return pulumi.get(self, "compute_capacity")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "disconnect_timeout_in_seconds")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional['outputs.FleetDomainJoinInfo']:
        return pulumi.get(self, "domain_join_info")

    @property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[bool]:
        return pulumi.get(self, "enable_default_internet_access")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[str]:
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "idle_disconnect_timeout_in_seconds")

    @property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[str]:
        return pulumi.get(self, "image_arn")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[str]:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> Optional[int]:
        return pulumi.get(self, "max_concurrent_sessions")

    @property
    @pulumi.getter(name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> Optional[int]:
        return pulumi.get(self, "max_user_duration_in_seconds")

    @property
    @pulumi.getter
    def platform(self) -> Optional[str]:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="sessionScriptS3Location")
    def session_script_s3_location(self) -> Optional['outputs.FleetS3Location']:
        return pulumi.get(self, "session_script_s3_location")

    @property
    @pulumi.getter(name="streamView")
    def stream_view(self) -> Optional[str]:
        return pulumi.get(self, "stream_view")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FleetTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="usbDeviceFilterStrings")
    def usb_device_filter_strings(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "usb_device_filter_strings")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional['outputs.FleetVpcConfig']:
        return pulumi.get(self, "vpc_config")


class AwaitableGetFleetResult(GetFleetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetResult(
            compute_capacity=self.compute_capacity,
            description=self.description,
            disconnect_timeout_in_seconds=self.disconnect_timeout_in_seconds,
            display_name=self.display_name,
            domain_join_info=self.domain_join_info,
            enable_default_internet_access=self.enable_default_internet_access,
            iam_role_arn=self.iam_role_arn,
            id=self.id,
            idle_disconnect_timeout_in_seconds=self.idle_disconnect_timeout_in_seconds,
            image_arn=self.image_arn,
            image_name=self.image_name,
            instance_type=self.instance_type,
            max_concurrent_sessions=self.max_concurrent_sessions,
            max_user_duration_in_seconds=self.max_user_duration_in_seconds,
            platform=self.platform,
            session_script_s3_location=self.session_script_s3_location,
            stream_view=self.stream_view,
            tags=self.tags,
            usb_device_filter_strings=self.usb_device_filter_strings,
            vpc_config=self.vpc_config)


def get_fleet(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetResult:
    """
    Resource Type definition for AWS::AppStream::Fleet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appstream:getFleet', __args__, opts=opts, typ=GetFleetResult).value

    return AwaitableGetFleetResult(
        compute_capacity=__ret__.compute_capacity,
        description=__ret__.description,
        disconnect_timeout_in_seconds=__ret__.disconnect_timeout_in_seconds,
        display_name=__ret__.display_name,
        domain_join_info=__ret__.domain_join_info,
        enable_default_internet_access=__ret__.enable_default_internet_access,
        iam_role_arn=__ret__.iam_role_arn,
        id=__ret__.id,
        idle_disconnect_timeout_in_seconds=__ret__.idle_disconnect_timeout_in_seconds,
        image_arn=__ret__.image_arn,
        image_name=__ret__.image_name,
        instance_type=__ret__.instance_type,
        max_concurrent_sessions=__ret__.max_concurrent_sessions,
        max_user_duration_in_seconds=__ret__.max_user_duration_in_seconds,
        platform=__ret__.platform,
        session_script_s3_location=__ret__.session_script_s3_location,
        stream_view=__ret__.stream_view,
        tags=__ret__.tags,
        usb_device_filter_strings=__ret__.usb_device_filter_strings,
        vpc_config=__ret__.vpc_config)


@_utilities.lift_output_func(get_fleet)
def get_fleet_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetResult]:
    """
    Resource Type definition for AWS::AppStream::Fleet
    """
    ...
