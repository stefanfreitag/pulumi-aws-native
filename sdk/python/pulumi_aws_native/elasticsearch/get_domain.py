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

__all__ = [
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    def __init__(__self__, access_policies=None, advanced_options=None, advanced_security_options=None, arn=None, cognito_options=None, domain_arn=None, domain_endpoint=None, domain_endpoint_options=None, ebs_options=None, elasticsearch_cluster_config=None, elasticsearch_version=None, encryption_at_rest_options=None, id=None, log_publishing_options=None, node_to_node_encryption_options=None, snapshot_options=None, tags=None, vpc_options=None):
        if access_policies and not isinstance(access_policies, dict):
            raise TypeError("Expected argument 'access_policies' to be a dict")
        pulumi.set(__self__, "access_policies", access_policies)
        if advanced_options and not isinstance(advanced_options, dict):
            raise TypeError("Expected argument 'advanced_options' to be a dict")
        pulumi.set(__self__, "advanced_options", advanced_options)
        if advanced_security_options and not isinstance(advanced_security_options, dict):
            raise TypeError("Expected argument 'advanced_security_options' to be a dict")
        pulumi.set(__self__, "advanced_security_options", advanced_security_options)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cognito_options and not isinstance(cognito_options, dict):
            raise TypeError("Expected argument 'cognito_options' to be a dict")
        pulumi.set(__self__, "cognito_options", cognito_options)
        if domain_arn and not isinstance(domain_arn, str):
            raise TypeError("Expected argument 'domain_arn' to be a str")
        pulumi.set(__self__, "domain_arn", domain_arn)
        if domain_endpoint and not isinstance(domain_endpoint, str):
            raise TypeError("Expected argument 'domain_endpoint' to be a str")
        pulumi.set(__self__, "domain_endpoint", domain_endpoint)
        if domain_endpoint_options and not isinstance(domain_endpoint_options, dict):
            raise TypeError("Expected argument 'domain_endpoint_options' to be a dict")
        pulumi.set(__self__, "domain_endpoint_options", domain_endpoint_options)
        if ebs_options and not isinstance(ebs_options, dict):
            raise TypeError("Expected argument 'ebs_options' to be a dict")
        pulumi.set(__self__, "ebs_options", ebs_options)
        if elasticsearch_cluster_config and not isinstance(elasticsearch_cluster_config, dict):
            raise TypeError("Expected argument 'elasticsearch_cluster_config' to be a dict")
        pulumi.set(__self__, "elasticsearch_cluster_config", elasticsearch_cluster_config)
        if elasticsearch_version and not isinstance(elasticsearch_version, str):
            raise TypeError("Expected argument 'elasticsearch_version' to be a str")
        pulumi.set(__self__, "elasticsearch_version", elasticsearch_version)
        if encryption_at_rest_options and not isinstance(encryption_at_rest_options, dict):
            raise TypeError("Expected argument 'encryption_at_rest_options' to be a dict")
        pulumi.set(__self__, "encryption_at_rest_options", encryption_at_rest_options)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_publishing_options and not isinstance(log_publishing_options, dict):
            raise TypeError("Expected argument 'log_publishing_options' to be a dict")
        pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if node_to_node_encryption_options and not isinstance(node_to_node_encryption_options, dict):
            raise TypeError("Expected argument 'node_to_node_encryption_options' to be a dict")
        pulumi.set(__self__, "node_to_node_encryption_options", node_to_node_encryption_options)
        if snapshot_options and not isinstance(snapshot_options, dict):
            raise TypeError("Expected argument 'snapshot_options' to be a dict")
        pulumi.set(__self__, "snapshot_options", snapshot_options)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_options and not isinstance(vpc_options, dict):
            raise TypeError("Expected argument 'vpc_options' to be a dict")
        pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Any]:
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Optional[Any]:
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Optional['outputs.DomainAdvancedSecurityOptionsInput']:
        return pulumi.get(self, "advanced_security_options")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional['outputs.DomainCognitoOptions']:
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[str]:
        return pulumi.get(self, "domain_arn")

    @property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "domain_endpoint")

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> Optional['outputs.DomainEndpointOptions']:
        return pulumi.get(self, "domain_endpoint_options")

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Optional['outputs.DomainEbsOptions']:
        return pulumi.get(self, "ebs_options")

    @property
    @pulumi.getter(name="elasticsearchClusterConfig")
    def elasticsearch_cluster_config(self) -> Optional['outputs.DomainElasticsearchClusterConfig']:
        return pulumi.get(self, "elasticsearch_cluster_config")

    @property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> Optional[str]:
        return pulumi.get(self, "elasticsearch_version")

    @property
    @pulumi.getter(name="encryptionAtRestOptions")
    def encryption_at_rest_options(self) -> Optional['outputs.DomainEncryptionAtRestOptions']:
        return pulumi.get(self, "encryption_at_rest_options")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[Any]:
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptionOptions")
    def node_to_node_encryption_options(self) -> Optional['outputs.DomainNodeToNodeEncryptionOptions']:
        return pulumi.get(self, "node_to_node_encryption_options")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional['outputs.DomainSnapshotOptions']:
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DomainTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional['outputs.DomainVpcOptions']:
        return pulumi.get(self, "vpc_options")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            access_policies=self.access_policies,
            advanced_options=self.advanced_options,
            advanced_security_options=self.advanced_security_options,
            arn=self.arn,
            cognito_options=self.cognito_options,
            domain_arn=self.domain_arn,
            domain_endpoint=self.domain_endpoint,
            domain_endpoint_options=self.domain_endpoint_options,
            ebs_options=self.ebs_options,
            elasticsearch_cluster_config=self.elasticsearch_cluster_config,
            elasticsearch_version=self.elasticsearch_version,
            encryption_at_rest_options=self.encryption_at_rest_options,
            id=self.id,
            log_publishing_options=self.log_publishing_options,
            node_to_node_encryption_options=self.node_to_node_encryption_options,
            snapshot_options=self.snapshot_options,
            tags=self.tags,
            vpc_options=self.vpc_options)


def get_domain(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Resource Type definition for AWS::Elasticsearch::Domain
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticsearch:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        access_policies=pulumi.get(__ret__, 'access_policies'),
        advanced_options=pulumi.get(__ret__, 'advanced_options'),
        advanced_security_options=pulumi.get(__ret__, 'advanced_security_options'),
        arn=pulumi.get(__ret__, 'arn'),
        cognito_options=pulumi.get(__ret__, 'cognito_options'),
        domain_arn=pulumi.get(__ret__, 'domain_arn'),
        domain_endpoint=pulumi.get(__ret__, 'domain_endpoint'),
        domain_endpoint_options=pulumi.get(__ret__, 'domain_endpoint_options'),
        ebs_options=pulumi.get(__ret__, 'ebs_options'),
        elasticsearch_cluster_config=pulumi.get(__ret__, 'elasticsearch_cluster_config'),
        elasticsearch_version=pulumi.get(__ret__, 'elasticsearch_version'),
        encryption_at_rest_options=pulumi.get(__ret__, 'encryption_at_rest_options'),
        id=pulumi.get(__ret__, 'id'),
        log_publishing_options=pulumi.get(__ret__, 'log_publishing_options'),
        node_to_node_encryption_options=pulumi.get(__ret__, 'node_to_node_encryption_options'),
        snapshot_options=pulumi.get(__ret__, 'snapshot_options'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_options=pulumi.get(__ret__, 'vpc_options'))


@_utilities.lift_output_func(get_domain)
def get_domain_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Resource Type definition for AWS::Elasticsearch::Domain
    """
    ...
