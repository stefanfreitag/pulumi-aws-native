# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'EventBusPolicyConditionArgs',
    'RuleAwsVpcConfigurationArgs',
    'RuleBatchArrayPropertiesArgs',
    'RuleBatchParametersArgs',
    'RuleBatchRetryStrategyArgs',
    'RuleCapacityProviderStrategyItemArgs',
    'RuleDeadLetterConfigArgs',
    'RuleEcsParametersArgs',
    'RuleHttpParametersArgs',
    'RuleInputTransformerArgs',
    'RuleKinesisParametersArgs',
    'RuleNetworkConfigurationArgs',
    'RulePlacementConstraintArgs',
    'RulePlacementStrategyArgs',
    'RuleRedshiftDataParametersArgs',
    'RuleRetryPolicyArgs',
    'RuleRunCommandParametersArgs',
    'RuleRunCommandTargetArgs',
    'RuleSqsParametersArgs',
    'RuleTagArgs',
    'RuleTargetArgs',
]

@pulumi.input_type
class EventBusPolicyConditionArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RuleAwsVpcConfigurationArgs:
    def __init__(__self__, *,
                 subnets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 assign_public_ip: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "subnets", subnets)
        if assign_public_ip is not None:
            pulumi.set(__self__, "assign_public_ip", assign_public_ip)
        if security_groups is not None:
            pulumi.set(__self__, "security_groups", security_groups)

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "assign_public_ip")

    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assign_public_ip", value)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_groups", value)


@pulumi.input_type
class RuleBatchArrayPropertiesArgs:
    def __init__(__self__, *,
                 size: Optional[pulumi.Input[int]] = None):
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class RuleBatchParametersArgs:
    def __init__(__self__, *,
                 job_definition: pulumi.Input[str],
                 job_name: pulumi.Input[str],
                 array_properties: Optional[pulumi.Input['RuleBatchArrayPropertiesArgs']] = None,
                 retry_strategy: Optional[pulumi.Input['RuleBatchRetryStrategyArgs']] = None):
        pulumi.set(__self__, "job_definition", job_definition)
        pulumi.set(__self__, "job_name", job_name)
        if array_properties is not None:
            pulumi.set(__self__, "array_properties", array_properties)
        if retry_strategy is not None:
            pulumi.set(__self__, "retry_strategy", retry_strategy)

    @property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> pulumi.Input[str]:
        return pulumi.get(self, "job_definition")

    @job_definition.setter
    def job_definition(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_definition", value)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter(name="arrayProperties")
    def array_properties(self) -> Optional[pulumi.Input['RuleBatchArrayPropertiesArgs']]:
        return pulumi.get(self, "array_properties")

    @array_properties.setter
    def array_properties(self, value: Optional[pulumi.Input['RuleBatchArrayPropertiesArgs']]):
        pulumi.set(self, "array_properties", value)

    @property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional[pulumi.Input['RuleBatchRetryStrategyArgs']]:
        return pulumi.get(self, "retry_strategy")

    @retry_strategy.setter
    def retry_strategy(self, value: Optional[pulumi.Input['RuleBatchRetryStrategyArgs']]):
        pulumi.set(self, "retry_strategy", value)


@pulumi.input_type
class RuleBatchRetryStrategyArgs:
    def __init__(__self__, *,
                 attempts: Optional[pulumi.Input[int]] = None):
        if attempts is not None:
            pulumi.set(__self__, "attempts", attempts)

    @property
    @pulumi.getter
    def attempts(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "attempts")

    @attempts.setter
    def attempts(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "attempts", value)


@pulumi.input_type
class RuleCapacityProviderStrategyItemArgs:
    def __init__(__self__, *,
                 capacity_provider: pulumi.Input[str],
                 base: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "capacity_provider", capacity_provider)
        if base is not None:
            pulumi.set(__self__, "base", base)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[str]:
        return pulumi.get(self, "capacity_provider")

    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "capacity_provider", value)

    @property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "base")

    @base.setter
    def base(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "base", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class RuleDeadLetterConfigArgs:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None):
        if arn is not None:
            pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)


