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
    'ConnectorApacheKafkaClusterArgs',
    'ConnectorAutoScalingArgs',
    'ConnectorCapacityArgs',
    'ConnectorCloudWatchLogsLogDeliveryArgs',
    'ConnectorCustomPluginArgs',
    'ConnectorFirehoseLogDeliveryArgs',
    'ConnectorKafkaClusterClientAuthenticationArgs',
    'ConnectorKafkaClusterEncryptionInTransitArgs',
    'ConnectorKafkaClusterArgs',
    'ConnectorLogDeliveryArgs',
    'ConnectorPluginArgs',
    'ConnectorProvisionedCapacityArgs',
    'ConnectorS3LogDeliveryArgs',
    'ConnectorScaleInPolicyArgs',
    'ConnectorScaleOutPolicyArgs',
    'ConnectorVpcArgs',
    'ConnectorWorkerConfigurationArgs',
    'ConnectorWorkerLogDeliveryArgs',
]

@pulumi.input_type
class ConnectorApacheKafkaClusterArgs:
    def __init__(__self__, *,
                 bootstrap_servers: pulumi.Input[str],
                 vpc: pulumi.Input['ConnectorVpcArgs']):
        """
        Details of how to connect to an Apache Kafka cluster.
        :param pulumi.Input[str] bootstrap_servers: The bootstrap servers string of the Apache Kafka cluster.
        """
        pulumi.set(__self__, "bootstrap_servers", bootstrap_servers)
        pulumi.set(__self__, "vpc", vpc)

    @property
    @pulumi.getter(name="bootstrapServers")
    def bootstrap_servers(self) -> pulumi.Input[str]:
        """
        The bootstrap servers string of the Apache Kafka cluster.
        """
        return pulumi.get(self, "bootstrap_servers")

    @bootstrap_servers.setter
    def bootstrap_servers(self, value: pulumi.Input[str]):
        pulumi.set(self, "bootstrap_servers", value)

    @property
    @pulumi.getter
    def vpc(self) -> pulumi.Input['ConnectorVpcArgs']:
        return pulumi.get(self, "vpc")

    @vpc.setter
    def vpc(self, value: pulumi.Input['ConnectorVpcArgs']):
        pulumi.set(self, "vpc", value)


@pulumi.input_type
class ConnectorAutoScalingArgs:
    def __init__(__self__, *,
                 max_worker_count: pulumi.Input[int],
                 mcu_count: pulumi.Input[int],
                 min_worker_count: pulumi.Input[int],
                 scale_in_policy: pulumi.Input['ConnectorScaleInPolicyArgs'],
                 scale_out_policy: pulumi.Input['ConnectorScaleOutPolicyArgs']):
        """
        Details about auto scaling of a connector.
        :param pulumi.Input[int] max_worker_count: The maximum number of workers for a connector.
        :param pulumi.Input[int] mcu_count: Specifies how many MSK Connect Units (MCU) as the minimum scaling unit.
        :param pulumi.Input[int] min_worker_count: The minimum number of workers for a connector.
        """
        pulumi.set(__self__, "max_worker_count", max_worker_count)
        pulumi.set(__self__, "mcu_count", mcu_count)
        pulumi.set(__self__, "min_worker_count", min_worker_count)
        pulumi.set(__self__, "scale_in_policy", scale_in_policy)
        pulumi.set(__self__, "scale_out_policy", scale_out_policy)

    @property
    @pulumi.getter(name="maxWorkerCount")
    def max_worker_count(self) -> pulumi.Input[int]:
        """
        The maximum number of workers for a connector.
        """
        return pulumi.get(self, "max_worker_count")

    @max_worker_count.setter
    def max_worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_worker_count", value)

    @property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> pulumi.Input[int]:
        """
        Specifies how many MSK Connect Units (MCU) as the minimum scaling unit.
        """
        return pulumi.get(self, "mcu_count")

    @mcu_count.setter
    def mcu_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "mcu_count", value)

    @property
    @pulumi.getter(name="minWorkerCount")
    def min_worker_count(self) -> pulumi.Input[int]:
        """
        The minimum number of workers for a connector.
        """
        return pulumi.get(self, "min_worker_count")

    @min_worker_count.setter
    def min_worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_worker_count", value)

    @property
    @pulumi.getter(name="scaleInPolicy")
    def scale_in_policy(self) -> pulumi.Input['ConnectorScaleInPolicyArgs']:
        return pulumi.get(self, "scale_in_policy")

    @scale_in_policy.setter
    def scale_in_policy(self, value: pulumi.Input['ConnectorScaleInPolicyArgs']):
        pulumi.set(self, "scale_in_policy", value)

    @property
    @pulumi.getter(name="scaleOutPolicy")
    def scale_out_policy(self) -> pulumi.Input['ConnectorScaleOutPolicyArgs']:
        return pulumi.get(self, "scale_out_policy")

    @scale_out_policy.setter
    def scale_out_policy(self, value: pulumi.Input['ConnectorScaleOutPolicyArgs']):
        pulumi.set(self, "scale_out_policy", value)


