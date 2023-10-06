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
    'GetThreatIntelSetResult',
    'AwaitableGetThreatIntelSetResult',
    'get_threat_intel_set',
    'get_threat_intel_set_output',
]

@pulumi.output_type
class GetThreatIntelSetResult:
    def __init__(__self__, activate=None, id=None, location=None, name=None, tags=None):
        if activate and not isinstance(activate, bool):
            raise TypeError("Expected argument 'activate' to be a bool")
        pulumi.set(__self__, "activate", activate)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def activate(self) -> Optional[bool]:
        return pulumi.get(self, "activate")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ThreatIntelSetTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetThreatIntelSetResult(GetThreatIntelSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetThreatIntelSetResult(
            activate=self.activate,
            id=self.id,
            location=self.location,
            name=self.name,
            tags=self.tags)


def get_threat_intel_set(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetThreatIntelSetResult:
    """
    Resource Type definition for AWS::GuardDuty::ThreatIntelSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:guardduty:getThreatIntelSet', __args__, opts=opts, typ=GetThreatIntelSetResult).value

    return AwaitableGetThreatIntelSetResult(
        activate=pulumi.get(__ret__, 'activate'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_threat_intel_set)
def get_threat_intel_set_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetThreatIntelSetResult]:
    """
    Resource Type definition for AWS::GuardDuty::ThreatIntelSet
    """
    ...
