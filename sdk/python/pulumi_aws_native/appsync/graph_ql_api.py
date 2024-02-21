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

__all__ = ['GraphQlApiArgs', 'GraphQlApi']

@pulumi.input_type
class GraphQlApiArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input[str],
                 additional_authentication_providers: Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiAdditionalAuthenticationProviderArgs']]]] = None,
                 api_type: Optional[pulumi.Input[str]] = None,
                 enhanced_metrics_config: Optional[pulumi.Input['GraphQlApiEnhancedMetricsConfigArgs']] = None,
                 environment_variables: Optional[Any] = None,
                 introspection_config: Optional[pulumi.Input[str]] = None,
                 lambda_authorizer_config: Optional[pulumi.Input['GraphQlApiLambdaAuthorizerConfigArgs']] = None,
                 log_config: Optional[pulumi.Input['GraphQlApiLogConfigArgs']] = None,
                 merged_api_execution_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_id_connect_config: Optional[pulumi.Input['GraphQlApiOpenIdConnectConfigArgs']] = None,
                 owner_contact: Optional[pulumi.Input[str]] = None,
                 query_depth_limit: Optional[pulumi.Input[int]] = None,
                 resolver_count_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiTagArgs']]]] = None,
                 user_pool_config: Optional[pulumi.Input['GraphQlApiUserPoolConfigArgs']] = None,
                 visibility: Optional[pulumi.Input[str]] = None,
                 xray_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GraphQlApi resource.
        :param Any environment_variables: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
        """
        pulumi.set(__self__, "authentication_type", authentication_type)
        if additional_authentication_providers is not None:
            pulumi.set(__self__, "additional_authentication_providers", additional_authentication_providers)
        if api_type is not None:
            pulumi.set(__self__, "api_type", api_type)
        if enhanced_metrics_config is not None:
            pulumi.set(__self__, "enhanced_metrics_config", enhanced_metrics_config)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if introspection_config is not None:
            pulumi.set(__self__, "introspection_config", introspection_config)
        if lambda_authorizer_config is not None:
            pulumi.set(__self__, "lambda_authorizer_config", lambda_authorizer_config)
        if log_config is not None:
            pulumi.set(__self__, "log_config", log_config)
        if merged_api_execution_role_arn is not None:
            pulumi.set(__self__, "merged_api_execution_role_arn", merged_api_execution_role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if open_id_connect_config is not None:
            pulumi.set(__self__, "open_id_connect_config", open_id_connect_config)
        if owner_contact is not None:
            pulumi.set(__self__, "owner_contact", owner_contact)
        if query_depth_limit is not None:
            pulumi.set(__self__, "query_depth_limit", query_depth_limit)
        if resolver_count_limit is not None:
            pulumi.set(__self__, "resolver_count_limit", resolver_count_limit)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_pool_config is not None:
            pulumi.set(__self__, "user_pool_config", user_pool_config)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)
        if xray_enabled is not None:
            pulumi.set(__self__, "xray_enabled", xray_enabled)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiAdditionalAuthenticationProviderArgs']]]]:
        return pulumi.get(self, "additional_authentication_providers")

    @additional_authentication_providers.setter
    def additional_authentication_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiAdditionalAuthenticationProviderArgs']]]]):
        pulumi.set(self, "additional_authentication_providers", value)

    @property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_type")

    @api_type.setter
    def api_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_type", value)

    @property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(self) -> Optional[pulumi.Input['GraphQlApiEnhancedMetricsConfigArgs']]:
        return pulumi.get(self, "enhanced_metrics_config")

    @enhanced_metrics_config.setter
    def enhanced_metrics_config(self, value: Optional[pulumi.Input['GraphQlApiEnhancedMetricsConfigArgs']]):
        pulumi.set(self, "enhanced_metrics_config", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[Any]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "introspection_config")

    @introspection_config.setter
    def introspection_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "introspection_config", value)

    @property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> Optional[pulumi.Input['GraphQlApiLambdaAuthorizerConfigArgs']]:
        return pulumi.get(self, "lambda_authorizer_config")

    @lambda_authorizer_config.setter
    def lambda_authorizer_config(self, value: Optional[pulumi.Input['GraphQlApiLambdaAuthorizerConfigArgs']]):
        pulumi.set(self, "lambda_authorizer_config", value)

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input['GraphQlApiLogConfigArgs']]:
        return pulumi.get(self, "log_config")

    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input['GraphQlApiLogConfigArgs']]):
        pulumi.set(self, "log_config", value)

    @property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "merged_api_execution_role_arn")

    @merged_api_execution_role_arn.setter
    def merged_api_execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "merged_api_execution_role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="openIdConnectConfig")
    def open_id_connect_config(self) -> Optional[pulumi.Input['GraphQlApiOpenIdConnectConfigArgs']]:
        return pulumi.get(self, "open_id_connect_config")

    @open_id_connect_config.setter
    def open_id_connect_config(self, value: Optional[pulumi.Input['GraphQlApiOpenIdConnectConfigArgs']]):
        pulumi.set(self, "open_id_connect_config", value)

    @property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "owner_contact")

    @owner_contact.setter
    def owner_contact(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_contact", value)

    @property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "query_depth_limit")

    @query_depth_limit.setter
    def query_depth_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "query_depth_limit", value)

    @property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "resolver_count_limit")

    @resolver_count_limit.setter
    def resolver_count_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "resolver_count_limit", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GraphQlApiTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(self) -> Optional[pulumi.Input['GraphQlApiUserPoolConfigArgs']]:
        return pulumi.get(self, "user_pool_config")

    @user_pool_config.setter
    def user_pool_config(self, value: Optional[pulumi.Input['GraphQlApiUserPoolConfigArgs']]):
        pulumi.set(self, "user_pool_config", value)

    @property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "visibility")

    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "visibility", value)

    @property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "xray_enabled")

    @xray_enabled.setter
    def xray_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "xray_enabled", value)


warnings.warn("""GraphQlApi is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class GraphQlApi(pulumi.CustomResource):
    warnings.warn("""GraphQlApi is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_authentication_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GraphQlApiAdditionalAuthenticationProviderArgs']]]]] = None,
                 api_type: Optional[pulumi.Input[str]] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 enhanced_metrics_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiEnhancedMetricsConfigArgs']]] = None,
                 environment_variables: Optional[Any] = None,
                 introspection_config: Optional[pulumi.Input[str]] = None,
                 lambda_authorizer_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiLambdaAuthorizerConfigArgs']]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiLogConfigArgs']]] = None,
                 merged_api_execution_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_id_connect_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiOpenIdConnectConfigArgs']]] = None,
                 owner_contact: Optional[pulumi.Input[str]] = None,
                 query_depth_limit: Optional[pulumi.Input[int]] = None,
                 resolver_count_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GraphQlApiTagArgs']]]]] = None,
                 user_pool_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiUserPoolConfigArgs']]] = None,
                 visibility: Optional[pulumi.Input[str]] = None,
                 xray_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppSync::GraphQLApi

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any environment_variables: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GraphQlApiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppSync::GraphQLApi

        :param str resource_name: The name of the resource.
        :param GraphQlApiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GraphQlApiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_authentication_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GraphQlApiAdditionalAuthenticationProviderArgs']]]]] = None,
                 api_type: Optional[pulumi.Input[str]] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 enhanced_metrics_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiEnhancedMetricsConfigArgs']]] = None,
                 environment_variables: Optional[Any] = None,
                 introspection_config: Optional[pulumi.Input[str]] = None,
                 lambda_authorizer_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiLambdaAuthorizerConfigArgs']]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiLogConfigArgs']]] = None,
                 merged_api_execution_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_id_connect_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiOpenIdConnectConfigArgs']]] = None,
                 owner_contact: Optional[pulumi.Input[str]] = None,
                 query_depth_limit: Optional[pulumi.Input[int]] = None,
                 resolver_count_limit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GraphQlApiTagArgs']]]]] = None,
                 user_pool_config: Optional[pulumi.Input[pulumi.InputType['GraphQlApiUserPoolConfigArgs']]] = None,
                 visibility: Optional[pulumi.Input[str]] = None,
                 xray_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""GraphQlApi is deprecated: GraphQlApi is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GraphQlApiArgs.__new__(GraphQlApiArgs)

            __props__.__dict__["additional_authentication_providers"] = additional_authentication_providers
            __props__.__dict__["api_type"] = api_type
            if authentication_type is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_type'")
            __props__.__dict__["authentication_type"] = authentication_type
            __props__.__dict__["enhanced_metrics_config"] = enhanced_metrics_config
            __props__.__dict__["environment_variables"] = environment_variables
            __props__.__dict__["introspection_config"] = introspection_config
            __props__.__dict__["lambda_authorizer_config"] = lambda_authorizer_config
            __props__.__dict__["log_config"] = log_config
            __props__.__dict__["merged_api_execution_role_arn"] = merged_api_execution_role_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["open_id_connect_config"] = open_id_connect_config
            __props__.__dict__["owner_contact"] = owner_contact
            __props__.__dict__["query_depth_limit"] = query_depth_limit
            __props__.__dict__["resolver_count_limit"] = resolver_count_limit
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_pool_config"] = user_pool_config
            __props__.__dict__["visibility"] = visibility
            __props__.__dict__["xray_enabled"] = xray_enabled
            __props__.__dict__["api_id"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["graph_ql_dns"] = None
            __props__.__dict__["graph_ql_endpoint_arn"] = None
            __props__.__dict__["graph_ql_url"] = None
            __props__.__dict__["realtime_dns"] = None
            __props__.__dict__["realtime_url"] = None
        super(GraphQlApi, __self__).__init__(
            'aws-native:appsync:GraphQlApi',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GraphQlApi':
        """
        Get an existing GraphQlApi resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GraphQlApiArgs.__new__(GraphQlApiArgs)

        __props__.__dict__["additional_authentication_providers"] = None
        __props__.__dict__["api_id"] = None
        __props__.__dict__["api_type"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["authentication_type"] = None
        __props__.__dict__["enhanced_metrics_config"] = None
        __props__.__dict__["environment_variables"] = None
        __props__.__dict__["graph_ql_dns"] = None
        __props__.__dict__["graph_ql_endpoint_arn"] = None
        __props__.__dict__["graph_ql_url"] = None
        __props__.__dict__["introspection_config"] = None
        __props__.__dict__["lambda_authorizer_config"] = None
        __props__.__dict__["log_config"] = None
        __props__.__dict__["merged_api_execution_role_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["open_id_connect_config"] = None
        __props__.__dict__["owner_contact"] = None
        __props__.__dict__["query_depth_limit"] = None
        __props__.__dict__["realtime_dns"] = None
        __props__.__dict__["realtime_url"] = None
        __props__.__dict__["resolver_count_limit"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_pool_config"] = None
        __props__.__dict__["visibility"] = None
        __props__.__dict__["xray_enabled"] = None
        return GraphQlApi(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(self) -> pulumi.Output[Optional[Sequence['outputs.GraphQlApiAdditionalAuthenticationProvider']]]:
        return pulumi.get(self, "additional_authentication_providers")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="apiType")
    def api_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_type")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(self) -> pulumi.Output[Optional['outputs.GraphQlApiEnhancedMetricsConfig']]:
        return pulumi.get(self, "enhanced_metrics_config")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Any]]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="graphQlDns")
    def graph_ql_dns(self) -> pulumi.Output[str]:
        return pulumi.get(self, "graph_ql_dns")

    @property
    @pulumi.getter(name="graphQlEndpointArn")
    def graph_ql_endpoint_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "graph_ql_endpoint_arn")

    @property
    @pulumi.getter(name="graphQlUrl")
    def graph_ql_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "graph_ql_url")

    @property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "introspection_config")

    @property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> pulumi.Output[Optional['outputs.GraphQlApiLambdaAuthorizerConfig']]:
        return pulumi.get(self, "lambda_authorizer_config")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional['outputs.GraphQlApiLogConfig']]:
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "merged_api_execution_role_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openIdConnectConfig")
    def open_id_connect_config(self) -> pulumi.Output[Optional['outputs.GraphQlApiOpenIdConnectConfig']]:
        return pulumi.get(self, "open_id_connect_config")

    @property
    @pulumi.getter(name="ownerContact")
    def owner_contact(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "owner_contact")

    @property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "query_depth_limit")

    @property
    @pulumi.getter(name="realtimeDns")
    def realtime_dns(self) -> pulumi.Output[str]:
        return pulumi.get(self, "realtime_dns")

    @property
    @pulumi.getter(name="realtimeUrl")
    def realtime_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "realtime_url")

    @property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "resolver_count_limit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.GraphQlApiTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(self) -> pulumi.Output[Optional['outputs.GraphQlApiUserPoolConfig']]:
        return pulumi.get(self, "user_pool_config")

    @property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "visibility")

    @property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "xray_enabled")

