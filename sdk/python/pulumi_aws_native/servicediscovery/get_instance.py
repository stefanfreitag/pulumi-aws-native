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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, instance_attributes=None):
        if instance_attributes and not isinstance(instance_attributes, dict):
            raise TypeError("Expected argument 'instance_attributes' to be a dict")
        pulumi.set(__self__, "instance_attributes", instance_attributes)

    @property
    @pulumi.getter(name="instanceAttributes")
    def instance_attributes(self) -> Optional[Any]:
        return pulumi.get(self, "instance_attributes")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            instance_attributes=self.instance_attributes)


def get_instance(instance_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Resource Type definition for AWS::ServiceDiscovery::Instance
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicediscovery:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        instance_attributes=__ret__.instance_attributes)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Resource Type definition for AWS::ServiceDiscovery::Instance
    """
    ...
