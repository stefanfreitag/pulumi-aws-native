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

__all__ = ['LocalGatewayRouteTableVpcAssociationArgs', 'LocalGatewayRouteTableVpcAssociation']

@pulumi.input_type
class LocalGatewayRouteTableVpcAssociationArgs:
    def __init__(__self__, *,
                 local_gateway_route_table_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LocalGatewayRouteTableVpcAssociationTagArgs']]]] = None):
        """
        The set of arguments for constructing a LocalGatewayRouteTableVpcAssociation resource.
        :param pulumi.Input[str] local_gateway_route_table_id: The ID of the local gateway route table.
        :param pulumi.Input[str] vpc_id: The ID of the VPC.
        :param pulumi.Input[Sequence[pulumi.Input['LocalGatewayRouteTableVpcAssociationTagArgs']]] tags: The tags for the association.
        """
        pulumi.set(__self__, "local_gateway_route_table_id", local_gateway_route_table_id)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Input[str]:
        """
        The ID of the local gateway route table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @local_gateway_route_table_id.setter
    def local_gateway_route_table_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "local_gateway_route_table_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPC.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalGatewayRouteTableVpcAssociationTagArgs']]]]:
        """
        The tags for the association.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalGatewayRouteTableVpcAssociationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LocalGatewayRouteTableVpcAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalGatewayRouteTableVpcAssociationTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes an association between a local gateway route table and a VPC.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] local_gateway_route_table_id: The ID of the local gateway route table.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalGatewayRouteTableVpcAssociationTagArgs']]]] tags: The tags for the association.
        :param pulumi.Input[str] vpc_id: The ID of the VPC.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalGatewayRouteTableVpcAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes an association between a local gateway route table and a VPC.

        :param str resource_name: The name of the resource.
        :param LocalGatewayRouteTableVpcAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalGatewayRouteTableVpcAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalGatewayRouteTableVpcAssociationTagArgs']]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalGatewayRouteTableVpcAssociationArgs.__new__(LocalGatewayRouteTableVpcAssociationArgs)

            if local_gateway_route_table_id is None and not opts.urn:
                raise TypeError("Missing required property 'local_gateway_route_table_id'")
            __props__.__dict__["local_gateway_route_table_id"] = local_gateway_route_table_id
            __props__.__dict__["tags"] = tags
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["local_gateway_id"] = None
            __props__.__dict__["local_gateway_route_table_vpc_association_id"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["local_gateway_route_table_id", "vpc_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LocalGatewayRouteTableVpcAssociation, __self__).__init__(
            'aws-native:ec2:LocalGatewayRouteTableVpcAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocalGatewayRouteTableVpcAssociation':
        """
        Get an existing LocalGatewayRouteTableVpcAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocalGatewayRouteTableVpcAssociationArgs.__new__(LocalGatewayRouteTableVpcAssociationArgs)

        __props__.__dict__["local_gateway_id"] = None
        __props__.__dict__["local_gateway_route_table_id"] = None
        __props__.__dict__["local_gateway_route_table_vpc_association_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_id"] = None
        return LocalGatewayRouteTableVpcAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the local gateway.
        """
        return pulumi.get(self, "local_gateway_id")

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Output[str]:
        """
        The ID of the local gateway route table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @property
    @pulumi.getter(name="localGatewayRouteTableVpcAssociationId")
    def local_gateway_route_table_vpc_association_id(self) -> pulumi.Output[str]:
        """
        The ID of the association.
        """
        return pulumi.get(self, "local_gateway_route_table_vpc_association_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the association.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LocalGatewayRouteTableVpcAssociationTag']]]:
        """
        The tags for the association.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC.
        """
        return pulumi.get(self, "vpc_id")

