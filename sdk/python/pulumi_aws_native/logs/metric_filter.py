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
from ._inputs import *

__all__ = ['MetricFilterArgs', 'MetricFilter']

@pulumi.input_type
class MetricFilterArgs:
    def __init__(__self__, *,
                 filter_pattern: pulumi.Input[str],
                 log_group_name: pulumi.Input[str],
                 metric_transformations: pulumi.Input[Sequence[pulumi.Input['MetricFilterMetricTransformationArgs']]],
                 filter_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MetricFilter resource.
        :param pulumi.Input[str] filter_pattern: Pattern that Logs follows to interpret each entry in a log.
        :param pulumi.Input[str] log_group_name: Existing log group that you want to associate with this filter.
        :param pulumi.Input[Sequence[pulumi.Input['MetricFilterMetricTransformationArgs']]] metric_transformations: A collection of information that defines how metric data gets emitted.
        :param pulumi.Input[str] filter_name: A name for the metric filter.
        """
        pulumi.set(__self__, "filter_pattern", filter_pattern)
        pulumi.set(__self__, "log_group_name", log_group_name)
        pulumi.set(__self__, "metric_transformations", metric_transformations)
        if filter_name is not None:
            pulumi.set(__self__, "filter_name", filter_name)

    @property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> pulumi.Input[str]:
        """
        Pattern that Logs follows to interpret each entry in a log.
        """
        return pulumi.get(self, "filter_pattern")

    @filter_pattern.setter
    def filter_pattern(self, value: pulumi.Input[str]):
        pulumi.set(self, "filter_pattern", value)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[str]:
        """
        Existing log group that you want to associate with this filter.
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_group_name", value)

    @property
    @pulumi.getter(name="metricTransformations")
    def metric_transformations(self) -> pulumi.Input[Sequence[pulumi.Input['MetricFilterMetricTransformationArgs']]]:
        """
        A collection of information that defines how metric data gets emitted.
        """
        return pulumi.get(self, "metric_transformations")

    @metric_transformations.setter
    def metric_transformations(self, value: pulumi.Input[Sequence[pulumi.Input['MetricFilterMetricTransformationArgs']]]):
        pulumi.set(self, "metric_transformations", value)

    @property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the metric filter.
        """
        return pulumi.get(self, "filter_name")

    @filter_name.setter
    def filter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_name", value)


class MetricFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filter_name: Optional[pulumi.Input[str]] = None,
                 filter_pattern: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 metric_transformations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricFilterMetricTransformationArgs']]]]] = None,
                 __props__=None):
        """
        Specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] filter_name: A name for the metric filter.
        :param pulumi.Input[str] filter_pattern: Pattern that Logs follows to interpret each entry in a log.
        :param pulumi.Input[str] log_group_name: Existing log group that you want to associate with this filter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricFilterMetricTransformationArgs']]]] metric_transformations: A collection of information that defines how metric data gets emitted.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricFilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics.

        :param str resource_name: The name of the resource.
        :param MetricFilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricFilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filter_name: Optional[pulumi.Input[str]] = None,
                 filter_pattern: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 metric_transformations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricFilterMetricTransformationArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricFilterArgs.__new__(MetricFilterArgs)

            __props__.__dict__["filter_name"] = filter_name
            if filter_pattern is None and not opts.urn:
                raise TypeError("Missing required property 'filter_pattern'")
            __props__.__dict__["filter_pattern"] = filter_pattern
            if log_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'log_group_name'")
            __props__.__dict__["log_group_name"] = log_group_name
            if metric_transformations is None and not opts.urn:
                raise TypeError("Missing required property 'metric_transformations'")
            __props__.__dict__["metric_transformations"] = metric_transformations
        super(MetricFilter, __self__).__init__(
            'aws-native:logs:MetricFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MetricFilter':
        """
        Get an existing MetricFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetricFilterArgs.__new__(MetricFilterArgs)

        __props__.__dict__["filter_name"] = None
        __props__.__dict__["filter_pattern"] = None
        __props__.__dict__["log_group_name"] = None
        __props__.__dict__["metric_transformations"] = None
        return MetricFilter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the metric filter.
        """
        return pulumi.get(self, "filter_name")

    @property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> pulumi.Output[str]:
        """
        Pattern that Logs follows to interpret each entry in a log.
        """
        return pulumi.get(self, "filter_pattern")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[str]:
        """
        Existing log group that you want to associate with this filter.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="metricTransformations")
    def metric_transformations(self) -> pulumi.Output[Sequence['outputs.MetricFilterMetricTransformation']]:
        """
        A collection of information that defines how metric data gets emitted.
        """
        return pulumi.get(self, "metric_transformations")

