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

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 access_token: Optional[pulumi.Input[str]] = None,
                 auto_branch_creation_config: Optional[pulumi.Input['AppAutoBranchCreationConfigArgs']] = None,
                 basic_auth_config: Optional[pulumi.Input['AppBasicAuthConfigArgs']] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AppCustomRuleArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_branch_auto_deletion: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]] = None,
                 i_am_service_role: Optional[pulumi.Input[str]] = None,
                 oauth_token: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]] = None):
        """
        The set of arguments for constructing a App resource.
        """
        pulumi.set(__self__, "name", name)
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if auto_branch_creation_config is not None:
            pulumi.set(__self__, "auto_branch_creation_config", auto_branch_creation_config)
        if basic_auth_config is not None:
            pulumi.set(__self__, "basic_auth_config", basic_auth_config)
        if build_spec is not None:
            pulumi.set(__self__, "build_spec", build_spec)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if custom_rules is not None:
            pulumi.set(__self__, "custom_rules", custom_rules)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_branch_auto_deletion is not None:
            pulumi.set(__self__, "enable_branch_auto_deletion", enable_branch_auto_deletion)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if i_am_service_role is not None:
            pulumi.set(__self__, "i_am_service_role", i_am_service_role)
        if oauth_token is not None:
            pulumi.set(__self__, "oauth_token", oauth_token)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_token")

    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_token", value)

    @property
    @pulumi.getter(name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> Optional[pulumi.Input['AppAutoBranchCreationConfigArgs']]:
        return pulumi.get(self, "auto_branch_creation_config")

    @auto_branch_creation_config.setter
    def auto_branch_creation_config(self, value: Optional[pulumi.Input['AppAutoBranchCreationConfigArgs']]):
        pulumi.set(self, "auto_branch_creation_config", value)

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> Optional[pulumi.Input['AppBasicAuthConfigArgs']]:
        return pulumi.get(self, "basic_auth_config")

    @basic_auth_config.setter
    def basic_auth_config(self, value: Optional[pulumi.Input['AppBasicAuthConfigArgs']]):
        pulumi.set(self, "basic_auth_config", value)

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "build_spec")

    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_spec", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppCustomRuleArgs']]]]:
        return pulumi.get(self, "custom_rules")

    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppCustomRuleArgs']]]]):
        pulumi.set(self, "custom_rules", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_branch_auto_deletion")

    @enable_branch_auto_deletion.setter
    def enable_branch_auto_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_branch_auto_deletion", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]:
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="iAMServiceRole")
    def i_am_service_role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "i_am_service_role")

    @i_am_service_role.setter
    def i_am_service_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "i_am_service_role", value)

    @property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "oauth_token")

    @oauth_token.setter
    def oauth_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_token", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]]):
        pulumi.set(self, "tags", value)


class App(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 auto_branch_creation_config: Optional[pulumi.Input[pulumi.InputType['AppAutoBranchCreationConfigArgs']]] = None,
                 basic_auth_config: Optional[pulumi.Input[pulumi.InputType['AppBasicAuthConfigArgs']]] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppCustomRuleArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_branch_auto_deletion: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppEnvironmentVariableArgs']]]]] = None,
                 i_am_service_role: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_token: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.

        :param str resource_name: The name of the resource.
        :param AppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 auto_branch_creation_config: Optional[pulumi.Input[pulumi.InputType['AppAutoBranchCreationConfigArgs']]] = None,
                 basic_auth_config: Optional[pulumi.Input[pulumi.InputType['AppBasicAuthConfigArgs']]] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppCustomRuleArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_branch_auto_deletion: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppEnvironmentVariableArgs']]]]] = None,
                 i_am_service_role: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_token: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTagArgs']]]]] = None,
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
            __props__ = AppArgs.__new__(AppArgs)

            __props__.__dict__["access_token"] = access_token
            __props__.__dict__["auto_branch_creation_config"] = auto_branch_creation_config
            __props__.__dict__["basic_auth_config"] = basic_auth_config
            __props__.__dict__["build_spec"] = build_spec
            __props__.__dict__["custom_headers"] = custom_headers
            __props__.__dict__["custom_rules"] = custom_rules
            __props__.__dict__["description"] = description
            __props__.__dict__["enable_branch_auto_deletion"] = enable_branch_auto_deletion
            __props__.__dict__["environment_variables"] = environment_variables
            __props__.__dict__["i_am_service_role"] = i_am_service_role
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["oauth_token"] = oauth_token
            __props__.__dict__["repository"] = repository
            __props__.__dict__["tags"] = tags
            __props__.__dict__["app_id"] = None
            __props__.__dict__["app_name"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["default_domain"] = None
        super(App, __self__).__init__(
            'aws-native:amplify:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppArgs.__new__(AppArgs)

        __props__.__dict__["access_token"] = None
        __props__.__dict__["app_id"] = None
        __props__.__dict__["app_name"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_branch_creation_config"] = None
        __props__.__dict__["basic_auth_config"] = None
        __props__.__dict__["build_spec"] = None
        __props__.__dict__["custom_headers"] = None
        __props__.__dict__["custom_rules"] = None
        __props__.__dict__["default_domain"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enable_branch_auto_deletion"] = None
        __props__.__dict__["environment_variables"] = None
        __props__.__dict__["i_am_service_role"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["oauth_token"] = None
        __props__.__dict__["repository"] = None
        __props__.__dict__["tags"] = None
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> pulumi.Output[Optional['outputs.AppAutoBranchCreationConfig']]:
        return pulumi.get(self, "auto_branch_creation_config")

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> pulumi.Output[Optional['outputs.AppBasicAuthConfig']]:
        return pulumi.get(self, "basic_auth_config")

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "build_spec")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[Sequence['outputs.AppCustomRule']]]:
        return pulumi.get(self, "custom_rules")

    @property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[str]:
        return pulumi.get(self, "default_domain")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_branch_auto_deletion")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Sequence['outputs.AppEnvironmentVariable']]]:
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="iAMServiceRole")
    def i_am_service_role(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "i_am_service_role")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "oauth_token")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AppTag']]]:
        return pulumi.get(self, "tags")

