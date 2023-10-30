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
    'GetMonitoringScheduleResult',
    'AwaitableGetMonitoringScheduleResult',
    'get_monitoring_schedule',
    'get_monitoring_schedule_output',
]

@pulumi.output_type
class GetMonitoringScheduleResult:
    def __init__(__self__, creation_time=None, endpoint_name=None, failure_reason=None, last_modified_time=None, last_monitoring_execution_summary=None, monitoring_schedule_arn=None, monitoring_schedule_config=None, monitoring_schedule_status=None, tags=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if endpoint_name and not isinstance(endpoint_name, str):
            raise TypeError("Expected argument 'endpoint_name' to be a str")
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        if failure_reason and not isinstance(failure_reason, str):
            raise TypeError("Expected argument 'failure_reason' to be a str")
        pulumi.set(__self__, "failure_reason", failure_reason)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if last_monitoring_execution_summary and not isinstance(last_monitoring_execution_summary, dict):
            raise TypeError("Expected argument 'last_monitoring_execution_summary' to be a dict")
        pulumi.set(__self__, "last_monitoring_execution_summary", last_monitoring_execution_summary)
        if monitoring_schedule_arn and not isinstance(monitoring_schedule_arn, str):
            raise TypeError("Expected argument 'monitoring_schedule_arn' to be a str")
        pulumi.set(__self__, "monitoring_schedule_arn", monitoring_schedule_arn)
        if monitoring_schedule_config and not isinstance(monitoring_schedule_config, dict):
            raise TypeError("Expected argument 'monitoring_schedule_config' to be a dict")
        pulumi.set(__self__, "monitoring_schedule_config", monitoring_schedule_config)
        if monitoring_schedule_status and not isinstance(monitoring_schedule_status, str):
            raise TypeError("Expected argument 'monitoring_schedule_status' to be a str")
        pulumi.set(__self__, "monitoring_schedule_status", monitoring_schedule_status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The time at which the schedule was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_name")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[str]:
        """
        Contains the reason a monitoring job failed, if it failed.
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        A timestamp that indicates the last time the monitoring job was modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="lastMonitoringExecutionSummary")
    def last_monitoring_execution_summary(self) -> Optional['outputs.MonitoringScheduleMonitoringExecutionSummary']:
        """
        Describes metadata on the last execution to run, if there was one.
        """
        return pulumi.get(self, "last_monitoring_execution_summary")

    @property
    @pulumi.getter(name="monitoringScheduleArn")
    def monitoring_schedule_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the monitoring schedule.
        """
        return pulumi.get(self, "monitoring_schedule_arn")

    @property
    @pulumi.getter(name="monitoringScheduleConfig")
    def monitoring_schedule_config(self) -> Optional['outputs.MonitoringScheduleConfig']:
        return pulumi.get(self, "monitoring_schedule_config")

    @property
    @pulumi.getter(name="monitoringScheduleStatus")
    def monitoring_schedule_status(self) -> Optional['MonitoringScheduleStatus']:
        """
        The status of a schedule job.
        """
        return pulumi.get(self, "monitoring_schedule_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.MonitoringScheduleTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetMonitoringScheduleResult(GetMonitoringScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMonitoringScheduleResult(
            creation_time=self.creation_time,
            endpoint_name=self.endpoint_name,
            failure_reason=self.failure_reason,
            last_modified_time=self.last_modified_time,
            last_monitoring_execution_summary=self.last_monitoring_execution_summary,
            monitoring_schedule_arn=self.monitoring_schedule_arn,
            monitoring_schedule_config=self.monitoring_schedule_config,
            monitoring_schedule_status=self.monitoring_schedule_status,
            tags=self.tags)


def get_monitoring_schedule(monitoring_schedule_arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMonitoringScheduleResult:
    """
    Resource Type definition for AWS::SageMaker::MonitoringSchedule


    :param str monitoring_schedule_arn: The Amazon Resource Name (ARN) of the monitoring schedule.
    """
    __args__ = dict()
    __args__['monitoringScheduleArn'] = monitoring_schedule_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getMonitoringSchedule', __args__, opts=opts, typ=GetMonitoringScheduleResult).value

    return AwaitableGetMonitoringScheduleResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        endpoint_name=pulumi.get(__ret__, 'endpoint_name'),
        failure_reason=pulumi.get(__ret__, 'failure_reason'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        last_monitoring_execution_summary=pulumi.get(__ret__, 'last_monitoring_execution_summary'),
        monitoring_schedule_arn=pulumi.get(__ret__, 'monitoring_schedule_arn'),
        monitoring_schedule_config=pulumi.get(__ret__, 'monitoring_schedule_config'),
        monitoring_schedule_status=pulumi.get(__ret__, 'monitoring_schedule_status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_monitoring_schedule)
def get_monitoring_schedule_output(monitoring_schedule_arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMonitoringScheduleResult]:
    """
    Resource Type definition for AWS::SageMaker::MonitoringSchedule


    :param str monitoring_schedule_arn: The Amazon Resource Name (ARN) of the monitoring schedule.
    """
    ...
