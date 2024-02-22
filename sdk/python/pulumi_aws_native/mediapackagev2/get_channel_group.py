# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetChannelGroupResult',
    'AwaitableGetChannelGroupResult',
    'get_channel_group',
    'get_channel_group_output',
]

@pulumi.output_type
class GetChannelGroupResult:
    def __init__(__self__, arn=None, created_at=None, description=None, egress_domain=None, modified_at=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if egress_domain and not isinstance(egress_domain, str):
            raise TypeError("Expected argument 'egress_domain' to be a str")
        pulumi.set(__self__, "egress_domain", egress_domain)
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
    @pulumi.getter(name="egressDomain")
    def egress_domain(self) -> Optional[str]:
        return pulumi.get(self, "egress_domain")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[str]:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetChannelGroupResult(GetChannelGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChannelGroupResult(
            arn=self.arn,
            created_at=self.created_at,
            description=self.description,
            egress_domain=self.egress_domain,
            modified_at=self.modified_at,
            tags=self.tags)


def get_channel_group(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChannelGroupResult:
    """
    Definition of AWS::MediaPackageV2::ChannelGroup Resource Type
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackagev2:getChannelGroup', __args__, opts=opts, typ=GetChannelGroupResult).value

    return AwaitableGetChannelGroupResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        egress_domain=pulumi.get(__ret__, 'egress_domain'),
        modified_at=pulumi.get(__ret__, 'modified_at'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_channel_group)
def get_channel_group_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetChannelGroupResult]:
    """
    Definition of AWS::MediaPackageV2::ChannelGroup Resource Type
    """
    ...
