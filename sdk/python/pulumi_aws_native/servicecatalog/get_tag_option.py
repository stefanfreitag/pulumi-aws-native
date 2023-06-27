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
    'GetTagOptionResult',
    'AwaitableGetTagOptionResult',
    'get_tag_option',
    'get_tag_option_output',
]

@pulumi.output_type
class GetTagOptionResult:
    def __init__(__self__, active=None, id=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def active(self) -> Optional[bool]:
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetTagOptionResult(GetTagOptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagOptionResult(
            active=self.active,
            id=self.id)


def get_tag_option(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagOptionResult:
    """
    Resource Type definition for AWS::ServiceCatalog::TagOption
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getTagOption', __args__, opts=opts, typ=GetTagOptionResult).value

    return AwaitableGetTagOptionResult(
        active=__ret__.active,
        id=__ret__.id)


@_utilities.lift_output_func(get_tag_option)
def get_tag_option_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagOptionResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::TagOption
    """
    ...
