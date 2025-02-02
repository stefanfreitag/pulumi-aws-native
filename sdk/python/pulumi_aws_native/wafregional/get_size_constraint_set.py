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
    'GetSizeConstraintSetResult',
    'AwaitableGetSizeConstraintSetResult',
    'get_size_constraint_set',
    'get_size_constraint_set_output',
]

@pulumi.output_type
class GetSizeConstraintSetResult:
    def __init__(__self__, id=None, size_constraints=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if size_constraints and not isinstance(size_constraints, list):
            raise TypeError("Expected argument 'size_constraints' to be a list")
        pulumi.set(__self__, "size_constraints", size_constraints)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[Sequence['outputs.SizeConstraintSetSizeConstraint']]:
        return pulumi.get(self, "size_constraints")


class AwaitableGetSizeConstraintSetResult(GetSizeConstraintSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSizeConstraintSetResult(
            id=self.id,
            size_constraints=self.size_constraints)


def get_size_constraint_set(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSizeConstraintSetResult:
    """
    Resource Type definition for AWS::WAFRegional::SizeConstraintSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wafregional:getSizeConstraintSet', __args__, opts=opts, typ=GetSizeConstraintSetResult).value

    return AwaitableGetSizeConstraintSetResult(
        id=pulumi.get(__ret__, 'id'),
        size_constraints=pulumi.get(__ret__, 'size_constraints'))


@_utilities.lift_output_func(get_size_constraint_set)
def get_size_constraint_set_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSizeConstraintSetResult]:
    """
    Resource Type definition for AWS::WAFRegional::SizeConstraintSet
    """
    ...
