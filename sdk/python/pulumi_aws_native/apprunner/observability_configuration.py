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

__all__ = ['ObservabilityConfigurationArgs', 'ObservabilityConfiguration']

@pulumi.input_type
class ObservabilityConfigurationArgs:
    def __init__(__self__, *,
                 observability_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ObservabilityConfigurationTagArgs']]]] = None,
                 trace_configuration: Optional[pulumi.Input['ObservabilityConfigurationTraceConfigurationArgs']] = None):
        """
        The set of arguments for constructing a ObservabilityConfiguration resource.
        :param pulumi.Input[str] observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        :param pulumi.Input[Sequence[pulumi.Input['ObservabilityConfigurationTagArgs']]] tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param pulumi.Input['ObservabilityConfigurationTraceConfigurationArgs'] trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        """
        if observability_configuration_name is not None:
            pulumi.set(__self__, "observability_configuration_name", observability_configuration_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trace_configuration is not None:
            pulumi.set(__self__, "trace_configuration", trace_configuration)

    @property
    @pulumi.getter(name="observabilityConfigurationName")
    def observability_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        """
        return pulumi.get(self, "observability_configuration_name")

    @observability_configuration_name.setter
    def observability_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "observability_configuration_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ObservabilityConfigurationTagArgs']]]]:
        """
        A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ObservabilityConfigurationTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="traceConfiguration")
    def trace_configuration(self) -> Optional[pulumi.Input['ObservabilityConfigurationTraceConfigurationArgs']]:
        """
        The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        """
        return pulumi.get(self, "trace_configuration")

    @trace_configuration.setter
    def trace_configuration(self, value: Optional[pulumi.Input['ObservabilityConfigurationTraceConfigurationArgs']]):
        pulumi.set(self, "trace_configuration", value)


class ObservabilityConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 observability_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObservabilityConfigurationTagArgs']]]]] = None,
                 trace_configuration: Optional[pulumi.Input[pulumi.InputType['ObservabilityConfigurationTraceConfigurationArgs']]] = None,
                 __props__=None):
        """
        The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObservabilityConfigurationTagArgs']]]] tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param pulumi.Input[pulumi.InputType['ObservabilityConfigurationTraceConfigurationArgs']] trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ObservabilityConfigurationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration

        :param str resource_name: The name of the resource.
        :param ObservabilityConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObservabilityConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 observability_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObservabilityConfigurationTagArgs']]]]] = None,
                 trace_configuration: Optional[pulumi.Input[pulumi.InputType['ObservabilityConfigurationTraceConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObservabilityConfigurationArgs.__new__(ObservabilityConfigurationArgs)

            __props__.__dict__["observability_configuration_name"] = observability_configuration_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trace_configuration"] = trace_configuration
            __props__.__dict__["latest"] = None
            __props__.__dict__["observability_configuration_arn"] = None
            __props__.__dict__["observability_configuration_revision"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["observability_configuration_name", "tags[*]", "trace_configuration"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ObservabilityConfiguration, __self__).__init__(
            'aws-native:apprunner:ObservabilityConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ObservabilityConfiguration':
        """
        Get an existing ObservabilityConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ObservabilityConfigurationArgs.__new__(ObservabilityConfigurationArgs)

        __props__.__dict__["latest"] = None
        __props__.__dict__["observability_configuration_arn"] = None
        __props__.__dict__["observability_configuration_name"] = None
        __props__.__dict__["observability_configuration_revision"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trace_configuration"] = None
        return ObservabilityConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def latest(self) -> pulumi.Output[bool]:
        """
        It's set to true for the configuration with the highest Revision among all configurations that share the same Name. It's set to false otherwise.
        """
        return pulumi.get(self, "latest")

    @property
    @pulumi.getter(name="observabilityConfigurationArn")
    def observability_configuration_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of this ObservabilityConfiguration
        """
        return pulumi.get(self, "observability_configuration_arn")

    @property
    @pulumi.getter(name="observabilityConfigurationName")
    def observability_configuration_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        """
        return pulumi.get(self, "observability_configuration_name")

    @property
    @pulumi.getter(name="observabilityConfigurationRevision")
    def observability_configuration_revision(self) -> pulumi.Output[int]:
        """
        The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.
        """
        return pulumi.get(self, "observability_configuration_revision")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ObservabilityConfigurationTag']]]:
        """
        A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="traceConfiguration")
    def trace_configuration(self) -> pulumi.Output[Optional['outputs.ObservabilityConfigurationTraceConfiguration']]:
        """
        The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        """
        return pulumi.get(self, "trace_configuration")

