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
    'GetScheduleResult',
    'AwaitableGetScheduleResult',
    'get_schedule',
    'get_schedule_output',
]

@pulumi.output_type
class GetScheduleResult:
    def __init__(__self__, arn=None, description=None, end_date=None, flexible_time_window=None, group_name=None, kms_key_arn=None, schedule_expression=None, schedule_expression_timezone=None, start_date=None, state=None, target=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if end_date and not isinstance(end_date, str):
            raise TypeError("Expected argument 'end_date' to be a str")
        pulumi.set(__self__, "end_date", end_date)
        if flexible_time_window and not isinstance(flexible_time_window, dict):
            raise TypeError("Expected argument 'flexible_time_window' to be a dict")
        pulumi.set(__self__, "flexible_time_window", flexible_time_window)
        if group_name and not isinstance(group_name, str):
            raise TypeError("Expected argument 'group_name' to be a str")
        pulumi.set(__self__, "group_name", group_name)
        if kms_key_arn and not isinstance(kms_key_arn, str):
            raise TypeError("Expected argument 'kms_key_arn' to be a str")
        pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if schedule_expression and not isinstance(schedule_expression, str):
            raise TypeError("Expected argument 'schedule_expression' to be a str")
        pulumi.set(__self__, "schedule_expression", schedule_expression)
        if schedule_expression_timezone and not isinstance(schedule_expression_timezone, str):
            raise TypeError("Expected argument 'schedule_expression_timezone' to be a str")
        pulumi.set(__self__, "schedule_expression_timezone", schedule_expression_timezone)
        if start_date and not isinstance(start_date, str):
            raise TypeError("Expected argument 'start_date' to be a str")
        pulumi.set(__self__, "start_date", start_date)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target and not isinstance(target, dict):
            raise TypeError("Expected argument 'target' to be a dict")
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the schedule.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[str]:
        """
        The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> Optional['outputs.ScheduleFlexibleTimeWindow']:
        return pulumi.get(self, "flexible_time_window")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        """
        The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[str]:
        """
        The ARN for a KMS Key that will be used to encrypt customer data.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[str]:
        """
        The scheduling expression.
        """
        return pulumi.get(self, "schedule_expression")

    @property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[str]:
        """
        The timezone in which the scheduling expression is evaluated.
        """
        return pulumi.get(self, "schedule_expression_timezone")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[str]:
        """
        The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def state(self) -> Optional['ScheduleState']:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def target(self) -> Optional['outputs.ScheduleTarget']:
        return pulumi.get(self, "target")


class AwaitableGetScheduleResult(GetScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduleResult(
            arn=self.arn,
            description=self.description,
            end_date=self.end_date,
            flexible_time_window=self.flexible_time_window,
            group_name=self.group_name,
            kms_key_arn=self.kms_key_arn,
            schedule_expression=self.schedule_expression,
            schedule_expression_timezone=self.schedule_expression_timezone,
            start_date=self.start_date,
            state=self.state,
            target=self.target)


def get_schedule(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleResult:
    """
    Definition of AWS::Scheduler::Schedule Resource Type
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:scheduler:getSchedule', __args__, opts=opts, typ=GetScheduleResult).value

    return AwaitableGetScheduleResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        end_date=pulumi.get(__ret__, 'end_date'),
        flexible_time_window=pulumi.get(__ret__, 'flexible_time_window'),
        group_name=pulumi.get(__ret__, 'group_name'),
        kms_key_arn=pulumi.get(__ret__, 'kms_key_arn'),
        schedule_expression=pulumi.get(__ret__, 'schedule_expression'),
        schedule_expression_timezone=pulumi.get(__ret__, 'schedule_expression_timezone'),
        start_date=pulumi.get(__ret__, 'start_date'),
        state=pulumi.get(__ret__, 'state'),
        target=pulumi.get(__ret__, 'target'))


@_utilities.lift_output_func(get_schedule)
def get_schedule_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleResult]:
    """
    Definition of AWS::Scheduler::Schedule Resource Type
    """
    ...
