# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetListenerResult',
    'AwaitableGetListenerResult',
    'get_listener',
    'get_listener_output',
]

@pulumi.output_type
class GetListenerResult:
    def __init__(__self__, arn=None, default_action=None, id=None, service_arn=None, service_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if default_action and not isinstance(default_action, dict):
            raise TypeError("Expected argument 'default_action' to be a dict")
        pulumi.set(__self__, "default_action", default_action)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if service_arn and not isinstance(service_arn, str):
            raise TypeError("Expected argument 'service_arn' to be a str")
        pulumi.set(__self__, "service_arn", service_arn)
        if service_id and not isinstance(service_id, str):
            raise TypeError("Expected argument 'service_id' to be a str")
        pulumi.set(__self__, "service_id", service_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional['outputs.ListenerDefaultAction']:
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> Optional[str]:
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[str]:
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ListenerTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetListenerResult(GetListenerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerResult(
            arn=self.arn,
            default_action=self.default_action,
            id=self.id,
            service_arn=self.service_arn,
            service_id=self.service_id,
            tags=self.tags)


def get_listener(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerResult:
    """
    Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:vpclattice:getListener', __args__, opts=opts, typ=GetListenerResult).value

    return AwaitableGetListenerResult(
        arn=pulumi.get(__ret__, 'arn'),
        default_action=pulumi.get(__ret__, 'default_action'),
        id=pulumi.get(__ret__, 'id'),
        service_arn=pulumi.get(__ret__, 'service_arn'),
        service_id=pulumi.get(__ret__, 'service_id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_listener)
def get_listener_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerResult]:
    """
    Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.
    """
    ...
