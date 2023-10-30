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
    'GetAutomationRuleResult',
    'AwaitableGetAutomationRuleResult',
    'get_automation_rule',
    'get_automation_rule_output',
]

@pulumi.output_type
class GetAutomationRuleResult:
    def __init__(__self__, actions=None, created_at=None, created_by=None, criteria=None, description=None, is_terminal=None, rule_arn=None, rule_name=None, rule_order=None, rule_status=None, tags=None, updated_at=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if criteria and not isinstance(criteria, dict):
            raise TypeError("Expected argument 'criteria' to be a dict")
        pulumi.set(__self__, "criteria", criteria)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if is_terminal and not isinstance(is_terminal, bool):
            raise TypeError("Expected argument 'is_terminal' to be a bool")
        pulumi.set(__self__, "is_terminal", is_terminal)
        if rule_arn and not isinstance(rule_arn, str):
            raise TypeError("Expected argument 'rule_arn' to be a str")
        pulumi.set(__self__, "rule_arn", rule_arn)
        if rule_name and not isinstance(rule_name, str):
            raise TypeError("Expected argument 'rule_name' to be a str")
        pulumi.set(__self__, "rule_name", rule_name)
        if rule_order and not isinstance(rule_order, int):
            raise TypeError("Expected argument 'rule_order' to be a int")
        pulumi.set(__self__, "rule_order", rule_order)
        if rule_status and not isinstance(rule_status, str):
            raise TypeError("Expected argument 'rule_status' to be a str")
        pulumi.set(__self__, "rule_status", rule_status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.AutomationRulesAction']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The date and time when Automation Rule was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identifier by which created the rule
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def criteria(self) -> Optional['outputs.AutomationRulesFindingFilters']:
        """
        The rule criteria for evaluating findings
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isTerminal")
    def is_terminal(self) -> Optional[bool]:
        """
        If Rule is a terminal rule
        """
        return pulumi.get(self, "is_terminal")

    @property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> Optional[str]:
        """
        An Automation Rule Arn is automatically created
        """
        return pulumi.get(self, "rule_arn")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[str]:
        """
        Rule name
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[int]:
        """
        Rule order value
        """
        return pulumi.get(self, "rule_order")

    @property
    @pulumi.getter(name="ruleStatus")
    def rule_status(self) -> Optional['AutomationRuleRuleStatus']:
        """
        Status of the Rule upon creation
        """
        return pulumi.get(self, "rule_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional['outputs.AutomationRuleTags']:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        """
        The date and time when Automation Rule was last updated
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetAutomationRuleResult(GetAutomationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutomationRuleResult(
            actions=self.actions,
            created_at=self.created_at,
            created_by=self.created_by,
            criteria=self.criteria,
            description=self.description,
            is_terminal=self.is_terminal,
            rule_arn=self.rule_arn,
            rule_name=self.rule_name,
            rule_order=self.rule_order,
            rule_status=self.rule_status,
            tags=self.tags,
            updated_at=self.updated_at)


def get_automation_rule(rule_arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutomationRuleResult:
    """
    The AWS::SecurityHub::AutomationRule resource represents the Automation Rule in your account. One rule resource is created for each Automation Rule in which you configure rule criteria and actions.


    :param str rule_arn: An Automation Rule Arn is automatically created
    """
    __args__ = dict()
    __args__['ruleArn'] = rule_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:securityhub:getAutomationRule', __args__, opts=opts, typ=GetAutomationRuleResult).value

    return AwaitableGetAutomationRuleResult(
        actions=pulumi.get(__ret__, 'actions'),
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        criteria=pulumi.get(__ret__, 'criteria'),
        description=pulumi.get(__ret__, 'description'),
        is_terminal=pulumi.get(__ret__, 'is_terminal'),
        rule_arn=pulumi.get(__ret__, 'rule_arn'),
        rule_name=pulumi.get(__ret__, 'rule_name'),
        rule_order=pulumi.get(__ret__, 'rule_order'),
        rule_status=pulumi.get(__ret__, 'rule_status'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'))


@_utilities.lift_output_func(get_automation_rule)
def get_automation_rule_output(rule_arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutomationRuleResult]:
    """
    The AWS::SecurityHub::AutomationRule resource represents the Automation Rule in your account. One rule resource is created for each Automation Rule in which you configure rule criteria and actions.


    :param str rule_arn: An Automation Rule Arn is automatically created
    """
    ...
