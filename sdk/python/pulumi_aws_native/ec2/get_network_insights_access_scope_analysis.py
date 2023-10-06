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
from ._enums import *

__all__ = [
    'GetNetworkInsightsAccessScopeAnalysisResult',
    'AwaitableGetNetworkInsightsAccessScopeAnalysisResult',
    'get_network_insights_access_scope_analysis',
    'get_network_insights_access_scope_analysis_output',
]

@pulumi.output_type
class GetNetworkInsightsAccessScopeAnalysisResult:
    def __init__(__self__, analyzed_eni_count=None, end_date=None, findings_found=None, network_insights_access_scope_analysis_arn=None, network_insights_access_scope_analysis_id=None, start_date=None, status=None, status_message=None, tags=None):
        if analyzed_eni_count and not isinstance(analyzed_eni_count, int):
            raise TypeError("Expected argument 'analyzed_eni_count' to be a int")
        pulumi.set(__self__, "analyzed_eni_count", analyzed_eni_count)
        if end_date and not isinstance(end_date, str):
            raise TypeError("Expected argument 'end_date' to be a str")
        pulumi.set(__self__, "end_date", end_date)
        if findings_found and not isinstance(findings_found, str):
            raise TypeError("Expected argument 'findings_found' to be a str")
        pulumi.set(__self__, "findings_found", findings_found)
        if network_insights_access_scope_analysis_arn and not isinstance(network_insights_access_scope_analysis_arn, str):
            raise TypeError("Expected argument 'network_insights_access_scope_analysis_arn' to be a str")
        pulumi.set(__self__, "network_insights_access_scope_analysis_arn", network_insights_access_scope_analysis_arn)
        if network_insights_access_scope_analysis_id and not isinstance(network_insights_access_scope_analysis_id, str):
            raise TypeError("Expected argument 'network_insights_access_scope_analysis_id' to be a str")
        pulumi.set(__self__, "network_insights_access_scope_analysis_id", network_insights_access_scope_analysis_id)
        if start_date and not isinstance(start_date, str):
            raise TypeError("Expected argument 'start_date' to be a str")
        pulumi.set(__self__, "start_date", start_date)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="analyzedEniCount")
    def analyzed_eni_count(self) -> Optional[int]:
        return pulumi.get(self, "analyzed_eni_count")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[str]:
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="findingsFound")
    def findings_found(self) -> Optional['NetworkInsightsAccessScopeAnalysisFindingsFound']:
        return pulumi.get(self, "findings_found")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeAnalysisArn")
    def network_insights_access_scope_analysis_arn(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_access_scope_analysis_arn")

    @property
    @pulumi.getter(name="networkInsightsAccessScopeAnalysisId")
    def network_insights_access_scope_analysis_id(self) -> Optional[str]:
        return pulumi.get(self, "network_insights_access_scope_analysis_id")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[str]:
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> Optional['NetworkInsightsAccessScopeAnalysisStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[str]:
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.NetworkInsightsAccessScopeAnalysisTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetNetworkInsightsAccessScopeAnalysisResult(GetNetworkInsightsAccessScopeAnalysisResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInsightsAccessScopeAnalysisResult(
            analyzed_eni_count=self.analyzed_eni_count,
            end_date=self.end_date,
            findings_found=self.findings_found,
            network_insights_access_scope_analysis_arn=self.network_insights_access_scope_analysis_arn,
            network_insights_access_scope_analysis_id=self.network_insights_access_scope_analysis_id,
            start_date=self.start_date,
            status=self.status,
            status_message=self.status_message,
            tags=self.tags)


def get_network_insights_access_scope_analysis(network_insights_access_scope_analysis_id: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInsightsAccessScopeAnalysisResult:
    """
    Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
    """
    __args__ = dict()
    __args__['networkInsightsAccessScopeAnalysisId'] = network_insights_access_scope_analysis_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkInsightsAccessScopeAnalysis', __args__, opts=opts, typ=GetNetworkInsightsAccessScopeAnalysisResult).value

    return AwaitableGetNetworkInsightsAccessScopeAnalysisResult(
        analyzed_eni_count=pulumi.get(__ret__, 'analyzed_eni_count'),
        end_date=pulumi.get(__ret__, 'end_date'),
        findings_found=pulumi.get(__ret__, 'findings_found'),
        network_insights_access_scope_analysis_arn=pulumi.get(__ret__, 'network_insights_access_scope_analysis_arn'),
        network_insights_access_scope_analysis_id=pulumi.get(__ret__, 'network_insights_access_scope_analysis_id'),
        start_date=pulumi.get(__ret__, 'start_date'),
        status=pulumi.get(__ret__, 'status'),
        status_message=pulumi.get(__ret__, 'status_message'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_insights_access_scope_analysis)
def get_network_insights_access_scope_analysis_output(network_insights_access_scope_analysis_id: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInsightsAccessScopeAnalysisResult]:
    """
    Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
    """
    ...
