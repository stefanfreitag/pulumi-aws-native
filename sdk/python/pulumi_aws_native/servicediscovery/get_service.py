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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    def __init__(__self__, arn=None, description=None, dns_config=None, health_check_config=None, id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_config and not isinstance(dns_config, dict):
            raise TypeError("Expected argument 'dns_config' to be a dict")
        pulumi.set(__self__, "dns_config", dns_config)
        if health_check_config and not isinstance(health_check_config, dict):
            raise TypeError("Expected argument 'health_check_config' to be a dict")
        pulumi.set(__self__, "health_check_config", health_check_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional['outputs.ServiceDnsConfig']:
        return pulumi.get(self, "dns_config")

    @property
    @pulumi.getter(name="healthCheckConfig")
    def health_check_config(self) -> Optional['outputs.ServiceHealthCheckConfig']:
        return pulumi.get(self, "health_check_config")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            arn=self.arn,
            description=self.description,
            dns_config=self.dns_config,
            health_check_config=self.health_check_config,
            id=self.id,
            tags=self.tags)


def get_service(id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Resource Type definition for AWS::ServiceDiscovery::Service
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicediscovery:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        dns_config=pulumi.get(__ret__, 'dns_config'),
        health_check_config=pulumi.get(__ret__, 'health_check_config'),
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_service)
def get_service_output(id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Resource Type definition for AWS::ServiceDiscovery::Service
    """
    ...
