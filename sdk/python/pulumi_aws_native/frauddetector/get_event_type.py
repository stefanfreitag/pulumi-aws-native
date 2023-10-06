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
    'GetEventTypeResult',
    'AwaitableGetEventTypeResult',
    'get_event_type',
    'get_event_type_output',
]

@pulumi.output_type
class GetEventTypeResult:
    def __init__(__self__, arn=None, created_time=None, description=None, entity_types=None, event_variables=None, labels=None, last_updated_time=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if entity_types and not isinstance(entity_types, list):
            raise TypeError("Expected argument 'entity_types' to be a list")
        pulumi.set(__self__, "entity_types", entity_types)
        if event_variables and not isinstance(event_variables, list):
            raise TypeError("Expected argument 'event_variables' to be a list")
        pulumi.set(__self__, "event_variables", event_variables)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the event type.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        The time when the event type was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the event type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="entityTypes")
    def entity_types(self) -> Optional[Sequence['outputs.EventTypeEntityType']]:
        return pulumi.get(self, "entity_types")

    @property
    @pulumi.getter(name="eventVariables")
    def event_variables(self) -> Optional[Sequence['outputs.EventTypeEventVariable']]:
        return pulumi.get(self, "event_variables")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.EventTypeLabel']]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The time when the event type was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.EventTypeTag']]:
        """
        Tags associated with this event type.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEventTypeResult(GetEventTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventTypeResult(
            arn=self.arn,
            created_time=self.created_time,
            description=self.description,
            entity_types=self.entity_types,
            event_variables=self.event_variables,
            labels=self.labels,
            last_updated_time=self.last_updated_time,
            tags=self.tags)


def get_event_type(arn: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventTypeResult:
    """
    A resource schema for an EventType in Amazon Fraud Detector.


    :param str arn: The ARN of the event type.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:frauddetector:getEventType', __args__, opts=opts, typ=GetEventTypeResult).value

    return AwaitableGetEventTypeResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        description=pulumi.get(__ret__, 'description'),
        entity_types=pulumi.get(__ret__, 'entity_types'),
        event_variables=pulumi.get(__ret__, 'event_variables'),
        labels=pulumi.get(__ret__, 'labels'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_event_type)
def get_event_type_output(arn: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventTypeResult]:
    """
    A resource schema for an EventType in Amazon Fraud Detector.


    :param str arn: The ARN of the event type.
    """
    ...
