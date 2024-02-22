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
    'GetConfigurationAggregatorResult',
    'AwaitableGetConfigurationAggregatorResult',
    'get_configuration_aggregator',
    'get_configuration_aggregator_output',
]

@pulumi.output_type
class GetConfigurationAggregatorResult:
    def __init__(__self__, account_aggregation_sources=None, configuration_aggregator_arn=None, organization_aggregation_source=None, tags=None):
        if account_aggregation_sources and not isinstance(account_aggregation_sources, list):
            raise TypeError("Expected argument 'account_aggregation_sources' to be a list")
        pulumi.set(__self__, "account_aggregation_sources", account_aggregation_sources)
        if configuration_aggregator_arn and not isinstance(configuration_aggregator_arn, str):
            raise TypeError("Expected argument 'configuration_aggregator_arn' to be a str")
        pulumi.set(__self__, "configuration_aggregator_arn", configuration_aggregator_arn)
        if organization_aggregation_source and not isinstance(organization_aggregation_source, dict):
            raise TypeError("Expected argument 'organization_aggregation_source' to be a dict")
        pulumi.set(__self__, "organization_aggregation_source", organization_aggregation_source)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountAggregationSources")
    def account_aggregation_sources(self) -> Optional[Sequence['outputs.ConfigurationAggregatorAccountAggregationSource']]:
        return pulumi.get(self, "account_aggregation_sources")

    @property
    @pulumi.getter(name="configurationAggregatorArn")
    def configuration_aggregator_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the aggregator.
        """
        return pulumi.get(self, "configuration_aggregator_arn")

    @property
    @pulumi.getter(name="organizationAggregationSource")
    def organization_aggregation_source(self) -> Optional['outputs.ConfigurationAggregatorOrganizationAggregationSource']:
        return pulumi.get(self, "organization_aggregation_source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags for the configuration aggregator.
        """
        return pulumi.get(self, "tags")


class AwaitableGetConfigurationAggregatorResult(GetConfigurationAggregatorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationAggregatorResult(
            account_aggregation_sources=self.account_aggregation_sources,
            configuration_aggregator_arn=self.configuration_aggregator_arn,
            organization_aggregation_source=self.organization_aggregation_source,
            tags=self.tags)


def get_configuration_aggregator(configuration_aggregator_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationAggregatorResult:
    """
    Resource Type definition for AWS::Config::ConfigurationAggregator


    :param str configuration_aggregator_name: The name of the aggregator.
    """
    __args__ = dict()
    __args__['configurationAggregatorName'] = configuration_aggregator_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:configuration:getConfigurationAggregator', __args__, opts=opts, typ=GetConfigurationAggregatorResult).value

    return AwaitableGetConfigurationAggregatorResult(
        account_aggregation_sources=pulumi.get(__ret__, 'account_aggregation_sources'),
        configuration_aggregator_arn=pulumi.get(__ret__, 'configuration_aggregator_arn'),
        organization_aggregation_source=pulumi.get(__ret__, 'organization_aggregation_source'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_configuration_aggregator)
def get_configuration_aggregator_output(configuration_aggregator_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationAggregatorResult]:
    """
    Resource Type definition for AWS::Config::ConfigurationAggregator


    :param str configuration_aggregator_name: The name of the aggregator.
    """
    ...
