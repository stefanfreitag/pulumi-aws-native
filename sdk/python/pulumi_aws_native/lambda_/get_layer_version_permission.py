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
    'GetLayerVersionPermissionResult',
    'AwaitableGetLayerVersionPermissionResult',
    'get_layer_version_permission',
    'get_layer_version_permission_output',
]

@pulumi.output_type
class GetLayerVersionPermissionResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID generated by service
        """
        return pulumi.get(self, "id")


class AwaitableGetLayerVersionPermissionResult(GetLayerVersionPermissionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLayerVersionPermissionResult(
            id=self.id)


def get_layer_version_permission(id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLayerVersionPermissionResult:
    """
    Schema for Lambda LayerVersionPermission


    :param str id: ID generated by service
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lambda:getLayerVersionPermission', __args__, opts=opts, typ=GetLayerVersionPermissionResult).value

    return AwaitableGetLayerVersionPermissionResult(
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_layer_version_permission)
def get_layer_version_permission_output(id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLayerVersionPermissionResult]:
    """
    Schema for Lambda LayerVersionPermission


    :param str id: ID generated by service
    """
    ...
