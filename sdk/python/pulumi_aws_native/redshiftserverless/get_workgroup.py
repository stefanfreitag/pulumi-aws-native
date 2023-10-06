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
from ._enums import *

__all__ = [
    'GetWorkgroupResult',
    'AwaitableGetWorkgroupResult',
    'get_workgroup',
    'get_workgroup_output',
]

@pulumi.output_type
class GetWorkgroupResult:
    def __init__(__self__, enhanced_vpc_routing=None, port=None, publicly_accessible=None, workgroup=None):
        if enhanced_vpc_routing and not isinstance(enhanced_vpc_routing, bool):
            raise TypeError("Expected argument 'enhanced_vpc_routing' to be a bool")
        pulumi.set(__self__, "enhanced_vpc_routing", enhanced_vpc_routing)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if publicly_accessible and not isinstance(publicly_accessible, bool):
            raise TypeError("Expected argument 'publicly_accessible' to be a bool")
        pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if workgroup and not isinstance(workgroup, dict):
            raise TypeError("Expected argument 'workgroup' to be a dict")
        pulumi.set(__self__, "workgroup", workgroup)

    @property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[bool]:
        return pulumi.get(self, "enhanced_vpc_routing")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[bool]:
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter
    def workgroup(self) -> Optional['outputs.Workgroup']:
        return pulumi.get(self, "workgroup")


class AwaitableGetWorkgroupResult(GetWorkgroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkgroupResult(
            enhanced_vpc_routing=self.enhanced_vpc_routing,
            port=self.port,
            publicly_accessible=self.publicly_accessible,
            workgroup=self.workgroup)


def get_workgroup(workgroup_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkgroupResult:
    """
    Definition of AWS::RedshiftServerless::Workgroup Resource Type
    """
    __args__ = dict()
    __args__['workgroupName'] = workgroup_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:redshiftserverless:getWorkgroup', __args__, opts=opts, typ=GetWorkgroupResult).value

    return AwaitableGetWorkgroupResult(
        enhanced_vpc_routing=pulumi.get(__ret__, 'enhanced_vpc_routing'),
        port=pulumi.get(__ret__, 'port'),
        publicly_accessible=pulumi.get(__ret__, 'publicly_accessible'),
        workgroup=pulumi.get(__ret__, 'workgroup'))


@_utilities.lift_output_func(get_workgroup)
def get_workgroup_output(workgroup_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkgroupResult]:
    """
    Definition of AWS::RedshiftServerless::Workgroup Resource Type
    """
    ...
