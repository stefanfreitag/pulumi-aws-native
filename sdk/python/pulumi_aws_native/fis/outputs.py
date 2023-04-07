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
    'ExperimentTemplateActionMap',
    'ExperimentTemplateLogConfiguration',
    'ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties',
    'ExperimentTemplateLogConfigurationS3ConfigurationProperties',
    'ExperimentTemplateStopCondition',
    'ExperimentTemplateTargetMap',
]

@pulumi.output_type
class ExperimentTemplateActionMap(dict):
    """
    The actions for the experiment.
    """
    def __init__(__self__):
        """
        The actions for the experiment.
        """
        pass


@pulumi.output_type
class ExperimentTemplateLogConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logSchemaVersion":
            suggest = "log_schema_version"
        elif key == "cloudWatchLogsConfiguration":
            suggest = "cloud_watch_logs_configuration"
        elif key == "s3Configuration":
            suggest = "s3_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExperimentTemplateLogConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExperimentTemplateLogConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExperimentTemplateLogConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_schema_version: int,
                 cloud_watch_logs_configuration: Optional['outputs.ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties'] = None,
                 s3_configuration: Optional['outputs.ExperimentTemplateLogConfigurationS3ConfigurationProperties'] = None):
        pulumi.set(__self__, "log_schema_version", log_schema_version)
        if cloud_watch_logs_configuration is not None:
            pulumi.set(__self__, "cloud_watch_logs_configuration", cloud_watch_logs_configuration)
        if s3_configuration is not None:
            pulumi.set(__self__, "s3_configuration", s3_configuration)

    @property
    @pulumi.getter(name="logSchemaVersion")
    def log_schema_version(self) -> int:
        return pulumi.get(self, "log_schema_version")

    @property
    @pulumi.getter(name="cloudWatchLogsConfiguration")
    def cloud_watch_logs_configuration(self) -> Optional['outputs.ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties']:
        return pulumi.get(self, "cloud_watch_logs_configuration")

    @property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional['outputs.ExperimentTemplateLogConfigurationS3ConfigurationProperties']:
        return pulumi.get(self, "s3_configuration")


@pulumi.output_type
class ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logGroupArn":
            suggest = "log_group_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExperimentTemplateLogConfigurationCloudWatchLogsConfigurationProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_group_arn: str):
        pulumi.set(__self__, "log_group_arn", log_group_arn)

    @property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> str:
        return pulumi.get(self, "log_group_arn")


@pulumi.output_type
class ExperimentTemplateLogConfigurationS3ConfigurationProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExperimentTemplateLogConfigurationS3ConfigurationProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExperimentTemplateLogConfigurationS3ConfigurationProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExperimentTemplateLogConfigurationS3ConfigurationProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str,
                 prefix: Optional[str] = None):
        pulumi.set(__self__, "bucket_name", bucket_name)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")


@pulumi.output_type
class ExperimentTemplateStopCondition(dict):
    def __init__(__self__, *,
                 source: str,
                 value: Optional[str] = None):
        pulumi.set(__self__, "source", source)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def source(self) -> str:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class ExperimentTemplateTargetMap(dict):
    """
    The targets for the experiment.
    """
    def __init__(__self__):
        """
        The targets for the experiment.
        """
        pass


