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
from ._enums import *
from ._inputs import *

__all__ = ['CollectionArgs', 'Collection']

@pulumi.input_type
class CollectionArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CollectionTagArgs']]]] = None,
                 type: Optional[pulumi.Input['CollectionType']] = None):
        """
        The set of arguments for constructing a Collection resource.
        :param pulumi.Input[str] description: The description of the collection
        :param pulumi.Input[str] name: The name of the collection.
               
               The name must meet the following criteria:
               Unique to your account and AWS Region
               Starts with a lowercase letter
               Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
               Contains between 3 and 32 characters
        :param pulumi.Input[Sequence[pulumi.Input['CollectionTagArgs']]] tags: List of tags to be added to the resource
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the collection
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the collection.

        The name must meet the following criteria:
        Unique to your account and AWS Region
        Starts with a lowercase letter
        Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
        Contains between 3 and 32 characters
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CollectionTagArgs']]]]:
        """
        List of tags to be added to the resource
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CollectionTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['CollectionType']]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['CollectionType']]):
        pulumi.set(self, "type", value)


class Collection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['CollectionType']] = None,
                 __props__=None):
        """
        Amazon OpenSearchServerless collection resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the collection
        :param pulumi.Input[str] name: The name of the collection.
               
               The name must meet the following criteria:
               Unique to your account and AWS Region
               Starts with a lowercase letter
               Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
               Contains between 3 and 32 characters
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionTagArgs']]]] tags: List of tags to be added to the resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CollectionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Amazon OpenSearchServerless collection resource

        :param str resource_name: The name of the resource.
        :param CollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectionTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['CollectionType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CollectionArgs.__new__(CollectionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
            __props__.__dict__["collection_endpoint"] = None
            __props__.__dict__["dashboard_endpoint"] = None
        super(Collection, __self__).__init__(
            'aws-native:opensearchserverless:Collection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Collection':
        """
        Get an existing Collection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CollectionArgs.__new__(CollectionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["collection_endpoint"] = None
        __props__.__dict__["dashboard_endpoint"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Collection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the collection.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="collectionEndpoint")
    def collection_endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint for the collection.
        """
        return pulumi.get(self, "collection_endpoint")

    @property
    @pulumi.getter(name="dashboardEndpoint")
    def dashboard_endpoint(self) -> pulumi.Output[str]:
        """
        The OpenSearch Dashboards endpoint for the collection.
        """
        return pulumi.get(self, "dashboard_endpoint")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the collection
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the collection.

        The name must meet the following criteria:
        Unique to your account and AWS Region
        Starts with a lowercase letter
        Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
        Contains between 3 and 32 characters
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CollectionTag']]]:
        """
        List of tags to be added to the resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional['CollectionType']]:
        return pulumi.get(self, "type")

