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
    'GetTaskResult',
    'AwaitableGetTaskResult',
    'get_task',
    'get_task_output',
]

@pulumi.output_type
class GetTaskResult:
    def __init__(__self__, cloud_watch_log_group_arn=None, destination_network_interface_arns=None, excludes=None, includes=None, name=None, options=None, schedule=None, source_network_interface_arns=None, status=None, tags=None, task_arn=None, task_report_config=None):
        if cloud_watch_log_group_arn and not isinstance(cloud_watch_log_group_arn, str):
            raise TypeError("Expected argument 'cloud_watch_log_group_arn' to be a str")
        pulumi.set(__self__, "cloud_watch_log_group_arn", cloud_watch_log_group_arn)
        if destination_network_interface_arns and not isinstance(destination_network_interface_arns, list):
            raise TypeError("Expected argument 'destination_network_interface_arns' to be a list")
        pulumi.set(__self__, "destination_network_interface_arns", destination_network_interface_arns)
        if excludes and not isinstance(excludes, list):
            raise TypeError("Expected argument 'excludes' to be a list")
        pulumi.set(__self__, "excludes", excludes)
        if includes and not isinstance(includes, list):
            raise TypeError("Expected argument 'includes' to be a list")
        pulumi.set(__self__, "includes", includes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, dict):
            raise TypeError("Expected argument 'options' to be a dict")
        pulumi.set(__self__, "options", options)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if source_network_interface_arns and not isinstance(source_network_interface_arns, list):
            raise TypeError("Expected argument 'source_network_interface_arns' to be a list")
        pulumi.set(__self__, "source_network_interface_arns", source_network_interface_arns)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if task_arn and not isinstance(task_arn, str):
            raise TypeError("Expected argument 'task_arn' to be a str")
        pulumi.set(__self__, "task_arn", task_arn)
        if task_report_config and not isinstance(task_report_config, dict):
            raise TypeError("Expected argument 'task_report_config' to be a dict")
        pulumi.set(__self__, "task_report_config", task_report_config)

    @property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[str]:
        """
        The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
        """
        return pulumi.get(self, "cloud_watch_log_group_arn")

    @property
    @pulumi.getter(name="destinationNetworkInterfaceArns")
    def destination_network_interface_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "destination_network_interface_arns")

    @property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence['outputs.TaskFilterRule']]:
        return pulumi.get(self, "excludes")

    @property
    @pulumi.getter
    def includes(self) -> Optional[Sequence['outputs.TaskFilterRule']]:
        return pulumi.get(self, "includes")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of a task. This value is a text reference that is used to identify the task in the console.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Optional['outputs.TaskOptions']:
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.TaskSchedule']:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="sourceNetworkInterfaceArns")
    def source_network_interface_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "source_network_interface_arns")

    @property
    @pulumi.getter
    def status(self) -> Optional['TaskStatus']:
        """
        The status of the task that was described.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskArn")
    def task_arn(self) -> Optional[str]:
        """
        The ARN of the task.
        """
        return pulumi.get(self, "task_arn")

    @property
    @pulumi.getter(name="taskReportConfig")
    def task_report_config(self) -> Optional['outputs.TaskReportConfig']:
        return pulumi.get(self, "task_report_config")


class AwaitableGetTaskResult(GetTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskResult(
            cloud_watch_log_group_arn=self.cloud_watch_log_group_arn,
            destination_network_interface_arns=self.destination_network_interface_arns,
            excludes=self.excludes,
            includes=self.includes,
            name=self.name,
            options=self.options,
            schedule=self.schedule,
            source_network_interface_arns=self.source_network_interface_arns,
            status=self.status,
            tags=self.tags,
            task_arn=self.task_arn,
            task_report_config=self.task_report_config)


def get_task(task_arn: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskResult:
    """
    Resource schema for AWS::DataSync::Task.


    :param str task_arn: The ARN of the task.
    """
    __args__ = dict()
    __args__['taskArn'] = task_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getTask', __args__, opts=opts, typ=GetTaskResult).value

    return AwaitableGetTaskResult(
        cloud_watch_log_group_arn=pulumi.get(__ret__, 'cloud_watch_log_group_arn'),
        destination_network_interface_arns=pulumi.get(__ret__, 'destination_network_interface_arns'),
        excludes=pulumi.get(__ret__, 'excludes'),
        includes=pulumi.get(__ret__, 'includes'),
        name=pulumi.get(__ret__, 'name'),
        options=pulumi.get(__ret__, 'options'),
        schedule=pulumi.get(__ret__, 'schedule'),
        source_network_interface_arns=pulumi.get(__ret__, 'source_network_interface_arns'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        task_arn=pulumi.get(__ret__, 'task_arn'),
        task_report_config=pulumi.get(__ret__, 'task_report_config'))


@_utilities.lift_output_func(get_task)
def get_task_output(task_arn: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTaskResult]:
    """
    Resource schema for AWS::DataSync::Task.


    :param str task_arn: The ARN of the task.
    """
    ...
