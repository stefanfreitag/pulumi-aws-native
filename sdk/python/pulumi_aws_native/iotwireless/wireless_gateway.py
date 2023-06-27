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

__all__ = ['WirelessGatewayArgs', 'WirelessGateway']

@pulumi.input_type
class WirelessGatewayArgs:
    def __init__(__self__, *,
                 lo_ra_wan: pulumi.Input['WirelessGatewayLoRaWANGatewayArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 last_uplink_received_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessGatewayTagArgs']]]] = None,
                 thing_arn: Optional[pulumi.Input[str]] = None,
                 thing_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WirelessGateway resource.
        :param pulumi.Input['WirelessGatewayLoRaWANGatewayArgs'] lo_ra_wan: The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
        :param pulumi.Input[str] description: Description of Wireless Gateway.
        :param pulumi.Input[str] last_uplink_received_at: The date and time when the most recent uplink was received.
        :param pulumi.Input[str] name: Name of Wireless Gateway.
        :param pulumi.Input[Sequence[pulumi.Input['WirelessGatewayTagArgs']]] tags: A list of key-value pairs that contain metadata for the gateway.
        :param pulumi.Input[str] thing_arn: Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
        :param pulumi.Input[str] thing_name: Thing Name. If there is a Thing created, this can be returned with a Get call.
        """
        pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if last_uplink_received_at is not None:
            pulumi.set(__self__, "last_uplink_received_at", last_uplink_received_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if thing_arn is not None:
            pulumi.set(__self__, "thing_arn", thing_arn)
        if thing_name is not None:
            pulumi.set(__self__, "thing_name", thing_name)

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> pulumi.Input['WirelessGatewayLoRaWANGatewayArgs']:
        """
        The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
        """
        return pulumi.get(self, "lo_ra_wan")

    @lo_ra_wan.setter
    def lo_ra_wan(self, value: pulumi.Input['WirelessGatewayLoRaWANGatewayArgs']):
        pulumi.set(self, "lo_ra_wan", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of Wireless Gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the most recent uplink was received.
        """
        return pulumi.get(self, "last_uplink_received_at")

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_uplink_received_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Wireless Gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WirelessGatewayTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessGatewayTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="thingArn")
    def thing_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
        """
        return pulumi.get(self, "thing_arn")

    @thing_arn.setter
    def thing_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thing_arn", value)

    @property
    @pulumi.getter(name="thingName")
    def thing_name(self) -> Optional[pulumi.Input[str]]:
        """
        Thing Name. If there is a Thing created, this can be returned with a Get call.
        """
        return pulumi.get(self, "thing_name")

    @thing_name.setter
    def thing_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thing_name", value)


class WirelessGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 last_uplink_received_at: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['WirelessGatewayLoRaWANGatewayArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessGatewayTagArgs']]]]] = None,
                 thing_arn: Optional[pulumi.Input[str]] = None,
                 thing_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create and manage wireless gateways, including LoRa gateways.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of Wireless Gateway.
        :param pulumi.Input[str] last_uplink_received_at: The date and time when the most recent uplink was received.
        :param pulumi.Input[pulumi.InputType['WirelessGatewayLoRaWANGatewayArgs']] lo_ra_wan: The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
        :param pulumi.Input[str] name: Name of Wireless Gateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessGatewayTagArgs']]]] tags: A list of key-value pairs that contain metadata for the gateway.
        :param pulumi.Input[str] thing_arn: Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
        :param pulumi.Input[str] thing_name: Thing Name. If there is a Thing created, this can be returned with a Get call.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WirelessGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create and manage wireless gateways, including LoRa gateways.

        :param str resource_name: The name of the resource.
        :param WirelessGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WirelessGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 last_uplink_received_at: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['WirelessGatewayLoRaWANGatewayArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessGatewayTagArgs']]]]] = None,
                 thing_arn: Optional[pulumi.Input[str]] = None,
                 thing_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WirelessGatewayArgs.__new__(WirelessGatewayArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["last_uplink_received_at"] = last_uplink_received_at
            if lo_ra_wan is None and not opts.urn:
                raise TypeError("Missing required property 'lo_ra_wan'")
            __props__.__dict__["lo_ra_wan"] = lo_ra_wan
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["thing_arn"] = thing_arn
            __props__.__dict__["thing_name"] = thing_name
            __props__.__dict__["arn"] = None
        super(WirelessGateway, __self__).__init__(
            'aws-native:iotwireless:WirelessGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WirelessGateway':
        """
        Get an existing WirelessGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WirelessGatewayArgs.__new__(WirelessGatewayArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_uplink_received_at"] = None
        __props__.__dict__["lo_ra_wan"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["thing_arn"] = None
        __props__.__dict__["thing_name"] = None
        return WirelessGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Arn for Wireless Gateway. Returned upon successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of Wireless Gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> pulumi.Output[Optional[str]]:
        """
        The date and time when the most recent uplink was received.
        """
        return pulumi.get(self, "last_uplink_received_at")

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> pulumi.Output['outputs.WirelessGatewayLoRaWANGateway']:
        """
        The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
        """
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of Wireless Gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.WirelessGatewayTag']]]:
        """
        A list of key-value pairs that contain metadata for the gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="thingArn")
    def thing_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
        """
        return pulumi.get(self, "thing_arn")

    @property
    @pulumi.getter(name="thingName")
    def thing_name(self) -> pulumi.Output[Optional[str]]:
        """
        Thing Name. If there is a Thing created, this can be returned with a Get call.
        """
        return pulumi.get(self, "thing_name")

