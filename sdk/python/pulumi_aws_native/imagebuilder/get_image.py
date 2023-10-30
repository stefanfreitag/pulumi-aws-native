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
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
    'get_image_output',
]

@pulumi.output_type
class GetImageResult:
    def __init__(__self__, arn=None, image_id=None, image_uri=None, name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if image_uri and not isinstance(image_uri, str):
            raise TypeError("Expected argument 'image_uri' to be a str")
        pulumi.set(__self__, "image_uri", image_uri)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the image.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[str]:
        """
        The AMI ID of the EC2 AMI in current region.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[str]:
        """
        URI for containers created in current Region with default ECR image tag
        """
        return pulumi.get(self, "image_uri")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the image.
        """
        return pulumi.get(self, "name")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            arn=self.arn,
            image_id=self.image_id,
            image_uri=self.image_uri,
            name=self.name)


def get_image(arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    Resource schema for AWS::ImageBuilder::Image


    :param str arn: The Amazon Resource Name (ARN) of the image.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:imagebuilder:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        arn=pulumi.get(__ret__, 'arn'),
        image_id=pulumi.get(__ret__, 'image_id'),
        image_uri=pulumi.get(__ret__, 'image_uri'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_image)
def get_image_output(arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageResult]:
    """
    Resource schema for AWS::ImageBuilder::Image


    :param str arn: The Amazon Resource Name (ARN) of the image.
    """
    ...
