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
    'GetInfrastructureConfigurationResult',
    'AwaitableGetInfrastructureConfigurationResult',
    'get_infrastructure_configuration',
    'get_infrastructure_configuration_output',
]

@pulumi.output_type
class GetInfrastructureConfigurationResult:
    def __init__(__self__, arn=None, description=None, instance_metadata_options=None, instance_profile_name=None, instance_types=None, key_pair=None, logging=None, resource_tags=None, security_group_ids=None, sns_topic_arn=None, subnet_id=None, tags=None, terminate_instance_on_failure=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if instance_metadata_options and not isinstance(instance_metadata_options, dict):
            raise TypeError("Expected argument 'instance_metadata_options' to be a dict")
        pulumi.set(__self__, "instance_metadata_options", instance_metadata_options)
        if instance_profile_name and not isinstance(instance_profile_name, str):
            raise TypeError("Expected argument 'instance_profile_name' to be a str")
        pulumi.set(__self__, "instance_profile_name", instance_profile_name)
        if instance_types and not isinstance(instance_types, list):
            raise TypeError("Expected argument 'instance_types' to be a list")
        pulumi.set(__self__, "instance_types", instance_types)
        if key_pair and not isinstance(key_pair, str):
            raise TypeError("Expected argument 'key_pair' to be a str")
        pulumi.set(__self__, "key_pair", key_pair)
        if logging and not isinstance(logging, dict):
            raise TypeError("Expected argument 'logging' to be a dict")
        pulumi.set(__self__, "logging", logging)
        if resource_tags and not isinstance(resource_tags, dict):
            raise TypeError("Expected argument 'resource_tags' to be a dict")
        pulumi.set(__self__, "resource_tags", resource_tags)
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        if sns_topic_arn and not isinstance(sns_topic_arn, str):
            raise TypeError("Expected argument 'sns_topic_arn' to be a str")
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if terminate_instance_on_failure and not isinstance(terminate_instance_on_failure, bool):
            raise TypeError("Expected argument 'terminate_instance_on_failure' to be a bool")
        pulumi.set(__self__, "terminate_instance_on_failure", terminate_instance_on_failure)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the infrastructure configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the infrastructure configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceMetadataOptions")
    def instance_metadata_options(self) -> Optional['outputs.InfrastructureConfigurationInstanceMetadataOptions']:
        """
        The instance metadata option settings for the infrastructure configuration.
        """
        return pulumi.get(self, "instance_metadata_options")

    @property
    @pulumi.getter(name="instanceProfileName")
    def instance_profile_name(self) -> Optional[str]:
        """
        The instance profile of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_profile_name")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[Sequence[str]]:
        """
        The instance types of the infrastructure configuration.
        """
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> Optional[str]:
        """
        The EC2 key pair of the infrastructure configuration..
        """
        return pulumi.get(self, "key_pair")

    @property
    @pulumi.getter
    def logging(self) -> Optional['outputs.InfrastructureConfigurationLogging']:
        """
        The logging configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Any]:
        """
        The tags attached to the resource created by Image Builder.
        """
        return pulumi.get(self, "resource_tags")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        """
        The security group IDs of the infrastructure configuration.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        """
        The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
        """
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The subnet ID of the infrastructure configuration.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(self) -> Optional[bool]:
        """
        The terminate instance on failure configuration of the infrastructure configuration.
        """
        return pulumi.get(self, "terminate_instance_on_failure")


class AwaitableGetInfrastructureConfigurationResult(GetInfrastructureConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInfrastructureConfigurationResult(
            arn=self.arn,
            description=self.description,
            instance_metadata_options=self.instance_metadata_options,
            instance_profile_name=self.instance_profile_name,
            instance_types=self.instance_types,
            key_pair=self.key_pair,
            logging=self.logging,
            resource_tags=self.resource_tags,
            security_group_ids=self.security_group_ids,
            sns_topic_arn=self.sns_topic_arn,
            subnet_id=self.subnet_id,
            tags=self.tags,
            terminate_instance_on_failure=self.terminate_instance_on_failure)


def get_infrastructure_configuration(arn: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInfrastructureConfigurationResult:
    """
    Resource schema for AWS::ImageBuilder::InfrastructureConfiguration


    :param str arn: The Amazon Resource Name (ARN) of the infrastructure configuration.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:imagebuilder:getInfrastructureConfiguration', __args__, opts=opts, typ=GetInfrastructureConfigurationResult).value

    return AwaitableGetInfrastructureConfigurationResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        instance_metadata_options=pulumi.get(__ret__, 'instance_metadata_options'),
        instance_profile_name=pulumi.get(__ret__, 'instance_profile_name'),
        instance_types=pulumi.get(__ret__, 'instance_types'),
        key_pair=pulumi.get(__ret__, 'key_pair'),
        logging=pulumi.get(__ret__, 'logging'),
        resource_tags=pulumi.get(__ret__, 'resource_tags'),
        security_group_ids=pulumi.get(__ret__, 'security_group_ids'),
        sns_topic_arn=pulumi.get(__ret__, 'sns_topic_arn'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        tags=pulumi.get(__ret__, 'tags'),
        terminate_instance_on_failure=pulumi.get(__ret__, 'terminate_instance_on_failure'))


@_utilities.lift_output_func(get_infrastructure_configuration)
def get_infrastructure_configuration_output(arn: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInfrastructureConfigurationResult]:
    """
    Resource schema for AWS::ImageBuilder::InfrastructureConfiguration


    :param str arn: The Amazon Resource Name (ARN) of the infrastructure configuration.
    """
    ...
