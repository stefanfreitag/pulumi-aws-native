# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 cname_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 operations_role: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentOptionSettingArgs']]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTagArgs']]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['EnvironmentTierArgs']] = None,
                 version_label: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] application_name: The name of the application that is associated with this environment.
        :param pulumi.Input[str] cname_prefix: If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        :param pulumi.Input[str] description: Your description for this environment.
        :param pulumi.Input[str] environment_name: A unique name for the environment.
        :param pulumi.Input[str] operations_role: The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentOptionSettingArgs']]] option_settings: Key-value pairs defining configuration options for this environment, such as the instance type.
        :param pulumi.Input[str] platform_arn: The Amazon Resource Name (ARN) of the custom platform to use with the environment.
        :param pulumi.Input[str] solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentTagArgs']]] tags: Specifies the tags applied to resources in the environment.
        :param pulumi.Input[str] template_name: The name of the Elastic Beanstalk configuration template to use with the environment.
        :param pulumi.Input['EnvironmentTierArgs'] tier: Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        :param pulumi.Input[str] version_label: The name of the application version to deploy.
        """
        EnvironmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_name=application_name,
            cname_prefix=cname_prefix,
            description=description,
            environment_name=environment_name,
            operations_role=operations_role,
            option_settings=option_settings,
            platform_arn=platform_arn,
            solution_stack_name=solution_stack_name,
            tags=tags,
            template_name=template_name,
            tier=tier,
            version_label=version_label,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_name: pulumi.Input[str],
             cname_prefix: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             environment_name: Optional[pulumi.Input[str]] = None,
             operations_role: Optional[pulumi.Input[str]] = None,
             option_settings: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentOptionSettingArgs']]]] = None,
             platform_arn: Optional[pulumi.Input[str]] = None,
             solution_stack_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTagArgs']]]] = None,
             template_name: Optional[pulumi.Input[str]] = None,
             tier: Optional[pulumi.Input['EnvironmentTierArgs']] = None,
             version_label: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("application_name", application_name)
        if cname_prefix is not None:
            _setter("cname_prefix", cname_prefix)
        if description is not None:
            _setter("description", description)
        if environment_name is not None:
            _setter("environment_name", environment_name)
        if operations_role is not None:
            _setter("operations_role", operations_role)
        if option_settings is not None:
            _setter("option_settings", option_settings)
        if platform_arn is not None:
            _setter("platform_arn", platform_arn)
        if solution_stack_name is not None:
            _setter("solution_stack_name", solution_stack_name)
        if tags is not None:
            _setter("tags", tags)
        if template_name is not None:
            _setter("template_name", template_name)
        if tier is not None:
            _setter("tier", tier)
        if version_label is not None:
            _setter("version_label", version_label)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        """
        The name of the application that is associated with this environment.
        """
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter(name="cnamePrefix")
    def cname_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        """
        return pulumi.get(self, "cname_prefix")

    @cname_prefix.setter
    def cname_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname_prefix", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Your description for this environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique name for the environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="operationsRole")
    def operations_role(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.
        """
        return pulumi.get(self, "operations_role")

    @operations_role.setter
    def operations_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operations_role", value)

    @property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentOptionSettingArgs']]]]:
        """
        Key-value pairs defining configuration options for this environment, such as the instance type.
        """
        return pulumi.get(self, "option_settings")

    @option_settings.setter
    def option_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentOptionSettingArgs']]]]):
        pulumi.set(self, "option_settings", value)

    @property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the custom platform to use with the environment.
        """
        return pulumi.get(self, "platform_arn")

    @platform_arn.setter
    def platform_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform_arn", value)

    @property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.
        """
        return pulumi.get(self, "solution_stack_name")

    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_stack_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTagArgs']]]]:
        """
        Specifies the tags applied to resources in the environment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Elastic Beanstalk configuration template to use with the environment.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['EnvironmentTierArgs']]:
        """
        Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['EnvironmentTierArgs']]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter(name="versionLabel")
    def version_label(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application version to deploy.
        """
        return pulumi.get(self, "version_label")

    @version_label.setter
    def version_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_label", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cname_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 operations_role: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentOptionSettingArgs']]]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTagArgs']]]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[pulumi.InputType['EnvironmentTierArgs']]] = None,
                 version_label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElasticBeanstalk::Environment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_name: The name of the application that is associated with this environment.
        :param pulumi.Input[str] cname_prefix: If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        :param pulumi.Input[str] description: Your description for this environment.
        :param pulumi.Input[str] environment_name: A unique name for the environment.
        :param pulumi.Input[str] operations_role: The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentOptionSettingArgs']]]] option_settings: Key-value pairs defining configuration options for this environment, such as the instance type.
        :param pulumi.Input[str] platform_arn: The Amazon Resource Name (ARN) of the custom platform to use with the environment.
        :param pulumi.Input[str] solution_stack_name: The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTagArgs']]]] tags: Specifies the tags applied to resources in the environment.
        :param pulumi.Input[str] template_name: The name of the Elastic Beanstalk configuration template to use with the environment.
        :param pulumi.Input[pulumi.InputType['EnvironmentTierArgs']] tier: Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        :param pulumi.Input[str] version_label: The name of the application version to deploy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElasticBeanstalk::Environment

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EnvironmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cname_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 operations_role: Optional[pulumi.Input[str]] = None,
                 option_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentOptionSettingArgs']]]]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentTagArgs']]]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[pulumi.InputType['EnvironmentTierArgs']]] = None,
                 version_label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            __props__.__dict__["cname_prefix"] = cname_prefix
            __props__.__dict__["description"] = description
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["operations_role"] = operations_role
            __props__.__dict__["option_settings"] = option_settings
            __props__.__dict__["platform_arn"] = platform_arn
            __props__.__dict__["solution_stack_name"] = solution_stack_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template_name"] = template_name
            if tier is not None and not isinstance(tier, EnvironmentTierArgs):
                tier = tier or {}
                def _setter(key, value):
                    tier[key] = value
                EnvironmentTierArgs._configure(_setter, **tier)
            __props__.__dict__["tier"] = tier
            __props__.__dict__["version_label"] = version_label
            __props__.__dict__["endpoint_url"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["application_name", "cname_prefix", "environment_name", "solution_stack_name", "tier.name", "tier.type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Environment, __self__).__init__(
            'aws-native:elasticbeanstalk:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["application_name"] = None
        __props__.__dict__["cname_prefix"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["endpoint_url"] = None
        __props__.__dict__["environment_name"] = None
        __props__.__dict__["operations_role"] = None
        __props__.__dict__["option_settings"] = None
        __props__.__dict__["platform_arn"] = None
        __props__.__dict__["solution_stack_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_name"] = None
        __props__.__dict__["tier"] = None
        __props__.__dict__["version_label"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[str]:
        """
        The name of the application that is associated with this environment.
        """
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="cnamePrefix")
    def cname_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
        """
        return pulumi.get(self, "cname_prefix")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Your description for this environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "endpoint_url")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[str]]:
        """
        A unique name for the environment.
        """
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter(name="operationsRole")
    def operations_role(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.
        """
        return pulumi.get(self, "operations_role")

    @property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentOptionSetting']]]:
        """
        Key-value pairs defining configuration options for this environment, such as the instance type.
        """
        return pulumi.get(self, "option_settings")

    @property
    @pulumi.getter(name="platformArn")
    def platform_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the custom platform to use with the environment.
        """
        return pulumi.get(self, "platform_arn")

    @property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.
        """
        return pulumi.get(self, "solution_stack_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentTag']]]:
        """
        Specifies the tags applied to resources in the environment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Elastic Beanstalk configuration template to use with the environment.
        """
        return pulumi.get(self, "template_name")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional['outputs.EnvironmentTier']]:
        """
        Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="versionLabel")
    def version_label(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the application version to deploy.
        """
        return pulumi.get(self, "version_label")

