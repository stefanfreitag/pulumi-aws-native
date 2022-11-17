# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AlarmDimensionArgs',
    'AlarmMetricDataQueryArgs',
    'AlarmMetricStatArgs',
    'AlarmMetricArgs',
    'AnomalyDetectorConfigurationArgs',
    'AnomalyDetectorDimensionArgs',
    'AnomalyDetectorMetricDataQueryArgs',
    'AnomalyDetectorMetricMathAnomalyDetectorArgs',
    'AnomalyDetectorMetricStatArgs',
    'AnomalyDetectorMetricArgs',
    'AnomalyDetectorRangeArgs',
    'AnomalyDetectorSingleMetricAnomalyDetectorArgs',
    'InsightRuleTagsArgs',
    'MetricStreamFilterArgs',
    'MetricStreamStatisticsConfigurationArgs',
    'MetricStreamStatisticsMetricArgs',
    'MetricStreamTagArgs',
]

@pulumi.input_type
class AlarmDimensionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        Dimensions are arbitrary name/value pairs that can be associated with a CloudWatch metric.
        :param pulumi.Input[str] name: The name of the dimension.
        :param pulumi.Input[str] value: The value for the dimension.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the dimension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the dimension.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class AlarmMetricDataQueryArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 metric_stat: Optional[pulumi.Input['AlarmMetricStatArgs']] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 return_data: Optional[pulumi.Input[bool]] = None):
        """
        This property type specifies the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data.
        :param pulumi.Input[str] id: A short name used to tie this object to the results in the response.
        :param pulumi.Input[str] account_id: The ID of the account where the metrics are located, if this is a cross-account alarm.
        :param pulumi.Input[str] expression: The math expression to be performed on the returned data.
        :param pulumi.Input[str] label: A human-readable label for this metric or expression.
        :param pulumi.Input['AlarmMetricStatArgs'] metric_stat: The metric to be returned, along with statistics, period, and units.
        :param pulumi.Input[int] period: The period in seconds, over which the statistic is applied.
        :param pulumi.Input[bool] return_data: This option indicates whether to return the timestamps and raw data values of this metric.
        """
        pulumi.set(__self__, "id", id)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if metric_stat is not None:
            pulumi.set(__self__, "metric_stat", metric_stat)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if return_data is not None:
            pulumi.set(__self__, "return_data", return_data)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        A short name used to tie this object to the results in the response.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the account where the metrics are located, if this is a cross-account alarm.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        """
        The math expression to be performed on the returned data.
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable label for this metric or expression.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[pulumi.Input['AlarmMetricStatArgs']]:
        """
        The metric to be returned, along with statistics, period, and units.
        """
        return pulumi.get(self, "metric_stat")

    @metric_stat.setter
    def metric_stat(self, value: Optional[pulumi.Input['AlarmMetricStatArgs']]):
        pulumi.set(self, "metric_stat", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        """
        The period in seconds, over which the statistic is applied.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[bool]]:
        """
        This option indicates whether to return the timestamps and raw data values of this metric.
        """
        return pulumi.get(self, "return_data")

    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "return_data", value)


