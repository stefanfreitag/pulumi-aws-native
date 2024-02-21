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
    'GetStackResult',
    'AwaitableGetStackResult',
    'get_stack',
    'get_stack_output',
]

@pulumi.output_type
class GetStackResult:
    def __init__(__self__, capabilities=None, change_set_id=None, creation_time=None, description=None, disable_rollback=None, enable_termination_protection=None, last_update_time=None, notification_arns=None, outputs=None, parameters=None, parent_id=None, role_arn=None, root_id=None, stack_id=None, stack_policy_body=None, stack_status=None, stack_status_reason=None, tags=None, template_body=None, timeout_in_minutes=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if change_set_id and not isinstance(change_set_id, str):
            raise TypeError("Expected argument 'change_set_id' to be a str")
        pulumi.set(__self__, "change_set_id", change_set_id)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_rollback and not isinstance(disable_rollback, bool):
            raise TypeError("Expected argument 'disable_rollback' to be a bool")
        pulumi.set(__self__, "disable_rollback", disable_rollback)
        if enable_termination_protection and not isinstance(enable_termination_protection, bool):
            raise TypeError("Expected argument 'enable_termination_protection' to be a bool")
        pulumi.set(__self__, "enable_termination_protection", enable_termination_protection)
        if last_update_time and not isinstance(last_update_time, str):
            raise TypeError("Expected argument 'last_update_time' to be a str")
        pulumi.set(__self__, "last_update_time", last_update_time)
        if notification_arns and not isinstance(notification_arns, list):
            raise TypeError("Expected argument 'notification_arns' to be a list")
        pulumi.set(__self__, "notification_arns", notification_arns)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        pulumi.set(__self__, "parent_id", parent_id)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if root_id and not isinstance(root_id, str):
            raise TypeError("Expected argument 'root_id' to be a str")
        pulumi.set(__self__, "root_id", root_id)
        if stack_id and not isinstance(stack_id, str):
            raise TypeError("Expected argument 'stack_id' to be a str")
        pulumi.set(__self__, "stack_id", stack_id)
        if stack_policy_body and not isinstance(stack_policy_body, dict):
            raise TypeError("Expected argument 'stack_policy_body' to be a dict")
        pulumi.set(__self__, "stack_policy_body", stack_policy_body)
        if stack_status and not isinstance(stack_status, str):
            raise TypeError("Expected argument 'stack_status' to be a str")
        pulumi.set(__self__, "stack_status", stack_status)
        if stack_status_reason and not isinstance(stack_status_reason, str):
            raise TypeError("Expected argument 'stack_status_reason' to be a str")
        pulumi.set(__self__, "stack_status_reason", stack_status_reason)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if template_body and not isinstance(template_body, dict):
            raise TypeError("Expected argument 'template_body' to be a dict")
        pulumi.set(__self__, "template_body", template_body)
        if timeout_in_minutes and not isinstance(timeout_in_minutes, int):
            raise TypeError("Expected argument 'timeout_in_minutes' to be a int")
        pulumi.set(__self__, "timeout_in_minutes", timeout_in_minutes)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence['StackCapabilitiesItem']]:
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="changeSetId")
    def change_set_id(self) -> Optional[str]:
        return pulumi.get(self, "change_set_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableRollback")
    def disable_rollback(self) -> Optional[bool]:
        return pulumi.get(self, "disable_rollback")

    @property
    @pulumi.getter(name="enableTerminationProtection")
    def enable_termination_protection(self) -> Optional[bool]:
        return pulumi.get(self, "enable_termination_protection")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[str]:
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "notification_arns")

    @property
    @pulumi.getter
    def outputs(self) -> Optional[Sequence['outputs.StackOutput']]:
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[str]:
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="rootId")
    def root_id(self) -> Optional[str]:
        return pulumi.get(self, "root_id")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[str]:
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter(name="stackPolicyBody")
    def stack_policy_body(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CloudFormation::Stack` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "stack_policy_body")

    @property
    @pulumi.getter(name="stackStatus")
    def stack_status(self) -> Optional['StackStatus']:
        return pulumi.get(self, "stack_status")

    @property
    @pulumi.getter(name="stackStatusReason")
    def stack_status_reason(self) -> Optional[str]:
        return pulumi.get(self, "stack_status_reason")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.StackTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CloudFormation::Stack` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[int]:
        return pulumi.get(self, "timeout_in_minutes")


class AwaitableGetStackResult(GetStackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStackResult(
            capabilities=self.capabilities,
            change_set_id=self.change_set_id,
            creation_time=self.creation_time,
            description=self.description,
            disable_rollback=self.disable_rollback,
            enable_termination_protection=self.enable_termination_protection,
            last_update_time=self.last_update_time,
            notification_arns=self.notification_arns,
            outputs=self.outputs,
            parameters=self.parameters,
            parent_id=self.parent_id,
            role_arn=self.role_arn,
            root_id=self.root_id,
            stack_id=self.stack_id,
            stack_policy_body=self.stack_policy_body,
            stack_status=self.stack_status,
            stack_status_reason=self.stack_status_reason,
            tags=self.tags,
            template_body=self.template_body,
            timeout_in_minutes=self.timeout_in_minutes)


def get_stack(stack_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStackResult:
    """
    The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.
    """
    __args__ = dict()
    __args__['stackId'] = stack_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudformation:getStack', __args__, opts=opts, typ=GetStackResult).value

    return AwaitableGetStackResult(
        capabilities=pulumi.get(__ret__, 'capabilities'),
        change_set_id=pulumi.get(__ret__, 'change_set_id'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        disable_rollback=pulumi.get(__ret__, 'disable_rollback'),
        enable_termination_protection=pulumi.get(__ret__, 'enable_termination_protection'),
        last_update_time=pulumi.get(__ret__, 'last_update_time'),
        notification_arns=pulumi.get(__ret__, 'notification_arns'),
        outputs=pulumi.get(__ret__, 'outputs'),
        parameters=pulumi.get(__ret__, 'parameters'),
        parent_id=pulumi.get(__ret__, 'parent_id'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        root_id=pulumi.get(__ret__, 'root_id'),
        stack_id=pulumi.get(__ret__, 'stack_id'),
        stack_policy_body=pulumi.get(__ret__, 'stack_policy_body'),
        stack_status=pulumi.get(__ret__, 'stack_status'),
        stack_status_reason=pulumi.get(__ret__, 'stack_status_reason'),
        tags=pulumi.get(__ret__, 'tags'),
        template_body=pulumi.get(__ret__, 'template_body'),
        timeout_in_minutes=pulumi.get(__ret__, 'timeout_in_minutes'))


@_utilities.lift_output_func(get_stack)
def get_stack_output(stack_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStackResult]:
    """
    The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.
    """
    ...
