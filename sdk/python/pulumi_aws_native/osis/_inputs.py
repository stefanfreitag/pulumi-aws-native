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
    'PipelineBufferOptionsArgs',
    'PipelineEncryptionAtRestOptionsArgs',
    'PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs',
    'PipelineLogPublishingOptionsArgs',
    'PipelineVpcOptionsArgs',
]

@pulumi.input_type
class PipelineBufferOptionsArgs:
    def __init__(__self__, *,
                 persistent_buffer_enabled: pulumi.Input[bool]):
        """
        Key-value pairs to configure buffering.
        :param pulumi.Input[bool] persistent_buffer_enabled: Whether persistent buffering should be enabled.
        """
        pulumi.set(__self__, "persistent_buffer_enabled", persistent_buffer_enabled)

    @property
    @pulumi.getter(name="persistentBufferEnabled")
    def persistent_buffer_enabled(self) -> pulumi.Input[bool]:
        """
        Whether persistent buffering should be enabled.
        """
        return pulumi.get(self, "persistent_buffer_enabled")

    @persistent_buffer_enabled.setter
    def persistent_buffer_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "persistent_buffer_enabled", value)


@pulumi.input_type
class PipelineEncryptionAtRestOptionsArgs:
    def __init__(__self__, *,
                 kms_key_arn: pulumi.Input[str]):
        """
        Key-value pairs to configure encryption at rest.
        :param pulumi.Input[str] kms_key_arn: The KMS key to use for encrypting data. By default an AWS owned key is used
        """
        pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[str]:
        """
        The KMS key to use for encrypting data. By default an AWS owned key is used
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "kms_key_arn", value)


@pulumi.input_type
class PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs:
    def __init__(__self__, *,
                 log_group: pulumi.Input[str]):
        """
        The destination for OpenSearch Ingestion Service logs sent to Amazon CloudWatch.
        """
        pulumi.set(__self__, "log_group", log_group)

    @property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> pulumi.Input[str]:
        return pulumi.get(self, "log_group")

    @log_group.setter
    def log_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_group", value)


@pulumi.input_type
class PipelineLogPublishingOptionsArgs:
    def __init__(__self__, *,
                 cloud_watch_log_destination: Optional[pulumi.Input['PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs']] = None,
                 is_logging_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Key-value pairs to configure log publishing.
        :param pulumi.Input['PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs'] cloud_watch_log_destination: The destination for OpenSearch Ingestion Service logs sent to Amazon CloudWatch.
        :param pulumi.Input[bool] is_logging_enabled: Whether logs should be published.
        """
        if cloud_watch_log_destination is not None:
            pulumi.set(__self__, "cloud_watch_log_destination", cloud_watch_log_destination)
        if is_logging_enabled is not None:
            pulumi.set(__self__, "is_logging_enabled", is_logging_enabled)

    @property
    @pulumi.getter(name="cloudWatchLogDestination")
    def cloud_watch_log_destination(self) -> Optional[pulumi.Input['PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs']]:
        """
        The destination for OpenSearch Ingestion Service logs sent to Amazon CloudWatch.
        """
        return pulumi.get(self, "cloud_watch_log_destination")

    @cloud_watch_log_destination.setter
    def cloud_watch_log_destination(self, value: Optional[pulumi.Input['PipelineLogPublishingOptionsCloudWatchLogDestinationPropertiesArgs']]):
        pulumi.set(self, "cloud_watch_log_destination", value)

    @property
    @pulumi.getter(name="isLoggingEnabled")
    def is_logging_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether logs should be published.
        """
        return pulumi.get(self, "is_logging_enabled")

    @is_logging_enabled.setter
    def is_logging_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_logging_enabled", value)


@pulumi.input_type
class PipelineVpcOptionsArgs:
    def __init__(__self__, *,
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion Service creates the pipeline with a public endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs associated with the VPC endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security groups associated with the VPC endpoint.
        """
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of subnet IDs associated with the VPC endpoint.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of security groups associated with the VPC endpoint.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)


