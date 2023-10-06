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
    'GetReplicationConfigResult',
    'AwaitableGetReplicationConfigResult',
    'get_replication_config',
    'get_replication_config_output',
]

@pulumi.output_type
class GetReplicationConfigResult:
    def __init__(__self__, compute_config=None, replication_config_arn=None, replication_config_identifier=None, replication_settings=None, replication_type=None, resource_identifier=None, source_endpoint_arn=None, supplemental_settings=None, table_mappings=None, tags=None, target_endpoint_arn=None):
        if compute_config and not isinstance(compute_config, dict):
            raise TypeError("Expected argument 'compute_config' to be a dict")
        pulumi.set(__self__, "compute_config", compute_config)
        if replication_config_arn and not isinstance(replication_config_arn, str):
            raise TypeError("Expected argument 'replication_config_arn' to be a str")
        pulumi.set(__self__, "replication_config_arn", replication_config_arn)
        if replication_config_identifier and not isinstance(replication_config_identifier, str):
            raise TypeError("Expected argument 'replication_config_identifier' to be a str")
        pulumi.set(__self__, "replication_config_identifier", replication_config_identifier)
        if replication_settings and not isinstance(replication_settings, dict):
            raise TypeError("Expected argument 'replication_settings' to be a dict")
        pulumi.set(__self__, "replication_settings", replication_settings)
        if replication_type and not isinstance(replication_type, str):
            raise TypeError("Expected argument 'replication_type' to be a str")
        pulumi.set(__self__, "replication_type", replication_type)
        if resource_identifier and not isinstance(resource_identifier, str):
            raise TypeError("Expected argument 'resource_identifier' to be a str")
        pulumi.set(__self__, "resource_identifier", resource_identifier)
        if source_endpoint_arn and not isinstance(source_endpoint_arn, str):
            raise TypeError("Expected argument 'source_endpoint_arn' to be a str")
        pulumi.set(__self__, "source_endpoint_arn", source_endpoint_arn)
        if supplemental_settings and not isinstance(supplemental_settings, dict):
            raise TypeError("Expected argument 'supplemental_settings' to be a dict")
        pulumi.set(__self__, "supplemental_settings", supplemental_settings)
        if table_mappings and not isinstance(table_mappings, dict):
            raise TypeError("Expected argument 'table_mappings' to be a dict")
        pulumi.set(__self__, "table_mappings", table_mappings)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if target_endpoint_arn and not isinstance(target_endpoint_arn, str):
            raise TypeError("Expected argument 'target_endpoint_arn' to be a str")
        pulumi.set(__self__, "target_endpoint_arn", target_endpoint_arn)

    @property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> Optional['outputs.ReplicationConfigComputeConfig']:
        return pulumi.get(self, "compute_config")

    @property
    @pulumi.getter(name="replicationConfigArn")
    def replication_config_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Replication Config
        """
        return pulumi.get(self, "replication_config_arn")

    @property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> Optional[str]:
        """
        A unique identifier of replication configuration
        """
        return pulumi.get(self, "replication_config_identifier")

    @property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> Optional[Any]:
        """
        JSON settings for Servereless replications that are provisioned using this replication configuration
        """
        return pulumi.get(self, "replication_settings")

    @property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> Optional['ReplicationConfigReplicationType']:
        """
        The type of AWS DMS Serverless replication to provision using this replication configuration
        """
        return pulumi.get(self, "replication_type")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[str]:
        """
        A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
        """
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "source_endpoint_arn")

    @property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> Optional[Any]:
        """
        JSON settings for specifying supplemental data
        """
        return pulumi.get(self, "supplemental_settings")

    @property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> Optional[Any]:
        """
        JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
        """
        return pulumi.get(self, "table_mappings")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ReplicationConfigTag']]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
        """
        return pulumi.get(self, "target_endpoint_arn")


class AwaitableGetReplicationConfigResult(GetReplicationConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationConfigResult(
            compute_config=self.compute_config,
            replication_config_arn=self.replication_config_arn,
            replication_config_identifier=self.replication_config_identifier,
            replication_settings=self.replication_settings,
            replication_type=self.replication_type,
            resource_identifier=self.resource_identifier,
            source_endpoint_arn=self.source_endpoint_arn,
            supplemental_settings=self.supplemental_settings,
            table_mappings=self.table_mappings,
            tags=self.tags,
            target_endpoint_arn=self.target_endpoint_arn)


def get_replication_config(replication_config_arn: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationConfigResult:
    """
    A replication configuration that you later provide to configure and start a AWS DMS Serverless replication


    :param str replication_config_arn: The Amazon Resource Name (ARN) of the Replication Config
    """
    __args__ = dict()
    __args__['replicationConfigArn'] = replication_config_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:dms:getReplicationConfig', __args__, opts=opts, typ=GetReplicationConfigResult).value

    return AwaitableGetReplicationConfigResult(
        compute_config=pulumi.get(__ret__, 'compute_config'),
        replication_config_arn=pulumi.get(__ret__, 'replication_config_arn'),
        replication_config_identifier=pulumi.get(__ret__, 'replication_config_identifier'),
        replication_settings=pulumi.get(__ret__, 'replication_settings'),
        replication_type=pulumi.get(__ret__, 'replication_type'),
        resource_identifier=pulumi.get(__ret__, 'resource_identifier'),
        source_endpoint_arn=pulumi.get(__ret__, 'source_endpoint_arn'),
        supplemental_settings=pulumi.get(__ret__, 'supplemental_settings'),
        table_mappings=pulumi.get(__ret__, 'table_mappings'),
        tags=pulumi.get(__ret__, 'tags'),
        target_endpoint_arn=pulumi.get(__ret__, 'target_endpoint_arn'))


@_utilities.lift_output_func(get_replication_config)
def get_replication_config_output(replication_config_arn: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationConfigResult]:
    """
    A replication configuration that you later provide to configure and start a AWS DMS Serverless replication


    :param str replication_config_arn: The Amazon Resource Name (ARN) of the Replication Config
    """
    ...
