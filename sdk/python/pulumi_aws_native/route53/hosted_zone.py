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

__all__ = ['HostedZoneArgs', 'HostedZone']

@pulumi.input_type
class HostedZoneArgs:
    def __init__(__self__, *,
                 hosted_zone_config: Optional[pulumi.Input['HostedZoneConfigArgs']] = None,
                 hosted_zone_tags: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneTagArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_logging_config: Optional[pulumi.Input['HostedZoneQueryLoggingConfigArgs']] = None,
                 vpcs: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneVpcArgs']]]] = None):
        """
        The set of arguments for constructing a HostedZone resource.
        :param pulumi.Input[Sequence[pulumi.Input['HostedZoneTagArgs']]] hosted_zone_tags: Adds, edits, or deletes tags for a health check or a hosted zone.
               
               For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
        :param pulumi.Input[str] name: The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
               
               If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
        :param pulumi.Input[Sequence[pulumi.Input['HostedZoneVpcArgs']]] vpcs: A complex type that contains information about the VPCs that are associated with the specified hosted zone.
        """
        HostedZoneArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            hosted_zone_config=hosted_zone_config,
            hosted_zone_tags=hosted_zone_tags,
            name=name,
            query_logging_config=query_logging_config,
            vpcs=vpcs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             hosted_zone_config: Optional[pulumi.Input['HostedZoneConfigArgs']] = None,
             hosted_zone_tags: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneTagArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             query_logging_config: Optional[pulumi.Input['HostedZoneQueryLoggingConfigArgs']] = None,
             vpcs: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneVpcArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if hosted_zone_config is not None:
            _setter("hosted_zone_config", hosted_zone_config)
        if hosted_zone_tags is not None:
            _setter("hosted_zone_tags", hosted_zone_tags)
        if name is not None:
            _setter("name", name)
        if query_logging_config is not None:
            _setter("query_logging_config", query_logging_config)
        if vpcs is not None:
            _setter("vpcs", vpcs)

    @property
    @pulumi.getter(name="hostedZoneConfig")
    def hosted_zone_config(self) -> Optional[pulumi.Input['HostedZoneConfigArgs']]:
        return pulumi.get(self, "hosted_zone_config")

    @hosted_zone_config.setter
    def hosted_zone_config(self, value: Optional[pulumi.Input['HostedZoneConfigArgs']]):
        pulumi.set(self, "hosted_zone_config", value)

    @property
    @pulumi.getter(name="hostedZoneTags")
    def hosted_zone_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneTagArgs']]]]:
        """
        Adds, edits, or deletes tags for a health check or a hosted zone.

        For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
        """
        return pulumi.get(self, "hosted_zone_tags")

    @hosted_zone_tags.setter
    def hosted_zone_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneTagArgs']]]]):
        pulumi.set(self, "hosted_zone_tags", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.

        If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queryLoggingConfig")
    def query_logging_config(self) -> Optional[pulumi.Input['HostedZoneQueryLoggingConfigArgs']]:
        return pulumi.get(self, "query_logging_config")

    @query_logging_config.setter
    def query_logging_config(self, value: Optional[pulumi.Input['HostedZoneQueryLoggingConfigArgs']]):
        pulumi.set(self, "query_logging_config", value)

    @property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneVpcArgs']]]]:
        """
        A complex type that contains information about the VPCs that are associated with the specified hosted zone.
        """
        return pulumi.get(self, "vpcs")

    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HostedZoneVpcArgs']]]]):
        pulumi.set(self, "vpcs", value)


class HostedZone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_config: Optional[pulumi.Input[pulumi.InputType['HostedZoneConfigArgs']]] = None,
                 hosted_zone_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneTagArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_logging_config: Optional[pulumi.Input[pulumi.InputType['HostedZoneQueryLoggingConfigArgs']]] = None,
                 vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneVpcArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53::HostedZone.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneTagArgs']]]] hosted_zone_tags: Adds, edits, or deletes tags for a health check or a hosted zone.
               
               For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
        :param pulumi.Input[str] name: The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
               
               If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneVpcArgs']]]] vpcs: A complex type that contains information about the VPCs that are associated with the specified hosted zone.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[HostedZoneArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53::HostedZone.

        :param str resource_name: The name of the resource.
        :param HostedZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HostedZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HostedZoneArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_config: Optional[pulumi.Input[pulumi.InputType['HostedZoneConfigArgs']]] = None,
                 hosted_zone_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneTagArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_logging_config: Optional[pulumi.Input[pulumi.InputType['HostedZoneQueryLoggingConfigArgs']]] = None,
                 vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostedZoneVpcArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HostedZoneArgs.__new__(HostedZoneArgs)

            if hosted_zone_config is not None and not isinstance(hosted_zone_config, HostedZoneConfigArgs):
                hosted_zone_config = hosted_zone_config or {}
                def _setter(key, value):
                    hosted_zone_config[key] = value
                HostedZoneConfigArgs._configure(_setter, **hosted_zone_config)
            __props__.__dict__["hosted_zone_config"] = hosted_zone_config
            __props__.__dict__["hosted_zone_tags"] = hosted_zone_tags
            __props__.__dict__["name"] = name
            if query_logging_config is not None and not isinstance(query_logging_config, HostedZoneQueryLoggingConfigArgs):
                query_logging_config = query_logging_config or {}
                def _setter(key, value):
                    query_logging_config[key] = value
                HostedZoneQueryLoggingConfigArgs._configure(_setter, **query_logging_config)
            __props__.__dict__["query_logging_config"] = query_logging_config
            __props__.__dict__["vpcs"] = vpcs
            __props__.__dict__["name_servers"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(HostedZone, __self__).__init__(
            'aws-native:route53:HostedZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HostedZone':
        """
        Get an existing HostedZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HostedZoneArgs.__new__(HostedZoneArgs)

        __props__.__dict__["hosted_zone_config"] = None
        __props__.__dict__["hosted_zone_tags"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["name_servers"] = None
        __props__.__dict__["query_logging_config"] = None
        __props__.__dict__["vpcs"] = None
        return HostedZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostedZoneConfig")
    def hosted_zone_config(self) -> pulumi.Output[Optional['outputs.HostedZoneConfig']]:
        return pulumi.get(self, "hosted_zone_config")

    @property
    @pulumi.getter(name="hostedZoneTags")
    def hosted_zone_tags(self) -> pulumi.Output[Optional[Sequence['outputs.HostedZoneTag']]]:
        """
        Adds, edits, or deletes tags for a health check or a hosted zone.

        For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
        """
        return pulumi.get(self, "hosted_zone_tags")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.

        If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter(name="queryLoggingConfig")
    def query_logging_config(self) -> pulumi.Output[Optional['outputs.HostedZoneQueryLoggingConfig']]:
        return pulumi.get(self, "query_logging_config")

    @property
    @pulumi.getter
    def vpcs(self) -> pulumi.Output[Optional[Sequence['outputs.HostedZoneVpc']]]:
        """
        A complex type that contains information about the VPCs that are associated with the specified hosted zone.
        """
        return pulumi.get(self, "vpcs")

