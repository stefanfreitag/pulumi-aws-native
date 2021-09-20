# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['IntegrationArgs', 'Integration']

@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 object_type_name: pulumi.Input[str],
                 flow_definition: Optional[pulumi.Input['IntegrationFlowDefinitionArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationTagArgs']]]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Integration resource.
        :param pulumi.Input[str] domain_name: The unique name of the domain.
        :param pulumi.Input[str] object_type_name: The name of the ObjectType defined for the 3rd party data in Profile Service
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationTagArgs']]] tags: The tags (keys and values) associated with the integration
        :param pulumi.Input[str] uri: The URI of the S3 bucket or any other type of data source.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "object_type_name", object_type_name)
        if flow_definition is not None:
            pulumi.set(__self__, "flow_definition", flow_definition)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The unique name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="objectTypeName")
    def object_type_name(self) -> pulumi.Input[str]:
        """
        The name of the ObjectType defined for the 3rd party data in Profile Service
        """
        return pulumi.get(self, "object_type_name")

    @object_type_name.setter
    def object_type_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "object_type_name", value)

    @property
    @pulumi.getter(name="flowDefinition")
    def flow_definition(self) -> Optional[pulumi.Input['IntegrationFlowDefinitionArgs']]:
        return pulumi.get(self, "flow_definition")

    @flow_definition.setter
    def flow_definition(self, value: Optional[pulumi.Input['IntegrationFlowDefinitionArgs']]):
        pulumi.set(self, "flow_definition", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationTagArgs']]]]:
        """
        The tags (keys and values) associated with the integration
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the S3 bucket or any other type of data source.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 flow_definition: Optional[pulumi.Input[pulumi.InputType['IntegrationFlowDefinitionArgs']]] = None,
                 object_type_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationTagArgs']]]]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The resource schema for creating an Amazon Connect Customer Profiles Integration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The unique name of the domain.
        :param pulumi.Input[str] object_type_name: The name of the ObjectType defined for the 3rd party data in Profile Service
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationTagArgs']]]] tags: The tags (keys and values) associated with the integration
        :param pulumi.Input[str] uri: The URI of the S3 bucket or any other type of data source.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The resource schema for creating an Amazon Connect Customer Profiles Integration.

        :param str resource_name: The name of the resource.
        :param IntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 flow_definition: Optional[pulumi.Input[pulumi.InputType['IntegrationFlowDefinitionArgs']]] = None,
                 object_type_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationTagArgs']]]]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationArgs.__new__(IntegrationArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["flow_definition"] = flow_definition
            if object_type_name is None and not opts.urn:
                raise TypeError("Missing required property 'object_type_name'")
            __props__.__dict__["object_type_name"] = object_type_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["uri"] = uri
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_updated_at"] = None
        super(Integration, __self__).__init__(
            'aws-native:customerprofiles:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationArgs.__new__(IntegrationArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["flow_definition"] = None
        __props__.__dict__["last_updated_at"] = None
        __props__.__dict__["object_type_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["uri"] = None
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time of this integration got created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The unique name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="flowDefinition")
    def flow_definition(self) -> pulumi.Output[Optional['outputs.IntegrationFlowDefinition']]:
        return pulumi.get(self, "flow_definition")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[str]:
        """
        The time of this integration got last updated at
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter(name="objectTypeName")
    def object_type_name(self) -> pulumi.Output[str]:
        """
        The name of the ObjectType defined for the 3rd party data in Profile Service
        """
        return pulumi.get(self, "object_type_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.IntegrationTag']]]:
        """
        The tags (keys and values) associated with the integration
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        """
        The URI of the S3 bucket or any other type of data source.
        """
        return pulumi.get(self, "uri")

