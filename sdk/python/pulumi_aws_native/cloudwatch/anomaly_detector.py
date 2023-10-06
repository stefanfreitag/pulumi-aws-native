# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AnomalyDetectorArgs', 'AnomalyDetector']

@pulumi.input_type
class AnomalyDetectorArgs:
    def __init__(__self__, *,
                 configuration: Optional[pulumi.Input['AnomalyDetectorConfigurationArgs']] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]] = None,
                 metric_math_anomaly_detector: Optional[pulumi.Input['AnomalyDetectorMetricMathAnomalyDetectorArgs']] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 single_metric_anomaly_detector: Optional[pulumi.Input['AnomalyDetectorSingleMetricAnomalyDetectorArgs']] = None,
                 stat: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AnomalyDetector resource.
        """
        AnomalyDetectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configuration=configuration,
            dimensions=dimensions,
            metric_math_anomaly_detector=metric_math_anomaly_detector,
            metric_name=metric_name,
            namespace=namespace,
            single_metric_anomaly_detector=single_metric_anomaly_detector,
            stat=stat,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configuration: Optional[pulumi.Input['AnomalyDetectorConfigurationArgs']] = None,
             dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]] = None,
             metric_math_anomaly_detector: Optional[pulumi.Input['AnomalyDetectorMetricMathAnomalyDetectorArgs']] = None,
             metric_name: Optional[pulumi.Input[str]] = None,
             namespace: Optional[pulumi.Input[str]] = None,
             single_metric_anomaly_detector: Optional[pulumi.Input['AnomalyDetectorSingleMetricAnomalyDetectorArgs']] = None,
             stat: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if configuration is not None:
            _setter("configuration", configuration)
        if dimensions is not None:
            _setter("dimensions", dimensions)
        if metric_math_anomaly_detector is not None:
            _setter("metric_math_anomaly_detector", metric_math_anomaly_detector)
        if metric_name is not None:
            _setter("metric_name", metric_name)
        if namespace is not None:
            _setter("namespace", namespace)
        if single_metric_anomaly_detector is not None:
            _setter("single_metric_anomaly_detector", single_metric_anomaly_detector)
        if stat is not None:
            _setter("stat", stat)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['AnomalyDetectorConfigurationArgs']]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['AnomalyDetectorConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]:
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="metricMathAnomalyDetector")
    def metric_math_anomaly_detector(self) -> Optional[pulumi.Input['AnomalyDetectorMetricMathAnomalyDetectorArgs']]:
        return pulumi.get(self, "metric_math_anomaly_detector")

    @metric_math_anomaly_detector.setter
    def metric_math_anomaly_detector(self, value: Optional[pulumi.Input['AnomalyDetectorMetricMathAnomalyDetectorArgs']]):
        pulumi.set(self, "metric_math_anomaly_detector", value)

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
    @pulumi.getter(name="singleMetricAnomalyDetector")
    def single_metric_anomaly_detector(self) -> Optional[pulumi.Input['AnomalyDetectorSingleMetricAnomalyDetectorArgs']]:
        return pulumi.get(self, "single_metric_anomaly_detector")

    @single_metric_anomaly_detector.setter
    def single_metric_anomaly_detector(self, value: Optional[pulumi.Input['AnomalyDetectorSingleMetricAnomalyDetectorArgs']]):
        pulumi.set(self, "single_metric_anomaly_detector", value)

    @property
    @pulumi.getter
    def stat(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stat")

    @stat.setter
    def stat(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stat", value)


warnings.warn("""AnomalyDetector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class AnomalyDetector(pulumi.CustomResource):
    warnings.warn("""AnomalyDetector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorConfigurationArgs']]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnomalyDetectorDimensionArgs']]]]] = None,
                 metric_math_anomaly_detector: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorMetricMathAnomalyDetectorArgs']]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 single_metric_anomaly_detector: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorSingleMetricAnomalyDetectorArgs']]] = None,
                 stat: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudWatch::AnomalyDetector

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AnomalyDetectorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudWatch::AnomalyDetector

        :param str resource_name: The name of the resource.
        :param AnomalyDetectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnomalyDetectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AnomalyDetectorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorConfigurationArgs']]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnomalyDetectorDimensionArgs']]]]] = None,
                 metric_math_anomaly_detector: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorMetricMathAnomalyDetectorArgs']]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 single_metric_anomaly_detector: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorSingleMetricAnomalyDetectorArgs']]] = None,
                 stat: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""AnomalyDetector is deprecated: AnomalyDetector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomalyDetectorArgs.__new__(AnomalyDetectorArgs)

            if configuration is not None and not isinstance(configuration, AnomalyDetectorConfigurationArgs):
                configuration = configuration or {}
                def _setter(key, value):
                    configuration[key] = value
                AnomalyDetectorConfigurationArgs._configure(_setter, **configuration)
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["dimensions"] = dimensions
            if metric_math_anomaly_detector is not None and not isinstance(metric_math_anomaly_detector, AnomalyDetectorMetricMathAnomalyDetectorArgs):
                metric_math_anomaly_detector = metric_math_anomaly_detector or {}
                def _setter(key, value):
                    metric_math_anomaly_detector[key] = value
                AnomalyDetectorMetricMathAnomalyDetectorArgs._configure(_setter, **metric_math_anomaly_detector)
            __props__.__dict__["metric_math_anomaly_detector"] = metric_math_anomaly_detector
            __props__.__dict__["metric_name"] = metric_name
            __props__.__dict__["namespace"] = namespace
            if single_metric_anomaly_detector is not None and not isinstance(single_metric_anomaly_detector, AnomalyDetectorSingleMetricAnomalyDetectorArgs):
                single_metric_anomaly_detector = single_metric_anomaly_detector or {}
                def _setter(key, value):
                    single_metric_anomaly_detector[key] = value
                AnomalyDetectorSingleMetricAnomalyDetectorArgs._configure(_setter, **single_metric_anomaly_detector)
            __props__.__dict__["single_metric_anomaly_detector"] = single_metric_anomaly_detector
            __props__.__dict__["stat"] = stat
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dimensions[*]", "metric_math_anomaly_detector", "metric_name", "namespace", "single_metric_anomaly_detector", "stat"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AnomalyDetector, __self__).__init__(
            'aws-native:cloudwatch:AnomalyDetector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AnomalyDetector':
        """
        Get an existing AnomalyDetector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AnomalyDetectorArgs.__new__(AnomalyDetectorArgs)

        __props__.__dict__["configuration"] = None
        __props__.__dict__["dimensions"] = None
        __props__.__dict__["metric_math_anomaly_detector"] = None
        __props__.__dict__["metric_name"] = None
        __props__.__dict__["namespace"] = None
        __props__.__dict__["single_metric_anomaly_detector"] = None
        __props__.__dict__["stat"] = None
        return AnomalyDetector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.AnomalyDetectorConfiguration']]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional[Sequence['outputs.AnomalyDetectorDimension']]]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="metricMathAnomalyDetector")
    def metric_math_anomaly_detector(self) -> pulumi.Output[Optional['outputs.AnomalyDetectorMetricMathAnomalyDetector']]:
        return pulumi.get(self, "metric_math_anomaly_detector")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="singleMetricAnomalyDetector")
    def single_metric_anomaly_detector(self) -> pulumi.Output[Optional['outputs.AnomalyDetectorSingleMetricAnomalyDetector']]:
        return pulumi.get(self, "single_metric_anomaly_detector")

    @property
    @pulumi.getter
    def stat(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "stat")

