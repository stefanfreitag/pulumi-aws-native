# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GlobalTableAttributeDefinition',
    'GlobalTableCapacityAutoScalingSettings',
    'GlobalTableContributorInsightsSpecification',
    'GlobalTableGlobalSecondaryIndex',
    'GlobalTableKeySchema',
    'GlobalTableLocalSecondaryIndex',
    'GlobalTablePointInTimeRecoverySpecification',
    'GlobalTableProjection',
    'GlobalTableReadProvisionedThroughputSettings',
    'GlobalTableReplicaGlobalSecondaryIndexSpecification',
    'GlobalTableReplicaSSESpecification',
    'GlobalTableReplicaSpecification',
    'GlobalTableSSESpecification',
    'GlobalTableStreamSpecification',
    'GlobalTableTag',
    'GlobalTableTargetTrackingScalingPolicyConfiguration',
    'GlobalTableTimeToLiveSpecification',
    'GlobalTableWriteProvisionedThroughputSettings',
]

@pulumi.output_type
class GlobalTableAttributeDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attributeName":
            suggest = "attribute_name"
        elif key == "attributeType":
            suggest = "attribute_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableAttributeDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableAttributeDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableAttributeDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attribute_name: str,
                 attribute_type: str):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "attribute_type", attribute_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> str:
        return pulumi.get(self, "attribute_name")

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> str:
        return pulumi.get(self, "attribute_type")


@pulumi.output_type
class GlobalTableCapacityAutoScalingSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxCapacity":
            suggest = "max_capacity"
        elif key == "minCapacity":
            suggest = "min_capacity"
        elif key == "targetTrackingScalingPolicyConfiguration":
            suggest = "target_tracking_scaling_policy_configuration"
        elif key == "seedCapacity":
            suggest = "seed_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableCapacityAutoScalingSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableCapacityAutoScalingSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableCapacityAutoScalingSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_capacity: int,
                 min_capacity: int,
                 target_tracking_scaling_policy_configuration: 'outputs.GlobalTableTargetTrackingScalingPolicyConfiguration',
                 seed_capacity: Optional[int] = None):
        pulumi.set(__self__, "max_capacity", max_capacity)
        pulumi.set(__self__, "min_capacity", min_capacity)
        pulumi.set(__self__, "target_tracking_scaling_policy_configuration", target_tracking_scaling_policy_configuration)
        if seed_capacity is not None:
            pulumi.set(__self__, "seed_capacity", seed_capacity)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> int:
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> int:
        return pulumi.get(self, "min_capacity")

    @property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(self) -> 'outputs.GlobalTableTargetTrackingScalingPolicyConfiguration':
        return pulumi.get(self, "target_tracking_scaling_policy_configuration")

    @property
    @pulumi.getter(name="seedCapacity")
    def seed_capacity(self) -> Optional[int]:
        return pulumi.get(self, "seed_capacity")


@pulumi.output_type
class GlobalTableContributorInsightsSpecification(dict):
    def __init__(__self__, *,
                 enabled: bool):
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")


@pulumi.output_type
class GlobalTableGlobalSecondaryIndex(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "indexName":
            suggest = "index_name"
        elif key == "keySchema":
            suggest = "key_schema"
        elif key == "writeProvisionedThroughputSettings":
            suggest = "write_provisioned_throughput_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableGlobalSecondaryIndex. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableGlobalSecondaryIndex.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableGlobalSecondaryIndex.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 index_name: str,
                 key_schema: Sequence['outputs.GlobalTableKeySchema'],
                 projection: 'outputs.GlobalTableProjection',
                 write_provisioned_throughput_settings: Optional['outputs.GlobalTableWriteProvisionedThroughputSettings'] = None):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)
        if write_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "write_provisioned_throughput_settings", write_provisioned_throughput_settings)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> str:
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> Sequence['outputs.GlobalTableKeySchema']:
        return pulumi.get(self, "key_schema")

    @property
    @pulumi.getter
    def projection(self) -> 'outputs.GlobalTableProjection':
        return pulumi.get(self, "projection")

    @property
    @pulumi.getter(name="writeProvisionedThroughputSettings")
    def write_provisioned_throughput_settings(self) -> Optional['outputs.GlobalTableWriteProvisionedThroughputSettings']:
        return pulumi.get(self, "write_provisioned_throughput_settings")


