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
    'ScalingPlanApplicationSource',
    'ScalingPlanCustomizedLoadMetricSpecification',
    'ScalingPlanCustomizedScalingMetricSpecification',
    'ScalingPlanMetricDimension',
    'ScalingPlanPredefinedLoadMetricSpecification',
    'ScalingPlanPredefinedScalingMetricSpecification',
    'ScalingPlanScalingInstruction',
    'ScalingPlanTagFilter',
    'ScalingPlanTargetTrackingConfiguration',
]

@pulumi.output_type
class ScalingPlanApplicationSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudFormationStackARN":
            suggest = "cloud_formation_stack_arn"
        elif key == "tagFilters":
            suggest = "tag_filters"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanApplicationSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanApplicationSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanApplicationSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_formation_stack_arn: Optional[str] = None,
                 tag_filters: Optional[Sequence['outputs.ScalingPlanTagFilter']] = None):
        if cloud_formation_stack_arn is not None:
            pulumi.set(__self__, "cloud_formation_stack_arn", cloud_formation_stack_arn)
        if tag_filters is not None:
            pulumi.set(__self__, "tag_filters", tag_filters)

    @property
    @pulumi.getter(name="cloudFormationStackARN")
    def cloud_formation_stack_arn(self) -> Optional[str]:
        return pulumi.get(self, "cloud_formation_stack_arn")

    @property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[Sequence['outputs.ScalingPlanTagFilter']]:
        return pulumi.get(self, "tag_filters")


@pulumi.output_type
class ScalingPlanCustomizedLoadMetricSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "metricName":
            suggest = "metric_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanCustomizedLoadMetricSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanCustomizedLoadMetricSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanCustomizedLoadMetricSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 metric_name: str,
                 namespace: str,
                 statistic: str,
                 dimensions: Optional[Sequence['outputs.ScalingPlanMetricDimension']] = None,
                 unit: Optional[str] = None):
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "statistic", statistic)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def statistic(self) -> str:
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.ScalingPlanMetricDimension']]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        return pulumi.get(self, "unit")


@pulumi.output_type
class ScalingPlanCustomizedScalingMetricSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "metricName":
            suggest = "metric_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanCustomizedScalingMetricSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanCustomizedScalingMetricSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanCustomizedScalingMetricSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 metric_name: str,
                 namespace: str,
                 statistic: str,
                 dimensions: Optional[Sequence['outputs.ScalingPlanMetricDimension']] = None,
                 unit: Optional[str] = None):
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "statistic", statistic)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def statistic(self) -> str:
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.ScalingPlanMetricDimension']]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        return pulumi.get(self, "unit")


@pulumi.output_type
class ScalingPlanMetricDimension(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class ScalingPlanPredefinedLoadMetricSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "predefinedLoadMetricType":
            suggest = "predefined_load_metric_type"
        elif key == "resourceLabel":
            suggest = "resource_label"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanPredefinedLoadMetricSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanPredefinedLoadMetricSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanPredefinedLoadMetricSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 predefined_load_metric_type: str,
                 resource_label: Optional[str] = None):
        pulumi.set(__self__, "predefined_load_metric_type", predefined_load_metric_type)
        if resource_label is not None:
            pulumi.set(__self__, "resource_label", resource_label)

    @property
    @pulumi.getter(name="predefinedLoadMetricType")
    def predefined_load_metric_type(self) -> str:
        return pulumi.get(self, "predefined_load_metric_type")

    @property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[str]:
        return pulumi.get(self, "resource_label")


@pulumi.output_type
class ScalingPlanPredefinedScalingMetricSpecification(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "predefinedScalingMetricType":
            suggest = "predefined_scaling_metric_type"
        elif key == "resourceLabel":
            suggest = "resource_label"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanPredefinedScalingMetricSpecification. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanPredefinedScalingMetricSpecification.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanPredefinedScalingMetricSpecification.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 predefined_scaling_metric_type: str,
                 resource_label: Optional[str] = None):
        pulumi.set(__self__, "predefined_scaling_metric_type", predefined_scaling_metric_type)
        if resource_label is not None:
            pulumi.set(__self__, "resource_label", resource_label)

    @property
    @pulumi.getter(name="predefinedScalingMetricType")
    def predefined_scaling_metric_type(self) -> str:
        return pulumi.get(self, "predefined_scaling_metric_type")

    @property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[str]:
        return pulumi.get(self, "resource_label")


