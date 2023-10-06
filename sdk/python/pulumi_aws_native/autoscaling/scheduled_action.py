# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ScheduledActionArgs', 'ScheduledAction']

@pulumi.input_type
class ScheduledActionArgs:
    def __init__(__self__, *,
                 auto_scaling_group_name: pulumi.Input[str],
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 recurrence: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScheduledAction resource.
        :param pulumi.Input[str] auto_scaling_group_name: The name of the Auto Scaling group.
        :param pulumi.Input[int] desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        :param pulumi.Input[str] end_time: The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :param pulumi.Input[int] max_size: The minimum size of the Auto Scaling group.
        :param pulumi.Input[int] min_size: The minimum size of the Auto Scaling group.
        :param pulumi.Input[str] recurrence: The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        :param pulumi.Input[str] start_time: The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :param pulumi.Input[str] time_zone: The time zone for the cron expression.
        """
        ScheduledActionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auto_scaling_group_name=auto_scaling_group_name,
            desired_capacity=desired_capacity,
            end_time=end_time,
            max_size=max_size,
            min_size=min_size,
            recurrence=recurrence,
            start_time=start_time,
            time_zone=time_zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auto_scaling_group_name: pulumi.Input[str],
             desired_capacity: Optional[pulumi.Input[int]] = None,
             end_time: Optional[pulumi.Input[str]] = None,
             max_size: Optional[pulumi.Input[int]] = None,
             min_size: Optional[pulumi.Input[int]] = None,
             recurrence: Optional[pulumi.Input[str]] = None,
             start_time: Optional[pulumi.Input[str]] = None,
             time_zone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("auto_scaling_group_name", auto_scaling_group_name)
        if desired_capacity is not None:
            _setter("desired_capacity", desired_capacity)
        if end_time is not None:
            _setter("end_time", end_time)
        if max_size is not None:
            _setter("max_size", max_size)
        if min_size is not None:
            _setter("min_size", min_size)
        if recurrence is not None:
            _setter("recurrence", recurrence)
        if start_time is not None:
            _setter("start_time", start_time)
        if time_zone is not None:
            _setter("time_zone", time_zone)

    @property
    @pulumi.getter(name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Auto Scaling group.
        """
        return pulumi.get(self, "auto_scaling_group_name")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "auto_scaling_group_name", value)

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        """
        return pulumi.get(self, "desired_capacity")

    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "desired_capacity", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "min_size")

    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_size", value)

    @property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[str]]:
        """
        The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        """
        return pulumi.get(self, "recurrence")

    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone for the cron expression.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class ScheduledAction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_group_name: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 recurrence: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_scaling_group_name: The name of the Auto Scaling group.
        :param pulumi.Input[int] desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        :param pulumi.Input[str] end_time: The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :param pulumi.Input[int] max_size: The minimum size of the Auto Scaling group.
        :param pulumi.Input[int] min_size: The minimum size of the Auto Scaling group.
        :param pulumi.Input[str] recurrence: The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        :param pulumi.Input[str] start_time: The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :param pulumi.Input[str] time_zone: The time zone for the cron expression.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.

        :param str resource_name: The name of the resource.
        :param ScheduledActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ScheduledActionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scaling_group_name: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 recurrence: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduledActionArgs.__new__(ScheduledActionArgs)

            if auto_scaling_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'auto_scaling_group_name'")
            __props__.__dict__["auto_scaling_group_name"] = auto_scaling_group_name
            __props__.__dict__["desired_capacity"] = desired_capacity
            __props__.__dict__["end_time"] = end_time
            __props__.__dict__["max_size"] = max_size
            __props__.__dict__["min_size"] = min_size
            __props__.__dict__["recurrence"] = recurrence
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["scheduled_action_name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["auto_scaling_group_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ScheduledAction, __self__).__init__(
            'aws-native:autoscaling:ScheduledAction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledAction':
        """
        Get an existing ScheduledAction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledActionArgs.__new__(ScheduledActionArgs)

        __props__.__dict__["auto_scaling_group_name"] = None
        __props__.__dict__["desired_capacity"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["max_size"] = None
        __props__.__dict__["min_size"] = None
        __props__.__dict__["recurrence"] = None
        __props__.__dict__["scheduled_action_name"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["time_zone"] = None
        return ScheduledAction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Auto Scaling group.
        """
        return pulumi.get(self, "auto_scaling_group_name")

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Output[Optional[int]]:
        """
        The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        """
        return pulumi.get(self, "desired_capacity")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter
    def recurrence(self) -> pulumi.Output[Optional[str]]:
        """
        The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        """
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> pulumi.Output[str]:
        """
        Auto-generated unique identifier
        """
        return pulumi.get(self, "scheduled_action_name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The time zone for the cron expression.
        """
        return pulumi.get(self, "time_zone")

