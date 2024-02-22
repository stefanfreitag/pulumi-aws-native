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
    'GetVirtualServiceResult',
    'AwaitableGetVirtualServiceResult',
    'get_virtual_service',
    'get_virtual_service_output',
]

@pulumi.output_type
class GetVirtualServiceResult:
    def __init__(__self__, arn=None, id=None, resource_owner=None, spec=None, tags=None, uid=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_owner and not isinstance(resource_owner, str):
            raise TypeError("Expected argument 'resource_owner' to be a str")
        pulumi.set(__self__, "resource_owner", resource_owner)
        if spec and not isinstance(spec, dict):
            raise TypeError("Expected argument 'spec' to be a dict")
        pulumi.set(__self__, "spec", spec)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> Optional[str]:
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.VirtualServiceSpec']:
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        return pulumi.get(self, "uid")


class AwaitableGetVirtualServiceResult(GetVirtualServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualServiceResult(
            arn=self.arn,
            id=self.id,
            resource_owner=self.resource_owner,
            spec=self.spec,
            tags=self.tags,
            uid=self.uid)


def get_virtual_service(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualServiceResult:
    """
    Resource Type definition for AWS::AppMesh::VirtualService
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appmesh:getVirtualService', __args__, opts=opts, typ=GetVirtualServiceResult).value

    return AwaitableGetVirtualServiceResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        resource_owner=pulumi.get(__ret__, 'resource_owner'),
        spec=pulumi.get(__ret__, 'spec'),
        tags=pulumi.get(__ret__, 'tags'),
        uid=pulumi.get(__ret__, 'uid'))


@_utilities.lift_output_func(get_virtual_service)
def get_virtual_service_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualServiceResult]:
    """
    Resource Type definition for AWS::AppMesh::VirtualService
    """
    ...