@pulumi.input_type
class ConnectorCapacityArgs:
    def __init__(__self__, *,
                 auto_scaling: Optional[pulumi.Input['ConnectorAutoScalingArgs']] = None,
                 provisioned_capacity: Optional[pulumi.Input['ConnectorProvisionedCapacityArgs']] = None):
        """
        Information about the capacity allocated to the connector.
        """
        if auto_scaling is not None:
            pulumi.set(__self__, "auto_scaling", auto_scaling)
        if provisioned_capacity is not None:
            pulumi.set(__self__, "provisioned_capacity", provisioned_capacity)

    @property
    @pulumi.getter(name="autoScaling")
    def auto_scaling(self) -> Optional[pulumi.Input['ConnectorAutoScalingArgs']]:
        return pulumi.get(self, "auto_scaling")

    @auto_scaling.setter
    def auto_scaling(self, value: Optional[pulumi.Input['ConnectorAutoScalingArgs']]):
        pulumi.set(self, "auto_scaling", value)

    @property
    @pulumi.getter(name="provisionedCapacity")
    def provisioned_capacity(self) -> Optional[pulumi.Input['ConnectorProvisionedCapacityArgs']]:
        return pulumi.get(self, "provisioned_capacity")

    @provisioned_capacity.setter
    def provisioned_capacity(self, value: Optional[pulumi.Input['ConnectorProvisionedCapacityArgs']]):
        pulumi.set(self, "provisioned_capacity", value)


@pulumi.input_type
class ConnectorCloudWatchLogsLogDeliveryArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 log_group: Optional[pulumi.Input[str]] = None):
        """
        Details about delivering logs to Amazon CloudWatch Logs.
        :param pulumi.Input[bool] enabled: Specifies whether the logs get sent to the specified CloudWatch Logs destination.
        :param pulumi.Input[str] log_group: The CloudWatch log group that is the destination for log delivery.
        """
        pulumi.set(__self__, "enabled", enabled)
        if log_group is not None:
            pulumi.set(__self__, "log_group", log_group)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether the logs get sent to the specified CloudWatch Logs destination.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[str]]:
        """
        The CloudWatch log group that is the destination for log delivery.
        """
        return pulumi.get(self, "log_group")

    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group", value)


@pulumi.input_type
class ConnectorCustomPluginArgs:
    def __init__(__self__, *,
                 custom_plugin_arn: pulumi.Input[str],
                 revision: pulumi.Input[int]):
        """
        Details about a custom plugin.
        :param pulumi.Input[str] custom_plugin_arn: The Amazon Resource Name (ARN) of the custom plugin to use.
        :param pulumi.Input[int] revision: The revision of the custom plugin to use.
        """
        pulumi.set(__self__, "custom_plugin_arn", custom_plugin_arn)
        pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter(name="customPluginArn")
    def custom_plugin_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the custom plugin to use.
        """
        return pulumi.get(self, "custom_plugin_arn")

    @custom_plugin_arn.setter
    def custom_plugin_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "custom_plugin_arn", value)

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Input[int]:
        """
        The revision of the custom plugin to use.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: pulumi.Input[int]):
        pulumi.set(self, "revision", value)


@pulumi.input_type
class ConnectorFirehoseLogDeliveryArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 delivery_stream: Optional[pulumi.Input[str]] = None):
        """
        Details about delivering logs to Amazon Kinesis Data Firehose.
        :param pulumi.Input[bool] enabled: Specifies whether the logs get sent to the specified Kinesis Data Firehose delivery stream.
        :param pulumi.Input[str] delivery_stream: The Kinesis Data Firehose delivery stream that is the destination for log delivery.
        """
        pulumi.set(__self__, "enabled", enabled)
        if delivery_stream is not None:
            pulumi.set(__self__, "delivery_stream", delivery_stream)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether the logs get sent to the specified Kinesis Data Firehose delivery stream.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> Optional[pulumi.Input[str]]:
        """
        The Kinesis Data Firehose delivery stream that is the destination for log delivery.
        """
        return pulumi.get(self, "delivery_stream")

    @delivery_stream.setter
    def delivery_stream(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_stream", value)


@pulumi.input_type
class ConnectorKafkaClusterClientAuthenticationArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input['ConnectorKafkaClusterClientAuthenticationType']):
        """
        Details of the client authentication used by the Kafka cluster.
        """
        pulumi.set(__self__, "authentication_type", authentication_type)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input['ConnectorKafkaClusterClientAuthenticationType']:
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input['ConnectorKafkaClusterClientAuthenticationType']):
        pulumi.set(self, "authentication_type", value)


