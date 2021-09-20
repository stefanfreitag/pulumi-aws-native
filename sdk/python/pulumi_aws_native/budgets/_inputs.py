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
    'BudgetsActionActionThresholdArgs',
    'BudgetsActionDefinitionArgs',
    'BudgetsActionIamActionDefinitionArgs',
    'BudgetsActionScpActionDefinitionArgs',
    'BudgetsActionSsmActionDefinitionArgs',
    'BudgetsActionSubscriberArgs',
]

@pulumi.input_type
class BudgetsActionActionThresholdArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['BudgetsActionActionThresholdType'],
                 value: pulumi.Input[float]):
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['BudgetsActionActionThresholdType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['BudgetsActionActionThresholdType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[float]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[float]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class BudgetsActionDefinitionArgs:
    def __init__(__self__, *,
                 iam_action_definition: Optional[pulumi.Input['BudgetsActionIamActionDefinitionArgs']] = None,
                 scp_action_definition: Optional[pulumi.Input['BudgetsActionScpActionDefinitionArgs']] = None,
                 ssm_action_definition: Optional[pulumi.Input['BudgetsActionSsmActionDefinitionArgs']] = None):
        if iam_action_definition is not None:
            pulumi.set(__self__, "iam_action_definition", iam_action_definition)
        if scp_action_definition is not None:
            pulumi.set(__self__, "scp_action_definition", scp_action_definition)
        if ssm_action_definition is not None:
            pulumi.set(__self__, "ssm_action_definition", ssm_action_definition)

    @property
    @pulumi.getter(name="iamActionDefinition")
    def iam_action_definition(self) -> Optional[pulumi.Input['BudgetsActionIamActionDefinitionArgs']]:
        return pulumi.get(self, "iam_action_definition")

    @iam_action_definition.setter
    def iam_action_definition(self, value: Optional[pulumi.Input['BudgetsActionIamActionDefinitionArgs']]):
        pulumi.set(self, "iam_action_definition", value)

    @property
    @pulumi.getter(name="scpActionDefinition")
    def scp_action_definition(self) -> Optional[pulumi.Input['BudgetsActionScpActionDefinitionArgs']]:
        return pulumi.get(self, "scp_action_definition")

    @scp_action_definition.setter
    def scp_action_definition(self, value: Optional[pulumi.Input['BudgetsActionScpActionDefinitionArgs']]):
        pulumi.set(self, "scp_action_definition", value)

    @property
    @pulumi.getter(name="ssmActionDefinition")
    def ssm_action_definition(self) -> Optional[pulumi.Input['BudgetsActionSsmActionDefinitionArgs']]:
        return pulumi.get(self, "ssm_action_definition")

    @ssm_action_definition.setter
    def ssm_action_definition(self, value: Optional[pulumi.Input['BudgetsActionSsmActionDefinitionArgs']]):
        pulumi.set(self, "ssm_action_definition", value)


@pulumi.input_type
class BudgetsActionIamActionDefinitionArgs:
    def __init__(__self__, *,
                 policy_arn: pulumi.Input[str],
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "policy_arn", policy_arn)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy_arn")

    @policy_arn.setter
    def policy_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_arn", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "users", value)


@pulumi.input_type
class BudgetsActionScpActionDefinitionArgs:
    def __init__(__self__, *,
                 policy_id: pulumi.Input[str],
                 target_ids: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "policy_id", policy_id)
        pulumi.set(__self__, "target_ids", target_ids)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "target_ids")

    @target_ids.setter
    def target_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "target_ids", value)


@pulumi.input_type
class BudgetsActionSsmActionDefinitionArgs:
    def __init__(__self__, *,
                 instance_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 region: pulumi.Input[str],
                 subtype: pulumi.Input['BudgetsActionSsmActionDefinitionSubtype']):
        pulumi.set(__self__, "instance_ids", instance_ids)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "subtype", subtype)

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "instance_ids")

    @instance_ids.setter
    def instance_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "instance_ids", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def subtype(self) -> pulumi.Input['BudgetsActionSsmActionDefinitionSubtype']:
        return pulumi.get(self, "subtype")

    @subtype.setter
    def subtype(self, value: pulumi.Input['BudgetsActionSsmActionDefinitionSubtype']):
        pulumi.set(self, "subtype", value)


@pulumi.input_type
class BudgetsActionSubscriberArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 type: pulumi.Input['BudgetsActionSubscriberType']):
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['BudgetsActionSubscriberType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['BudgetsActionSubscriberType']):
        pulumi.set(self, "type", value)


