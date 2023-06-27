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
    'GetByteMatchSetResult',
    'AwaitableGetByteMatchSetResult',
    'get_byte_match_set',
    'get_byte_match_set_output',
]

@pulumi.output_type
class GetByteMatchSetResult:
    def __init__(__self__, byte_match_tuples=None, id=None):
        if byte_match_tuples and not isinstance(byte_match_tuples, list):
            raise TypeError("Expected argument 'byte_match_tuples' to be a list")
        pulumi.set(__self__, "byte_match_tuples", byte_match_tuples)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="byteMatchTuples")
    def byte_match_tuples(self) -> Optional[Sequence['outputs.ByteMatchSetByteMatchTuple']]:
        return pulumi.get(self, "byte_match_tuples")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetByteMatchSetResult(GetByteMatchSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetByteMatchSetResult(
            byte_match_tuples=self.byte_match_tuples,
            id=self.id)


def get_byte_match_set(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetByteMatchSetResult:
    """
    Resource Type definition for AWS::WAFRegional::ByteMatchSet
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wafregional:getByteMatchSet', __args__, opts=opts, typ=GetByteMatchSetResult).value

    return AwaitableGetByteMatchSetResult(
        byte_match_tuples=__ret__.byte_match_tuples,
        id=__ret__.id)


@_utilities.lift_output_func(get_byte_match_set)
def get_byte_match_set_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetByteMatchSetResult]:
    """
    Resource Type definition for AWS::WAFRegional::ByteMatchSet
    """
    ...