@pulumi.input_type
class ConnectorKafkaClusterEncryptionInTransitArgs:
    def __init__(__self__, *,
                 encryption_type: pulumi.Input['ConnectorKafkaClusterEncryptionInTransitType']):
        """
        Details of encryption in transit to the Kafka cluster.
        """
        pulumi.set(__self__, "encryption_type", encryption_type)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input['ConnectorKafkaClusterEncryptionInTransitType']:
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input['ConnectorKafkaClusterEncryptionInTransitType']):
        pulumi.set(self, "encryption_type", value)


@pulumi.input_type
class ConnectorKafkaClusterArgs:
    def __init__(__self__, *,
                 apache_kafka_cluster: pulumi.Input['ConnectorApacheKafkaClusterArgs']):
        """
        Details of how to connect to the Kafka cluster.
        """
        pulumi.set(__self__, "apache_kafka_cluster", apache_kafka_cluster)

    @property
    @pulumi.getter(name="apacheKafkaCluster")
    def apache_kafka_cluster(self) -> pulumi.Input['ConnectorApacheKafkaClusterArgs']:
        return pulumi.get(self, "apache_kafka_cluster")

    @apache_kafka_cluster.setter
    def apache_kafka_cluster(self, value: pulumi.Input['ConnectorApacheKafkaClusterArgs']):
        pulumi.set(self, "apache_kafka_cluster", value)


@pulumi.input_type
class ConnectorLogDeliveryArgs:
    def __init__(__self__, *,
                 worker_log_delivery: pulumi.Input['ConnectorWorkerLogDeliveryArgs']):
        """
        Details of what logs are delivered and where they are delivered.
        """
        pulumi.set(__self__, "worker_log_delivery", worker_log_delivery)

    @property
    @pulumi.getter(name="workerLogDelivery")
    def worker_log_delivery(self) -> pulumi.Input['ConnectorWorkerLogDeliveryArgs']:
        return pulumi.get(self, "worker_log_delivery")

    @worker_log_delivery.setter
    def worker_log_delivery(self, value: pulumi.Input['ConnectorWorkerLogDeliveryArgs']):
        pulumi.set(self, "worker_log_delivery", value)


@pulumi.input_type
class ConnectorPluginArgs:
    def __init__(__self__, *,
                 custom_plugin: pulumi.Input['ConnectorCustomPluginArgs']):
        """
        Details about a Kafka Connect plugin which will be used with the connector.
        """
        pulumi.set(__self__, "custom_plugin", custom_plugin)

    @property
    @pulumi.getter(name="customPlugin")
    def custom_plugin(self) -> pulumi.Input['ConnectorCustomPluginArgs']:
        return pulumi.get(self, "custom_plugin")

    @custom_plugin.setter
    def custom_plugin(self, value: pulumi.Input['ConnectorCustomPluginArgs']):
        pulumi.set(self, "custom_plugin", value)


@pulumi.input_type
class ConnectorProvisionedCapacityArgs:
    def __init__(__self__, *,
                 worker_count: pulumi.Input[int],
                 mcu_count: Optional[pulumi.Input[int]] = None):
        """
        Details about a fixed capacity allocated to a connector.
        :param pulumi.Input[int] worker_count: Number of workers for a connector.
        :param pulumi.Input[int] mcu_count: Specifies how many MSK Connect Units (MCU) are allocated to the connector.
        """
        pulumi.set(__self__, "worker_count", worker_count)
        if mcu_count is not None:
            pulumi.set(__self__, "mcu_count", mcu_count)

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[int]:
        """
        Number of workers for a connector.
        """
        return pulumi.get(self, "worker_count")

    @worker_count.setter
    def worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "worker_count", value)

    @property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies how many MSK Connect Units (MCU) are allocated to the connector.
        """
        return pulumi.get(self, "mcu_count")

    @mcu_count.setter
    def mcu_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mcu_count", value)


@pulumi.input_type
class ConnectorS3LogDeliveryArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 bucket: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        Details about delivering logs to Amazon S3.
        :param pulumi.Input[bool] enabled: Specifies whether the logs get sent to the specified Amazon S3 destination.
        :param pulumi.Input[str] bucket: The name of the S3 bucket that is the destination for log delivery.
        :param pulumi.Input[str] prefix: The S3 prefix that is the destination for log delivery.
        """
        pulumi.set(__self__, "enabled", enabled)
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies whether the logs get sent to the specified Amazon S3 destination.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the S3 bucket that is the destination for log delivery.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The S3 prefix that is the destination for log delivery.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class ConnectorScaleInPolicyArgs:
    def __init__(__self__, *,
                 cpu_utilization_percentage: pulumi.Input[int]):
        """
        Information about the scale in policy of the connector.
        :param pulumi.Input[int] cpu_utilization_percentage: Specifies the CPU utilization percentage threshold at which connector scale in should trigger.
        """
        pulumi.set(__self__, "cpu_utilization_percentage", cpu_utilization_percentage)

    @property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> pulumi.Input[int]:
        """
        Specifies the CPU utilization percentage threshold at which connector scale in should trigger.
        """
        return pulumi.get(self, "cpu_utilization_percentage")

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: pulumi.Input[int]):
        pulumi.set(self, "cpu_utilization_percentage", value)


