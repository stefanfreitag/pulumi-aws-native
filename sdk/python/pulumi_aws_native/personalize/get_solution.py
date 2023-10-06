# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSolutionResult',
    'AwaitableGetSolutionResult',
    'get_solution',
    'get_solution_output',
]

@pulumi.output_type
class GetSolutionResult:
    def __init__(__self__, solution_arn=None):
        if solution_arn and not isinstance(solution_arn, str):
            raise TypeError("Expected argument 'solution_arn' to be a str")
        pulumi.set(__self__, "solution_arn", solution_arn)

    @property
    @pulumi.getter(name="solutionArn")
    def solution_arn(self) -> Optional[str]:
        return pulumi.get(self, "solution_arn")


class AwaitableGetSolutionResult(GetSolutionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSolutionResult(
            solution_arn=self.solution_arn)


def get_solution(solution_arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSolutionResult:
    """
    Resource schema for AWS::Personalize::Solution.
    """
    __args__ = dict()
    __args__['solutionArn'] = solution_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:personalize:getSolution', __args__, opts=opts, typ=GetSolutionResult).value

    return AwaitableGetSolutionResult(
        solution_arn=pulumi.get(__ret__, 'solution_arn'))


@_utilities.lift_output_func(get_solution)
def get_solution_output(solution_arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSolutionResult]:
    """
    Resource schema for AWS::Personalize::Solution.
    """
    ...
