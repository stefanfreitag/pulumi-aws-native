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
    'GetSafetyRuleResult',
    'AwaitableGetSafetyRuleResult',
    'get_safety_rule',
    'get_safety_rule_output',
]

@pulumi.output_type
class GetSafetyRuleResult:
    def __init__(__self__, assertion_rule=None, gating_rule=None, name=None, safety_rule_arn=None, status=None):
        if assertion_rule and not isinstance(assertion_rule, dict):
            raise TypeError("Expected argument 'assertion_rule' to be a dict")
        pulumi.set(__self__, "assertion_rule", assertion_rule)
        if gating_rule and not isinstance(gating_rule, dict):
            raise TypeError("Expected argument 'gating_rule' to be a dict")
        pulumi.set(__self__, "gating_rule", gating_rule)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if safety_rule_arn and not isinstance(safety_rule_arn, str):
            raise TypeError("Expected argument 'safety_rule_arn' to be a str")
        pulumi.set(__self__, "safety_rule_arn", safety_rule_arn)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="assertionRule")
    def assertion_rule(self) -> Optional['outputs.SafetyRuleAssertionRule']:
        return pulumi.get(self, "assertion_rule")

    @property
    @pulumi.getter(name="gatingRule")
    def gating_rule(self) -> Optional['outputs.SafetyRuleGatingRule']:
        return pulumi.get(self, "gating_rule")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="safetyRuleArn")
    def safety_rule_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the safety rule.
        """
        return pulumi.get(self, "safety_rule_arn")

    @property
    @pulumi.getter
    def status(self) -> Optional['SafetyRuleStatus']:
        """
        The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
        """
        return pulumi.get(self, "status")


class AwaitableGetSafetyRuleResult(GetSafetyRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSafetyRuleResult(
            assertion_rule=self.assertion_rule,
            gating_rule=self.gating_rule,
            name=self.name,
            safety_rule_arn=self.safety_rule_arn,
            status=self.status)


def get_safety_rule(safety_rule_arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSafetyRuleResult:
    """
    Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.


    :param str safety_rule_arn: The Amazon Resource Name (ARN) of the safety rule.
    """
    __args__ = dict()
    __args__['safetyRuleArn'] = safety_rule_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53recoverycontrol:getSafetyRule', __args__, opts=opts, typ=GetSafetyRuleResult).value

    return AwaitableGetSafetyRuleResult(
        assertion_rule=pulumi.get(__ret__, 'assertion_rule'),
        gating_rule=pulumi.get(__ret__, 'gating_rule'),
        name=pulumi.get(__ret__, 'name'),
        safety_rule_arn=pulumi.get(__ret__, 'safety_rule_arn'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_safety_rule)
def get_safety_rule_output(safety_rule_arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSafetyRuleResult]:
    """
    Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.


    :param str safety_rule_arn: The Amazon Resource Name (ARN) of the safety rule.
    """
    ...
