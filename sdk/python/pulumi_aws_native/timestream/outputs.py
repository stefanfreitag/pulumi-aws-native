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

__all__ = [
    'DatabaseTag',
    'MagneticStoreWritePropertiesProperties',
    'MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties',
    'MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties',
    'RetentionPropertiesProperties',
    'ScheduledQueryDimensionMapping',
    'ScheduledQueryErrorReportConfiguration',
    'ScheduledQueryMixedMeasureMapping',
    'ScheduledQueryMultiMeasureAttributeMapping',
    'ScheduledQueryMultiMeasureMappings',
    'ScheduledQueryNotificationConfiguration',
    'ScheduledQueryS3Configuration',
    'ScheduledQueryScheduleConfiguration',
    'ScheduledQuerySnsConfiguration',
    'ScheduledQueryTag',
    'ScheduledQueryTargetConfiguration',
    'ScheduledQueryTimestreamConfiguration',
    'SchemaProperties',
    'TablePartitionKey',
    'TableTag',
]

@pulumi.output_type
class DatabaseTag(dict):
    """
    You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
    """
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        """
        You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class MagneticStoreWritePropertiesProperties(dict):
    """
    The properties that determine whether magnetic store writes are enabled.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enableMagneticStoreWrites":
            suggest = "enable_magnetic_store_writes"
        elif key == "magneticStoreRejectedDataLocation":
            suggest = "magnetic_store_rejected_data_location"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MagneticStoreWritePropertiesProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MagneticStoreWritePropertiesProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MagneticStoreWritePropertiesProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_magnetic_store_writes: bool,
                 magnetic_store_rejected_data_location: Optional['outputs.MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties'] = None):
        """
        The properties that determine whether magnetic store writes are enabled.
        :param bool enable_magnetic_store_writes: Boolean flag indicating whether magnetic store writes are enabled.
        :param 'MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties' magnetic_store_rejected_data_location: Location to store information about records that were asynchronously rejected during magnetic store writes.
        """
        pulumi.set(__self__, "enable_magnetic_store_writes", enable_magnetic_store_writes)
        if magnetic_store_rejected_data_location is not None:
            pulumi.set(__self__, "magnetic_store_rejected_data_location", magnetic_store_rejected_data_location)

    @property
    @pulumi.getter(name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(self) -> bool:
        """
        Boolean flag indicating whether magnetic store writes are enabled.
        """
        return pulumi.get(self, "enable_magnetic_store_writes")

    @property
    @pulumi.getter(name="magneticStoreRejectedDataLocation")
    def magnetic_store_rejected_data_location(self) -> Optional['outputs.MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties']:
        """
        Location to store information about records that were asynchronously rejected during magnetic store writes.
        """
        return pulumi.get(self, "magnetic_store_rejected_data_location")


@pulumi.output_type
class MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties(dict):
    """
    Location to store information about records that were asynchronously rejected during magnetic store writes.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "s3Configuration":
            suggest = "s3_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 s3_configuration: Optional['outputs.MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties'] = None):
        """
        Location to store information about records that were asynchronously rejected during magnetic store writes.
        :param 'MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties' s3_configuration: S3 configuration for location to store rejections from magnetic store writes
        """
        if s3_configuration is not None:
            pulumi.set(__self__, "s3_configuration", s3_configuration)

    @property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional['outputs.MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties']:
        """
        S3 configuration for location to store rejections from magnetic store writes
        """
        return pulumi.get(self, "s3_configuration")


@pulumi.output_type
class MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties(dict):
    """
    S3 configuration for location to store rejections from magnetic store writes
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"
        elif key == "encryptionOption":
            suggest = "encryption_option"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"
        elif key == "objectKeyPrefix":
            suggest = "object_key_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MagneticStoreWritePropertiesPropertiesMagneticStoreRejectedDataLocationPropertiesS3ConfigurationProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str,
                 encryption_option: str,
                 kms_key_id: Optional[str] = None,
                 object_key_prefix: Optional[str] = None):
        """
        S3 configuration for location to store rejections from magnetic store writes
        :param str bucket_name: The bucket name used to store the data.
        :param str encryption_option: Either SSE_KMS or SSE_S3.
        :param str kms_key_id: Must be provided if SSE_KMS is specified as the encryption option
        :param str object_key_prefix: String used to prefix all data in the bucket.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "encryption_option", encryption_option)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if object_key_prefix is not None:
            pulumi.set(__self__, "object_key_prefix", object_key_prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The bucket name used to store the data.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> str:
        """
        Either SSE_KMS or SSE_S3.
        """
        return pulumi.get(self, "encryption_option")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        Must be provided if SSE_KMS is specified as the encryption option
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[str]:
        """
        String used to prefix all data in the bucket.
        """
        return pulumi.get(self, "object_key_prefix")


@pulumi.output_type
class RetentionPropertiesProperties(dict):
    """
    The retention duration of the memory store and the magnetic store.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "magneticStoreRetentionPeriodInDays":
            suggest = "magnetic_store_retention_period_in_days"
        elif key == "memoryStoreRetentionPeriodInHours":
            suggest = "memory_store_retention_period_in_hours"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RetentionPropertiesProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RetentionPropertiesProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RetentionPropertiesProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 magnetic_store_retention_period_in_days: Optional[str] = None,
                 memory_store_retention_period_in_hours: Optional[str] = None):
        """
        The retention duration of the memory store and the magnetic store.
        :param str magnetic_store_retention_period_in_days: The duration for which data must be stored in the magnetic store.
        :param str memory_store_retention_period_in_hours: The duration for which data must be stored in the memory store.
        """
        if magnetic_store_retention_period_in_days is not None:
            pulumi.set(__self__, "magnetic_store_retention_period_in_days", magnetic_store_retention_period_in_days)
        if memory_store_retention_period_in_hours is not None:
            pulumi.set(__self__, "memory_store_retention_period_in_hours", memory_store_retention_period_in_hours)

    @property
    @pulumi.getter(name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> Optional[str]:
        """
        The duration for which data must be stored in the magnetic store.
        """
        return pulumi.get(self, "magnetic_store_retention_period_in_days")

    @property
    @pulumi.getter(name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> Optional[str]:
        """
        The duration for which data must be stored in the memory store.
        """
        return pulumi.get(self, "memory_store_retention_period_in_hours")


@pulumi.output_type
class ScheduledQueryDimensionMapping(dict):
    """
    This type is used to map column(s) from the query result to a dimension in the destination table.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dimensionValueType":
            suggest = "dimension_value_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryDimensionMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryDimensionMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryDimensionMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dimension_value_type: 'ScheduledQueryDimensionValueType',
                 name: str):
        """
        This type is used to map column(s) from the query result to a dimension in the destination table.
        """
        pulumi.set(__self__, "dimension_value_type", dimension_value_type)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dimensionValueType")
    def dimension_value_type(self) -> 'ScheduledQueryDimensionValueType':
        return pulumi.get(self, "dimension_value_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class ScheduledQueryErrorReportConfiguration(dict):
    """
    Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "s3Configuration":
            suggest = "s3_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryErrorReportConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryErrorReportConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryErrorReportConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 s3_configuration: 'outputs.ScheduledQueryS3Configuration'):
        """
        Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
        """
        pulumi.set(__self__, "s3_configuration", s3_configuration)

    @property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> 'outputs.ScheduledQueryS3Configuration':
        return pulumi.get(self, "s3_configuration")


@pulumi.output_type
class ScheduledQueryMixedMeasureMapping(dict):
    """
    MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "measureValueType":
            suggest = "measure_value_type"
        elif key == "measureName":
            suggest = "measure_name"
        elif key == "multiMeasureAttributeMappings":
            suggest = "multi_measure_attribute_mappings"
        elif key == "sourceColumn":
            suggest = "source_column"
        elif key == "targetMeasureName":
            suggest = "target_measure_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryMixedMeasureMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryMixedMeasureMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryMixedMeasureMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 measure_value_type: 'ScheduledQueryMixedMeasureMappingMeasureValueType',
                 measure_name: Optional[str] = None,
                 multi_measure_attribute_mappings: Optional[Sequence['outputs.ScheduledQueryMultiMeasureAttributeMapping']] = None,
                 source_column: Optional[str] = None,
                 target_measure_name: Optional[str] = None):
        """
        MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.
        """
        pulumi.set(__self__, "measure_value_type", measure_value_type)
        if measure_name is not None:
            pulumi.set(__self__, "measure_name", measure_name)
        if multi_measure_attribute_mappings is not None:
            pulumi.set(__self__, "multi_measure_attribute_mappings", multi_measure_attribute_mappings)
        if source_column is not None:
            pulumi.set(__self__, "source_column", source_column)
        if target_measure_name is not None:
            pulumi.set(__self__, "target_measure_name", target_measure_name)

    @property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> 'ScheduledQueryMixedMeasureMappingMeasureValueType':
        return pulumi.get(self, "measure_value_type")

    @property
    @pulumi.getter(name="measureName")
    def measure_name(self) -> Optional[str]:
        return pulumi.get(self, "measure_name")

    @property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(self) -> Optional[Sequence['outputs.ScheduledQueryMultiMeasureAttributeMapping']]:
        return pulumi.get(self, "multi_measure_attribute_mappings")

    @property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> Optional[str]:
        return pulumi.get(self, "source_column")

    @property
    @pulumi.getter(name="targetMeasureName")
    def target_measure_name(self) -> Optional[str]:
        return pulumi.get(self, "target_measure_name")


@pulumi.output_type
class ScheduledQueryMultiMeasureAttributeMapping(dict):
    """
    An attribute mapping to be used for mapping query results to ingest data for multi-measure attributes.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "measureValueType":
            suggest = "measure_value_type"
        elif key == "sourceColumn":
            suggest = "source_column"
        elif key == "targetMultiMeasureAttributeName":
            suggest = "target_multi_measure_attribute_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryMultiMeasureAttributeMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryMultiMeasureAttributeMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryMultiMeasureAttributeMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 measure_value_type: 'ScheduledQueryMultiMeasureAttributeMappingMeasureValueType',
                 source_column: str,
                 target_multi_measure_attribute_name: Optional[str] = None):
        """
        An attribute mapping to be used for mapping query results to ingest data for multi-measure attributes.
        """
        pulumi.set(__self__, "measure_value_type", measure_value_type)
        pulumi.set(__self__, "source_column", source_column)
        if target_multi_measure_attribute_name is not None:
            pulumi.set(__self__, "target_multi_measure_attribute_name", target_multi_measure_attribute_name)

    @property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> 'ScheduledQueryMultiMeasureAttributeMappingMeasureValueType':
        return pulumi.get(self, "measure_value_type")

    @property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> str:
        return pulumi.get(self, "source_column")

    @property
    @pulumi.getter(name="targetMultiMeasureAttributeName")
    def target_multi_measure_attribute_name(self) -> Optional[str]:
        return pulumi.get(self, "target_multi_measure_attribute_name")


@pulumi.output_type
class ScheduledQueryMultiMeasureMappings(dict):
    """
    Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided. MultiMeasureMappings can be used to ingest data as multi measures in the derived table.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "multiMeasureAttributeMappings":
            suggest = "multi_measure_attribute_mappings"
        elif key == "targetMultiMeasureName":
            suggest = "target_multi_measure_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryMultiMeasureMappings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryMultiMeasureMappings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryMultiMeasureMappings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 multi_measure_attribute_mappings: Sequence['outputs.ScheduledQueryMultiMeasureAttributeMapping'],
                 target_multi_measure_name: Optional[str] = None):
        """
        Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided. MultiMeasureMappings can be used to ingest data as multi measures in the derived table.
        """
        pulumi.set(__self__, "multi_measure_attribute_mappings", multi_measure_attribute_mappings)
        if target_multi_measure_name is not None:
            pulumi.set(__self__, "target_multi_measure_name", target_multi_measure_name)

    @property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(self) -> Sequence['outputs.ScheduledQueryMultiMeasureAttributeMapping']:
        return pulumi.get(self, "multi_measure_attribute_mappings")

    @property
    @pulumi.getter(name="targetMultiMeasureName")
    def target_multi_measure_name(self) -> Optional[str]:
        return pulumi.get(self, "target_multi_measure_name")


@pulumi.output_type
class ScheduledQueryNotificationConfiguration(dict):
    """
    Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "snsConfiguration":
            suggest = "sns_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryNotificationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryNotificationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryNotificationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sns_configuration: 'outputs.ScheduledQuerySnsConfiguration'):
        """
        Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
        """
        pulumi.set(__self__, "sns_configuration", sns_configuration)

    @property
    @pulumi.getter(name="snsConfiguration")
    def sns_configuration(self) -> 'outputs.ScheduledQuerySnsConfiguration':
        return pulumi.get(self, "sns_configuration")


@pulumi.output_type
class ScheduledQueryS3Configuration(dict):
    """
    Details on S3 location for error reports that result from running a query.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"
        elif key == "encryptionOption":
            suggest = "encryption_option"
        elif key == "objectKeyPrefix":
            suggest = "object_key_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryS3Configuration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryS3Configuration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryS3Configuration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str,
                 encryption_option: Optional['ScheduledQueryEncryptionOption'] = None,
                 object_key_prefix: Optional[str] = None):
        """
        Details on S3 location for error reports that result from running a query.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        if encryption_option is not None:
            pulumi.set(__self__, "encryption_option", encryption_option)
        if object_key_prefix is not None:
            pulumi.set(__self__, "object_key_prefix", object_key_prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional['ScheduledQueryEncryptionOption']:
        return pulumi.get(self, "encryption_option")

    @property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[str]:
        return pulumi.get(self, "object_key_prefix")


@pulumi.output_type
class ScheduledQueryScheduleConfiguration(dict):
    """
    Configuration for when the scheduled query is executed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scheduleExpression":
            suggest = "schedule_expression"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryScheduleConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryScheduleConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryScheduleConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule_expression: str):
        """
        Configuration for when the scheduled query is executed.
        """
        pulumi.set(__self__, "schedule_expression", schedule_expression)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> str:
        return pulumi.get(self, "schedule_expression")


@pulumi.output_type
class ScheduledQuerySnsConfiguration(dict):
    """
    SNS configuration for notification upon scheduled query execution.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "topicArn":
            suggest = "topic_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQuerySnsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQuerySnsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQuerySnsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 topic_arn: str):
        """
        SNS configuration for notification upon scheduled query execution.
        """
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> str:
        return pulumi.get(self, "topic_arn")


@pulumi.output_type
class ScheduledQueryTag(dict):
    """
    A key-value pair to label the scheduled query.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to label the scheduled query.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class ScheduledQueryTargetConfiguration(dict):
    """
    Configuration of target store where scheduled query results are written to.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "timestreamConfiguration":
            suggest = "timestream_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryTargetConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryTargetConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryTargetConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 timestream_configuration: 'outputs.ScheduledQueryTimestreamConfiguration'):
        """
        Configuration of target store where scheduled query results are written to.
        """
        pulumi.set(__self__, "timestream_configuration", timestream_configuration)

    @property
    @pulumi.getter(name="timestreamConfiguration")
    def timestream_configuration(self) -> 'outputs.ScheduledQueryTimestreamConfiguration':
        return pulumi.get(self, "timestream_configuration")


@pulumi.output_type
class ScheduledQueryTimestreamConfiguration(dict):
    """
    Configuration needed to write data into the Timestream database and table.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "databaseName":
            suggest = "database_name"
        elif key == "dimensionMappings":
            suggest = "dimension_mappings"
        elif key == "tableName":
            suggest = "table_name"
        elif key == "timeColumn":
            suggest = "time_column"
        elif key == "measureNameColumn":
            suggest = "measure_name_column"
        elif key == "mixedMeasureMappings":
            suggest = "mixed_measure_mappings"
        elif key == "multiMeasureMappings":
            suggest = "multi_measure_mappings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduledQueryTimestreamConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduledQueryTimestreamConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduledQueryTimestreamConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 database_name: str,
                 dimension_mappings: Sequence['outputs.ScheduledQueryDimensionMapping'],
                 table_name: str,
                 time_column: str,
                 measure_name_column: Optional[str] = None,
                 mixed_measure_mappings: Optional[Sequence['outputs.ScheduledQueryMixedMeasureMapping']] = None,
                 multi_measure_mappings: Optional['outputs.ScheduledQueryMultiMeasureMappings'] = None):
        """
        Configuration needed to write data into the Timestream database and table.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "dimension_mappings", dimension_mappings)
        pulumi.set(__self__, "table_name", table_name)
        pulumi.set(__self__, "time_column", time_column)
        if measure_name_column is not None:
            pulumi.set(__self__, "measure_name_column", measure_name_column)
        if mixed_measure_mappings is not None:
            pulumi.set(__self__, "mixed_measure_mappings", mixed_measure_mappings)
        if multi_measure_mappings is not None:
            pulumi.set(__self__, "multi_measure_mappings", multi_measure_mappings)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="dimensionMappings")
    def dimension_mappings(self) -> Sequence['outputs.ScheduledQueryDimensionMapping']:
        return pulumi.get(self, "dimension_mappings")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> str:
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter(name="timeColumn")
    def time_column(self) -> str:
        return pulumi.get(self, "time_column")

    @property
    @pulumi.getter(name="measureNameColumn")
    def measure_name_column(self) -> Optional[str]:
        return pulumi.get(self, "measure_name_column")

    @property
    @pulumi.getter(name="mixedMeasureMappings")
    def mixed_measure_mappings(self) -> Optional[Sequence['outputs.ScheduledQueryMixedMeasureMapping']]:
        return pulumi.get(self, "mixed_measure_mappings")

    @property
    @pulumi.getter(name="multiMeasureMappings")
    def multi_measure_mappings(self) -> Optional['outputs.ScheduledQueryMultiMeasureMappings']:
        return pulumi.get(self, "multi_measure_mappings")


