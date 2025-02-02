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
from .. import outputs as _root_outputs

__all__ = [
    'GetChannelResult',
    'AwaitableGetChannelResult',
    'get_channel',
    'get_channel_output',
]

@pulumi.output_type
class GetChannelResult:
    def __init__(__self__, arn=None, created_at=None, description=None, ingest_endpoints=None, modified_at=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if ingest_endpoints and not isinstance(ingest_endpoints, list):
            raise TypeError("Expected argument 'ingest_endpoints' to be a list")
        pulumi.set(__self__, "ingest_endpoints", ingest_endpoints)
        if modified_at and not isinstance(modified_at, str):
            raise TypeError("Expected argument 'modified_at' to be a str")
        pulumi.set(__self__, "modified_at", modified_at)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ingestEndpoints")
    def ingest_endpoints(self) -> Optional[Sequence['outputs.ChannelIngestEndpoint']]:
        return pulumi.get(self, "ingest_endpoints")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[str]:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetChannelResult(GetChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChannelResult(
            arn=self.arn,
            created_at=self.created_at,
            description=self.description,
            ingest_endpoints=self.ingest_endpoints,
            modified_at=self.modified_at,
            tags=self.tags)


def get_channel(arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChannelResult:
    """
    Definition of AWS::MediaPackageV2::Channel Resource Type
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackagev2:getChannel', __args__, opts=opts, typ=GetChannelResult).value

    return AwaitableGetChannelResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        ingest_endpoints=pulumi.get(__ret__, 'ingest_endpoints'),
        modified_at=pulumi.get(__ret__, 'modified_at'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_channel)
def get_channel_output(arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetChannelResult]:
    """
    Definition of AWS::MediaPackageV2::Channel Resource Type
    """
    ...