@pulumi.output_type
class GlobalTableKeySchema(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attributeName":
            suggest = "attribute_name"
        elif key == "keyType":
            suggest = "key_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableKeySchema. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableKeySchema.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableKeySchema.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attribute_name: str,
                 key_type: str):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "key_type", key_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> str:
        return pulumi.get(self, "attribute_name")

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> str:
        return pulumi.get(self, "key_type")


@pulumi.output_type
class GlobalTableLocalSecondaryIndex(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "indexName":
            suggest = "index_name"
        elif key == "keySchema":
            suggest = "key_schema"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableLocalSecondaryIndex. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableLocalSecondaryIndex.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableLocalSecondaryIndex.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 index_name: str,
                 key_schema: Sequence['outputs.GlobalTableKeySchema'],
                 projection: 'outputs.GlobalTableProjection'):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> str:
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> Sequence['outputs.GlobalTableKeySchema']:
        return pulumi.get(self, "key_schema")

    @property
    @pulumi.getter
    def projection(self) -> 'outputs.GlobalTableProjection':
        return pulumi.get(self, "projection")


@pulumi.output_type
class GlobalTablePointInTimeRecoverySpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pointInTimeRecoveryEnabled":
            suggest = "point_in_time_recovery_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTablePointInTimeRecoverySpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTablePointInTimeRecoverySpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTablePointInTimeRecoverySpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 point_in_time_recovery_enabled: Optional[bool] = None):
        if point_in_time_recovery_enabled is not None:
            pulumi.set(__self__, "point_in_time_recovery_enabled", point_in_time_recovery_enabled)

    @property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "point_in_time_recovery_enabled")


@pulumi.output_type
class GlobalTableProjection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nonKeyAttributes":
            suggest = "non_key_attributes"
        elif key == "projectionType":
            suggest = "projection_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableProjection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableProjection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableProjection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 non_key_attributes: Optional[Sequence[str]] = None,
                 projection_type: Optional[str] = None):
        if non_key_attributes is not None:
            pulumi.set(__self__, "non_key_attributes", non_key_attributes)
        if projection_type is not None:
            pulumi.set(__self__, "projection_type", projection_type)

    @property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "non_key_attributes")

    @property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> Optional[str]:
        return pulumi.get(self, "projection_type")


@pulumi.output_type
class GlobalTableReadProvisionedThroughputSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "readCapacityAutoScalingSettings":
            suggest = "read_capacity_auto_scaling_settings"
        elif key == "readCapacityUnits":
            suggest = "read_capacity_units"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableReadProvisionedThroughputSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableReadProvisionedThroughputSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableReadProvisionedThroughputSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 read_capacity_auto_scaling_settings: Optional['outputs.GlobalTableCapacityAutoScalingSettings'] = None,
                 read_capacity_units: Optional[int] = None):
        if read_capacity_auto_scaling_settings is not None:
            pulumi.set(__self__, "read_capacity_auto_scaling_settings", read_capacity_auto_scaling_settings)
        if read_capacity_units is not None:
            pulumi.set(__self__, "read_capacity_units", read_capacity_units)

    @property
    @pulumi.getter(name="readCapacityAutoScalingSettings")
    def read_capacity_auto_scaling_settings(self) -> Optional['outputs.GlobalTableCapacityAutoScalingSettings']:
        return pulumi.get(self, "read_capacity_auto_scaling_settings")

    @property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[int]:
        return pulumi.get(self, "read_capacity_units")


