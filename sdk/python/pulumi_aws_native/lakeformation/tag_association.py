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
from ._inputs import *

__all__ = ['TagAssociationArgs', 'TagAssociation']

@pulumi.input_type
class TagAssociationArgs:
    def __init__(__self__, *,
                 l_f_tags: pulumi.Input[Sequence[pulumi.Input['TagAssociationLFTagPairArgs']]],
                 resource: pulumi.Input['TagAssociationResourceArgs']):
        """
        The set of arguments for constructing a TagAssociation resource.
        :param pulumi.Input[Sequence[pulumi.Input['TagAssociationLFTagPairArgs']]] l_f_tags: List of Lake Formation Tags to associate with the Lake Formation Resource
        :param pulumi.Input['TagAssociationResourceArgs'] resource: Resource to tag with the Lake Formation Tags
        """
        pulumi.set(__self__, "l_f_tags", l_f_tags)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter(name="lFTags")
    def l_f_tags(self) -> pulumi.Input[Sequence[pulumi.Input['TagAssociationLFTagPairArgs']]]:
        """
        List of Lake Formation Tags to associate with the Lake Formation Resource
        """
        return pulumi.get(self, "l_f_tags")

    @l_f_tags.setter
    def l_f_tags(self, value: pulumi.Input[Sequence[pulumi.Input['TagAssociationLFTagPairArgs']]]):
        pulumi.set(self, "l_f_tags", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input['TagAssociationResourceArgs']:
        """
        Resource to tag with the Lake Formation Tags
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['TagAssociationResourceArgs']):
        pulumi.set(self, "resource", value)


class TagAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 l_f_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TagAssociationLFTagPairArgs']]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['TagAssociationResourceArgs']]] = None,
                 __props__=None):
        """
        A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TagAssociationLFTagPairArgs']]]] l_f_tags: List of Lake Formation Tags to associate with the Lake Formation Resource
        :param pulumi.Input[pulumi.InputType['TagAssociationResourceArgs']] resource: Resource to tag with the Lake Formation Tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.

        :param str resource_name: The name of the resource.
        :param TagAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 l_f_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TagAssociationLFTagPairArgs']]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['TagAssociationResourceArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagAssociationArgs.__new__(TagAssociationArgs)

            if l_f_tags is None and not opts.urn:
                raise TypeError("Missing required property 'l_f_tags'")
            __props__.__dict__["l_f_tags"] = l_f_tags
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
            __props__.__dict__["resource_identifier"] = None
            __props__.__dict__["tags_identifier"] = None
        super(TagAssociation, __self__).__init__(
            'aws-native:lakeformation:TagAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TagAssociation':
        """
        Get an existing TagAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagAssociationArgs.__new__(TagAssociationArgs)

        __props__.__dict__["l_f_tags"] = None
        __props__.__dict__["resource"] = None
        __props__.__dict__["resource_identifier"] = None
        __props__.__dict__["tags_identifier"] = None
        return TagAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="lFTags")
    def l_f_tags(self) -> pulumi.Output[Sequence['outputs.TagAssociationLFTagPair']]:
        """
        List of Lake Formation Tags to associate with the Lake Formation Resource
        """
        return pulumi.get(self, "l_f_tags")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output['outputs.TagAssociationResource']:
        """
        Resource to tag with the Lake Formation Tags
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[str]:
        """
        Unique string identifying the resource. Used as primary identifier, which ideally should be a string
        """
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter(name="tagsIdentifier")
    def tags_identifier(self) -> pulumi.Output[str]:
        """
        Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
        """
        return pulumi.get(self, "tags_identifier")

