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

__all__ = ['ResolverEndpointArgs', 'ResolverEndpoint']

@pulumi.input_type
class ResolverEndpointArgs:
    def __init__(__self__, *,
                 direction: pulumi.Input[str],
                 ip_addresses: pulumi.Input[Sequence[pulumi.Input['ResolverEndpointIpAddressRequestArgs']]],
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 preferred_instance_type: Optional[pulumi.Input[str]] = None,
                 resolver_endpoint_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ResolverEndpointTagArgs']]]] = None):
        """
        The set of arguments for constructing a ResolverEndpoint resource.
        """
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "ip_addresses", ip_addresses)
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if outpost_arn is not None:
            pulumi.set(__self__, "outpost_arn", outpost_arn)
        if preferred_instance_type is not None:
            pulumi.set(__self__, "preferred_instance_type", preferred_instance_type)
        if resolver_endpoint_type is not None:
            pulumi.set(__self__, "resolver_endpoint_type", resolver_endpoint_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Input[Sequence[pulumi.Input['ResolverEndpointIpAddressRequestArgs']]]:
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: pulumi.Input[Sequence[pulumi.Input['ResolverEndpointIpAddressRequestArgs']]]):
        pulumi.set(self, "ip_addresses", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "outpost_arn")

    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outpost_arn", value)

    @property
    @pulumi.getter(name="preferredInstanceType")
    def preferred_instance_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_instance_type")

    @preferred_instance_type.setter
    def preferred_instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_instance_type", value)

    @property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resolver_endpoint_type")

    @resolver_endpoint_type.setter
    def resolver_endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolver_endpoint_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResolverEndpointTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResolverEndpointTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""ResolverEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ResolverEndpoint(pulumi.CustomResource):
    warnings.warn("""ResolverEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressRequestArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 preferred_instance_type: Optional[pulumi.Input[str]] = None,
                 resolver_endpoint_type: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Route53Resolver::ResolverEndpoint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResolverEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Route53Resolver::ResolverEndpoint

        :param str resource_name: The name of the resource.
        :param ResolverEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressRequestArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 preferred_instance_type: Optional[pulumi.Input[str]] = None,
                 resolver_endpoint_type: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ResolverEndpoint is deprecated: ResolverEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverEndpointArgs.__new__(ResolverEndpointArgs)

            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            if ip_addresses is None and not opts.urn:
                raise TypeError("Missing required property 'ip_addresses'")
            __props__.__dict__["ip_addresses"] = ip_addresses
            __props__.__dict__["name"] = name
            __props__.__dict__["outpost_arn"] = outpost_arn
            __props__.__dict__["preferred_instance_type"] = preferred_instance_type
            __props__.__dict__["resolver_endpoint_type"] = resolver_endpoint_type
            if security_group_ids is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["host_vpc_id"] = None
            __props__.__dict__["ip_address_count"] = None
            __props__.__dict__["resolver_endpoint_id"] = None
        super(ResolverEndpoint, __self__).__init__(
            'aws-native:route53resolver:ResolverEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResolverEndpoint':
        """
        Get an existing ResolverEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResolverEndpointArgs.__new__(ResolverEndpointArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["direction"] = None
        __props__.__dict__["host_vpc_id"] = None
        __props__.__dict__["ip_address_count"] = None
        __props__.__dict__["ip_addresses"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["outpost_arn"] = None
        __props__.__dict__["preferred_instance_type"] = None
        __props__.__dict__["resolver_endpoint_id"] = None
        __props__.__dict__["resolver_endpoint_type"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["tags"] = None
        return ResolverEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="hostVPCId")
    def host_vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "host_vpc_id")

    @property
    @pulumi.getter(name="ipAddressCount")
    def ip_address_count(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ip_address_count")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence['outputs.ResolverEndpointIpAddressRequest']]:
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="preferredInstanceType")
    def preferred_instance_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_instance_type")

    @property
    @pulumi.getter(name="resolverEndpointId")
    def resolver_endpoint_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resolver_endpoint_id")

    @property
    @pulumi.getter(name="resolverEndpointType")
    def resolver_endpoint_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resolver_endpoint_type")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ResolverEndpointTag']]]:
        return pulumi.get(self, "tags")