@pulumi.output_type
class ScalingPlanScalingInstruction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxCapacity":
            suggest = "max_capacity"
        elif key == "minCapacity":
            suggest = "min_capacity"
        elif key == "resourceId":
            suggest = "resource_id"
        elif key == "scalableDimension":
            suggest = "scalable_dimension"
        elif key == "serviceNamespace":
            suggest = "service_namespace"
        elif key == "targetTrackingConfigurations":
            suggest = "target_tracking_configurations"
        elif key == "customizedLoadMetricSpecification":
            suggest = "customized_load_metric_specification"
        elif key == "disableDynamicScaling":
            suggest = "disable_dynamic_scaling"
        elif key == "predefinedLoadMetricSpecification":
            suggest = "predefined_load_metric_specification"
        elif key == "predictiveScalingMaxCapacityBehavior":
            suggest = "predictive_scaling_max_capacity_behavior"
        elif key == "predictiveScalingMaxCapacityBuffer":
            suggest = "predictive_scaling_max_capacity_buffer"
        elif key == "predictiveScalingMode":
            suggest = "predictive_scaling_mode"
        elif key == "scalingPolicyUpdateBehavior":
            suggest = "scaling_policy_update_behavior"
        elif key == "scheduledActionBufferTime":
            suggest = "scheduled_action_buffer_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanScalingInstruction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanScalingInstruction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanScalingInstruction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_capacity: int,
                 min_capacity: int,
                 resource_id: str,
                 scalable_dimension: str,
                 service_namespace: str,
                 target_tracking_configurations: Sequence['outputs.ScalingPlanTargetTrackingConfiguration'],
                 customized_load_metric_specification: Optional['outputs.ScalingPlanCustomizedLoadMetricSpecification'] = None,
                 disable_dynamic_scaling: Optional[bool] = None,
                 predefined_load_metric_specification: Optional['outputs.ScalingPlanPredefinedLoadMetricSpecification'] = None,
                 predictive_scaling_max_capacity_behavior: Optional[str] = None,
                 predictive_scaling_max_capacity_buffer: Optional[int] = None,
                 predictive_scaling_mode: Optional[str] = None,
                 scaling_policy_update_behavior: Optional[str] = None,
                 scheduled_action_buffer_time: Optional[int] = None):
        pulumi.set(__self__, "max_capacity", max_capacity)
        pulumi.set(__self__, "min_capacity", min_capacity)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "scalable_dimension", scalable_dimension)
        pulumi.set(__self__, "service_namespace", service_namespace)
        pulumi.set(__self__, "target_tracking_configurations", target_tracking_configurations)
        if customized_load_metric_specification is not None:
            pulumi.set(__self__, "customized_load_metric_specification", customized_load_metric_specification)
        if disable_dynamic_scaling is not None:
            pulumi.set(__self__, "disable_dynamic_scaling", disable_dynamic_scaling)
        if predefined_load_metric_specification is not None:
            pulumi.set(__self__, "predefined_load_metric_specification", predefined_load_metric_specification)
        if predictive_scaling_max_capacity_behavior is not None:
            pulumi.set(__self__, "predictive_scaling_max_capacity_behavior", predictive_scaling_max_capacity_behavior)
        if predictive_scaling_max_capacity_buffer is not None:
            pulumi.set(__self__, "predictive_scaling_max_capacity_buffer", predictive_scaling_max_capacity_buffer)
        if predictive_scaling_mode is not None:
            pulumi.set(__self__, "predictive_scaling_mode", predictive_scaling_mode)
        if scaling_policy_update_behavior is not None:
            pulumi.set(__self__, "scaling_policy_update_behavior", scaling_policy_update_behavior)
        if scheduled_action_buffer_time is not None:
            pulumi.set(__self__, "scheduled_action_buffer_time", scheduled_action_buffer_time)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> int:
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> int:
        return pulumi.get(self, "min_capacity")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> str:
        return pulumi.get(self, "scalable_dimension")

    @property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> str:
        return pulumi.get(self, "service_namespace")

    @property
    @pulumi.getter(name="targetTrackingConfigurations")
    def target_tracking_configurations(self) -> Sequence['outputs.ScalingPlanTargetTrackingConfiguration']:
        return pulumi.get(self, "target_tracking_configurations")

    @property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(self) -> Optional['outputs.ScalingPlanCustomizedLoadMetricSpecification']:
        return pulumi.get(self, "customized_load_metric_specification")

    @property
    @pulumi.getter(name="disableDynamicScaling")
    def disable_dynamic_scaling(self) -> Optional[bool]:
        return pulumi.get(self, "disable_dynamic_scaling")

    @property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(self) -> Optional['outputs.ScalingPlanPredefinedLoadMetricSpecification']:
        return pulumi.get(self, "predefined_load_metric_specification")

    @property
    @pulumi.getter(name="predictiveScalingMaxCapacityBehavior")
    def predictive_scaling_max_capacity_behavior(self) -> Optional[str]:
        return pulumi.get(self, "predictive_scaling_max_capacity_behavior")

    @property
    @pulumi.getter(name="predictiveScalingMaxCapacityBuffer")
    def predictive_scaling_max_capacity_buffer(self) -> Optional[int]:
        return pulumi.get(self, "predictive_scaling_max_capacity_buffer")

    @property
    @pulumi.getter(name="predictiveScalingMode")
    def predictive_scaling_mode(self) -> Optional[str]:
        return pulumi.get(self, "predictive_scaling_mode")

    @property
    @pulumi.getter(name="scalingPolicyUpdateBehavior")
    def scaling_policy_update_behavior(self) -> Optional[str]:
        return pulumi.get(self, "scaling_policy_update_behavior")

    @property
    @pulumi.getter(name="scheduledActionBufferTime")
    def scheduled_action_buffer_time(self) -> Optional[int]:
        return pulumi.get(self, "scheduled_action_buffer_time")


