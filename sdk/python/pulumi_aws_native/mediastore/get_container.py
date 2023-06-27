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
    'GetContainerResult',
    'AwaitableGetContainerResult',
    'get_container',
    'get_container_output',
]

@pulumi.output_type
class GetContainerResult:
    def __init__(__self__, access_logging_enabled=None, cors_policy=None, endpoint=None, id=None, lifecycle_policy=None, metric_policy=None, policy=None, tags=None):
        if access_logging_enabled and not isinstance(access_logging_enabled, bool):
            raise TypeError("Expected argument 'access_logging_enabled' to be a bool")
        pulumi.set(__self__, "access_logging_enabled", access_logging_enabled)
        if cors_policy and not isinstance(cors_policy, list):
            raise TypeError("Expected argument 'cors_policy' to be a list")
        pulumi.set(__self__, "cors_policy", cors_policy)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_policy and not isinstance(lifecycle_policy, str):
            raise TypeError("Expected argument 'lifecycle_policy' to be a str")
        pulumi.set(__self__, "lifecycle_policy", lifecycle_policy)
        if metric_policy and not isinstance(metric_policy, dict):
            raise TypeError("Expected argument 'metric_policy' to be a dict")
        pulumi.set(__self__, "metric_policy", metric_policy)
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        pulumi.set(__self__, "policy", policy)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessLoggingEnabled")
    def access_logging_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "access_logging_enabled")

    @property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> Optional[Sequence['outputs.ContainerCorsRule']]:
        return pulumi.get(self, "cors_policy")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> Optional[str]:
        return pulumi.get(self, "lifecycle_policy")

    @property
    @pulumi.getter(name="metricPolicy")
    def metric_policy(self) -> Optional['outputs.ContainerMetricPolicy']:
        return pulumi.get(self, "metric_policy")

    @property
    @pulumi.getter
    def policy(self) -> Optional[str]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ContainerTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetContainerResult(GetContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerResult(
            access_logging_enabled=self.access_logging_enabled,
            cors_policy=self.cors_policy,
            endpoint=self.endpoint,
            id=self.id,
            lifecycle_policy=self.lifecycle_policy,
            metric_policy=self.metric_policy,
            policy=self.policy,
            tags=self.tags)


def get_container(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerResult:
    """
    Resource Type definition for AWS::MediaStore::Container
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediastore:getContainer', __args__, opts=opts, typ=GetContainerResult).value

    return AwaitableGetContainerResult(
        access_logging_enabled=__ret__.access_logging_enabled,
        cors_policy=__ret__.cors_policy,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        lifecycle_policy=__ret__.lifecycle_policy,
        metric_policy=__ret__.metric_policy,
        policy=__ret__.policy,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_container)
def get_container_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerResult]:
    """
    Resource Type definition for AWS::MediaStore::Container
    """
    ...
