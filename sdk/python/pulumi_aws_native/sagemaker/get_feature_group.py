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
from ._enums import *

__all__ = [
    'GetFeatureGroupResult',
    'AwaitableGetFeatureGroupResult',
    'get_feature_group',
    'get_feature_group_output',
]

@pulumi.output_type
class GetFeatureGroupResult:
    def __init__(__self__, creation_time=None, feature_definitions=None, feature_group_status=None, throughput_config=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if feature_definitions and not isinstance(feature_definitions, list):
            raise TypeError("Expected argument 'feature_definitions' to be a list")
        pulumi.set(__self__, "feature_definitions", feature_definitions)
        if feature_group_status and not isinstance(feature_group_status, str):
            raise TypeError("Expected argument 'feature_group_status' to be a str")
        pulumi.set(__self__, "feature_group_status", feature_group_status)
        if throughput_config and not isinstance(throughput_config, dict):
            raise TypeError("Expected argument 'throughput_config' to be a dict")
        pulumi.set(__self__, "throughput_config", throughput_config)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        A timestamp of FeatureGroup creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> Optional[Sequence['outputs.FeatureGroupFeatureDefinition']]:
        """
        An Array of Feature Definition
        """
        return pulumi.get(self, "feature_definitions")

    @property
    @pulumi.getter(name="featureGroupStatus")
    def feature_group_status(self) -> Optional[str]:
        """
        The status of the feature group.
        """
        return pulumi.get(self, "feature_group_status")

    @property
    @pulumi.getter(name="throughputConfig")
    def throughput_config(self) -> Optional['outputs.FeatureGroupThroughputConfig']:
        return pulumi.get(self, "throughput_config")


class AwaitableGetFeatureGroupResult(GetFeatureGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFeatureGroupResult(
            creation_time=self.creation_time,
            feature_definitions=self.feature_definitions,
            feature_group_status=self.feature_group_status,
            throughput_config=self.throughput_config)


def get_feature_group(feature_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFeatureGroupResult:
    """
    Resource Type definition for AWS::SageMaker::FeatureGroup


    :param str feature_group_name: The Name of the FeatureGroup.
    """
    __args__ = dict()
    __args__['featureGroupName'] = feature_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getFeatureGroup', __args__, opts=opts, typ=GetFeatureGroupResult).value

    return AwaitableGetFeatureGroupResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        feature_definitions=pulumi.get(__ret__, 'feature_definitions'),
        feature_group_status=pulumi.get(__ret__, 'feature_group_status'),
        throughput_config=pulumi.get(__ret__, 'throughput_config'))


@_utilities.lift_output_func(get_feature_group)
def get_feature_group_output(feature_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFeatureGroupResult]:
    """
    Resource Type definition for AWS::SageMaker::FeatureGroup


    :param str feature_group_name: The Name of the FeatureGroup.
    """
    ...
