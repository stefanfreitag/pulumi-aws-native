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
from ._enums import *
from ._inputs import *

__all__ = ['StateMachineAliasArgs', 'StateMachineAlias']

@pulumi.input_type
class StateMachineAliasArgs:
    def __init__(__self__, *,
                 deployment_preference: Optional[pulumi.Input['StateMachineAliasDeploymentPreferenceArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineAliasRoutingConfigurationVersionArgs']]]] = None):
        """
        The set of arguments for constructing a StateMachineAlias resource.
        :param pulumi.Input[str] description: An optional description of the alias.
        :param pulumi.Input[str] name: The alias name.
        """
        StateMachineAliasArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            deployment_preference=deployment_preference,
            description=description,
            name=name,
            routing_configuration=routing_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             deployment_preference: Optional[pulumi.Input['StateMachineAliasDeploymentPreferenceArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             routing_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineAliasRoutingConfigurationVersionArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if deployment_preference is not None:
            _setter("deployment_preference", deployment_preference)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if routing_configuration is not None:
            _setter("routing_configuration", routing_configuration)

    @property
    @pulumi.getter(name="deploymentPreference")
    def deployment_preference(self) -> Optional[pulumi.Input['StateMachineAliasDeploymentPreferenceArgs']]:
        return pulumi.get(self, "deployment_preference")

    @deployment_preference.setter
    def deployment_preference(self, value: Optional[pulumi.Input['StateMachineAliasDeploymentPreferenceArgs']]):
        pulumi.set(self, "deployment_preference", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of the alias.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The alias name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineAliasRoutingConfigurationVersionArgs']]]]:
        return pulumi.get(self, "routing_configuration")

    @routing_configuration.setter
    def routing_configuration(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StateMachineAliasRoutingConfigurationVersionArgs']]]]):
        pulumi.set(self, "routing_configuration", value)


class StateMachineAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_preference: Optional[pulumi.Input[pulumi.InputType['StateMachineAliasDeploymentPreferenceArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StateMachineAliasRoutingConfigurationVersionArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for StateMachineAlias

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of the alias.
        :param pulumi.Input[str] name: The alias name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StateMachineAliasArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for StateMachineAlias

        :param str resource_name: The name of the resource.
        :param StateMachineAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StateMachineAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            StateMachineAliasArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_preference: Optional[pulumi.Input[pulumi.InputType['StateMachineAliasDeploymentPreferenceArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StateMachineAliasRoutingConfigurationVersionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StateMachineAliasArgs.__new__(StateMachineAliasArgs)

            if deployment_preference is not None and not isinstance(deployment_preference, StateMachineAliasDeploymentPreferenceArgs):
                deployment_preference = deployment_preference or {}
                def _setter(key, value):
                    deployment_preference[key] = value
                StateMachineAliasDeploymentPreferenceArgs._configure(_setter, **deployment_preference)
            __props__.__dict__["deployment_preference"] = deployment_preference
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["routing_configuration"] = routing_configuration
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(StateMachineAlias, __self__).__init__(
            'aws-native:stepfunctions:StateMachineAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StateMachineAlias':
        """
        Get an existing StateMachineAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StateMachineAliasArgs.__new__(StateMachineAliasArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["deployment_preference"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["routing_configuration"] = None
        return StateMachineAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the alias.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deploymentPreference")
    def deployment_preference(self) -> pulumi.Output[Optional['outputs.StateMachineAliasDeploymentPreference']]:
        return pulumi.get(self, "deployment_preference")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of the alias.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The alias name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> pulumi.Output[Optional[Sequence['outputs.StateMachineAliasRoutingConfigurationVersion']]]:
        return pulumi.get(self, "routing_configuration")

