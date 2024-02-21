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
    'GetTriggerResult',
    'AwaitableGetTriggerResult',
    'get_trigger',
    'get_trigger_output',
]

@pulumi.output_type
class GetTriggerResult:
    def __init__(__self__, actions=None, description=None, event_batching_condition=None, id=None, predicate=None, schedule=None, start_on_creation=None, tags=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if event_batching_condition and not isinstance(event_batching_condition, dict):
            raise TypeError("Expected argument 'event_batching_condition' to be a dict")
        pulumi.set(__self__, "event_batching_condition", event_batching_condition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if predicate and not isinstance(predicate, dict):
            raise TypeError("Expected argument 'predicate' to be a dict")
        pulumi.set(__self__, "predicate", predicate)
        if schedule and not isinstance(schedule, str):
            raise TypeError("Expected argument 'schedule' to be a str")
        pulumi.set(__self__, "schedule", schedule)
        if start_on_creation and not isinstance(start_on_creation, bool):
            raise TypeError("Expected argument 'start_on_creation' to be a bool")
        pulumi.set(__self__, "start_on_creation", start_on_creation)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.TriggerAction']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventBatchingCondition")
    def event_batching_condition(self) -> Optional['outputs.TriggerEventBatchingCondition']:
        return pulumi.get(self, "event_batching_condition")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def predicate(self) -> Optional['outputs.TriggerPredicate']:
        return pulumi.get(self, "predicate")

    @property
    @pulumi.getter
    def schedule(self) -> Optional[str]:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="startOnCreation")
    def start_on_creation(self) -> Optional[bool]:
        return pulumi.get(self, "start_on_creation")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Trigger` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")


class AwaitableGetTriggerResult(GetTriggerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTriggerResult(
            actions=self.actions,
            description=self.description,
            event_batching_condition=self.event_batching_condition,
            id=self.id,
            predicate=self.predicate,
            schedule=self.schedule,
            start_on_creation=self.start_on_creation,
            tags=self.tags)


def get_trigger(id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTriggerResult:
    """
    Resource Type definition for AWS::Glue::Trigger
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getTrigger', __args__, opts=opts, typ=GetTriggerResult).value

    return AwaitableGetTriggerResult(
        actions=pulumi.get(__ret__, 'actions'),
        description=pulumi.get(__ret__, 'description'),
        event_batching_condition=pulumi.get(__ret__, 'event_batching_condition'),
        id=pulumi.get(__ret__, 'id'),
        predicate=pulumi.get(__ret__, 'predicate'),
        schedule=pulumi.get(__ret__, 'schedule'),
        start_on_creation=pulumi.get(__ret__, 'start_on_creation'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_trigger)
def get_trigger_output(id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTriggerResult]:
    """
    Resource Type definition for AWS::Glue::Trigger
    """
    ...