@pulumi.input_type
class RuleEcsParametersArgs:
    def __init__(__self__, *,
                 task_definition_arn: pulumi.Input[str],
                 capacity_provider_strategy: Optional[pulumi.Input[Sequence[pulumi.Input['RuleCapacityProviderStrategyItemArgs']]]] = None,
                 enable_ecs_managed_tags: Optional[pulumi.Input[bool]] = None,
                 enable_execute_command: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 launch_type: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input['RuleNetworkConfigurationArgs']] = None,
                 placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementConstraintArgs']]]] = None,
                 placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementStrategyArgs']]]] = None,
                 platform_version: Optional[pulumi.Input[str]] = None,
                 propagate_tags: Optional[pulumi.Input[str]] = None,
                 reference_id: Optional[pulumi.Input[str]] = None,
                 tag_list: Optional[pulumi.Input[Sequence[pulumi.Input['RuleTagArgs']]]] = None,
                 task_count: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "task_definition_arn", task_definition_arn)
        if capacity_provider_strategy is not None:
            pulumi.set(__self__, "capacity_provider_strategy", capacity_provider_strategy)
        if enable_ecs_managed_tags is not None:
            pulumi.set(__self__, "enable_ecs_managed_tags", enable_ecs_managed_tags)
        if enable_execute_command is not None:
            pulumi.set(__self__, "enable_execute_command", enable_execute_command)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if launch_type is not None:
            pulumi.set(__self__, "launch_type", launch_type)
        if network_configuration is not None:
            pulumi.set(__self__, "network_configuration", network_configuration)
        if placement_constraints is not None:
            pulumi.set(__self__, "placement_constraints", placement_constraints)
        if placement_strategies is not None:
            pulumi.set(__self__, "placement_strategies", placement_strategies)
        if platform_version is not None:
            pulumi.set(__self__, "platform_version", platform_version)
        if propagate_tags is not None:
            pulumi.set(__self__, "propagate_tags", propagate_tags)
        if reference_id is not None:
            pulumi.set(__self__, "reference_id", reference_id)
        if tag_list is not None:
            pulumi.set(__self__, "tag_list", tag_list)
        if task_count is not None:
            pulumi.set(__self__, "task_count", task_count)

    @property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "task_definition_arn")

    @task_definition_arn.setter
    def task_definition_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "task_definition_arn", value)

    @property
    @pulumi.getter(name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RuleCapacityProviderStrategyItemArgs']]]]:
        return pulumi.get(self, "capacity_provider_strategy")

    @capacity_provider_strategy.setter
    def capacity_provider_strategy(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RuleCapacityProviderStrategyItemArgs']]]]):
        pulumi.set(self, "capacity_provider_strategy", value)

    @property
    @pulumi.getter(name="enableECSManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_ecs_managed_tags")

    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ecs_managed_tags", value)

    @property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_execute_command")

    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_execute_command", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "launch_type")

    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_type", value)

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input['RuleNetworkConfigurationArgs']]:
        return pulumi.get(self, "network_configuration")

    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input['RuleNetworkConfigurationArgs']]):
        pulumi.set(self, "network_configuration", value)

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementConstraintArgs']]]]:
        return pulumi.get(self, "placement_constraints")

    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementConstraintArgs']]]]):
        pulumi.set(self, "placement_constraints", value)

    @property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementStrategyArgs']]]]:
        return pulumi.get(self, "placement_strategies")

    @placement_strategies.setter
    def placement_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulePlacementStrategyArgs']]]]):
        pulumi.set(self, "placement_strategies", value)

    @property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "platform_version")

    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform_version", value)

    @property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "propagate_tags")

    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "propagate_tags", value)

    @property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reference_id")

    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reference_id", value)

    @property
    @pulumi.getter(name="tagList")
    def tag_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RuleTagArgs']]]]:
        return pulumi.get(self, "tag_list")

    @tag_list.setter
    def tag_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RuleTagArgs']]]]):
        pulumi.set(self, "tag_list", value)

    @property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "task_count")

    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "task_count", value)


