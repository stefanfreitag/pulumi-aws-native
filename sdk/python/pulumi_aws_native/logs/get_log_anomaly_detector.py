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
    'GetLogAnomalyDetectorResult',
    'AwaitableGetLogAnomalyDetectorResult',
    'get_log_anomaly_detector',
    'get_log_anomaly_detector_output',
]

@pulumi.output_type
class GetLogAnomalyDetectorResult:
    def __init__(__self__, anomaly_detector_arn=None, anomaly_detector_status=None, anomaly_visibility_time=None, creation_time_stamp=None, detector_name=None, evaluation_frequency=None, filter_pattern=None, kms_key_id=None, last_modified_time_stamp=None, log_group_arn_list=None):
        if anomaly_detector_arn and not isinstance(anomaly_detector_arn, str):
            raise TypeError("Expected argument 'anomaly_detector_arn' to be a str")
        pulumi.set(__self__, "anomaly_detector_arn", anomaly_detector_arn)
        if anomaly_detector_status and not isinstance(anomaly_detector_status, str):
            raise TypeError("Expected argument 'anomaly_detector_status' to be a str")
        pulumi.set(__self__, "anomaly_detector_status", anomaly_detector_status)
        if anomaly_visibility_time and not isinstance(anomaly_visibility_time, float):
            raise TypeError("Expected argument 'anomaly_visibility_time' to be a float")
        pulumi.set(__self__, "anomaly_visibility_time", anomaly_visibility_time)
        if creation_time_stamp and not isinstance(creation_time_stamp, float):
            raise TypeError("Expected argument 'creation_time_stamp' to be a float")
        pulumi.set(__self__, "creation_time_stamp", creation_time_stamp)
        if detector_name and not isinstance(detector_name, str):
            raise TypeError("Expected argument 'detector_name' to be a str")
        pulumi.set(__self__, "detector_name", detector_name)
        if evaluation_frequency and not isinstance(evaluation_frequency, str):
            raise TypeError("Expected argument 'evaluation_frequency' to be a str")
        pulumi.set(__self__, "evaluation_frequency", evaluation_frequency)
        if filter_pattern and not isinstance(filter_pattern, str):
            raise TypeError("Expected argument 'filter_pattern' to be a str")
        pulumi.set(__self__, "filter_pattern", filter_pattern)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if last_modified_time_stamp and not isinstance(last_modified_time_stamp, float):
            raise TypeError("Expected argument 'last_modified_time_stamp' to be a float")
        pulumi.set(__self__, "last_modified_time_stamp", last_modified_time_stamp)
        if log_group_arn_list and not isinstance(log_group_arn_list, list):
            raise TypeError("Expected argument 'log_group_arn_list' to be a list")
        pulumi.set(__self__, "log_group_arn_list", log_group_arn_list)

    @property
    @pulumi.getter(name="anomalyDetectorArn")
    def anomaly_detector_arn(self) -> Optional[str]:
        """
        ARN of LogAnomalyDetector
        """
        return pulumi.get(self, "anomaly_detector_arn")

    @property
    @pulumi.getter(name="anomalyDetectorStatus")
    def anomaly_detector_status(self) -> Optional[str]:
        """
        Current status of detector.
        """
        return pulumi.get(self, "anomaly_detector_status")

    @property
    @pulumi.getter(name="anomalyVisibilityTime")
    def anomaly_visibility_time(self) -> Optional[float]:
        return pulumi.get(self, "anomaly_visibility_time")

    @property
    @pulumi.getter(name="creationTimeStamp")
    def creation_time_stamp(self) -> Optional[float]:
        """
        When detector was created.
        """
        return pulumi.get(self, "creation_time_stamp")

    @property
    @pulumi.getter(name="detectorName")
    def detector_name(self) -> Optional[str]:
        """
        Name of detector
        """
        return pulumi.get(self, "detector_name")

    @property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional['LogAnomalyDetectorEvaluationFrequency']:
        """
        How often log group is evaluated
        """
        return pulumi.get(self, "evaluation_frequency")

    @property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> Optional[str]:
        return pulumi.get(self, "filter_pattern")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="lastModifiedTimeStamp")
    def last_modified_time_stamp(self) -> Optional[float]:
        """
        When detector was lsat modified.
        """
        return pulumi.get(self, "last_modified_time_stamp")

    @property
    @pulumi.getter(name="logGroupArnList")
    def log_group_arn_list(self) -> Optional[Sequence[str]]:
        """
        List of Arns for the given log group
        """
        return pulumi.get(self, "log_group_arn_list")


class AwaitableGetLogAnomalyDetectorResult(GetLogAnomalyDetectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogAnomalyDetectorResult(
            anomaly_detector_arn=self.anomaly_detector_arn,
            anomaly_detector_status=self.anomaly_detector_status,
            anomaly_visibility_time=self.anomaly_visibility_time,
            creation_time_stamp=self.creation_time_stamp,
            detector_name=self.detector_name,
            evaluation_frequency=self.evaluation_frequency,
            filter_pattern=self.filter_pattern,
            kms_key_id=self.kms_key_id,
            last_modified_time_stamp=self.last_modified_time_stamp,
            log_group_arn_list=self.log_group_arn_list)


def get_log_anomaly_detector(anomaly_detector_arn: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogAnomalyDetectorResult:
    """
    The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.


    :param str anomaly_detector_arn: ARN of LogAnomalyDetector
    """
    __args__ = dict()
    __args__['anomalyDetectorArn'] = anomaly_detector_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getLogAnomalyDetector', __args__, opts=opts, typ=GetLogAnomalyDetectorResult).value

    return AwaitableGetLogAnomalyDetectorResult(
        anomaly_detector_arn=pulumi.get(__ret__, 'anomaly_detector_arn'),
        anomaly_detector_status=pulumi.get(__ret__, 'anomaly_detector_status'),
        anomaly_visibility_time=pulumi.get(__ret__, 'anomaly_visibility_time'),
        creation_time_stamp=pulumi.get(__ret__, 'creation_time_stamp'),
        detector_name=pulumi.get(__ret__, 'detector_name'),
        evaluation_frequency=pulumi.get(__ret__, 'evaluation_frequency'),
        filter_pattern=pulumi.get(__ret__, 'filter_pattern'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        last_modified_time_stamp=pulumi.get(__ret__, 'last_modified_time_stamp'),
        log_group_arn_list=pulumi.get(__ret__, 'log_group_arn_list'))


@_utilities.lift_output_func(get_log_anomaly_detector)
def get_log_anomaly_detector_output(anomaly_detector_arn: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogAnomalyDetectorResult]:
    """
    The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.


    :param str anomaly_detector_arn: ARN of LogAnomalyDetector
    """
    ...
