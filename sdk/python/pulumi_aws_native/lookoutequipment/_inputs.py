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
    'DataInputConfigurationPropertiesArgs',
    'DataOutputConfigurationPropertiesArgs',
    'InferenceSchedulerInputNameConfigurationArgs',
    'InferenceSchedulerS3InputConfigurationArgs',
    'InferenceSchedulerS3OutputConfigurationArgs',
]

@pulumi.input_type
class DataInputConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 s3_input_configuration: pulumi.Input['InferenceSchedulerS3InputConfigurationArgs'],
                 inference_input_name_configuration: Optional[pulumi.Input['InferenceSchedulerInputNameConfigurationArgs']] = None,
                 input_time_zone_offset: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.
        :param pulumi.Input[str] input_time_zone_offset: Indicates the difference between your time zone and Greenwich Mean Time (GMT).
        """
        pulumi.set(__self__, "s3_input_configuration", s3_input_configuration)
        if inference_input_name_configuration is not None:
            pulumi.set(__self__, "inference_input_name_configuration", inference_input_name_configuration)
        if input_time_zone_offset is not None:
            pulumi.set(__self__, "input_time_zone_offset", input_time_zone_offset)

    @property
    @pulumi.getter(name="s3InputConfiguration")
    def s3_input_configuration(self) -> pulumi.Input['InferenceSchedulerS3InputConfigurationArgs']:
        return pulumi.get(self, "s3_input_configuration")

    @s3_input_configuration.setter
    def s3_input_configuration(self, value: pulumi.Input['InferenceSchedulerS3InputConfigurationArgs']):
        pulumi.set(self, "s3_input_configuration", value)

    @property
    @pulumi.getter(name="inferenceInputNameConfiguration")
    def inference_input_name_configuration(self) -> Optional[pulumi.Input['InferenceSchedulerInputNameConfigurationArgs']]:
        return pulumi.get(self, "inference_input_name_configuration")

    @inference_input_name_configuration.setter
    def inference_input_name_configuration(self, value: Optional[pulumi.Input['InferenceSchedulerInputNameConfigurationArgs']]):
        pulumi.set(self, "inference_input_name_configuration", value)

    @property
    @pulumi.getter(name="inputTimeZoneOffset")
    def input_time_zone_offset(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the difference between your time zone and Greenwich Mean Time (GMT).
        """
        return pulumi.get(self, "input_time_zone_offset")

    @input_time_zone_offset.setter
    def input_time_zone_offset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_time_zone_offset", value)


@pulumi.input_type
class DataOutputConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 s3_output_configuration: pulumi.Input['InferenceSchedulerS3OutputConfigurationArgs'],
                 kms_key_id: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.
        :param pulumi.Input[str] kms_key_id: The ID number for the AWS KMS key used to encrypt the inference output.
        """
        pulumi.set(__self__, "s3_output_configuration", s3_output_configuration)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)

    @property
    @pulumi.getter(name="s3OutputConfiguration")
    def s3_output_configuration(self) -> pulumi.Input['InferenceSchedulerS3OutputConfigurationArgs']:
        return pulumi.get(self, "s3_output_configuration")

    @s3_output_configuration.setter
    def s3_output_configuration(self, value: pulumi.Input['InferenceSchedulerS3OutputConfigurationArgs']):
        pulumi.set(self, "s3_output_configuration", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID number for the AWS KMS key used to encrypt the inference output.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)


@pulumi.input_type
class InferenceSchedulerInputNameConfigurationArgs:
    def __init__(__self__, *,
                 component_timestamp_delimiter: Optional[pulumi.Input[str]] = None,
                 timestamp_format: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
        :param pulumi.Input[str] component_timestamp_delimiter: Indicates the delimiter character used between items in the data.
        :param pulumi.Input[str] timestamp_format: The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
        """
        if component_timestamp_delimiter is not None:
            pulumi.set(__self__, "component_timestamp_delimiter", component_timestamp_delimiter)
        if timestamp_format is not None:
            pulumi.set(__self__, "timestamp_format", timestamp_format)

    @property
    @pulumi.getter(name="componentTimestampDelimiter")
    def component_timestamp_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the delimiter character used between items in the data.
        """
        return pulumi.get(self, "component_timestamp_delimiter")

    @component_timestamp_delimiter.setter
    def component_timestamp_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_timestamp_delimiter", value)

    @property
    @pulumi.getter(name="timestampFormat")
    def timestamp_format(self) -> Optional[pulumi.Input[str]]:
        """
        The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
        """
        return pulumi.get(self, "timestamp_format")

    @timestamp_format.setter
    def timestamp_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timestamp_format", value)


@pulumi.input_type
class InferenceSchedulerS3InputConfigurationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration information for the input data for the inference, including input data S3 location.
        """
        pulumi.set(__self__, "bucket", bucket)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class InferenceSchedulerS3OutputConfigurationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration information for the output results from the inference, including output S3 location.
        """
        pulumi.set(__self__, "bucket", bucket)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


