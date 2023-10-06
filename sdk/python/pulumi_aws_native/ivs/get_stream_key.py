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
    'GetStreamKeyResult',
    'AwaitableGetStreamKeyResult',
    'get_stream_key',
    'get_stream_key_output',
]

@pulumi.output_type
class GetStreamKeyResult:
    def __init__(__self__, arn=None, tags=None, value=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.StreamKeyTag']]:
        """
        A list of key-value pairs that contain metadata for the asset model.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Stream-key value.
        """
        return pulumi.get(self, "value")


class AwaitableGetStreamKeyResult(GetStreamKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamKeyResult(
            arn=self.arn,
            tags=self.tags,
            value=self.value)


def get_stream_key(arn: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamKeyResult:
    """
    Resource Type definition for AWS::IVS::StreamKey


    :param str arn: Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ivs:getStreamKey', __args__, opts=opts, typ=GetStreamKeyResult).value

    return AwaitableGetStreamKeyResult(
        arn=pulumi.get(__ret__, 'arn'),
        tags=pulumi.get(__ret__, 'tags'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_stream_key)
def get_stream_key_output(arn: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamKeyResult]:
    """
    Resource Type definition for AWS::IVS::StreamKey


    :param str arn: Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
    """
    ...
