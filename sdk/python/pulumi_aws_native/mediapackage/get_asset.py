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
    'GetAssetResult',
    'AwaitableGetAssetResult',
    'get_asset',
    'get_asset_output',
]

@pulumi.output_type
class GetAssetResult:
    def __init__(__self__, arn=None, created_at=None, egress_endpoints=None, id=None, packaging_group_id=None, resource_id=None, source_arn=None, source_role_arn=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if egress_endpoints and not isinstance(egress_endpoints, list):
            raise TypeError("Expected argument 'egress_endpoints' to be a list")
        pulumi.set(__self__, "egress_endpoints", egress_endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if packaging_group_id and not isinstance(packaging_group_id, str):
            raise TypeError("Expected argument 'packaging_group_id' to be a str")
        pulumi.set(__self__, "packaging_group_id", packaging_group_id)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if source_arn and not isinstance(source_arn, str):
            raise TypeError("Expected argument 'source_arn' to be a str")
        pulumi.set(__self__, "source_arn", source_arn)
        if source_role_arn and not isinstance(source_role_arn, str):
            raise TypeError("Expected argument 'source_role_arn' to be a str")
        pulumi.set(__self__, "source_role_arn", source_role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the Asset.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The time the Asset was initially submitted for Ingest.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="egressEndpoints")
    def egress_endpoints(self) -> Optional[Sequence['outputs.AssetEgressEndpoint']]:
        """
        The list of egress endpoints available for the Asset.
        """
        return pulumi.get(self, "egress_endpoints")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The unique identifier for the Asset.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="packagingGroupId")
    def packaging_group_id(self) -> Optional[str]:
        """
        The ID of the PackagingGroup for the Asset.
        """
        return pulumi.get(self, "packaging_group_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        The resource ID to include in SPEKE key requests.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[str]:
        """
        ARN of the source object in S3.
        """
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter(name="sourceRoleArn")
    def source_role_arn(self) -> Optional[str]:
        """
        The IAM role_arn used to access the source S3 bucket.
        """
        return pulumi.get(self, "source_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetAssetResult(GetAssetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetResult(
            arn=self.arn,
            created_at=self.created_at,
            egress_endpoints=self.egress_endpoints,
            id=self.id,
            packaging_group_id=self.packaging_group_id,
            resource_id=self.resource_id,
            source_arn=self.source_arn,
            source_role_arn=self.source_role_arn,
            tags=self.tags)


def get_asset(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetResult:
    """
    Resource schema for AWS::MediaPackage::Asset


    :param str id: The unique identifier for the Asset.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackage:getAsset', __args__, opts=opts, typ=GetAssetResult).value

    return AwaitableGetAssetResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        egress_endpoints=pulumi.get(__ret__, 'egress_endpoints'),
        id=pulumi.get(__ret__, 'id'),
        packaging_group_id=pulumi.get(__ret__, 'packaging_group_id'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        source_arn=pulumi.get(__ret__, 'source_arn'),
        source_role_arn=pulumi.get(__ret__, 'source_role_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_asset)
def get_asset_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetResult]:
    """
    Resource schema for AWS::MediaPackage::Asset


    :param str id: The unique identifier for the Asset.
    """
    ...
