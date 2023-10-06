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
    'GetCompositeAlarmResult',
    'AwaitableGetCompositeAlarmResult',
    'get_composite_alarm',
    'get_composite_alarm_output',
]

@pulumi.output_type
class GetCompositeAlarmResult:
    def __init__(__self__, actions_enabled=None, actions_suppressor=None, actions_suppressor_extension_period=None, actions_suppressor_wait_period=None, alarm_actions=None, alarm_description=None, alarm_rule=None, arn=None, insufficient_data_actions=None, ok_actions=None):
        if actions_enabled and not isinstance(actions_enabled, bool):
            raise TypeError("Expected argument 'actions_enabled' to be a bool")
        pulumi.set(__self__, "actions_enabled", actions_enabled)
        if actions_suppressor and not isinstance(actions_suppressor, str):
            raise TypeError("Expected argument 'actions_suppressor' to be a str")
        pulumi.set(__self__, "actions_suppressor", actions_suppressor)
        if actions_suppressor_extension_period and not isinstance(actions_suppressor_extension_period, int):
            raise TypeError("Expected argument 'actions_suppressor_extension_period' to be a int")
        pulumi.set(__self__, "actions_suppressor_extension_period", actions_suppressor_extension_period)
        if actions_suppressor_wait_period and not isinstance(actions_suppressor_wait_period, int):
            raise TypeError("Expected argument 'actions_suppressor_wait_period' to be a int")
        pulumi.set(__self__, "actions_suppressor_wait_period", actions_suppressor_wait_period)
        if alarm_actions and not isinstance(alarm_actions, list):
            raise TypeError("Expected argument 'alarm_actions' to be a list")
        pulumi.set(__self__, "alarm_actions", alarm_actions)
        if alarm_description and not isinstance(alarm_description, str):
            raise TypeError("Expected argument 'alarm_description' to be a str")
        pulumi.set(__self__, "alarm_description", alarm_description)
        if alarm_rule and not isinstance(alarm_rule, str):
            raise TypeError("Expected argument 'alarm_rule' to be a str")
        pulumi.set(__self__, "alarm_rule", alarm_rule)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if insufficient_data_actions and not isinstance(insufficient_data_actions, list):
            raise TypeError("Expected argument 'insufficient_data_actions' to be a list")
        pulumi.set(__self__, "insufficient_data_actions", insufficient_data_actions)
        if ok_actions and not isinstance(ok_actions, list):
            raise TypeError("Expected argument 'ok_actions' to be a list")
        pulumi.set(__self__, "ok_actions", ok_actions)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[bool]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @property
    @pulumi.getter(name="actionsSuppressor")
    def actions_suppressor(self) -> Optional[str]:
        """
        Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. 
        """
        return pulumi.get(self, "actions_suppressor")

    @property
    @pulumi.getter(name="actionsSuppressorExtensionPeriod")
    def actions_suppressor_extension_period(self) -> Optional[int]:
        """
        Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.
        """
        return pulumi.get(self, "actions_suppressor_extension_period")

    @property
    @pulumi.getter(name="actionsSuppressorWaitPeriod")
    def actions_suppressor_wait_period(self) -> Optional[int]:
        """
        Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.
        """
        return pulumi.get(self, "actions_suppressor_wait_period")

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[Sequence[str]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "alarm_actions")

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[str]:
        """
        The description of the alarm
        """
        return pulumi.get(self, "alarm_description")

    @property
    @pulumi.getter(name="alarmRule")
    def alarm_rule(self) -> Optional[str]:
        """
        Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
        """
        return pulumi.get(self, "alarm_rule")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the alarm
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[Sequence[str]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "insufficient_data_actions")

    @property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> Optional[Sequence[str]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "ok_actions")


class AwaitableGetCompositeAlarmResult(GetCompositeAlarmResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCompositeAlarmResult(
            actions_enabled=self.actions_enabled,
            actions_suppressor=self.actions_suppressor,
            actions_suppressor_extension_period=self.actions_suppressor_extension_period,
            actions_suppressor_wait_period=self.actions_suppressor_wait_period,
            alarm_actions=self.alarm_actions,
            alarm_description=self.alarm_description,
            alarm_rule=self.alarm_rule,
            arn=self.arn,
            insufficient_data_actions=self.insufficient_data_actions,
            ok_actions=self.ok_actions)


def get_composite_alarm(alarm_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCompositeAlarmResult:
    """
    The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression


    :param str alarm_name: The name of the Composite Alarm
    """
    __args__ = dict()
    __args__['alarmName'] = alarm_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudwatch:getCompositeAlarm', __args__, opts=opts, typ=GetCompositeAlarmResult).value

    return AwaitableGetCompositeAlarmResult(
        actions_enabled=pulumi.get(__ret__, 'actions_enabled'),
        actions_suppressor=pulumi.get(__ret__, 'actions_suppressor'),
        actions_suppressor_extension_period=pulumi.get(__ret__, 'actions_suppressor_extension_period'),
        actions_suppressor_wait_period=pulumi.get(__ret__, 'actions_suppressor_wait_period'),
        alarm_actions=pulumi.get(__ret__, 'alarm_actions'),
        alarm_description=pulumi.get(__ret__, 'alarm_description'),
        alarm_rule=pulumi.get(__ret__, 'alarm_rule'),
        arn=pulumi.get(__ret__, 'arn'),
        insufficient_data_actions=pulumi.get(__ret__, 'insufficient_data_actions'),
        ok_actions=pulumi.get(__ret__, 'ok_actions'))


@_utilities.lift_output_func(get_composite_alarm)
def get_composite_alarm_output(alarm_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCompositeAlarmResult]:
    """
    The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression


    :param str alarm_name: The name of the Composite Alarm
    """
    ...
