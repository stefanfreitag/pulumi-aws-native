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

__all__ = ['StageArgs', 'Stage']

@pulumi.input_type
class StageArgs:
    def __init__(__self__, *,
                 rest_api_id: pulumi.Input[str],
                 access_log_setting: Optional[pulumi.Input['StageAccessLogSettingArgs']] = None,
                 cache_cluster_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_cluster_size: Optional[pulumi.Input[str]] = None,
                 canary_setting: Optional[pulumi.Input['StageCanarySettingArgs']] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 documentation_version: Optional[pulumi.Input[str]] = None,
                 method_settings: Optional[pulumi.Input[Sequence[pulumi.Input['StageMethodSettingArgs']]]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StageTagArgs']]]] = None,
                 tracing_enabled: Optional[pulumi.Input[bool]] = None,
                 variables: Optional[Any] = None):
        """
        The set of arguments for constructing a Stage resource.
        :param pulumi.Input[str] rest_api_id: The string identifier of the associated RestApi.
        :param pulumi.Input['StageAccessLogSettingArgs'] access_log_setting: Access log settings, including the access log format and access log destination ARN.
        :param pulumi.Input[bool] cache_cluster_enabled: Specifies whether a cache cluster is enabled for the stage.
        :param pulumi.Input[str] cache_cluster_size: The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
        :param pulumi.Input['StageCanarySettingArgs'] canary_setting: Settings for the canary deployment in this stage.
        :param pulumi.Input[str] client_certificate_id: The identifier of a client certificate for an API stage.
        :param pulumi.Input[str] deployment_id: The identifier of the Deployment that the stage points to.
        :param pulumi.Input[str] description: The stage's description.
        :param pulumi.Input[str] documentation_version: The version of the associated API documentation.
        :param pulumi.Input[Sequence[pulumi.Input['StageMethodSettingArgs']]] method_settings: A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.
        :param pulumi.Input[str] stage_name: The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
        :param pulumi.Input[Sequence[pulumi.Input['StageTagArgs']]] tags: The collection of tags. Each tag element is associated with a given resource.
        :param pulumi.Input[bool] tracing_enabled: Specifies whether active tracing with X-ray is enabled for the Stage.
        :param Any variables: A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
        """
        pulumi.set(__self__, "rest_api_id", rest_api_id)
        if access_log_setting is not None:
            pulumi.set(__self__, "access_log_setting", access_log_setting)
        if cache_cluster_enabled is not None:
            pulumi.set(__self__, "cache_cluster_enabled", cache_cluster_enabled)
        if cache_cluster_size is not None:
            pulumi.set(__self__, "cache_cluster_size", cache_cluster_size)
        if canary_setting is not None:
            pulumi.set(__self__, "canary_setting", canary_setting)
        if client_certificate_id is not None:
            pulumi.set(__self__, "client_certificate_id", client_certificate_id)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if documentation_version is not None:
            pulumi.set(__self__, "documentation_version", documentation_version)
        if method_settings is not None:
            pulumi.set(__self__, "method_settings", method_settings)
        if stage_name is not None:
            pulumi.set(__self__, "stage_name", stage_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tracing_enabled is not None:
            pulumi.set(__self__, "tracing_enabled", tracing_enabled)
        if variables is not None:
            pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[str]:
        """
        The string identifier of the associated RestApi.
        """
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rest_api_id", value)

    @property
    @pulumi.getter(name="accessLogSetting")
    def access_log_setting(self) -> Optional[pulumi.Input['StageAccessLogSettingArgs']]:
        """
        Access log settings, including the access log format and access log destination ARN.
        """
        return pulumi.get(self, "access_log_setting")

    @access_log_setting.setter
    def access_log_setting(self, value: Optional[pulumi.Input['StageAccessLogSettingArgs']]):
        pulumi.set(self, "access_log_setting", value)

    @property
    @pulumi.getter(name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether a cache cluster is enabled for the stage.
        """
        return pulumi.get(self, "cache_cluster_enabled")

    @cache_cluster_enabled.setter
    def cache_cluster_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cache_cluster_enabled", value)

    @property
    @pulumi.getter(name="cacheClusterSize")
    def cache_cluster_size(self) -> Optional[pulumi.Input[str]]:
        """
        The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
        """
        return pulumi.get(self, "cache_cluster_size")

    @cache_cluster_size.setter
    def cache_cluster_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_cluster_size", value)

    @property
    @pulumi.getter(name="canarySetting")
    def canary_setting(self) -> Optional[pulumi.Input['StageCanarySettingArgs']]:
        """
        Settings for the canary deployment in this stage.
        """
        return pulumi.get(self, "canary_setting")

    @canary_setting.setter
    def canary_setting(self, value: Optional[pulumi.Input['StageCanarySettingArgs']]):
        pulumi.set(self, "canary_setting", value)

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of a client certificate for an API stage.
        """
        return pulumi.get(self, "client_certificate_id")

    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate_id", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the Deployment that the stage points to.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The stage's description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="documentationVersion")
    def documentation_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the associated API documentation.
        """
        return pulumi.get(self, "documentation_version")

    @documentation_version.setter
    def documentation_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "documentation_version", value)

    @property
    @pulumi.getter(name="methodSettings")
    def method_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StageMethodSettingArgs']]]]:
        """
        A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.
        """
        return pulumi.get(self, "method_settings")

    @method_settings.setter
    def method_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StageMethodSettingArgs']]]]):
        pulumi.set(self, "method_settings", value)

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
        """
        return pulumi.get(self, "stage_name")

    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StageTagArgs']]]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StageTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tracingEnabled")
    def tracing_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether active tracing with X-ray is enabled for the Stage.
        """
        return pulumi.get(self, "tracing_enabled")

    @tracing_enabled.setter
    def tracing_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tracing_enabled", value)

    @property
    @pulumi.getter
    def variables(self) -> Optional[Any]:
        """
        A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
        """
        return pulumi.get(self, "variables")

    @variables.setter
    def variables(self, value: Optional[Any]):
        pulumi.set(self, "variables", value)


class Stage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_log_setting: Optional[pulumi.Input[pulumi.InputType['StageAccessLogSettingArgs']]] = None,
                 cache_cluster_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_cluster_size: Optional[pulumi.Input[str]] = None,
                 canary_setting: Optional[pulumi.Input[pulumi.InputType['StageCanarySettingArgs']]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 documentation_version: Optional[pulumi.Input[str]] = None,
                 method_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageMethodSettingArgs']]]]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageTagArgs']]]]] = None,
                 tracing_enabled: Optional[pulumi.Input[bool]] = None,
                 variables: Optional[Any] = None,
                 __props__=None):
        """
        The ``AWS::ApiGateway::Stage`` resource creates a stage for a deployment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['StageAccessLogSettingArgs']] access_log_setting: Access log settings, including the access log format and access log destination ARN.
        :param pulumi.Input[bool] cache_cluster_enabled: Specifies whether a cache cluster is enabled for the stage.
        :param pulumi.Input[str] cache_cluster_size: The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
        :param pulumi.Input[pulumi.InputType['StageCanarySettingArgs']] canary_setting: Settings for the canary deployment in this stage.
        :param pulumi.Input[str] client_certificate_id: The identifier of a client certificate for an API stage.
        :param pulumi.Input[str] deployment_id: The identifier of the Deployment that the stage points to.
        :param pulumi.Input[str] description: The stage's description.
        :param pulumi.Input[str] documentation_version: The version of the associated API documentation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageMethodSettingArgs']]]] method_settings: A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.
        :param pulumi.Input[str] rest_api_id: The string identifier of the associated RestApi.
        :param pulumi.Input[str] stage_name: The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageTagArgs']]]] tags: The collection of tags. Each tag element is associated with a given resource.
        :param pulumi.Input[bool] tracing_enabled: Specifies whether active tracing with X-ray is enabled for the Stage.
        :param Any variables: A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGateway::Stage`` resource creates a stage for a deployment.

        :param str resource_name: The name of the resource.
        :param StageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_log_setting: Optional[pulumi.Input[pulumi.InputType['StageAccessLogSettingArgs']]] = None,
                 cache_cluster_enabled: Optional[pulumi.Input[bool]] = None,
                 cache_cluster_size: Optional[pulumi.Input[str]] = None,
                 canary_setting: Optional[pulumi.Input[pulumi.InputType['StageCanarySettingArgs']]] = None,
                 client_certificate_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 documentation_version: Optional[pulumi.Input[str]] = None,
                 method_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageMethodSettingArgs']]]]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StageTagArgs']]]]] = None,
                 tracing_enabled: Optional[pulumi.Input[bool]] = None,
                 variables: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StageArgs.__new__(StageArgs)

            __props__.__dict__["access_log_setting"] = access_log_setting
            __props__.__dict__["cache_cluster_enabled"] = cache_cluster_enabled
            __props__.__dict__["cache_cluster_size"] = cache_cluster_size
            __props__.__dict__["canary_setting"] = canary_setting
            __props__.__dict__["client_certificate_id"] = client_certificate_id
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["description"] = description
            __props__.__dict__["documentation_version"] = documentation_version
            __props__.__dict__["method_settings"] = method_settings
            if rest_api_id is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api_id'")
            __props__.__dict__["rest_api_id"] = rest_api_id
            __props__.__dict__["stage_name"] = stage_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tracing_enabled"] = tracing_enabled
            __props__.__dict__["variables"] = variables
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["rest_api_id", "stage_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Stage, __self__).__init__(
            'aws-native:apigateway:Stage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Stage':
        """
        Get an existing Stage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StageArgs.__new__(StageArgs)

        __props__.__dict__["access_log_setting"] = None
        __props__.__dict__["cache_cluster_enabled"] = None
        __props__.__dict__["cache_cluster_size"] = None
        __props__.__dict__["canary_setting"] = None
        __props__.__dict__["client_certificate_id"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["documentation_version"] = None
        __props__.__dict__["method_settings"] = None
        __props__.__dict__["rest_api_id"] = None
        __props__.__dict__["stage_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tracing_enabled"] = None
        __props__.__dict__["variables"] = None
        return Stage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLogSetting")
    def access_log_setting(self) -> pulumi.Output[Optional['outputs.StageAccessLogSetting']]:
        """
        Access log settings, including the access log format and access log destination ARN.
        """
        return pulumi.get(self, "access_log_setting")

    @property
    @pulumi.getter(name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether a cache cluster is enabled for the stage.
        """
        return pulumi.get(self, "cache_cluster_enabled")

    @property
    @pulumi.getter(name="cacheClusterSize")
    def cache_cluster_size(self) -> pulumi.Output[Optional[str]]:
        """
        The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
        """
        return pulumi.get(self, "cache_cluster_size")

    @property
    @pulumi.getter(name="canarySetting")
    def canary_setting(self) -> pulumi.Output[Optional['outputs.StageCanarySetting']]:
        """
        Settings for the canary deployment in this stage.
        """
        return pulumi.get(self, "canary_setting")

    @property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of a client certificate for an API stage.
        """
        return pulumi.get(self, "client_certificate_id")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the Deployment that the stage points to.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The stage's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationVersion")
    def documentation_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the associated API documentation.
        """
        return pulumi.get(self, "documentation_version")

    @property
    @pulumi.getter(name="methodSettings")
    def method_settings(self) -> pulumi.Output[Optional[Sequence['outputs.StageMethodSetting']]]:
        """
        A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.
        """
        return pulumi.get(self, "method_settings")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[str]:
        """
        The string identifier of the associated RestApi.
        """
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
        """
        return pulumi.get(self, "stage_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StageTag']]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tracingEnabled")
    def tracing_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether active tracing with X-ray is enabled for the Stage.
        """
        return pulumi.get(self, "tracing_enabled")

    @property
    @pulumi.getter
    def variables(self) -> pulumi.Output[Optional[Any]]:
        """
        A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
        """
        return pulumi.get(self, "variables")

