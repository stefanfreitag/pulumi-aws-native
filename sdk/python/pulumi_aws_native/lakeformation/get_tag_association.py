# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTagAssociationResult',
    'AwaitableGetTagAssociationResult',
    'get_tag_association',
    'get_tag_association_output',
]

@pulumi.output_type
class GetTagAssociationResult:
    def __init__(__self__, resource_identifier=None, tags_identifier=None):
        if resource_identifier and not isinstance(resource_identifier, str):
            raise TypeError("Expected argument 'resource_identifier' to be a str")
        pulumi.set(__self__, "resource_identifier", resource_identifier)
        if tags_identifier and not isinstance(tags_identifier, str):
            raise TypeError("Expected argument 'tags_identifier' to be a str")
        pulumi.set(__self__, "tags_identifier", tags_identifier)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[str]:
        """
        Unique string identifying the resource. Used as primary identifier, which ideally should be a string
        """
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter(name="tagsIdentifier")
    def tags_identifier(self) -> Optional[str]:
        """
        Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
        """
        return pulumi.get(self, "tags_identifier")


class AwaitableGetTagAssociationResult(GetTagAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagAssociationResult(
            resource_identifier=self.resource_identifier,
            tags_identifier=self.tags_identifier)


def get_tag_association(resource_identifier: Optional[str] = None,
                        tags_identifier: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagAssociationResult:
    """
    A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.


    :param str resource_identifier: Unique string identifying the resource. Used as primary identifier, which ideally should be a string
    :param str tags_identifier: Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
    """
    __args__ = dict()
    __args__['resourceIdentifier'] = resource_identifier
    __args__['tagsIdentifier'] = tags_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lakeformation:getTagAssociation', __args__, opts=opts, typ=GetTagAssociationResult).value

    return AwaitableGetTagAssociationResult(
        resource_identifier=pulumi.get(__ret__, 'resource_identifier'),
        tags_identifier=pulumi.get(__ret__, 'tags_identifier'))


@_utilities.lift_output_func(get_tag_association)
def get_tag_association_output(resource_identifier: Optional[pulumi.Input[str]] = None,
                               tags_identifier: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagAssociationResult]:
    """
    A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.


    :param str resource_identifier: Unique string identifying the resource. Used as primary identifier, which ideally should be a string
    :param str tags_identifier: Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
    """
    ...
