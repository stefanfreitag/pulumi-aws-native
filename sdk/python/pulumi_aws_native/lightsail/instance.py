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

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 blueprint_id: pulumi.Input[str],
                 bundle_id: pulumi.Input[str],
                 add_ons: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceAddOnArgs']]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 hardware: Optional[pulumi.Input['InstanceHardwareArgs']] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input['InstanceLocationArgs']] = None,
                 networking: Optional[pulumi.Input['InstanceNetworkingArgs']] = None,
                 state: Optional[pulumi.Input['InstanceStateArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        :param pulumi.Input[str] bundle_id: The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        :param pulumi.Input[Sequence[pulumi.Input['InstanceAddOnArgs']]] add_ons: An array of objects representing the add-ons to enable for the new instance.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        :param pulumi.Input[str] instance_name: The names to use for your new Lightsail instance.
        :param pulumi.Input[str] key_pair_name: The name of your key pair.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] user_data: A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        """
        pulumi.set(__self__, "blueprint_id", blueprint_id)
        pulumi.set(__self__, "bundle_id", bundle_id)
        if add_ons is not None:
            pulumi.set(__self__, "add_ons", add_ons)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if hardware is not None:
            pulumi.set(__self__, "hardware", hardware)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if key_pair_name is not None:
            pulumi.set(__self__, "key_pair_name", key_pair_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if networking is not None:
            pulumi.set(__self__, "networking", networking)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_data is not None:
            pulumi.set(__self__, "user_data", user_data)

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Input[str]:
        """
        The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        """
        return pulumi.get(self, "blueprint_id")

    @blueprint_id.setter
    def blueprint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "blueprint_id", value)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[str]:
        """
        The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        """
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter(name="addOns")
    def add_ons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceAddOnArgs']]]]:
        """
        An array of objects representing the add-ons to enable for the new instance.
        """
        return pulumi.get(self, "add_ons")

    @add_ons.setter
    def add_ons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceAddOnArgs']]]]):
        pulumi.set(self, "add_ons", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter
    def hardware(self) -> Optional[pulumi.Input['InstanceHardwareArgs']]:
        return pulumi.get(self, "hardware")

    @hardware.setter
    def hardware(self, value: Optional[pulumi.Input['InstanceHardwareArgs']]):
        pulumi.set(self, "hardware", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The names to use for your new Lightsail instance.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of your key pair.
        """
        return pulumi.get(self, "key_pair_name")

    @key_pair_name.setter
    def key_pair_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_pair_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input['InstanceLocationArgs']]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input['InstanceLocationArgs']]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def networking(self) -> Optional[pulumi.Input['InstanceNetworkingArgs']]:
        return pulumi.get(self, "networking")

    @networking.setter
    def networking(self, value: Optional[pulumi.Input['InstanceNetworkingArgs']]):
        pulumi.set(self, "networking", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['InstanceStateArgs']]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['InstanceStateArgs']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[str]]:
        """
        A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        """
        return pulumi.get(self, "user_data")

    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_data", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_ons: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceAddOnArgs']]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 hardware: Optional[pulumi.Input[pulumi.InputType['InstanceHardwareArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['InstanceLocationArgs']]] = None,
                 networking: Optional[pulumi.Input[pulumi.InputType['InstanceNetworkingArgs']]] = None,
                 state: Optional[pulumi.Input[pulumi.InputType['InstanceStateArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lightsail::Instance

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceAddOnArgs']]]] add_ons: An array of objects representing the add-ons to enable for the new instance.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        :param pulumi.Input[str] bundle_id: The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        :param pulumi.Input[str] instance_name: The names to use for your new Lightsail instance.
        :param pulumi.Input[str] key_pair_name: The name of your key pair.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] user_data: A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lightsail::Instance

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_ons: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceAddOnArgs']]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 hardware: Optional[pulumi.Input[pulumi.InputType['InstanceHardwareArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['InstanceLocationArgs']]] = None,
                 networking: Optional[pulumi.Input[pulumi.InputType['InstanceNetworkingArgs']]] = None,
                 state: Optional[pulumi.Input[pulumi.InputType['InstanceStateArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["add_ons"] = add_ons
            __props__.__dict__["availability_zone"] = availability_zone
            if blueprint_id is None and not opts.urn:
                raise TypeError("Missing required property 'blueprint_id'")
            __props__.__dict__["blueprint_id"] = blueprint_id
            if bundle_id is None and not opts.urn:
                raise TypeError("Missing required property 'bundle_id'")
            __props__.__dict__["bundle_id"] = bundle_id
            __props__.__dict__["hardware"] = hardware
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["key_pair_name"] = key_pair_name
            __props__.__dict__["location"] = location
            __props__.__dict__["networking"] = networking
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_data"] = user_data
            __props__.__dict__["instance_arn"] = None
            __props__.__dict__["is_static_ip"] = None
            __props__.__dict__["private_ip_address"] = None
            __props__.__dict__["public_ip_address"] = None
            __props__.__dict__["resource_type"] = None
            __props__.__dict__["ssh_key_name"] = None
            __props__.__dict__["support_code"] = None
            __props__.__dict__["user_name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["availability_zone", "blueprint_id", "bundle_id", "instance_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Instance, __self__).__init__(
            'aws-native:lightsail:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["add_ons"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["blueprint_id"] = None
        __props__.__dict__["bundle_id"] = None
        __props__.__dict__["hardware"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["instance_name"] = None
        __props__.__dict__["is_static_ip"] = None
        __props__.__dict__["key_pair_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["networking"] = None
        __props__.__dict__["private_ip_address"] = None
        __props__.__dict__["public_ip_address"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["ssh_key_name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["support_code"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_data"] = None
        __props__.__dict__["user_name"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addOns")
    def add_ons(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceAddOn']]]:
        """
        An array of objects representing the add-ons to enable for the new instance.
        """
        return pulumi.get(self, "add_ons")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Output[str]:
        """
        The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
        """
        return pulumi.get(self, "blueprint_id")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[str]:
        """
        The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter
    def hardware(self) -> pulumi.Output[Optional['outputs.InstanceHardware']]:
        return pulumi.get(self, "hardware")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The names to use for your new Lightsail instance.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="isStaticIp")
    def is_static_ip(self) -> pulumi.Output[bool]:
        """
        Is the IP Address of the Instance is the static IP
        """
        return pulumi.get(self, "is_static_ip")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of your key pair.
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional['outputs.InstanceLocation']]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def networking(self) -> pulumi.Output[Optional['outputs.InstanceNetworking']]:
        return pulumi.get(self, "networking")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[str]:
        """
        Private IP Address of the Instance
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[str]:
        """
        Public IP Address of the Instance
        """
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        Resource type of Lightsail instance.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="sshKeyName")
    def ssh_key_name(self) -> pulumi.Output[str]:
        """
        SSH Key Name of the  Lightsail instance.
        """
        return pulumi.get(self, "ssh_key_name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional['outputs.InstanceState']]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> pulumi.Output[str]:
        """
        Support code to help identify any issues
        """
        return pulumi.get(self, "support_code")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[str]]:
        """
        A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
        """
        return pulumi.get(self, "user_data")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Username of the  Lightsail instance.
        """
        return pulumi.get(self, "user_name")

