# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GraphQlSchemaArgs', 'GraphQlSchema']

@pulumi.input_type
class GraphQlSchemaArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 definition: Optional[pulumi.Input[str]] = None,
                 definition_s3_location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GraphQlSchema resource.
        """
        GraphQlSchemaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_id=api_id,
            definition=definition,
            definition_s3_location=definition_s3_location,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_id: pulumi.Input[str],
             definition: Optional[pulumi.Input[str]] = None,
             definition_s3_location: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("api_id", api_id)
        if definition is not None:
            _setter("definition", definition)
        if definition_s3_location is not None:
            _setter("definition_s3_location", definition_s3_location)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="definitionS3Location")
    def definition_s3_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "definition_s3_location")

    @definition_s3_location.setter
    def definition_s3_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition_s3_location", value)


warnings.warn("""GraphQlSchema is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class GraphQlSchema(pulumi.CustomResource):
    warnings.warn("""GraphQlSchema is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 definition_s3_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppSync::GraphQLSchema

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GraphQlSchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppSync::GraphQLSchema

        :param str resource_name: The name of the resource.
        :param GraphQlSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GraphQlSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GraphQlSchemaArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 definition_s3_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""GraphQlSchema is deprecated: GraphQlSchema is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GraphQlSchemaArgs.__new__(GraphQlSchemaArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["definition"] = definition
            __props__.__dict__["definition_s3_location"] = definition_s3_location
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(GraphQlSchema, __self__).__init__(
            'aws-native:appsync:GraphQlSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GraphQlSchema':
        """
        Get an existing GraphQlSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GraphQlSchemaArgs.__new__(GraphQlSchemaArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["definition"] = None
        __props__.__dict__["definition_s3_location"] = None
        return GraphQlSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="definitionS3Location")
    def definition_s3_location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "definition_s3_location")