@pulumi.output_type
class ScalingPlanTagFilter(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "key", key)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "values")


@pulumi.output_type
class ScalingPlanTargetTrackingConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetValue":
            suggest = "target_value"
        elif key == "customizedScalingMetricSpecification":
            suggest = "customized_scaling_metric_specification"
        elif key == "disableScaleIn":
            suggest = "disable_scale_in"
        elif key == "estimatedInstanceWarmup":
            suggest = "estimated_instance_warmup"
        elif key == "predefinedScalingMetricSpecification":
            suggest = "predefined_scaling_metric_specification"
        elif key == "scaleInCooldown":
            suggest = "scale_in_cooldown"
        elif key == "scaleOutCooldown":
            suggest = "scale_out_cooldown"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanTargetTrackingConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanTargetTrackingConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanTargetTrackingConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_value: float,
                 customized_scaling_metric_specification: Optional['outputs.ScalingPlanCustomizedScalingMetricSpecification'] = None,
                 disable_scale_in: Optional[bool] = None,
                 estimated_instance_warmup: Optional[int] = None,
                 predefined_scaling_metric_specification: Optional['outputs.ScalingPlanPredefinedScalingMetricSpecification'] = None,
                 scale_in_cooldown: Optional[int] = None,
                 scale_out_cooldown: Optional[int] = None):
        pulumi.set(__self__, "target_value", target_value)
        if customized_scaling_metric_specification is not None:
            pulumi.set(__self__, "customized_scaling_metric_specification", customized_scaling_metric_specification)
        if disable_scale_in is not None:
            pulumi.set(__self__, "disable_scale_in", disable_scale_in)
        if estimated_instance_warmup is not None:
            pulumi.set(__self__, "estimated_instance_warmup", estimated_instance_warmup)
        if predefined_scaling_metric_specification is not None:
            pulumi.set(__self__, "predefined_scaling_metric_specification", predefined_scaling_metric_specification)
        if scale_in_cooldown is not None:
            pulumi.set(__self__, "scale_in_cooldown", scale_in_cooldown)
        if scale_out_cooldown is not None:
            pulumi.set(__self__, "scale_out_cooldown", scale_out_cooldown)

    @property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> float:
        return pulumi.get(self, "target_value")

    @property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(self) -> Optional['outputs.ScalingPlanCustomizedScalingMetricSpecification']:
        return pulumi.get(self, "customized_scaling_metric_specification")

    @property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[bool]:
        return pulumi.get(self, "disable_scale_in")

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[int]:
        return pulumi.get(self, "estimated_instance_warmup")

    @property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(self) -> Optional['outputs.ScalingPlanPredefinedScalingMetricSpecification']:
        return pulumi.get(self, "predefined_scaling_metric_specification")

    @property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[int]:
        return pulumi.get(self, "scale_in_cooldown")

    @property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[int]:
        return pulumi.get(self, "scale_out_cooldown")


