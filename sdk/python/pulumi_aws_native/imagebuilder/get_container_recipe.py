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
    'GetContainerRecipeResult',
    'AwaitableGetContainerRecipeResult',
    'get_container_recipe',
    'get_container_recipe_output',
]

@pulumi.output_type
class GetContainerRecipeResult:
    def __init__(__self__, arn=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the container recipe.
        """
        return pulumi.get(self, "arn")


class AwaitableGetContainerRecipeResult(GetContainerRecipeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerRecipeResult(
            arn=self.arn)


def get_container_recipe(arn: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerRecipeResult:
    """
    Resource schema for AWS::ImageBuilder::ContainerRecipe


    :param str arn: The Amazon Resource Name (ARN) of the container recipe.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:imagebuilder:getContainerRecipe', __args__, opts=opts, typ=GetContainerRecipeResult).value

    return AwaitableGetContainerRecipeResult(
        arn=pulumi.get(__ret__, 'arn'))


@_utilities.lift_output_func(get_container_recipe)
def get_container_recipe_output(arn: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerRecipeResult]:
    """
    Resource schema for AWS::ImageBuilder::ContainerRecipe


    :param str arn: The Amazon Resource Name (ARN) of the container recipe.
    """
    ...
