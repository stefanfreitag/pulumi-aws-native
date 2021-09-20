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

__all__ = [
    'FirewallPolicyActionDefinition',
    'FirewallPolicyCustomAction',
    'FirewallPolicyDimension',
    'FirewallPolicyFirewallPolicy',
    'FirewallPolicyPublishMetricAction',
    'FirewallPolicyStatefulRuleGroupReference',
    'FirewallPolicyStatelessRuleGroupReference',
    'FirewallPolicyTag',
    'FirewallSubnetMapping',
    'FirewallTag',
    'LoggingConfigurationLogDestinationConfig',
    'LoggingConfigurationLoggingConfiguration',
    'RuleGroupActionDefinition',
    'RuleGroupAddress',
    'RuleGroupCustomAction',
    'RuleGroupDimension',
    'RuleGroupHeader',
    'RuleGroupMatchAttributes',
    'RuleGroupPortRange',
    'RuleGroupPublishMetricAction',
    'RuleGroupRuleDefinition',
    'RuleGroupRuleGroup',
    'RuleGroupRuleOption',
    'RuleGroupRuleVariables',
    'RuleGroupRulesSource',
    'RuleGroupRulesSourceList',
    'RuleGroupStatefulRule',
    'RuleGroupStatelessRule',
    'RuleGroupStatelessRulesAndCustomActions',
    'RuleGroupTCPFlagField',
    'RuleGroupTag',
]

@pulumi.output_type
class FirewallPolicyActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publishMetricAction":
            suggest = "publish_metric_action"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallPolicyActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallPolicyActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallPolicyActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 publish_metric_action: Optional['outputs.FirewallPolicyPublishMetricAction'] = None):
        if publish_metric_action is not None:
            pulumi.set(__self__, "publish_metric_action", publish_metric_action)

    @property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(self) -> Optional['outputs.FirewallPolicyPublishMetricAction']:
        return pulumi.get(self, "publish_metric_action")


@pulumi.output_type
class FirewallPolicyCustomAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionDefinition":
            suggest = "action_definition"
        elif key == "actionName":
            suggest = "action_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallPolicyCustomAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallPolicyCustomAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallPolicyCustomAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_definition: 'outputs.FirewallPolicyActionDefinition',
                 action_name: str):
        pulumi.set(__self__, "action_definition", action_definition)
        pulumi.set(__self__, "action_name", action_name)

    @property
    @pulumi.getter(name="actionDefinition")
    def action_definition(self) -> 'outputs.FirewallPolicyActionDefinition':
        return pulumi.get(self, "action_definition")

    @property
    @pulumi.getter(name="actionName")
    def action_name(self) -> str:
        return pulumi.get(self, "action_name")


@pulumi.output_type
class FirewallPolicyDimension(dict):
    def __init__(__self__, *,
                 value: str):
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class FirewallPolicyFirewallPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "statelessDefaultActions":
            suggest = "stateless_default_actions"
        elif key == "statelessFragmentDefaultActions":
            suggest = "stateless_fragment_default_actions"
        elif key == "statefulRuleGroupReferences":
            suggest = "stateful_rule_group_references"
        elif key == "statelessCustomActions":
            suggest = "stateless_custom_actions"
        elif key == "statelessRuleGroupReferences":
            suggest = "stateless_rule_group_references"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallPolicyFirewallPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallPolicyFirewallPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallPolicyFirewallPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stateless_default_actions: Sequence[str],
                 stateless_fragment_default_actions: Sequence[str],
                 stateful_rule_group_references: Optional[Sequence['outputs.FirewallPolicyStatefulRuleGroupReference']] = None,
                 stateless_custom_actions: Optional[Sequence['outputs.FirewallPolicyCustomAction']] = None,
                 stateless_rule_group_references: Optional[Sequence['outputs.FirewallPolicyStatelessRuleGroupReference']] = None):
        pulumi.set(__self__, "stateless_default_actions", stateless_default_actions)
        pulumi.set(__self__, "stateless_fragment_default_actions", stateless_fragment_default_actions)
        if stateful_rule_group_references is not None:
            pulumi.set(__self__, "stateful_rule_group_references", stateful_rule_group_references)
        if stateless_custom_actions is not None:
            pulumi.set(__self__, "stateless_custom_actions", stateless_custom_actions)
        if stateless_rule_group_references is not None:
            pulumi.set(__self__, "stateless_rule_group_references", stateless_rule_group_references)

    @property
    @pulumi.getter(name="statelessDefaultActions")
    def stateless_default_actions(self) -> Sequence[str]:
        return pulumi.get(self, "stateless_default_actions")

    @property
    @pulumi.getter(name="statelessFragmentDefaultActions")
    def stateless_fragment_default_actions(self) -> Sequence[str]:
        return pulumi.get(self, "stateless_fragment_default_actions")

    @property
    @pulumi.getter(name="statefulRuleGroupReferences")
    def stateful_rule_group_references(self) -> Optional[Sequence['outputs.FirewallPolicyStatefulRuleGroupReference']]:
        return pulumi.get(self, "stateful_rule_group_references")

    @property
    @pulumi.getter(name="statelessCustomActions")
    def stateless_custom_actions(self) -> Optional[Sequence['outputs.FirewallPolicyCustomAction']]:
        return pulumi.get(self, "stateless_custom_actions")

    @property
    @pulumi.getter(name="statelessRuleGroupReferences")
    def stateless_rule_group_references(self) -> Optional[Sequence['outputs.FirewallPolicyStatelessRuleGroupReference']]:
        return pulumi.get(self, "stateless_rule_group_references")


