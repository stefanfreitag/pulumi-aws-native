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
    'GetMetricStreamResult',
    'AwaitableGetMetricStreamResult',
    'get_metric_stream',
    'get_metric_stream_output',
]

@pulumi.output_type
class GetMetricStreamResult:
    def __init__(__self__, arn=None, creation_date=None, exclude_filters=None, firehose_arn=None, include_filters=None, include_linked_accounts_metrics=None, last_update_date=None, output_format=None, role_arn=None, state=None, statistics_configurations=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if exclude_filters and not isinstance(exclude_filters, list):
            raise TypeError("Expected argument 'exclude_filters' to be a list")
        pulumi.set(__self__, "exclude_filters", exclude_filters)
        if firehose_arn and not isinstance(firehose_arn, str):
            raise TypeError("Expected argument 'firehose_arn' to be a str")
        pulumi.set(__self__, "firehose_arn", firehose_arn)
        if include_filters and not isinstance(include_filters, list):
            raise TypeError("Expected argument 'include_filters' to be a list")
        pulumi.set(__self__, "include_filters", include_filters)
        if include_linked_accounts_metrics and not isinstance(include_linked_accounts_metrics, bool):
            raise TypeError("Expected argument 'include_linked_accounts_metrics' to be a bool")
        pulumi.set(__self__, "include_linked_accounts_metrics", include_linked_accounts_metrics)
        if last_update_date and not isinstance(last_update_date, str):
            raise TypeError("Expected argument 'last_update_date' to be a str")
        pulumi.set(__self__, "last_update_date", last_update_date)
        if output_format and not isinstance(output_format, str):
            raise TypeError("Expected argument 'output_format' to be a str")
        pulumi.set(__self__, "output_format", output_format)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if statistics_configurations and not isinstance(statistics_configurations, list):
            raise TypeError("Expected argument 'statistics_configurations' to be a list")
        pulumi.set(__self__, "statistics_configurations", statistics_configurations)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name of the metric stream.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        The date of creation of the metric stream.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="excludeFilters")
    def exclude_filters(self) -> Optional[Sequence['outputs.MetricStreamFilter']]:
        """
        Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "exclude_filters")

    @property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> Optional[str]:
        """
        The ARN of the Kinesis Firehose where to stream the data.
        """
        return pulumi.get(self, "firehose_arn")

    @property
    @pulumi.getter(name="includeFilters")
    def include_filters(self) -> Optional[Sequence['outputs.MetricStreamFilter']]:
        """
        Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
        """
        return pulumi.get(self, "include_filters")

    @property
    @pulumi.getter(name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(self) -> Optional[bool]:
        """
        If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is false.
        """
        return pulumi.get(self, "include_linked_accounts_metrics")

    @property
    @pulumi.getter(name="lastUpdateDate")
    def last_update_date(self) -> Optional[str]:
        """
        The date of the last update of the metric stream.
        """
        return pulumi.get(self, "last_update_date")

    @property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[str]:
        """
        The output format of the data streamed to the Kinesis Firehose.
        """
        return pulumi.get(self, "output_format")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of the role that provides access to the Kinesis Firehose.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Displays the state of the Metric Stream.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="statisticsConfigurations")
    def statistics_configurations(self) -> Optional[Sequence['outputs.MetricStreamStatisticsConfiguration']]:
        """
        By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
        """
        return pulumi.get(self, "statistics_configurations")


class AwaitableGetMetricStreamResult(GetMetricStreamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetricStreamResult(
            arn=self.arn,
            creation_date=self.creation_date,
            exclude_filters=self.exclude_filters,
            firehose_arn=self.firehose_arn,
            include_filters=self.include_filters,
            include_linked_accounts_metrics=self.include_linked_accounts_metrics,
            last_update_date=self.last_update_date,
            output_format=self.output_format,
            role_arn=self.role_arn,
            state=self.state,
            statistics_configurations=self.statistics_configurations)


def get_metric_stream(name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetricStreamResult:
    """
    Resource Type definition for Metric Stream


    :param str name: Name of the metric stream.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudwatch:getMetricStream', __args__, opts=opts, typ=GetMetricStreamResult).value

    return AwaitableGetMetricStreamResult(
        arn=pulumi.get(__ret__, 'arn'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        exclude_filters=pulumi.get(__ret__, 'exclude_filters'),
        firehose_arn=pulumi.get(__ret__, 'firehose_arn'),
        include_filters=pulumi.get(__ret__, 'include_filters'),
        include_linked_accounts_metrics=pulumi.get(__ret__, 'include_linked_accounts_metrics'),
        last_update_date=pulumi.get(__ret__, 'last_update_date'),
        output_format=pulumi.get(__ret__, 'output_format'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        state=pulumi.get(__ret__, 'state'),
        statistics_configurations=pulumi.get(__ret__, 'statistics_configurations'))


@_utilities.lift_output_func(get_metric_stream)
def get_metric_stream_output(name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetricStreamResult]:
    """
    Resource Type definition for Metric Stream


    :param str name: Name of the metric stream.
    """
    ...
