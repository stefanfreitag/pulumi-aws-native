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
    'GetDistributionResult',
    'AwaitableGetDistributionResult',
    'get_distribution',
    'get_distribution_output',
]

@pulumi.output_type
class GetDistributionResult:
    def __init__(__self__, able_to_update_bundle=None, bundle_id=None, cache_behavior_settings=None, cache_behaviors=None, certificate_name=None, default_cache_behavior=None, distribution_arn=None, is_enabled=None, origin=None, status=None, tags=None):
        if able_to_update_bundle and not isinstance(able_to_update_bundle, bool):
            raise TypeError("Expected argument 'able_to_update_bundle' to be a bool")
        pulumi.set(__self__, "able_to_update_bundle", able_to_update_bundle)
        if bundle_id and not isinstance(bundle_id, str):
            raise TypeError("Expected argument 'bundle_id' to be a str")
        pulumi.set(__self__, "bundle_id", bundle_id)
        if cache_behavior_settings and not isinstance(cache_behavior_settings, dict):
            raise TypeError("Expected argument 'cache_behavior_settings' to be a dict")
        pulumi.set(__self__, "cache_behavior_settings", cache_behavior_settings)
        if cache_behaviors and not isinstance(cache_behaviors, list):
            raise TypeError("Expected argument 'cache_behaviors' to be a list")
        pulumi.set(__self__, "cache_behaviors", cache_behaviors)
        if certificate_name and not isinstance(certificate_name, str):
            raise TypeError("Expected argument 'certificate_name' to be a str")
        pulumi.set(__self__, "certificate_name", certificate_name)
        if default_cache_behavior and not isinstance(default_cache_behavior, dict):
            raise TypeError("Expected argument 'default_cache_behavior' to be a dict")
        pulumi.set(__self__, "default_cache_behavior", default_cache_behavior)
        if distribution_arn and not isinstance(distribution_arn, str):
            raise TypeError("Expected argument 'distribution_arn' to be a str")
        pulumi.set(__self__, "distribution_arn", distribution_arn)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if origin and not isinstance(origin, dict):
            raise TypeError("Expected argument 'origin' to be a dict")
        pulumi.set(__self__, "origin", origin)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="ableToUpdateBundle")
    def able_to_update_bundle(self) -> Optional[bool]:
        """
        Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.
        """
        return pulumi.get(self, "able_to_update_bundle")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[str]:
        """
        The bundle ID to use for the distribution.
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="cacheBehaviorSettings")
    def cache_behavior_settings(self) -> Optional['outputs.DistributionCacheSettings']:
        """
        An object that describes the cache behavior settings for the distribution.
        """
        return pulumi.get(self, "cache_behavior_settings")

    @property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(self) -> Optional[Sequence['outputs.DistributionCacheBehaviorPerPath']]:
        """
        An array of objects that describe the per-path cache behavior for the distribution.
        """
        return pulumi.get(self, "cache_behaviors")

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[str]:
        """
        The certificate attached to the Distribution.
        """
        return pulumi.get(self, "certificate_name")

    @property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> Optional['outputs.DistributionCacheBehavior']:
        """
        An object that describes the default cache behavior for the distribution.
        """
        return pulumi.get(self, "default_cache_behavior")

    @property
    @pulumi.getter(name="distributionArn")
    def distribution_arn(self) -> Optional[str]:
        return pulumi.get(self, "distribution_arn")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Indicates whether the distribution is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def origin(self) -> Optional['outputs.DistributionInputOrigin']:
        """
        An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the distribution.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DistributionTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDistributionResult(GetDistributionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDistributionResult(
            able_to_update_bundle=self.able_to_update_bundle,
            bundle_id=self.bundle_id,
            cache_behavior_settings=self.cache_behavior_settings,
            cache_behaviors=self.cache_behaviors,
            certificate_name=self.certificate_name,
            default_cache_behavior=self.default_cache_behavior,
            distribution_arn=self.distribution_arn,
            is_enabled=self.is_enabled,
            origin=self.origin,
            status=self.status,
            tags=self.tags)


def get_distribution(distribution_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDistributionResult:
    """
    Resource Type definition for AWS::Lightsail::Distribution


    :param str distribution_name: The name for the distribution.
    """
    __args__ = dict()
    __args__['distributionName'] = distribution_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getDistribution', __args__, opts=opts, typ=GetDistributionResult).value

    return AwaitableGetDistributionResult(
        able_to_update_bundle=pulumi.get(__ret__, 'able_to_update_bundle'),
        bundle_id=pulumi.get(__ret__, 'bundle_id'),
        cache_behavior_settings=pulumi.get(__ret__, 'cache_behavior_settings'),
        cache_behaviors=pulumi.get(__ret__, 'cache_behaviors'),
        certificate_name=pulumi.get(__ret__, 'certificate_name'),
        default_cache_behavior=pulumi.get(__ret__, 'default_cache_behavior'),
        distribution_arn=pulumi.get(__ret__, 'distribution_arn'),
        is_enabled=pulumi.get(__ret__, 'is_enabled'),
        origin=pulumi.get(__ret__, 'origin'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_distribution)
def get_distribution_output(distribution_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDistributionResult]:
    """
    Resource Type definition for AWS::Lightsail::Distribution


    :param str distribution_name: The name for the distribution.
    """
    ...
