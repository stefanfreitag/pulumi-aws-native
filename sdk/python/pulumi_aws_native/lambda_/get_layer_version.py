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
    'GetLayerVersionResult',
    'AwaitableGetLayerVersionResult',
    'get_layer_version',
    'get_layer_version_output',
]

@pulumi.output_type
class GetLayerVersionResult:
    def __init__(__self__, layer_version_arn=None):
        if layer_version_arn and not isinstance(layer_version_arn, str):
            raise TypeError("Expected argument 'layer_version_arn' to be a str")
        pulumi.set(__self__, "layer_version_arn", layer_version_arn)

    @property
    @pulumi.getter(name="layerVersionArn")
    def layer_version_arn(self) -> Optional[str]:
        return pulumi.get(self, "layer_version_arn")


class AwaitableGetLayerVersionResult(GetLayerVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLayerVersionResult(
            layer_version_arn=self.layer_version_arn)


def get_layer_version(layer_version_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLayerVersionResult:
    """
    Resource Type definition for AWS::Lambda::LayerVersion
    """
    __args__ = dict()
    __args__['layerVersionArn'] = layer_version_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lambda:getLayerVersion', __args__, opts=opts, typ=GetLayerVersionResult).value

    return AwaitableGetLayerVersionResult(
        layer_version_arn=pulumi.get(__ret__, 'layer_version_arn'))


@_utilities.lift_output_func(get_layer_version)
def get_layer_version_output(layer_version_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLayerVersionResult]:
    """
    Resource Type definition for AWS::Lambda::LayerVersion
    """
    ...