@pulumi.output_type
class FirewallPolicyPublishMetricAction(dict):
    def __init__(__self__, *,
                 dimensions: Sequence['outputs.FirewallPolicyDimension']):
        pulumi.set(__self__, "dimensions", dimensions)

    @property
    @pulumi.getter
    def dimensions(self) -> Sequence['outputs.FirewallPolicyDimension']:
        return pulumi.get(self, "dimensions")


@pulumi.output_type
class FirewallPolicyStatefulRuleGroupReference(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceArn":
            suggest = "resource_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallPolicyStatefulRuleGroupReference. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallPolicyStatefulRuleGroupReference.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallPolicyStatefulRuleGroupReference.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_arn: str):
        pulumi.set(__self__, "resource_arn", resource_arn)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> str:
        return pulumi.get(self, "resource_arn")


@pulumi.output_type
class FirewallPolicyStatelessRuleGroupReference(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceArn":
            suggest = "resource_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallPolicyStatelessRuleGroupReference. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallPolicyStatelessRuleGroupReference.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallPolicyStatelessRuleGroupReference.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 priority: int,
                 resource_arn: str):
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "resource_arn", resource_arn)

    @property
    @pulumi.getter
    def priority(self) -> int:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> str:
        return pulumi.get(self, "resource_arn")