@pulumi.output_type
class GlobalTableReplicaGlobalSecondaryIndexSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "indexName":
            suggest = "index_name"
        elif key == "contributorInsightsSpecification":
            suggest = "contributor_insights_specification"
        elif key == "readProvisionedThroughputSettings":
            suggest = "read_provisioned_throughput_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableReplicaGlobalSecondaryIndexSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableReplicaGlobalSecondaryIndexSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableReplicaGlobalSecondaryIndexSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 index_name: str,
                 contributor_insights_specification: Optional['outputs.GlobalTableContributorInsightsSpecification'] = None,
                 read_provisioned_throughput_settings: Optional['outputs.GlobalTableReadProvisionedThroughputSettings'] = None):
        pulumi.set(__self__, "index_name", index_name)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if read_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "read_provisioned_throughput_settings", read_provisioned_throughput_settings)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> str:
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional['outputs.GlobalTableContributorInsightsSpecification']:
        return pulumi.get(self, "contributor_insights_specification")

    @property
    @pulumi.getter(name="readProvisionedThroughputSettings")
    def read_provisioned_throughput_settings(self) -> Optional['outputs.GlobalTableReadProvisionedThroughputSettings']:
        return pulumi.get(self, "read_provisioned_throughput_settings")


@pulumi.output_type
class GlobalTableReplicaSSESpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kMSMasterKeyId":
            suggest = "k_ms_master_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableReplicaSSESpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableReplicaSSESpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableReplicaSSESpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 k_ms_master_key_id: str):
        pulumi.set(__self__, "k_ms_master_key_id", k_ms_master_key_id)

    @property
    @pulumi.getter(name="kMSMasterKeyId")
    def k_ms_master_key_id(self) -> str:
        return pulumi.get(self, "k_ms_master_key_id")


@pulumi.output_type
class GlobalTableReplicaSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contributorInsightsSpecification":
            suggest = "contributor_insights_specification"
        elif key == "globalSecondaryIndexes":
            suggest = "global_secondary_indexes"
        elif key == "pointInTimeRecoverySpecification":
            suggest = "point_in_time_recovery_specification"
        elif key == "readProvisionedThroughputSettings":
            suggest = "read_provisioned_throughput_settings"
        elif key == "sSESpecification":
            suggest = "s_se_specification"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableReplicaSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableReplicaSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableReplicaSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 region: str,
                 contributor_insights_specification: Optional['outputs.GlobalTableContributorInsightsSpecification'] = None,
                 global_secondary_indexes: Optional[Sequence['outputs.GlobalTableReplicaGlobalSecondaryIndexSpecification']] = None,
                 point_in_time_recovery_specification: Optional['outputs.GlobalTablePointInTimeRecoverySpecification'] = None,
                 read_provisioned_throughput_settings: Optional['outputs.GlobalTableReadProvisionedThroughputSettings'] = None,
                 s_se_specification: Optional['outputs.GlobalTableReplicaSSESpecification'] = None,
                 tags: Optional[Sequence['outputs.GlobalTableTag']] = None):
        pulumi.set(__self__, "region", region)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if global_secondary_indexes is not None:
            pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if point_in_time_recovery_specification is not None:
            pulumi.set(__self__, "point_in_time_recovery_specification", point_in_time_recovery_specification)
        if read_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "read_provisioned_throughput_settings", read_provisioned_throughput_settings)
        if s_se_specification is not None:
            pulumi.set(__self__, "s_se_specification", s_se_specification)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional['outputs.GlobalTableContributorInsightsSpecification']:
        return pulumi.get(self, "contributor_insights_specification")

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[Sequence['outputs.GlobalTableReplicaGlobalSecondaryIndexSpecification']]:
        return pulumi.get(self, "global_secondary_indexes")

    @property
    @pulumi.getter(name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> Optional['outputs.GlobalTablePointInTimeRecoverySpecification']:
        return pulumi.get(self, "point_in_time_recovery_specification")

    @property
    @pulumi.getter(name="readProvisionedThroughputSettings")
    def read_provisioned_throughput_settings(self) -> Optional['outputs.GlobalTableReadProvisionedThroughputSettings']:
        return pulumi.get(self, "read_provisioned_throughput_settings")

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> Optional['outputs.GlobalTableReplicaSSESpecification']:
        return pulumi.get(self, "s_se_specification")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GlobalTableTag']]:
        return pulumi.get(self, "tags")


@pulumi.output_type
class GlobalTableSSESpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sSEEnabled":
            suggest = "s_se_enabled"
        elif key == "sSEType":
            suggest = "s_se_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableSSESpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableSSESpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableSSESpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 s_se_enabled: bool,
                 s_se_type: Optional[str] = None):
        pulumi.set(__self__, "s_se_enabled", s_se_enabled)
        if s_se_type is not None:
            pulumi.set(__self__, "s_se_type", s_se_type)

    @property
    @pulumi.getter(name="sSEEnabled")
    def s_se_enabled(self) -> bool:
        return pulumi.get(self, "s_se_enabled")

    @property
    @pulumi.getter(name="sSEType")
    def s_se_type(self) -> Optional[str]:
        return pulumi.get(self, "s_se_type")


