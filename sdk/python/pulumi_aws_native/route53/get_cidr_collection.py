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
    'GetCidrCollectionResult',
    'AwaitableGetCidrCollectionResult',
    'get_cidr_collection',
    'get_cidr_collection_output',
]

@pulumi.output_type
class GetCidrCollectionResult:
    def __init__(__self__, arn=None, id=None, locations=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if locations and not isinstance(locations, list):
            raise TypeError("Expected argument 'locations' to be a list")
        pulumi.set(__self__, "locations", locations)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon resource name (ARN) to uniquely identify the AWS resource.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        UUID of the CIDR collection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def locations(self) -> Optional[Sequence['outputs.CidrCollectionLocation']]:
        """
        A complex type that contains information about the list of CIDR locations.
        """
        return pulumi.get(self, "locations")


class AwaitableGetCidrCollectionResult(GetCidrCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCidrCollectionResult(
            arn=self.arn,
            id=self.id,
            locations=self.locations)


def get_cidr_collection(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCidrCollectionResult:
    """
    Resource schema for AWS::Route53::CidrCollection.


    :param str id: UUID of the CIDR collection.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:route53:getCidrCollection', __args__, opts=opts, typ=GetCidrCollectionResult).value

    return AwaitableGetCidrCollectionResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        locations=pulumi.get(__ret__, 'locations'))


@_utilities.lift_output_func(get_cidr_collection)
def get_cidr_collection_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCidrCollectionResult]:
    """
    Resource schema for AWS::Route53::CidrCollection.


    :param str id: UUID of the CIDR collection.
    """
    ...