@pulumi.output_type
class FirewallPolicyTag(dict):
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
class FirewallSubnetMapping(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallSubnetMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallSubnetMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallSubnetMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_id: str):
        """
        :param str subnet_id: A SubnetId.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        A SubnetId.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class FirewallTag(dict):
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
class LoggingConfigurationLogDestinationConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logDestination":
            suggest = "log_destination"
        elif key == "logDestinationType":
            suggest = "log_destination_type"
        elif key == "logType":
            suggest = "log_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationLogDestinationConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationLogDestinationConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationLogDestinationConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_destination: Any,
                 log_destination_type: 'LoggingConfigurationLogDestinationConfigLogDestinationType',
                 log_type: 'LoggingConfigurationLogDestinationConfigLogType'):
        """
        :param Any log_destination: A key-value pair to configure the logDestinations.
        """
        pulumi.set(__self__, "log_destination", log_destination)
        pulumi.set(__self__, "log_destination_type", log_destination_type)
        pulumi.set(__self__, "log_type", log_type)

    @property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Any:
        """
        A key-value pair to configure the logDestinations.
        """
        return pulumi.get(self, "log_destination")

    @property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> 'LoggingConfigurationLogDestinationConfigLogDestinationType':
        return pulumi.get(self, "log_destination_type")

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> 'LoggingConfigurationLogDestinationConfigLogType':
        return pulumi.get(self, "log_type")


@pulumi.output_type
class LoggingConfigurationLoggingConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logDestinationConfigs":
            suggest = "log_destination_configs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationLoggingConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationLoggingConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationLoggingConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_destination_configs: Sequence['outputs.LoggingConfigurationLogDestinationConfig']):
        pulumi.set(__self__, "log_destination_configs", log_destination_configs)

    @property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> Sequence['outputs.LoggingConfigurationLogDestinationConfig']:
        return pulumi.get(self, "log_destination_configs")


@pulumi.output_type
class RuleGroupActionDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publishMetricAction":
            suggest = "publish_metric_action"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupActionDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupActionDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupActionDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 publish_metric_action: Optional['outputs.RuleGroupPublishMetricAction'] = None):
        if publish_metric_action is not None:
            pulumi.set(__self__, "publish_metric_action", publish_metric_action)

    @property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(self) -> Optional['outputs.RuleGroupPublishMetricAction']:
        return pulumi.get(self, "publish_metric_action")


@pulumi.output_type
class RuleGroupAddress(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addressDefinition":
            suggest = "address_definition"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupAddress. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupAddress.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupAddress.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 address_definition: str):
        pulumi.set(__self__, "address_definition", address_definition)

    @property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> str:
        return pulumi.get(self, "address_definition")


@pulumi.output_type
class RuleGroupCustomAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionDefinition":
            suggest = "action_definition"
        elif key == "actionName":
            suggest = "action_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupCustomAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupCustomAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupCustomAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_definition: 'outputs.RuleGroupActionDefinition',
                 action_name: str):
        pulumi.set(__self__, "action_definition", action_definition)
        pulumi.set(__self__, "action_name", action_name)

    @property
    @pulumi.getter(name="actionDefinition")
    def action_definition(self) -> 'outputs.RuleGroupActionDefinition':
        return pulumi.get(self, "action_definition")

    @property
    @pulumi.getter(name="actionName")
    def action_name(self) -> str:
        return pulumi.get(self, "action_name")


@pulumi.output_type
class RuleGroupDimension(dict):
    def __init__(__self__, *,
                 value: str):
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class RuleGroupHeader(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationPort":
            suggest = "destination_port"
        elif key == "sourcePort":
            suggest = "source_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupHeader. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupHeader.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupHeader.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination: str,
                 destination_port: str,
                 direction: 'RuleGroupHeaderDirection',
                 protocol: 'RuleGroupHeaderProtocol',
                 source: str,
                 source_port: str):
        pulumi.set(__self__, "destination", destination)
        pulumi.set(__self__, "destination_port", destination_port)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "source_port", source_port)

    @property
    @pulumi.getter
    def destination(self) -> str:
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> str:
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter
    def direction(self) -> 'RuleGroupHeaderDirection':
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def protocol(self) -> 'RuleGroupHeaderProtocol':
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def source(self) -> str:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> str:
        return pulumi.get(self, "source_port")


@pulumi.output_type
class RuleGroupMatchAttributes(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationPorts":
            suggest = "destination_ports"
        elif key == "sourcePorts":
            suggest = "source_ports"
        elif key == "tCPFlags":
            suggest = "t_cp_flags"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupMatchAttributes. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupMatchAttributes.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupMatchAttributes.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination_ports: Optional[Sequence['outputs.RuleGroupPortRange']] = None,
                 destinations: Optional[Sequence['outputs.RuleGroupAddress']] = None,
                 protocols: Optional[Sequence[int]] = None,
                 source_ports: Optional[Sequence['outputs.RuleGroupPortRange']] = None,
                 sources: Optional[Sequence['outputs.RuleGroupAddress']] = None,
                 t_cp_flags: Optional[Sequence['outputs.RuleGroupTCPFlagField']] = None):
        if destination_ports is not None:
            pulumi.set(__self__, "destination_ports", destination_ports)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if protocols is not None:
            pulumi.set(__self__, "protocols", protocols)
        if source_ports is not None:
            pulumi.set(__self__, "source_ports", source_ports)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if t_cp_flags is not None:
            pulumi.set(__self__, "t_cp_flags", t_cp_flags)

    @property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Optional[Sequence['outputs.RuleGroupPortRange']]:
        return pulumi.get(self, "destination_ports")

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.RuleGroupAddress']]:
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[int]]:
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Optional[Sequence['outputs.RuleGroupPortRange']]:
        return pulumi.get(self, "source_ports")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.RuleGroupAddress']]:
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="tCPFlags")
    def t_cp_flags(self) -> Optional[Sequence['outputs.RuleGroupTCPFlagField']]:
        return pulumi.get(self, "t_cp_flags")


@pulumi.output_type
class RuleGroupPortRange(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fromPort":
            suggest = "from_port"
        elif key == "toPort":
            suggest = "to_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupPortRange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupPortRange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupPortRange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 from_port: int,
                 to_port: int):
        pulumi.set(__self__, "from_port", from_port)
        pulumi.set(__self__, "to_port", to_port)

    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> int:
        return pulumi.get(self, "from_port")

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> int:
        return pulumi.get(self, "to_port")


@pulumi.output_type
class RuleGroupPublishMetricAction(dict):
    def __init__(__self__, *,
                 dimensions: Sequence['outputs.RuleGroupDimension']):
        pulumi.set(__self__, "dimensions", dimensions)

    @property
    @pulumi.getter
    def dimensions(self) -> Sequence['outputs.RuleGroupDimension']:
        return pulumi.get(self, "dimensions")


@pulumi.output_type
class RuleGroupRuleDefinition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "matchAttributes":
            suggest = "match_attributes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupRuleDefinition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupRuleDefinition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupRuleDefinition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions: Sequence[str],
                 match_attributes: 'outputs.RuleGroupMatchAttributes'):
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "match_attributes", match_attributes)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[str]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="matchAttributes")
    def match_attributes(self) -> 'outputs.RuleGroupMatchAttributes':
        return pulumi.get(self, "match_attributes")


@pulumi.output_type
class RuleGroupRuleGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rulesSource":
            suggest = "rules_source"
        elif key == "ruleVariables":
            suggest = "rule_variables"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupRuleGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupRuleGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupRuleGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rules_source: 'outputs.RuleGroupRulesSource',
                 rule_variables: Optional['outputs.RuleGroupRuleVariables'] = None):
        pulumi.set(__self__, "rules_source", rules_source)
        if rule_variables is not None:
            pulumi.set(__self__, "rule_variables", rule_variables)

    @property
    @pulumi.getter(name="rulesSource")
    def rules_source(self) -> 'outputs.RuleGroupRulesSource':
        return pulumi.get(self, "rules_source")

    @property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(self) -> Optional['outputs.RuleGroupRuleVariables']:
        return pulumi.get(self, "rule_variables")


@pulumi.output_type
class RuleGroupRuleOption(dict):
    def __init__(__self__, *,
                 keyword: str,
                 settings: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "keyword", keyword)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def keyword(self) -> str:
        return pulumi.get(self, "keyword")

    @property
    @pulumi.getter
    def settings(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "settings")


@pulumi.output_type
class RuleGroupRuleVariables(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "iPSets":
            suggest = "i_p_sets"
        elif key == "portSets":
            suggest = "port_sets"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupRuleVariables. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupRuleVariables.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupRuleVariables.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 i_p_sets: Optional[Any] = None,
                 port_sets: Optional[Any] = None):
        if i_p_sets is not None:
            pulumi.set(__self__, "i_p_sets", i_p_sets)
        if port_sets is not None:
            pulumi.set(__self__, "port_sets", port_sets)

    @property
    @pulumi.getter(name="iPSets")
    def i_p_sets(self) -> Optional[Any]:
        return pulumi.get(self, "i_p_sets")

    @property
    @pulumi.getter(name="portSets")
    def port_sets(self) -> Optional[Any]:
        return pulumi.get(self, "port_sets")


@pulumi.output_type
class RuleGroupRulesSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rulesSourceList":
            suggest = "rules_source_list"
        elif key == "rulesString":
            suggest = "rules_string"
        elif key == "statefulRules":
            suggest = "stateful_rules"
        elif key == "statelessRulesAndCustomActions":
            suggest = "stateless_rules_and_custom_actions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupRulesSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupRulesSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupRulesSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rules_source_list: Optional['outputs.RuleGroupRulesSourceList'] = None,
                 rules_string: Optional[str] = None,
                 stateful_rules: Optional[Sequence['outputs.RuleGroupStatefulRule']] = None,
                 stateless_rules_and_custom_actions: Optional['outputs.RuleGroupStatelessRulesAndCustomActions'] = None):
        if rules_source_list is not None:
            pulumi.set(__self__, "rules_source_list", rules_source_list)
        if rules_string is not None:
            pulumi.set(__self__, "rules_string", rules_string)
        if stateful_rules is not None:
            pulumi.set(__self__, "stateful_rules", stateful_rules)
        if stateless_rules_and_custom_actions is not None:
            pulumi.set(__self__, "stateless_rules_and_custom_actions", stateless_rules_and_custom_actions)

    @property
    @pulumi.getter(name="rulesSourceList")
    def rules_source_list(self) -> Optional['outputs.RuleGroupRulesSourceList']:
        return pulumi.get(self, "rules_source_list")

    @property
    @pulumi.getter(name="rulesString")
    def rules_string(self) -> Optional[str]:
        return pulumi.get(self, "rules_string")

    @property
    @pulumi.getter(name="statefulRules")
    def stateful_rules(self) -> Optional[Sequence['outputs.RuleGroupStatefulRule']]:
        return pulumi.get(self, "stateful_rules")

    @property
    @pulumi.getter(name="statelessRulesAndCustomActions")
    def stateless_rules_and_custom_actions(self) -> Optional['outputs.RuleGroupStatelessRulesAndCustomActions']:
        return pulumi.get(self, "stateless_rules_and_custom_actions")


@pulumi.output_type
class RuleGroupRulesSourceList(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "generatedRulesType":
            suggest = "generated_rules_type"
        elif key == "targetTypes":
            suggest = "target_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupRulesSourceList. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupRulesSourceList.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupRulesSourceList.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 generated_rules_type: 'RuleGroupGeneratedRulesType',
                 target_types: Sequence['RuleGroupTargetType'],
                 targets: Sequence[str]):
        pulumi.set(__self__, "generated_rules_type", generated_rules_type)
        pulumi.set(__self__, "target_types", target_types)
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter(name="generatedRulesType")
    def generated_rules_type(self) -> 'RuleGroupGeneratedRulesType':
        return pulumi.get(self, "generated_rules_type")

    @property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> Sequence['RuleGroupTargetType']:
        return pulumi.get(self, "target_types")

    @property
    @pulumi.getter
    def targets(self) -> Sequence[str]:
        return pulumi.get(self, "targets")


@pulumi.output_type
class RuleGroupStatefulRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ruleOptions":
            suggest = "rule_options"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupStatefulRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupStatefulRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupStatefulRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action: 'RuleGroupStatefulRuleAction',
                 header: 'outputs.RuleGroupHeader',
                 rule_options: Sequence['outputs.RuleGroupRuleOption']):
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "header", header)
        pulumi.set(__self__, "rule_options", rule_options)

    @property
    @pulumi.getter
    def action(self) -> 'RuleGroupStatefulRuleAction':
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def header(self) -> 'outputs.RuleGroupHeader':
        return pulumi.get(self, "header")

    @property
    @pulumi.getter(name="ruleOptions")
    def rule_options(self) -> Sequence['outputs.RuleGroupRuleOption']:
        return pulumi.get(self, "rule_options")


@pulumi.output_type
class RuleGroupStatelessRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ruleDefinition":
            suggest = "rule_definition"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupStatelessRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupStatelessRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupStatelessRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 priority: int,
                 rule_definition: 'outputs.RuleGroupRuleDefinition'):
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "rule_definition", rule_definition)

    @property
    @pulumi.getter
    def priority(self) -> int:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(self) -> 'outputs.RuleGroupRuleDefinition':
        return pulumi.get(self, "rule_definition")


@pulumi.output_type
class RuleGroupStatelessRulesAndCustomActions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "statelessRules":
            suggest = "stateless_rules"
        elif key == "customActions":
            suggest = "custom_actions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleGroupStatelessRulesAndCustomActions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleGroupStatelessRulesAndCustomActions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleGroupStatelessRulesAndCustomActions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stateless_rules: Sequence['outputs.RuleGroupStatelessRule'],
                 custom_actions: Optional[Sequence['outputs.RuleGroupCustomAction']] = None):
        pulumi.set(__self__, "stateless_rules", stateless_rules)
        if custom_actions is not None:
            pulumi.set(__self__, "custom_actions", custom_actions)

    @property
    @pulumi.getter(name="statelessRules")
    def stateless_rules(self) -> Sequence['outputs.RuleGroupStatelessRule']:
        return pulumi.get(self, "stateless_rules")

    @property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[Sequence['outputs.RuleGroupCustomAction']]:
        return pulumi.get(self, "custom_actions")


@pulumi.output_type
class RuleGroupTCPFlagField(dict):
    def __init__(__self__, *,
                 flags: Sequence['RuleGroupTCPFlag'],
                 masks: Optional[Sequence['RuleGroupTCPFlag']] = None):
        pulumi.set(__self__, "flags", flags)
        if masks is not None:
            pulumi.set(__self__, "masks", masks)

    @property
    @pulumi.getter
    def flags(self) -> Sequence['RuleGroupTCPFlag']:
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter
    def masks(self) -> Optional[Sequence['RuleGroupTCPFlag']]:
        return pulumi.get(self, "masks")


@pulumi.output_type
class RuleGroupTag(dict):
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