@pulumi.output_type
class GlobalTableStreamSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "streamViewType":
            suggest = "stream_view_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableStreamSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableStreamSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableStreamSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stream_view_type: str):
        pulumi.set(__self__, "stream_view_type", stream_view_type)

    @property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> str:
        return pulumi.get(self, "stream_view_type")


@pulumi.output_type
class GlobalTableTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
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
class GlobalTableTargetTrackingScalingPolicyConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetValue":
            suggest = "target_value"
        elif key == "disableScaleIn":
            suggest = "disable_scale_in"
        elif key == "scaleInCooldown":
            suggest = "scale_in_cooldown"
        elif key == "scaleOutCooldown":
            suggest = "scale_out_cooldown"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableTargetTrackingScalingPolicyConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableTargetTrackingScalingPolicyConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableTargetTrackingScalingPolicyConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_value: float,
                 disable_scale_in: Optional[bool] = None,
                 scale_in_cooldown: Optional[int] = None,
                 scale_out_cooldown: Optional[int] = None):
        pulumi.set(__self__, "target_value", target_value)
        if disable_scale_in is not None:
            pulumi.set(__self__, "disable_scale_in", disable_scale_in)
        if scale_in_cooldown is not None:
            pulumi.set(__self__, "scale_in_cooldown", scale_in_cooldown)
        if scale_out_cooldown is not None:
            pulumi.set(__self__, "scale_out_cooldown", scale_out_cooldown)

    @property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> float:
        return pulumi.get(self, "target_value")

    @property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[bool]:
        return pulumi.get(self, "disable_scale_in")

    @property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[int]:
        return pulumi.get(self, "scale_in_cooldown")

    @property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[int]:
        return pulumi.get(self, "scale_out_cooldown")


@pulumi.output_type
class GlobalTableTimeToLiveSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attributeName":
            suggest = "attribute_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableTimeToLiveSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableTimeToLiveSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableTimeToLiveSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 attribute_name: Optional[str] = None):
        pulumi.set(__self__, "enabled", enabled)
        if attribute_name is not None:
            pulumi.set(__self__, "attribute_name", attribute_name)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[str]:
        return pulumi.get(self, "attribute_name")


@pulumi.output_type
class GlobalTableWriteProvisionedThroughputSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "writeCapacityAutoScalingSettings":
            suggest = "write_capacity_auto_scaling_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GlobalTableWriteProvisionedThroughputSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GlobalTableWriteProvisionedThroughputSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GlobalTableWriteProvisionedThroughputSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 write_capacity_auto_scaling_settings: Optional['outputs.GlobalTableCapacityAutoScalingSettings'] = None):
        if write_capacity_auto_scaling_settings is not None:
            pulumi.set(__self__, "write_capacity_auto_scaling_settings", write_capacity_auto_scaling_settings)

    @property
    @pulumi.getter(name="writeCapacityAutoScalingSettings")
    def write_capacity_auto_scaling_settings(self) -> Optional['outputs.GlobalTableCapacityAutoScalingSettings']:
        return pulumi.get(self, "write_capacity_auto_scaling_settings")


