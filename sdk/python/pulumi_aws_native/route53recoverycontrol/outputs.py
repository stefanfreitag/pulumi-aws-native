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
    'ClusterEndpoint',
    'ClusterTag',
    'ControlPanelTag',
    'SafetyRuleAssertionRule',
    'SafetyRuleGatingRule',
    'SafetyRuleRuleConfig',
    'SafetyRuleTag',
]

@pulumi.output_type
class ClusterEndpoint(dict):
    def __init__(__self__, *,
                 endpoint: Optional[str] = None,
                 region: Optional[str] = None):
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")


@pulumi.output_type
class ClusterTag(dict):
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
class ControlPanelTag(dict):
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
class SafetyRuleAssertionRule(dict):
    """
    An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assertedControls":
            suggest = "asserted_controls"
        elif key == "waitPeriodMs":
            suggest = "wait_period_ms"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SafetyRuleAssertionRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SafetyRuleAssertionRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SafetyRuleAssertionRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 asserted_controls: Sequence[str],
                 wait_period_ms: int):
        """
        An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.
        :param Sequence[str] asserted_controls: The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
        :param int wait_period_ms: An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
        """
        pulumi.set(__self__, "asserted_controls", asserted_controls)
        pulumi.set(__self__, "wait_period_ms", wait_period_ms)

    @property
    @pulumi.getter(name="assertedControls")
    def asserted_controls(self) -> Sequence[str]:
        """
        The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
        """
        return pulumi.get(self, "asserted_controls")

    @property
    @pulumi.getter(name="waitPeriodMs")
    def wait_period_ms(self) -> int:
        """
        An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
        """
        return pulumi.get(self, "wait_period_ms")


@pulumi.output_type
class SafetyRuleGatingRule(dict):
    """
    A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gatingControls":
            suggest = "gating_controls"
        elif key == "targetControls":
            suggest = "target_controls"
        elif key == "waitPeriodMs":
            suggest = "wait_period_ms"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SafetyRuleGatingRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SafetyRuleGatingRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SafetyRuleGatingRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gating_controls: Sequence[str],
                 target_controls: Sequence[str],
                 wait_period_ms: int):
        """
        A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.
        :param Sequence[str] gating_controls: The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
        :param Sequence[str] target_controls: Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true. 
               In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
        :param int wait_period_ms: An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
        """
        pulumi.set(__self__, "gating_controls", gating_controls)
        pulumi.set(__self__, "target_controls", target_controls)
        pulumi.set(__self__, "wait_period_ms", wait_period_ms)

    @property
    @pulumi.getter(name="gatingControls")
    def gating_controls(self) -> Sequence[str]:
        """
        The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
        """
        return pulumi.get(self, "gating_controls")

    @property
    @pulumi.getter(name="targetControls")
    def target_controls(self) -> Sequence[str]:
        """
        Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true. 
        In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
        """
        return pulumi.get(self, "target_controls")

    @property
    @pulumi.getter(name="waitPeriodMs")
    def wait_period_ms(self) -> int:
        """
        An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
        """
        return pulumi.get(self, "wait_period_ms")


@pulumi.output_type
class SafetyRuleRuleConfig(dict):
    """
    The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.
    """
    def __init__(__self__, *,
                 inverted: bool,
                 threshold: int,
                 type: 'SafetyRuleRuleType'):
        """
        The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.
        :param bool inverted: Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
        :param int threshold: The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
        """
        pulumi.set(__self__, "inverted", inverted)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def inverted(self) -> bool:
        """
        Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
        """
        return pulumi.get(self, "inverted")

    @property
    @pulumi.getter
    def threshold(self) -> int:
        """
        The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def type(self) -> 'SafetyRuleRuleType':
        return pulumi.get(self, "type")


@pulumi.output_type
class SafetyRuleTag(dict):
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