@pulumi.input_type
class RuleHttpParametersArgs:
    def __init__(__self__, *,
                 header_parameters: Optional[Any] = None,
                 path_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 query_string_parameters: Optional[Any] = None):
        if header_parameters is not None:
            pulumi.set(__self__, "header_parameters", header_parameters)
        if path_parameter_values is not None:
            pulumi.set(__self__, "path_parameter_values", path_parameter_values)
        if query_string_parameters is not None:
            pulumi.set(__self__, "query_string_parameters", query_string_parameters)

    @property
    @pulumi.getter(name="headerParameters")
    def header_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "header_parameters")

    @header_parameters.setter
    def header_parameters(self, value: Optional[Any]):
        pulumi.set(self, "header_parameters", value)

    @property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "path_parameter_values")

    @path_parameter_values.setter
    def path_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "path_parameter_values", value)

    @property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "query_string_parameters")

    @query_string_parameters.setter
    def query_string_parameters(self, value: Optional[Any]):
        pulumi.set(self, "query_string_parameters", value)


@pulumi.input_type
class RuleInputTransformerArgs:
    def __init__(__self__, *,
                 input_template: pulumi.Input[str],
                 input_paths_map: Optional[Any] = None):
        pulumi.set(__self__, "input_template", input_template)
        if input_paths_map is not None:
            pulumi.set(__self__, "input_paths_map", input_paths_map)

    @property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> pulumi.Input[str]:
        return pulumi.get(self, "input_template")

    @input_template.setter
    def input_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "input_template", value)

    @property
    @pulumi.getter(name="inputPathsMap")
    def input_paths_map(self) -> Optional[Any]:
        return pulumi.get(self, "input_paths_map")

    @input_paths_map.setter
    def input_paths_map(self, value: Optional[Any]):
        pulumi.set(self, "input_paths_map", value)


@pulumi.input_type
class RuleKinesisParametersArgs:
    def __init__(__self__, *,
                 partition_key_path: pulumi.Input[str]):
        pulumi.set(__self__, "partition_key_path", partition_key_path)

    @property
    @pulumi.getter(name="partitionKeyPath")
    def partition_key_path(self) -> pulumi.Input[str]:
        return pulumi.get(self, "partition_key_path")

    @partition_key_path.setter
    def partition_key_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "partition_key_path", value)


@pulumi.input_type
class RuleNetworkConfigurationArgs:
    def __init__(__self__, *,
                 aws_vpc_configuration: Optional[pulumi.Input['RuleAwsVpcConfigurationArgs']] = None):
        if aws_vpc_configuration is not None:
            pulumi.set(__self__, "aws_vpc_configuration", aws_vpc_configuration)

    @property
    @pulumi.getter(name="awsVpcConfiguration")
    def aws_vpc_configuration(self) -> Optional[pulumi.Input['RuleAwsVpcConfigurationArgs']]:
        return pulumi.get(self, "aws_vpc_configuration")

    @aws_vpc_configuration.setter
    def aws_vpc_configuration(self, value: Optional[pulumi.Input['RuleAwsVpcConfigurationArgs']]):
        pulumi.set(self, "aws_vpc_configuration", value)


@pulumi.input_type
class RulePlacementConstraintArgs:
    def __init__(__self__, *,
                 expression: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class RulePlacementStrategyArgs:
    def __init__(__self__, *,
                 field: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if field is not None:
            pulumi.set(__self__, "field", field)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "field")

    @field.setter
    def field(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class RuleRedshiftDataParametersArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 sql: pulumi.Input[str],
                 db_user: Optional[pulumi.Input[str]] = None,
                 secret_manager_arn: Optional[pulumi.Input[str]] = None,
                 statement_name: Optional[pulumi.Input[str]] = None,
                 with_event: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "sql", sql)
        if db_user is not None:
            pulumi.set(__self__, "db_user", db_user)
        if secret_manager_arn is not None:
            pulumi.set(__self__, "secret_manager_arn", secret_manager_arn)
        if statement_name is not None:
            pulumi.set(__self__, "statement_name", statement_name)
        if with_event is not None:
            pulumi.set(__self__, "with_event", with_event)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def sql(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sql")

    @sql.setter
    def sql(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql", value)

    @property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_user")

    @db_user.setter
    def db_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_user", value)

    @property
    @pulumi.getter(name="secretManagerArn")
    def secret_manager_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secret_manager_arn")

    @secret_manager_arn.setter
    def secret_manager_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_manager_arn", value)

    @property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "statement_name")

    @statement_name.setter
    def statement_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "statement_name", value)

    @property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "with_event")

    @with_event.setter
    def with_event(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_event", value)


@pulumi.input_type
class RuleRetryPolicyArgs:
    def __init__(__self__, *,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[int]] = None):
        if maximum_event_age_in_seconds is not None:
            pulumi.set(__self__, "maximum_event_age_in_seconds", maximum_event_age_in_seconds)
        if maximum_retry_attempts is not None:
            pulumi.set(__self__, "maximum_retry_attempts", maximum_retry_attempts)

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_event_age_in_seconds", value)

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "maximum_retry_attempts")

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_retry_attempts", value)


