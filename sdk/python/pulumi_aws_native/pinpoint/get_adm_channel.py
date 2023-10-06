# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetAdmChannelResult',
    'AwaitableGetAdmChannelResult',
    'get_adm_channel',
    'get_adm_channel_output',
]

@pulumi.output_type
class GetAdmChannelResult:
    def __init__(__self__, client_id=None, client_secret=None, enabled=None, id=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetAdmChannelResult(GetAdmChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAdmChannelResult(
            client_id=self.client_id,
            client_secret=self.client_secret,
            enabled=self.enabled,
            id=self.id)


def get_adm_channel(id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAdmChannelResult:
    """
    Resource Type definition for AWS::Pinpoint::ADMChannel
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpoint:getAdmChannel', __args__, opts=opts, typ=GetAdmChannelResult).value

    return AwaitableGetAdmChannelResult(
        client_id=pulumi.get(__ret__, 'client_id'),
        client_secret=pulumi.get(__ret__, 'client_secret'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_adm_channel)
def get_adm_channel_output(id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAdmChannelResult]:
    """
    Resource Type definition for AWS::Pinpoint::ADMChannel
    """
    ...
