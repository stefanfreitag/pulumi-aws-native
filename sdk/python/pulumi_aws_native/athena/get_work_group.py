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
    'GetWorkGroupResult',
    'AwaitableGetWorkGroupResult',
    'get_work_group',
    'get_work_group_output',
]

@pulumi.output_type
class GetWorkGroupResult:
    def __init__(__self__, creation_time=None, description=None, state=None, tags=None, work_group_configuration=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if work_group_configuration and not isinstance(work_group_configuration, dict):
            raise TypeError("Expected argument 'work_group_configuration' to be a dict")
        pulumi.set(__self__, "work_group_configuration", work_group_configuration)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The date and time the workgroup was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The workgroup description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def state(self) -> Optional['WorkGroupState']:
        """
        The state of the workgroup: ENABLED or DISABLED.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WorkGroupTag']]:
        """
        One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workGroupConfiguration")
    def work_group_configuration(self) -> Optional['outputs.WorkGroupConfiguration']:
        """
        The workgroup configuration
        """
        return pulumi.get(self, "work_group_configuration")


class AwaitableGetWorkGroupResult(GetWorkGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkGroupResult(
            creation_time=self.creation_time,
            description=self.description,
            state=self.state,
            tags=self.tags,
            work_group_configuration=self.work_group_configuration)


def get_work_group(name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkGroupResult:
    """
    Resource schema for AWS::Athena::WorkGroup


    :param str name: The workGroup name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:athena:getWorkGroup', __args__, opts=opts, typ=GetWorkGroupResult).value

    return AwaitableGetWorkGroupResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'),
        work_group_configuration=pulumi.get(__ret__, 'work_group_configuration'))


@_utilities.lift_output_func(get_work_group)
def get_work_group_output(name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkGroupResult]:
    """
    Resource schema for AWS::Athena::WorkGroup


    :param str name: The workGroup name.
    """
    ...
