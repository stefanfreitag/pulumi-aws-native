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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetRotationResult',
    'AwaitableGetRotationResult',
    'get_rotation',
    'get_rotation_output',
]

@pulumi.output_type
class GetRotationResult:
    def __init__(__self__, arn=None, contact_ids=None, name=None, recurrence=None, start_time=None, tags=None, time_zone_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if contact_ids and not isinstance(contact_ids, list):
            raise TypeError("Expected argument 'contact_ids' to be a list")
        pulumi.set(__self__, "contact_ids", contact_ids)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recurrence and not isinstance(recurrence, dict):
            raise TypeError("Expected argument 'recurrence' to be a dict")
        pulumi.set(__self__, "recurrence", recurrence)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if time_zone_id and not isinstance(time_zone_id, str):
            raise TypeError("Expected argument 'time_zone_id' to be a str")
        pulumi.set(__self__, "time_zone_id", time_zone_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the rotation.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contactIds")
    def contact_ids(self) -> Optional[Sequence[str]]:
        """
        Members of the rotation
        """
        return pulumi.get(self, "contact_ids")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the Rotation
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def recurrence(self) -> Optional['outputs.RotationRecurrenceSettings']:
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Start time of the first shift of Oncall Schedule
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[str]:
        """
        TimeZone Identifier for the Oncall Schedule
        """
        return pulumi.get(self, "time_zone_id")


class AwaitableGetRotationResult(GetRotationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRotationResult(
            arn=self.arn,
            contact_ids=self.contact_ids,
            name=self.name,
            recurrence=self.recurrence,
            start_time=self.start_time,
            tags=self.tags,
            time_zone_id=self.time_zone_id)


def get_rotation(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRotationResult:
    """
    Resource Type definition for AWS::SSMContacts::Rotation.


    :param str arn: The Amazon Resource Name (ARN) of the rotation.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ssmcontacts:getRotation', __args__, opts=opts, typ=GetRotationResult).value

    return AwaitableGetRotationResult(
        arn=pulumi.get(__ret__, 'arn'),
        contact_ids=pulumi.get(__ret__, 'contact_ids'),
        name=pulumi.get(__ret__, 'name'),
        recurrence=pulumi.get(__ret__, 'recurrence'),
        start_time=pulumi.get(__ret__, 'start_time'),
        tags=pulumi.get(__ret__, 'tags'),
        time_zone_id=pulumi.get(__ret__, 'time_zone_id'))


@_utilities.lift_output_func(get_rotation)
def get_rotation_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRotationResult]:
    """
    Resource Type definition for AWS::SSMContacts::Rotation.


    :param str arn: The Amazon Resource Name (ARN) of the rotation.
    """
    ...