@pulumi.input_type
class ConnectorScaleOutPolicyArgs:
    def __init__(__self__, *,
                 cpu_utilization_percentage: pulumi.Input[int]):
        """
        Information about the scale out policy of the connector.
        :param pulumi.Input[int] cpu_utilization_percentage: Specifies the CPU utilization percentage threshold at which connector scale out should trigger.
        """
        pulumi.set(__self__, "cpu_utilization_percentage", cpu_utilization_percentage)

    @property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> pulumi.Input[int]:
        """
        Specifies the CPU utilization percentage threshold at which connector scale out should trigger.
        """
        return pulumi.get(self, "cpu_utilization_percentage")

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: pulumi.Input[int]):
        pulumi.set(self, "cpu_utilization_percentage", value)


@pulumi.input_type
class ConnectorVpcArgs:
    def __init__(__self__, *,
                 security_groups: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnets: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Information about a VPC used with the connector.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: The AWS security groups to associate with the elastic network interfaces in order to specify what the connector has access to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The list of subnets to connect to in the virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets.
        """
        pulumi.set(__self__, "security_groups", security_groups)
        pulumi.set(__self__, "subnets", subnets)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The AWS security groups to associate with the elastic network interfaces in order to specify what the connector has access to.
        """
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_groups", value)

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of subnets to connect to in the virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnets", value)


@pulumi.input_type
class ConnectorWorkerConfigurationArgs:
    def __init__(__self__, *,
                 revision: pulumi.Input[int],
                 worker_configuration_arn: pulumi.Input[str]):
        """
        Specifies the worker configuration to use with the connector.
        :param pulumi.Input[int] revision: The revision of the worker configuration to use.
        :param pulumi.Input[str] worker_configuration_arn: The Amazon Resource Name (ARN) of the worker configuration to use.
        """
        pulumi.set(__self__, "revision", revision)
        pulumi.set(__self__, "worker_configuration_arn", worker_configuration_arn)

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Input[int]:
        """
        The revision of the worker configuration to use.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: pulumi.Input[int]):
        pulumi.set(self, "revision", value)

    @property
    @pulumi.getter(name="workerConfigurationArn")
    def worker_configuration_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the worker configuration to use.
        """
        return pulumi.get(self, "worker_configuration_arn")

    @worker_configuration_arn.setter
    def worker_configuration_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "worker_configuration_arn", value)


@pulumi.input_type
class ConnectorWorkerLogDeliveryArgs:
    def __init__(__self__, *,
                 cloud_watch_logs: Optional[pulumi.Input['ConnectorCloudWatchLogsLogDeliveryArgs']] = None,
                 firehose: Optional[pulumi.Input['ConnectorFirehoseLogDeliveryArgs']] = None,
                 s3: Optional[pulumi.Input['ConnectorS3LogDeliveryArgs']] = None):
        """
        Specifies where worker logs are delivered.
        """
        if cloud_watch_logs is not None:
            pulumi.set(__self__, "cloud_watch_logs", cloud_watch_logs)
        if firehose is not None:
            pulumi.set(__self__, "firehose", firehose)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter(name="cloudWatchLogs")
    def cloud_watch_logs(self) -> Optional[pulumi.Input['ConnectorCloudWatchLogsLogDeliveryArgs']]:
        return pulumi.get(self, "cloud_watch_logs")

    @cloud_watch_logs.setter
    def cloud_watch_logs(self, value: Optional[pulumi.Input['ConnectorCloudWatchLogsLogDeliveryArgs']]):
        pulumi.set(self, "cloud_watch_logs", value)

    @property
    @pulumi.getter
    def firehose(self) -> Optional[pulumi.Input['ConnectorFirehoseLogDeliveryArgs']]:
        return pulumi.get(self, "firehose")

    @firehose.setter
    def firehose(self, value: Optional[pulumi.Input['ConnectorFirehoseLogDeliveryArgs']]):
        pulumi.set(self, "firehose", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['ConnectorS3LogDeliveryArgs']]:
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['ConnectorS3LogDeliveryArgs']]):
        pulumi.set(self, "s3", value)


