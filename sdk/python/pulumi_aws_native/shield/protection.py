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

__all__ = ['ProtectionArgs', 'Protection']

@pulumi.input_type
class ProtectionArgs:
    def __init__(__self__, *,
                 resource_arn: pulumi.Input[str],
                 application_layer_automatic_response_configuration: Optional[pulumi.Input['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']] = None,
                 health_check_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionTagArgs']]]] = None):
        """
        The set of arguments for constructing a Protection resource.
        :param pulumi.Input[str] resource_arn: The ARN (Amazon Resource Name) of the resource to be protected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] health_check_arns: The Amazon Resource Names (ARNs) of the health check to associate with the protection.
        :param pulumi.Input[str] name: Friendly name for the Protection.
        :param pulumi.Input[Sequence[pulumi.Input['ProtectionTagArgs']]] tags: One or more tag key-value pairs for the Protection object.
        """
        ProtectionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_arn=resource_arn,
            application_layer_automatic_response_configuration=application_layer_automatic_response_configuration,
            health_check_arns=health_check_arns,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_arn: pulumi.Input[str],
             application_layer_automatic_response_configuration: Optional[pulumi.Input['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']] = None,
             health_check_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("resource_arn", resource_arn)
        if application_layer_automatic_response_configuration is not None:
            _setter("application_layer_automatic_response_configuration", application_layer_automatic_response_configuration)
        if health_check_arns is not None:
            _setter("health_check_arns", health_check_arns)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        The ARN (Amazon Resource Name) of the resource to be protected.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="applicationLayerAutomaticResponseConfiguration")
    def application_layer_automatic_response_configuration(self) -> Optional[pulumi.Input['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']]:
        return pulumi.get(self, "application_layer_automatic_response_configuration")

    @application_layer_automatic_response_configuration.setter
    def application_layer_automatic_response_configuration(self, value: Optional[pulumi.Input['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']]):
        pulumi.set(self, "application_layer_automatic_response_configuration", value)

    @property
    @pulumi.getter(name="healthCheckArns")
    def health_check_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Amazon Resource Names (ARNs) of the health check to associate with the protection.
        """
        return pulumi.get(self, "health_check_arns")

    @health_check_arns.setter
    def health_check_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "health_check_arns", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name for the Protection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionTagArgs']]]]:
        """
        One or more tag key-value pairs for the Protection object.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Protection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_layer_automatic_response_configuration: Optional[pulumi.Input[pulumi.InputType['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']]] = None,
                 health_check_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionTagArgs']]]]] = None,
                 __props__=None):
        """
        Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] health_check_arns: The Amazon Resource Names (ARNs) of the health check to associate with the protection.
        :param pulumi.Input[str] name: Friendly name for the Protection.
        :param pulumi.Input[str] resource_arn: The ARN (Amazon Resource Name) of the resource to be protected.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionTagArgs']]]] tags: One or more tag key-value pairs for the Protection object.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProtectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

        :param str resource_name: The name of the resource.
        :param ProtectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProtectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProtectionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_layer_automatic_response_configuration: Optional[pulumi.Input[pulumi.InputType['ProtectionApplicationLayerAutomaticResponseConfigurationArgs']]] = None,
                 health_check_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProtectionArgs.__new__(ProtectionArgs)

            if application_layer_automatic_response_configuration is not None and not isinstance(application_layer_automatic_response_configuration, ProtectionApplicationLayerAutomaticResponseConfigurationArgs):
                application_layer_automatic_response_configuration = application_layer_automatic_response_configuration or {}
                def _setter(key, value):
                    application_layer_automatic_response_configuration[key] = value
                ProtectionApplicationLayerAutomaticResponseConfigurationArgs._configure(_setter, **application_layer_automatic_response_configuration)
            __props__.__dict__["application_layer_automatic_response_configuration"] = application_layer_automatic_response_configuration
            __props__.__dict__["health_check_arns"] = health_check_arns
            __props__.__dict__["name"] = name
            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["protection_arn"] = None
            __props__.__dict__["protection_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "resource_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Protection, __self__).__init__(
            'aws-native:shield:Protection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Protection':
        """
        Get an existing Protection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProtectionArgs.__new__(ProtectionArgs)

        __props__.__dict__["application_layer_automatic_response_configuration"] = None
        __props__.__dict__["health_check_arns"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["protection_arn"] = None
        __props__.__dict__["protection_id"] = None
        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["tags"] = None
        return Protection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationLayerAutomaticResponseConfiguration")
    def application_layer_automatic_response_configuration(self) -> pulumi.Output[Optional['outputs.ProtectionApplicationLayerAutomaticResponseConfiguration']]:
        return pulumi.get(self, "application_layer_automatic_response_configuration")

    @property
    @pulumi.getter(name="healthCheckArns")
    def health_check_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Amazon Resource Names (ARNs) of the health check to associate with the protection.
        """
        return pulumi.get(self, "health_check_arns")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Friendly name for the Protection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="protectionArn")
    def protection_arn(self) -> pulumi.Output[str]:
        """
        The ARN (Amazon Resource Name) of the protection.
        """
        return pulumi.get(self, "protection_arn")

    @property
    @pulumi.getter(name="protectionId")
    def protection_id(self) -> pulumi.Output[str]:
        """
        The unique identifier (ID) of the protection.
        """
        return pulumi.get(self, "protection_id")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        The ARN (Amazon Resource Name) of the resource to be protected.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ProtectionTag']]]:
        """
        One or more tag key-value pairs for the Protection object.
        """
        return pulumi.get(self, "tags")

