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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['VpcIngressConnectionArgs', 'VpcIngressConnection']

@pulumi.input_type
class VpcIngressConnectionArgs:
    def __init__(__self__, *,
                 ingress_vpc_configuration: pulumi.Input['VpcIngressConnectionIngressVpcConfigurationArgs'],
                 service_arn: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]] = None,
                 vpc_ingress_connection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcIngressConnection resource.
        :param pulumi.Input[str] service_arn: The Amazon Resource Name (ARN) of the service.
        :param pulumi.Input[str] vpc_ingress_connection_name: The customer-provided Vpc Ingress Connection name.
        """
        pulumi.set(__self__, "ingress_vpc_configuration", ingress_vpc_configuration)
        pulumi.set(__self__, "service_arn", service_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_ingress_connection_name is not None:
            pulumi.set(__self__, "vpc_ingress_connection_name", vpc_ingress_connection_name)

    @property
    @pulumi.getter(name="ingressVpcConfiguration")
    def ingress_vpc_configuration(self) -> pulumi.Input['VpcIngressConnectionIngressVpcConfigurationArgs']:
        return pulumi.get(self, "ingress_vpc_configuration")

    @ingress_vpc_configuration.setter
    def ingress_vpc_configuration(self, value: pulumi.Input['VpcIngressConnectionIngressVpcConfigurationArgs']):
        pulumi.set(self, "ingress_vpc_configuration", value)

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the service.
        """
        return pulumi.get(self, "service_arn")

    @service_arn.setter
    def service_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcIngressConnectionName")
    def vpc_ingress_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The customer-provided Vpc Ingress Connection name.
        """
        return pulumi.get(self, "vpc_ingress_connection_name")

    @vpc_ingress_connection_name.setter
    def vpc_ingress_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_ingress_connection_name", value)


class VpcIngressConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ingress_vpc_configuration: Optional[pulumi.Input[pulumi.InputType['VpcIngressConnectionIngressVpcConfigurationArgs']]] = None,
                 service_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 vpc_ingress_connection_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] service_arn: The Amazon Resource Name (ARN) of the service.
        :param pulumi.Input[str] vpc_ingress_connection_name: The customer-provided Vpc Ingress Connection name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcIngressConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.

        :param str resource_name: The name of the resource.
        :param VpcIngressConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcIngressConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ingress_vpc_configuration: Optional[pulumi.Input[pulumi.InputType['VpcIngressConnectionIngressVpcConfigurationArgs']]] = None,
                 service_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 vpc_ingress_connection_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcIngressConnectionArgs.__new__(VpcIngressConnectionArgs)

            if ingress_vpc_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'ingress_vpc_configuration'")
            __props__.__dict__["ingress_vpc_configuration"] = ingress_vpc_configuration
            if service_arn is None and not opts.urn:
                raise TypeError("Missing required property 'service_arn'")
            __props__.__dict__["service_arn"] = service_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_ingress_connection_name"] = vpc_ingress_connection_name
            __props__.__dict__["domain_name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["vpc_ingress_connection_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["service_arn", "tags[*]", "vpc_ingress_connection_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VpcIngressConnection, __self__).__init__(
            'aws-native:apprunner:VpcIngressConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpcIngressConnection':
        """
        Get an existing VpcIngressConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcIngressConnectionArgs.__new__(VpcIngressConnectionArgs)

        __props__.__dict__["domain_name"] = None
        __props__.__dict__["ingress_vpc_configuration"] = None
        __props__.__dict__["service_arn"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_ingress_connection_arn"] = None
        __props__.__dict__["vpc_ingress_connection_name"] = None
        return VpcIngressConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The Domain name associated with the VPC Ingress Connection.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="ingressVpcConfiguration")
    def ingress_vpc_configuration(self) -> pulumi.Output['outputs.VpcIngressConnectionIngressVpcConfiguration']:
        return pulumi.get(self, "ingress_vpc_configuration")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the service.
        """
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['VpcIngressConnectionStatus']:
        """
        The current status of the VpcIngressConnection.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.CreateOnlyTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcIngressConnectionArn")
    def vpc_ingress_connection_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the VpcIngressConnection.
        """
        return pulumi.get(self, "vpc_ingress_connection_arn")

    @property
    @pulumi.getter(name="vpcIngressConnectionName")
    def vpc_ingress_connection_name(self) -> pulumi.Output[Optional[str]]:
        """
        The customer-provided Vpc Ingress Connection name.
        """
        return pulumi.get(self, "vpc_ingress_connection_name")

