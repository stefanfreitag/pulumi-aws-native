# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'DeliveryDestinationTagArgs',
    'DeliverySourceTagArgs',
    'DeliveryTagArgs',
    'LogGroupTagArgs',
    'MetricFilterDimensionArgs',
    'MetricFilterMetricTransformationArgs',
]

@pulumi.input_type
class DeliveryDestinationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DeliverySourceTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DeliveryTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class LogGroupTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., :, /, =, +, - and @.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., :, /, =, +, - and @.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., :, /, =, +, - and @.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., :, /, =, +, - and @.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class MetricFilterDimensionArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        the key-value pairs that further define a metric.
        :param pulumi.Input[str] key: The key of the dimension. Maximum length of 255.
        :param pulumi.Input[str] value: The value of the dimension. Maximum length of 255.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key of the dimension. Maximum length of 255.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the dimension. Maximum length of 255.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class MetricFilterMetricTransformationArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 metric_namespace: pulumi.Input[str],
                 metric_value: pulumi.Input[str],
                 default_value: Optional[pulumi.Input[float]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['MetricFilterDimensionArgs']]]] = None,
                 unit: Optional[pulumi.Input['MetricFilterMetricTransformationUnit']] = None):
        """
        :param pulumi.Input[str] metric_name: The name of the CloudWatch metric. Metric name must be in ASCII format.
        :param pulumi.Input[str] metric_namespace: The namespace of the CloudWatch metric.
        :param pulumi.Input[str] metric_value: The value to publish to the CloudWatch metric when a filter pattern matches a log event.
        :param pulumi.Input[float] default_value: The value to emit when a filter pattern does not match a log event. This value can be null.
        :param pulumi.Input[Sequence[pulumi.Input['MetricFilterDimensionArgs']]] dimensions: Dimensions are the key-value pairs that further define a metric
        :param pulumi.Input['MetricFilterMetricTransformationUnit'] unit: The unit to assign to the metric. If you omit this, the unit is set as None.
        """
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "metric_namespace", metric_namespace)
        pulumi.set(__self__, "metric_value", metric_value)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        """
        The name of the CloudWatch metric. Metric name must be in ASCII format.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> pulumi.Input[str]:
        """
        The namespace of the CloudWatch metric.
        """
        return pulumi.get(self, "metric_namespace")

    @metric_namespace.setter
    def metric_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_namespace", value)

    @property
    @pulumi.getter(name="metricValue")
    def metric_value(self) -> pulumi.Input[str]:
        """
        The value to publish to the CloudWatch metric when a filter pattern matches a log event.
        """
        return pulumi.get(self, "metric_value")

    @metric_value.setter
    def metric_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_value", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[float]]:
        """
        The value to emit when a filter pattern does not match a log event. This value can be null.
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricFilterDimensionArgs']]]]:
        """
        Dimensions are the key-value pairs that further define a metric
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricFilterDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input['MetricFilterMetricTransformationUnit']]:
        """
        The unit to assign to the metric. If you omit this, the unit is set as None.
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input['MetricFilterMetricTransformationUnit']]):
        pulumi.set(self, "unit", value)


