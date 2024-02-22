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
    'GetNetworkInsightsPathResult',
    'AwaitableGetNetworkInsightsPathResult',
    'get_network_insights_path',
    'get_network_insights_path_output',
]

@pulumi.output_type
class GetNetworkInsightsPathResult:
    def __init__(__self__, created_date=None, destination_arn=None, network_insights_path_arn=None, network_insights_path_id=None, source_arn=None, tags=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if destination_arn and not isinstance(destination_arn, str):
            raise TypeError("Expected argument 'destination_arn' to be a str")
        pulumi.set(__self__, "destination_arn", destination_arn)
        if network_insights_path_arn and not isinstance(network_insights_path_arn, str):
            raise TypeError("Expected argument 'network_insights_path_arn' to be a str")
        pulumi.set(__self__, "network_insights_path_arn", network_insights_path_arn)
        if network_insights_path_id and not isinstance(network_insights_path_id, str):
            raise TypeError("Expected argument 'network_insights_path_id' to be a str")
        pulumi.set(__self__, "network_insights_path_id", network_insights_path_id)
        if source_arn and not isinstance(source_arn, str):
            raise TypeError("Expected argument 'source_arn' to be a str")
        pulumi.set(__self__, "source_arn", source_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[str]:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[str]:
        return pulumi.get(self, "destination_arn")

    @property
    @pulumi.getter(name="networkInsightsPathArn")
    def network_insights_path_arn(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_path_arn")

    @property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_path_id")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[str]:
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetNetworkInsightsPathResult(GetNetworkInsightsPathResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInsightsPathResult(
            created_date=self.created_date,
            destination_arn=self.destination_arn,
            network_insights_path_arn=self.network_insights_path_arn,
            network_insights_path_id=self.network_insights_path_id,
            source_arn=self.source_arn,
            tags=self.tags)


def get_network_insights_path(network_insights_path_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInsightsPathResult:
    """
    Resource schema for AWS::EC2::NetworkInsightsPath
    """
    __args__ = dict()
    __args__['networkInsightsPathId'] = network_insights_path_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkInsightsPath', __args__, opts=opts, typ=GetNetworkInsightsPathResult).value

    return AwaitableGetNetworkInsightsPathResult(
        created_date=pulumi.get(__ret__, 'created_date'),
        destination_arn=pulumi.get(__ret__, 'destination_arn'),
        network_insights_path_arn=pulumi.get(__ret__, 'network_insights_path_arn'),
        network_insights_path_id=pulumi.get(__ret__, 'network_insights_path_id'),
        source_arn=pulumi.get(__ret__, 'source_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_insights_path)
def get_network_insights_path_output(network_insights_path_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInsightsPathResult]:
    """
    Resource schema for AWS::EC2::NetworkInsightsPath
    """
    ...
