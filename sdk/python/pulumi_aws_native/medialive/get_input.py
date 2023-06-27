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
    'GetInputResult',
    'AwaitableGetInputResult',
    'get_input',
    'get_input_output',
]

@pulumi.output_type
class GetInputResult:
    def __init__(__self__, arn=None, destinations=None, id=None, input_devices=None, input_security_groups=None, media_connect_flows=None, name=None, role_arn=None, sources=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if destinations and not isinstance(destinations, list):
            raise TypeError("Expected argument 'destinations' to be a list")
        pulumi.set(__self__, "destinations", destinations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if input_devices and not isinstance(input_devices, list):
            raise TypeError("Expected argument 'input_devices' to be a list")
        pulumi.set(__self__, "input_devices", input_devices)
        if input_security_groups and not isinstance(input_security_groups, list):
            raise TypeError("Expected argument 'input_security_groups' to be a list")
        pulumi.set(__self__, "input_security_groups", input_security_groups)
        if media_connect_flows and not isinstance(media_connect_flows, list):
            raise TypeError("Expected argument 'media_connect_flows' to be a list")
        pulumi.set(__self__, "media_connect_flows", media_connect_flows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.InputDestinationRequest']]:
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[Sequence['outputs.InputDeviceSettings']]:
        return pulumi.get(self, "input_devices")

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "input_security_groups")

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[Sequence['outputs.InputMediaConnectFlowRequest']]:
        return pulumi.get(self, "media_connect_flows")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.InputSourceRequest']]:
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")


class AwaitableGetInputResult(GetInputResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInputResult(
            arn=self.arn,
            destinations=self.destinations,
            id=self.id,
            input_devices=self.input_devices,
            input_security_groups=self.input_security_groups,
            media_connect_flows=self.media_connect_flows,
            name=self.name,
            role_arn=self.role_arn,
            sources=self.sources,
            tags=self.tags)


def get_input(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInputResult:
    """
    Resource Type definition for AWS::MediaLive::Input
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:medialive:getInput', __args__, opts=opts, typ=GetInputResult).value

    return AwaitableGetInputResult(
        arn=__ret__.arn,
        destinations=__ret__.destinations,
        id=__ret__.id,
        input_devices=__ret__.input_devices,
        input_security_groups=__ret__.input_security_groups,
        media_connect_flows=__ret__.media_connect_flows,
        name=__ret__.name,
        role_arn=__ret__.role_arn,
        sources=__ret__.sources,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_input)
def get_input_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInputResult]:
    """
    Resource Type definition for AWS::MediaLive::Input
    """
    ...
