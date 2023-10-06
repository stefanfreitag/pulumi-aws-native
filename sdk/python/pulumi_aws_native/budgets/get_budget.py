# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetBudgetResult',
    'AwaitableGetBudgetResult',
    'get_budget',
    'get_budget_output',
]

@pulumi.output_type
class GetBudgetResult:
    def __init__(__self__, budget=None, id=None):
        if budget and not isinstance(budget, dict):
            raise TypeError("Expected argument 'budget' to be a dict")
        pulumi.set(__self__, "budget", budget)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def budget(self) -> Optional['outputs.BudgetData']:
        return pulumi.get(self, "budget")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetBudgetResult(GetBudgetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBudgetResult(
            budget=self.budget,
            id=self.id)


def get_budget(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBudgetResult:
    """
    Resource Type definition for AWS::Budgets::Budget
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:budgets:getBudget', __args__, opts=opts, typ=GetBudgetResult).value

    return AwaitableGetBudgetResult(
        budget=pulumi.get(__ret__, 'budget'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_budget)
def get_budget_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBudgetResult]:
    """
    Resource Type definition for AWS::Budgets::Budget
    """
    ...
