# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['AnomalyDetectorArgs', 'AnomalyDetector']

@pulumi.input_type
class AnomalyDetectorArgs:
    def __init__(__self__, *,
                 anomaly_detector_config: pulumi.Input['AnomalyDetectorAnomalyDetectorConfigArgs'],
                 metric_set_list: pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricSetArgs']]],
                 anomaly_detector_description: Optional[pulumi.Input[str]] = None,
                 anomaly_detector_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AnomalyDetector resource.
        :param pulumi.Input['AnomalyDetectorAnomalyDetectorConfigArgs'] anomaly_detector_config: Configuration options for the AnomalyDetector
        :param pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricSetArgs']]] metric_set_list: List of metric sets for anomaly detection
        :param pulumi.Input[str] anomaly_detector_description: A description for the AnomalyDetector.
        :param pulumi.Input[str] anomaly_detector_name: Name for the Amazon Lookout for Metrics Anomaly Detector
        :param pulumi.Input[str] kms_key_arn: KMS key used to encrypt the AnomalyDetector data
        """
        pulumi.set(__self__, "anomaly_detector_config", anomaly_detector_config)
        pulumi.set(__self__, "metric_set_list", metric_set_list)
        if anomaly_detector_description is not None:
            pulumi.set(__self__, "anomaly_detector_description", anomaly_detector_description)
        if anomaly_detector_name is not None:
            pulumi.set(__self__, "anomaly_detector_name", anomaly_detector_name)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="anomalyDetectorConfig")
    def anomaly_detector_config(self) -> pulumi.Input['AnomalyDetectorAnomalyDetectorConfigArgs']:
        """
        Configuration options for the AnomalyDetector
        """
        return pulumi.get(self, "anomaly_detector_config")

    @anomaly_detector_config.setter
    def anomaly_detector_config(self, value: pulumi.Input['AnomalyDetectorAnomalyDetectorConfigArgs']):
        pulumi.set(self, "anomaly_detector_config", value)

    @property
    @pulumi.getter(name="metricSetList")
    def metric_set_list(self) -> pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricSetArgs']]]:
        """
        List of metric sets for anomaly detection
        """
        return pulumi.get(self, "metric_set_list")

    @metric_set_list.setter
    def metric_set_list(self, value: pulumi.Input[Sequence[pulumi.Input['AnomalyDetectorMetricSetArgs']]]):
        pulumi.set(self, "metric_set_list", value)

    @property
    @pulumi.getter(name="anomalyDetectorDescription")
    def anomaly_detector_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the AnomalyDetector.
        """
        return pulumi.get(self, "anomaly_detector_description")

    @anomaly_detector_description.setter
    def anomaly_detector_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "anomaly_detector_description", value)

    @property
    @pulumi.getter(name="anomalyDetectorName")
    def anomaly_detector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the Amazon Lookout for Metrics Anomaly Detector
        """
        return pulumi.get(self, "anomaly_detector_name")

    @anomaly_detector_name.setter
    def anomaly_detector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "anomaly_detector_name", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key used to encrypt the AnomalyDetector data
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)


class AnomalyDetector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_detector_config: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorAnomalyDetectorConfigArgs']]] = None,
                 anomaly_detector_description: Optional[pulumi.Input[str]] = None,
                 anomaly_detector_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 metric_set_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnomalyDetectorMetricSetArgs']]]]] = None,
                 __props__=None):
        """
        An Amazon Lookout for Metrics Detector

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AnomalyDetectorAnomalyDetectorConfigArgs']] anomaly_detector_config: Configuration options for the AnomalyDetector
        :param pulumi.Input[str] anomaly_detector_description: A description for the AnomalyDetector.
        :param pulumi.Input[str] anomaly_detector_name: Name for the Amazon Lookout for Metrics Anomaly Detector
        :param pulumi.Input[str] kms_key_arn: KMS key used to encrypt the AnomalyDetector data
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnomalyDetectorMetricSetArgs']]]] metric_set_list: List of metric sets for anomaly detection
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnomalyDetectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Amazon Lookout for Metrics Detector

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
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_detector_config: Optional[pulumi.Input[pulumi.InputType['AnomalyDetectorAnomalyDetectorConfigArgs']]] = None,
                 anomaly_detector_description: Optional[pulumi.Input[str]] = None,
                 anomaly_detector_name: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 metric_set_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnomalyDetectorMetricSetArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomalyDetectorArgs.__new__(AnomalyDetectorArgs)

            if anomaly_detector_config is None and not opts.urn:
                raise TypeError("Missing required property 'anomaly_detector_config'")
            __props__.__dict__["anomaly_detector_config"] = anomaly_detector_config
            __props__.__dict__["anomaly_detector_description"] = anomaly_detector_description
            __props__.__dict__["anomaly_detector_name"] = anomaly_detector_name
            __props__.__dict__["kms_key_arn"] = kms_key_arn
            if metric_set_list is None and not opts.urn:
                raise TypeError("Missing required property 'metric_set_list'")
            __props__.__dict__["metric_set_list"] = metric_set_list
            __props__.__dict__["arn"] = None
        super(AnomalyDetector, __self__).__init__(
            'aws-native:lookoutmetrics:AnomalyDetector',
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

        __props__.__dict__["anomaly_detector_config"] = None
        __props__.__dict__["anomaly_detector_description"] = None
        __props__.__dict__["anomaly_detector_name"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["kms_key_arn"] = None
        __props__.__dict__["metric_set_list"] = None
        return AnomalyDetector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="anomalyDetectorConfig")
    def anomaly_detector_config(self) -> pulumi.Output['outputs.AnomalyDetectorAnomalyDetectorConfig']:
        """
        Configuration options for the AnomalyDetector
        """
        return pulumi.get(self, "anomaly_detector_config")

    @property
    @pulumi.getter(name="anomalyDetectorDescription")
    def anomaly_detector_description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the AnomalyDetector.
        """
        return pulumi.get(self, "anomaly_detector_description")

    @property
    @pulumi.getter(name="anomalyDetectorName")
    def anomaly_detector_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name for the Amazon Lookout for Metrics Anomaly Detector
        """
        return pulumi.get(self, "anomaly_detector_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        KMS key used to encrypt the AnomalyDetector data
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="metricSetList")
    def metric_set_list(self) -> pulumi.Output[Sequence['outputs.AnomalyDetectorMetricSet']]:
        """
        List of metric sets for anomaly detection
        """
        return pulumi.get(self, "metric_set_list")