@pulumi.output_type
class SchemaProperties(dict):
    """
    A Schema specifies the expected data model of the table.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "compositePartitionKey":
            suggest = "composite_partition_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SchemaProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SchemaProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SchemaProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 composite_partition_key: Optional[Sequence['outputs.TablePartitionKey']] = None):
        """
        A Schema specifies the expected data model of the table.
        """
        if composite_partition_key is not None:
            pulumi.set(__self__, "composite_partition_key", composite_partition_key)

    @property
    @pulumi.getter(name="compositePartitionKey")
    def composite_partition_key(self) -> Optional[Sequence['outputs.TablePartitionKey']]:
        return pulumi.get(self, "composite_partition_key")


@pulumi.output_type
class TablePartitionKey(dict):
    """
    An attribute used in partitioning data in a table. There are two types of partition keys: dimension keys and measure keys. A dimension key partitions data on a dimension name, while a measure key partitions data on the measure name.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enforcementInRecord":
            suggest = "enforcement_in_record"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TablePartitionKey. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TablePartitionKey.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TablePartitionKey.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'TablePartitionKeyType',
                 enforcement_in_record: Optional['TablePartitionKeyEnforcementLevel'] = None,
                 name: Optional[str] = None):
        """
        An attribute used in partitioning data in a table. There are two types of partition keys: dimension keys and measure keys. A dimension key partitions data on a dimension name, while a measure key partitions data on the measure name.
        """
        pulumi.set(__self__, "type", type)
        if enforcement_in_record is not None:
            pulumi.set(__self__, "enforcement_in_record", enforcement_in_record)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def type(self) -> 'TablePartitionKeyType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="enforcementInRecord")
    def enforcement_in_record(self) -> Optional['TablePartitionKeyEnforcementLevel']:
        return pulumi.get(self, "enforcement_in_record")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


@pulumi.output_type
class TableTag(dict):
    """
    You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
    """
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        """
        You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


