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
    'GetEventBusPolicyResult',
    'AwaitableGetEventBusPolicyResult',
    'get_event_bus_policy',
    'get_event_bus_policy_output',
]

@pulumi.output_type
class GetEventBusPolicyResult:
    def __init__(__self__, action=None, condition=None, id=None, principal=None, statement=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if condition and not isinstance(condition, dict):
            raise TypeError("Expected argument 'condition' to be a dict")
        pulumi.set(__self__, "condition", condition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if principal and not isinstance(principal, str):
            raise TypeError("Expected argument 'principal' to be a str")
        pulumi.set(__self__, "principal", principal)
        if statement and not isinstance(statement, dict):
            raise TypeError("Expected argument 'statement' to be a dict")
        pulumi.set(__self__, "statement", statement)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def condition(self) -> Optional['outputs.EventBusPolicyCondition']:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def principal(self) -> Optional[str]:
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter
    def statement(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Events::EventBusPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "statement")


class AwaitableGetEventBusPolicyResult(GetEventBusPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventBusPolicyResult(
            action=self.action,
            condition=self.condition,
            id=self.id,
            principal=self.principal,
            statement=self.statement)


def get_event_bus_policy(id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventBusPolicyResult:
    """
    Resource Type definition for AWS::Events::EventBusPolicy
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:events:getEventBusPolicy', __args__, opts=opts, typ=GetEventBusPolicyResult).value

    return AwaitableGetEventBusPolicyResult(
        action=pulumi.get(__ret__, 'action'),
        condition=pulumi.get(__ret__, 'condition'),
        id=pulumi.get(__ret__, 'id'),
        principal=pulumi.get(__ret__, 'principal'),
        statement=pulumi.get(__ret__, 'statement'))


@_utilities.lift_output_func(get_event_bus_policy)
def get_event_bus_policy_output(id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventBusPolicyResult]:
    """
    Resource Type definition for AWS::Events::EventBusPolicy
    """
    ...