@pulumi.input_type
class AlarmMetricStatArgs:
    def __init__(__self__, *,
                 metric: pulumi.Input['AlarmMetricArgs'],
                 period: pulumi.Input[int],
                 stat: pulumi.Input[str],
                 unit: Optional[pulumi.Input[str]] = None):
        """
        This structure defines the metric to be returned, along with the statistics, period, and units.
        :param pulumi.Input['AlarmMetricArgs'] metric: The metric to return, including the metric name, namespace, and dimensions.
        :param pulumi.Input[int] period: The granularity, in seconds, of the returned data points.
        :param pulumi.Input[str] stat: The statistic to return.
        :param pulumi.Input[str] unit: The unit to use for the returned data points.
        """
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "period", period)
        pulumi.set(__self__, "stat", stat)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Input['AlarmMetricArgs']:
        """
        The metric to return, including the metric name, namespace, and dimensions.
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: pulumi.Input['AlarmMetricArgs']):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter
    def period(self) -> pulumi.Input[int]:
        """
        The granularity, in seconds, of the returned data points.
        """
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: pulumi.Input[int]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter
    def stat(self) -> pulumi.Input[str]:
        """
        The statistic to return.
        """
        return pulumi.get(self, "stat")

    @stat.setter
    def stat(self, value: pulumi.Input[str]):
        pulumi.set(self, "stat", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        The unit to use for the returned data points.
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


@pulumi.input_type
class AlarmMetricArgs:
    def __init__(__self__, *,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        The Metric property type represents a specific metric.
        :param pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]] dimensions: The dimensions for the metric.
        :param pulumi.Input[str] metric_name: The name of the metric.
        :param pulumi.Input[str] namespace: The namespace of the metric.
        """
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if metric_name is not None:
            pulumi.set(__self__, "metric_name", metric_name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]]:
        """
        The dimensions for the metric.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AlarmDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace of the metric.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class AnomalyDetectorConfigurationArgs:
    def __init__(__self__, *,
                 excluded_time_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorRangeArgs']]]] = None,
                 metric_time_zone: Optional[pulumi.Input[str]] = None):
        if excluded_time_ranges is not None:
            pulumi.set(__self__, "excluded_time_ranges", excluded_time_ranges)
        if metric_time_zone is not None:
            pulumi.set(__self__, "metric_time_zone", metric_time_zone)

    @property
    @pulumi.getter(name="excludedTimeRanges")
    def excluded_time_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorRangeArgs']]]]:
        return pulumi.get(self, "excluded_time_ranges")

    @excluded_time_ranges.setter
    def excluded_time_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorRangeArgs']]]]):
        pulumi.set(self, "excluded_time_ranges", value)

    @property
    @pulumi.getter(name="metricTimeZone")
    def metric_time_zone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metric_time_zone")

    @metric_time_zone.setter
    def metric_time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_time_zone", value)


@pulumi.input_type
class AnomalyDetectorDimensionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class AnomalyDetectorMetricDataQueryArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 metric_stat: Optional[pulumi.Input['AnomalyDetectorMetricStatArgs']] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 return_data: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "id", id)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if metric_stat is not None:
            pulumi.set(__self__, "metric_stat", metric_stat)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if return_data is not None:
            pulumi.set(__self__, "return_data", return_data)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[pulumi.Input['AnomalyDetectorMetricStatArgs']]:
        return pulumi.get(self, "metric_stat")

    @metric_stat.setter
    def metric_stat(self, value: Optional[pulumi.Input['AnomalyDetectorMetricStatArgs']]):
        pulumi.set(self, "metric_stat", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "return_data")

    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "return_data", value)


@pulumi.input_type
class AnomalyDetectorMetricMathAnomalyDetectorArgs:
    def __init__(__self__, *,
                 metric_data_queries: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricDataQueryArgs']]]] = None):
        if metric_data_queries is not None:
            pulumi.set(__self__, "metric_data_queries", metric_data_queries)

    @property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricDataQueryArgs']]]]:
        return pulumi.get(self, "metric_data_queries")

    @metric_data_queries.setter
    def metric_data_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricDataQueryArgs']]]]):
        pulumi.set(self, "metric_data_queries", value)


@pulumi.input_type
class AnomalyDetectorMetricStatArgs:
    def __init__(__self__, *,
                 metric: pulumi.Input['AnomalyDetectorMetricArgs'],
                 period: pulumi.Input[int],
                 stat: pulumi.Input[str],
                 unit: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "period", period)
        pulumi.set(__self__, "stat", stat)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Input['AnomalyDetectorMetricArgs']:
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: pulumi.Input['AnomalyDetectorMetricArgs']):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter
    def period(self) -> pulumi.Input[int]:
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: pulumi.Input[int]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter
    def stat(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stat")

    @stat.setter
    def stat(self, value: pulumi.Input[str]):
        pulumi.set(self, "stat", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


@pulumi.input_type
class AnomalyDetectorMetricArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]] = None):
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]:
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)


@pulumi.input_type
class AnomalyDetectorRangeArgs:
    def __init__(__self__, *,
                 end_time: pulumi.Input[str],
                 start_time: pulumi.Input[str]):
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[str]:
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[str]:
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_time", value)


@pulumi.input_type
class AnomalyDetectorSingleMetricAnomalyDetectorArgs:
    def __init__(__self__, *,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 stat: Optional[pulumi.Input[str]] = None):
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if metric_name is not None:
            pulumi.set(__self__, "metric_name", metric_name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if stat is not None:
            pulumi.set(__self__, "stat", stat)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]:
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def stat(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stat")

    @stat.setter
    def stat(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stat", value)


@pulumi.input_type
class InsightRuleTagsArgs:
    def __init__(__self__):
        pass


@pulumi.input_type
class MetricStreamFilterArgs:
    def __init__(__self__, *,
                 namespace: pulumi.Input[str]):
        """
        This structure defines the metrics that will be streamed.
        :param pulumi.Input[str] namespace: Only metrics with Namespace matching this value will be streamed.
        """
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        Only metrics with Namespace matching this value will be streamed.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class MetricStreamStatisticsConfigurationArgs:
    def __init__(__self__, *,
                 additional_statistics: pulumi.Input[Sequence[pulumi.Input[str]]],
                 include_metrics: pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsMetricArgs']]]):
        """
        This structure specifies a list of additional statistics to stream, and the metrics to stream those additional statistics for. All metrics that match the combination of metric name and namespace will be streamed with the extended statistics, no matter their dimensions.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_statistics: The additional statistics to stream for the metrics listed in IncludeMetrics.
        :param pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsMetricArgs']]] include_metrics: An array that defines the metrics that are to have additional statistics streamed.
        """
        pulumi.set(__self__, "additional_statistics", additional_statistics)
        pulumi.set(__self__, "include_metrics", include_metrics)

    @property
    @pulumi.getter(name="additionalStatistics")
    def additional_statistics(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The additional statistics to stream for the metrics listed in IncludeMetrics.
        """
        return pulumi.get(self, "additional_statistics")

    @additional_statistics.setter
    def additional_statistics(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "additional_statistics", value)

    @property
    @pulumi.getter(name="includeMetrics")
    def include_metrics(self) -> pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsMetricArgs']]]:
        """
        An array that defines the metrics that are to have additional statistics streamed.
        """
        return pulumi.get(self, "include_metrics")

    @include_metrics.setter
    def include_metrics(self, value: pulumi.Input[Sequence[pulumi.Input['MetricStreamStatisticsMetricArgs']]]):
        pulumi.set(self, "include_metrics", value)


@pulumi.input_type
class MetricStreamStatisticsMetricArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 namespace: pulumi.Input[str]):
        """
        A structure that specifies the metric name and namespace for one metric that is going to have additional statistics included in the stream.
        :param pulumi.Input[str] metric_name: The name of the metric.
        :param pulumi.Input[str] namespace: The namespace of the metric.
        """
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        """
        The name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The namespace of the metric.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class MetricStreamTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: Optional[pulumi.Input[str]] = None):
        """
        Metadata that you can assign to a Metric Stream, consisting of a key-value pair.
        :param pulumi.Input[str] key: A unique identifier for the tag.
        :param pulumi.Input[str] value: An optional string, which you can use to describe or define the tag.
        """
        pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        A unique identifier for the tag.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        An optional string, which you can use to describe or define the tag.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


