# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetWaitConditionResult',
    'AwaitableGetWaitConditionResult',
    'get_wait_condition',
    'get_wait_condition_output',
]

@pulumi.output_type
class GetWaitConditionResult:
    def __init__(__self__, count=None, data=None, handle=None, id=None, timeout=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if data and not isinstance(data, dict):
            raise TypeError("Expected argument 'data' to be a dict")
        pulumi.set(__self__, "data", data)
        if handle and not isinstance(handle, str):
            raise TypeError("Expected argument 'handle' to be a str")
        pulumi.set(__self__, "handle", handle)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if timeout and not isinstance(timeout, str):
            raise TypeError("Expected argument 'timeout' to be a str")
        pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def data(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CloudFormation::WaitCondition` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def handle(self) -> Optional[str]:
        return pulumi.get(self, "handle")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def timeout(self) -> Optional[str]:
        return pulumi.get(self, "timeout")


class AwaitableGetWaitConditionResult(GetWaitConditionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWaitConditionResult(
            count=self.count,
            data=self.data,
            handle=self.handle,
            id=self.id,
            timeout=self.timeout)


def get_wait_condition(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWaitConditionResult:
    """
    Resource Type definition for AWS::CloudFormation::WaitCondition
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudformation:getWaitCondition', __args__, opts=opts, typ=GetWaitConditionResult).value

    return AwaitableGetWaitConditionResult(
        count=pulumi.get(__ret__, 'count'),
        data=pulumi.get(__ret__, 'data'),
        handle=pulumi.get(__ret__, 'handle'),
        id=pulumi.get(__ret__, 'id'),
        timeout=pulumi.get(__ret__, 'timeout'))


@_utilities.lift_output_func(get_wait_condition)
def get_wait_condition_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWaitConditionResult]:
    """
    Resource Type definition for AWS::CloudFormation::WaitCondition
    """
    ...
