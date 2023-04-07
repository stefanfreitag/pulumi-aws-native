# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetApiCacheResult',
    'AwaitableGetApiCacheResult',
    'get_api_cache',
    'get_api_cache_output',
]

@pulumi.output_type
class GetApiCacheResult:
    def __init__(__self__, api_caching_behavior=None, at_rest_encryption_enabled=None, id=None, transit_encryption_enabled=None, ttl=None, type=None):
        if api_caching_behavior and not isinstance(api_caching_behavior, str):
            raise TypeError("Expected argument 'api_caching_behavior' to be a str")
        pulumi.set(__self__, "api_caching_behavior", api_caching_behavior)
        if at_rest_encryption_enabled and not isinstance(at_rest_encryption_enabled, bool):
            raise TypeError("Expected argument 'at_rest_encryption_enabled' to be a bool")
        pulumi.set(__self__, "at_rest_encryption_enabled", at_rest_encryption_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if transit_encryption_enabled and not isinstance(transit_encryption_enabled, bool):
            raise TypeError("Expected argument 'transit_encryption_enabled' to be a bool")
        pulumi.set(__self__, "transit_encryption_enabled", transit_encryption_enabled)
        if ttl and not isinstance(ttl, float):
            raise TypeError("Expected argument 'ttl' to be a float")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiCachingBehavior")
    def api_caching_behavior(self) -> Optional[str]:
        return pulumi.get(self, "api_caching_behavior")

    @property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "at_rest_encryption_enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "transit_encryption_enabled")

    @property
    @pulumi.getter
    def ttl(self) -> Optional[float]:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetApiCacheResult(GetApiCacheResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiCacheResult(
            api_caching_behavior=self.api_caching_behavior,
            at_rest_encryption_enabled=self.at_rest_encryption_enabled,
            id=self.id,
            transit_encryption_enabled=self.transit_encryption_enabled,
            ttl=self.ttl,
            type=self.type)


def get_api_cache(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiCacheResult:
    """
    Resource Type definition for AWS::AppSync::ApiCache
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appsync:getApiCache', __args__, opts=opts, typ=GetApiCacheResult).value

    return AwaitableGetApiCacheResult(
        api_caching_behavior=__ret__.api_caching_behavior,
        at_rest_encryption_enabled=__ret__.at_rest_encryption_enabled,
        id=__ret__.id,
        transit_encryption_enabled=__ret__.transit_encryption_enabled,
        ttl=__ret__.ttl,
        type=__ret__.type)


@_utilities.lift_output_func(get_api_cache)
def get_api_cache_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiCacheResult]:
    """
    Resource Type definition for AWS::AppSync::ApiCache
    """
    ...