@pulumi.input_type
class RuleRunCommandParametersArgs:
    def __init__(__self__, *,
                 run_command_targets: pulumi.Input[Sequence[pulumi.Input['RuleRunCommandTargetArgs']]]):
        pulumi.set(__self__, "run_command_targets", run_command_targets)

    @property
    @pulumi.getter(name="runCommandTargets")
    def run_command_targets(self) -> pulumi.Input[Sequence[pulumi.Input['RuleRunCommandTargetArgs']]]:
        return pulumi.get(self, "run_command_targets")

    @run_command_targets.setter
    def run_command_targets(self, value: pulumi.Input[Sequence[pulumi.Input['RuleRunCommandTargetArgs']]]):
        pulumi.set(self, "run_command_targets", value)


@pulumi.input_type
class RuleRunCommandTargetArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class RuleSqsParametersArgs:
    def __init__(__self__, *,
                 message_group_id: pulumi.Input[str]):
        pulumi.set(__self__, "message_group_id", message_group_id)

    @property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "message_group_id")

    @message_group_id.setter
    def message_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "message_group_id", value)


@pulumi.input_type
class RuleTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class RuleTargetArgs:
    def __init__(__self__, *,
                 arn: pulumi.Input[str],
                 id: pulumi.Input[str],
                 batch_parameters: Optional[pulumi.Input['RuleBatchParametersArgs']] = None,
                 dead_letter_config: Optional[pulumi.Input['RuleDeadLetterConfigArgs']] = None,
                 ecs_parameters: Optional[pulumi.Input['RuleEcsParametersArgs']] = None,
                 http_parameters: Optional[pulumi.Input['RuleHttpParametersArgs']] = None,
                 input: Optional[pulumi.Input[str]] = None,
                 input_path: Optional[pulumi.Input[str]] = None,
                 input_transformer: Optional[pulumi.Input['RuleInputTransformerArgs']] = None,
                 kinesis_parameters: Optional[pulumi.Input['RuleKinesisParametersArgs']] = None,
                 redshift_data_parameters: Optional[pulumi.Input['RuleRedshiftDataParametersArgs']] = None,
                 retry_policy: Optional[pulumi.Input['RuleRetryPolicyArgs']] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 run_command_parameters: Optional[pulumi.Input['RuleRunCommandParametersArgs']] = None,
                 sqs_parameters: Optional[pulumi.Input['RuleSqsParametersArgs']] = None):
        pulumi.set(__self__, "arn", arn)
        pulumi.set(__self__, "id", id)
        if batch_parameters is not None:
            pulumi.set(__self__, "batch_parameters", batch_parameters)
        if dead_letter_config is not None:
            pulumi.set(__self__, "dead_letter_config", dead_letter_config)
        if ecs_parameters is not None:
            pulumi.set(__self__, "ecs_parameters", ecs_parameters)
        if http_parameters is not None:
            pulumi.set(__self__, "http_parameters", http_parameters)
        if input is not None:
            pulumi.set(__self__, "input", input)
        if input_path is not None:
            pulumi.set(__self__, "input_path", input_path)
        if input_transformer is not None:
            pulumi.set(__self__, "input_transformer", input_transformer)
        if kinesis_parameters is not None:
            pulumi.set(__self__, "kinesis_parameters", kinesis_parameters)
        if redshift_data_parameters is not None:
            pulumi.set(__self__, "redshift_data_parameters", redshift_data_parameters)
        if retry_policy is not None:
            pulumi.set(__self__, "retry_policy", retry_policy)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if run_command_parameters is not None:
            pulumi.set(__self__, "run_command_parameters", run_command_parameters)
        if sqs_parameters is not None:
            pulumi.set(__self__, "sqs_parameters", sqs_parameters)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="batchParameters")
    def batch_parameters(self) -> Optional[pulumi.Input['RuleBatchParametersArgs']]:
        return pulumi.get(self, "batch_parameters")

    @batch_parameters.setter
    def batch_parameters(self, value: Optional[pulumi.Input['RuleBatchParametersArgs']]):
        pulumi.set(self, "batch_parameters", value)

    @property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[pulumi.Input['RuleDeadLetterConfigArgs']]:
        return pulumi.get(self, "dead_letter_config")

    @dead_letter_config.setter
    def dead_letter_config(self, value: Optional[pulumi.Input['RuleDeadLetterConfigArgs']]):
        pulumi.set(self, "dead_letter_config", value)

    @property
    @pulumi.getter(name="ecsParameters")
    def ecs_parameters(self) -> Optional[pulumi.Input['RuleEcsParametersArgs']]:
        return pulumi.get(self, "ecs_parameters")

    @ecs_parameters.setter
    def ecs_parameters(self, value: Optional[pulumi.Input['RuleEcsParametersArgs']]):
        pulumi.set(self, "ecs_parameters", value)

    @property
    @pulumi.getter(name="httpParameters")
    def http_parameters(self) -> Optional[pulumi.Input['RuleHttpParametersArgs']]:
        return pulumi.get(self, "http_parameters")

    @http_parameters.setter
    def http_parameters(self, value: Optional[pulumi.Input['RuleHttpParametersArgs']]):
        pulumi.set(self, "http_parameters", value)

    @property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter(name="inputPath")
    def input_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "input_path")

    @input_path.setter
    def input_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_path", value)

    @property
    @pulumi.getter(name="inputTransformer")
    def input_transformer(self) -> Optional[pulumi.Input['RuleInputTransformerArgs']]:
        return pulumi.get(self, "input_transformer")

    @input_transformer.setter
    def input_transformer(self, value: Optional[pulumi.Input['RuleInputTransformerArgs']]):
        pulumi.set(self, "input_transformer", value)

    @property
    @pulumi.getter(name="kinesisParameters")
    def kinesis_parameters(self) -> Optional[pulumi.Input['RuleKinesisParametersArgs']]:
        return pulumi.get(self, "kinesis_parameters")

    @kinesis_parameters.setter
    def kinesis_parameters(self, value: Optional[pulumi.Input['RuleKinesisParametersArgs']]):
        pulumi.set(self, "kinesis_parameters", value)

    @property
    @pulumi.getter(name="redshiftDataParameters")
    def redshift_data_parameters(self) -> Optional[pulumi.Input['RuleRedshiftDataParametersArgs']]:
        return pulumi.get(self, "redshift_data_parameters")

    @redshift_data_parameters.setter
    def redshift_data_parameters(self, value: Optional[pulumi.Input['RuleRedshiftDataParametersArgs']]):
        pulumi.set(self, "redshift_data_parameters", value)

    @property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input['RuleRetryPolicyArgs']]:
        return pulumi.get(self, "retry_policy")

    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input['RuleRetryPolicyArgs']]):
        pulumi.set(self, "retry_policy", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="runCommandParameters")
    def run_command_parameters(self) -> Optional[pulumi.Input['RuleRunCommandParametersArgs']]:
        return pulumi.get(self, "run_command_parameters")

    @run_command_parameters.setter
    def run_command_parameters(self, value: Optional[pulumi.Input['RuleRunCommandParametersArgs']]):
        pulumi.set(self, "run_command_parameters", value)

    @property
    @pulumi.getter(name="sqsParameters")
    def sqs_parameters(self) -> Optional[pulumi.Input['RuleSqsParametersArgs']]:
        return pulumi.get(self, "sqs_parameters")

    @sqs_parameters.setter
    def sqs_parameters(self, value: Optional[pulumi.Input['RuleSqsParametersArgs']]):
        pulumi.set(self, "sqs_parameters", value)


