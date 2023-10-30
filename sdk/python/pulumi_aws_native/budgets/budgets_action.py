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
from ._inputs import *

__all__ = ['BudgetsActionArgs', 'BudgetsAction']

@pulumi.input_type
class BudgetsActionArgs:
    def __init__(__self__, *,
                 action_threshold: pulumi.Input['BudgetsActionActionThresholdArgs'],
                 action_type: pulumi.Input['BudgetsActionActionType'],
                 budget_name: pulumi.Input[str],
                 definition: pulumi.Input['BudgetsActionDefinitionArgs'],
                 execution_role_arn: pulumi.Input[str],
                 notification_type: pulumi.Input['BudgetsActionNotificationType'],
                 subscribers: pulumi.Input[Sequence[pulumi.Input['BudgetsActionSubscriberArgs']]],
                 approval_model: Optional[pulumi.Input['BudgetsActionApprovalModel']] = None):
        """
        The set of arguments for constructing a BudgetsAction resource.
        """
        pulumi.set(__self__, "action_threshold", action_threshold)
        pulumi.set(__self__, "action_type", action_type)
        pulumi.set(__self__, "budget_name", budget_name)
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        pulumi.set(__self__, "notification_type", notification_type)
        pulumi.set(__self__, "subscribers", subscribers)
        if approval_model is not None:
            pulumi.set(__self__, "approval_model", approval_model)

    @property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> pulumi.Input['BudgetsActionActionThresholdArgs']:
        return pulumi.get(self, "action_threshold")

    @action_threshold.setter
    def action_threshold(self, value: pulumi.Input['BudgetsActionActionThresholdArgs']):
        pulumi.set(self, "action_threshold", value)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input['BudgetsActionActionType']:
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: pulumi.Input['BudgetsActionActionType']):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "budget_name")

    @budget_name.setter
    def budget_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "budget_name", value)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input['BudgetsActionDefinitionArgs']:
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input['BudgetsActionDefinitionArgs']):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input['BudgetsActionNotificationType']:
        return pulumi.get(self, "notification_type")

    @notification_type.setter
    def notification_type(self, value: pulumi.Input['BudgetsActionNotificationType']):
        pulumi.set(self, "notification_type", value)

    @property
    @pulumi.getter
    def subscribers(self) -> pulumi.Input[Sequence[pulumi.Input['BudgetsActionSubscriberArgs']]]:
        return pulumi.get(self, "subscribers")

    @subscribers.setter
    def subscribers(self, value: pulumi.Input[Sequence[pulumi.Input['BudgetsActionSubscriberArgs']]]):
        pulumi.set(self, "subscribers", value)

    @property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> Optional[pulumi.Input['BudgetsActionApprovalModel']]:
        return pulumi.get(self, "approval_model")

    @approval_model.setter
    def approval_model(self, value: Optional[pulumi.Input['BudgetsActionApprovalModel']]):
        pulumi.set(self, "approval_model", value)


class BudgetsAction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_threshold: Optional[pulumi.Input[pulumi.InputType['BudgetsActionActionThresholdArgs']]] = None,
                 action_type: Optional[pulumi.Input['BudgetsActionActionType']] = None,
                 approval_model: Optional[pulumi.Input['BudgetsActionApprovalModel']] = None,
                 budget_name: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['BudgetsActionDefinitionArgs']]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 notification_type: Optional[pulumi.Input['BudgetsActionNotificationType']] = None,
                 subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetsActionSubscriberArgs']]]]] = None,
                 __props__=None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BudgetsActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An example resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param BudgetsActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BudgetsActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_threshold: Optional[pulumi.Input[pulumi.InputType['BudgetsActionActionThresholdArgs']]] = None,
                 action_type: Optional[pulumi.Input['BudgetsActionActionType']] = None,
                 approval_model: Optional[pulumi.Input['BudgetsActionApprovalModel']] = None,
                 budget_name: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['BudgetsActionDefinitionArgs']]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 notification_type: Optional[pulumi.Input['BudgetsActionNotificationType']] = None,
                 subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BudgetsActionSubscriberArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BudgetsActionArgs.__new__(BudgetsActionArgs)

            if action_threshold is None and not opts.urn:
                raise TypeError("Missing required property 'action_threshold'")
            __props__.__dict__["action_threshold"] = action_threshold
            if action_type is None and not opts.urn:
                raise TypeError("Missing required property 'action_type'")
            __props__.__dict__["action_type"] = action_type
            __props__.__dict__["approval_model"] = approval_model
            if budget_name is None and not opts.urn:
                raise TypeError("Missing required property 'budget_name'")
            __props__.__dict__["budget_name"] = budget_name
            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if execution_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'execution_role_arn'")
            __props__.__dict__["execution_role_arn"] = execution_role_arn
            if notification_type is None and not opts.urn:
                raise TypeError("Missing required property 'notification_type'")
            __props__.__dict__["notification_type"] = notification_type
            if subscribers is None and not opts.urn:
                raise TypeError("Missing required property 'subscribers'")
            __props__.__dict__["subscribers"] = subscribers
            __props__.__dict__["action_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["action_type", "budget_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BudgetsAction, __self__).__init__(
            'aws-native:budgets:BudgetsAction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BudgetsAction':
        """
        Get an existing BudgetsAction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BudgetsActionArgs.__new__(BudgetsActionArgs)

        __props__.__dict__["action_id"] = None
        __props__.__dict__["action_threshold"] = None
        __props__.__dict__["action_type"] = None
        __props__.__dict__["approval_model"] = None
        __props__.__dict__["budget_name"] = None
        __props__.__dict__["definition"] = None
        __props__.__dict__["execution_role_arn"] = None
        __props__.__dict__["notification_type"] = None
        __props__.__dict__["subscribers"] = None
        return BudgetsAction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "action_id")

    @property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> pulumi.Output['outputs.BudgetsActionActionThreshold']:
        return pulumi.get(self, "action_threshold")

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Output['BudgetsActionActionType']:
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> pulumi.Output[Optional['BudgetsActionApprovalModel']]:
        return pulumi.get(self, "approval_model")

    @property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "budget_name")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.BudgetsActionDefinition']:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output['BudgetsActionNotificationType']:
        return pulumi.get(self, "notification_type")

    @property
    @pulumi.getter
    def subscribers(self) -> pulumi.Output[Sequence['outputs.BudgetsActionSubscriber']]:
        return pulumi.get(self, "subscribers")

