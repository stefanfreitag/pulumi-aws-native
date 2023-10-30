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

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, add_ons=None, hardware=None, instance_arn=None, is_static_ip=None, key_pair_name=None, location=None, networking=None, private_ip_address=None, public_ip_address=None, resource_type=None, ssh_key_name=None, state=None, support_code=None, tags=None, user_name=None):
        if add_ons and not isinstance(add_ons, list):
            raise TypeError("Expected argument 'add_ons' to be a list")
        pulumi.set(__self__, "add_ons", add_ons)
        if hardware and not isinstance(hardware, dict):
            raise TypeError("Expected argument 'hardware' to be a dict")
        pulumi.set(__self__, "hardware", hardware)
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if is_static_ip and not isinstance(is_static_ip, bool):
            raise TypeError("Expected argument 'is_static_ip' to be a bool")
        pulumi.set(__self__, "is_static_ip", is_static_ip)
        if key_pair_name and not isinstance(key_pair_name, str):
            raise TypeError("Expected argument 'key_pair_name' to be a str")
        pulumi.set(__self__, "key_pair_name", key_pair_name)
        if location and not isinstance(location, dict):
            raise TypeError("Expected argument 'location' to be a dict")
        pulumi.set(__self__, "location", location)
        if networking and not isinstance(networking, dict):
            raise TypeError("Expected argument 'networking' to be a dict")
        pulumi.set(__self__, "networking", networking)
        if private_ip_address and not isinstance(private_ip_address, str):
            raise TypeError("Expected argument 'private_ip_address' to be a str")
        pulumi.set(__self__, "private_ip_address", private_ip_address)
        if public_ip_address and not isinstance(public_ip_address, str):
            raise TypeError("Expected argument 'public_ip_address' to be a str")
        pulumi.set(__self__, "public_ip_address", public_ip_address)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if ssh_key_name and not isinstance(ssh_key_name, str):
            raise TypeError("Expected argument 'ssh_key_name' to be a str")
        pulumi.set(__self__, "ssh_key_name", ssh_key_name)
        if state and not isinstance(state, dict):
            raise TypeError("Expected argument 'state' to be a dict")
        pulumi.set(__self__, "state", state)
        if support_code and not isinstance(support_code, str):
            raise TypeError("Expected argument 'support_code' to be a str")
        pulumi.set(__self__, "support_code", support_code)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="addOns")
    def add_ons(self) -> Optional[Sequence['outputs.InstanceAddOn']]:
        """
        An array of objects representing the add-ons to enable for the new instance.
        """
        return pulumi.get(self, "add_ons")

    @property
    @pulumi.getter
    def hardware(self) -> Optional['outputs.InstanceHardware']:
        return pulumi.get(self, "hardware")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[str]:
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="isStaticIp")
    def is_static_ip(self) -> Optional[bool]:
        """
        Is the IP Address of the Instance is the static IP
        """
        return pulumi.get(self, "is_static_ip")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> Optional[str]:
        """
        The name of your key pair.
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter
    def location(self) -> Optional['outputs.InstanceLocation']:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def networking(self) -> Optional['outputs.InstanceNetworking']:
        return pulumi.get(self, "networking")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        Private IP Address of the Instance
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[str]:
        """
        Public IP Address of the Instance
        """
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Resource type of Lightsail instance.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="sshKeyName")
    def ssh_key_name(self) -> Optional[str]:
        """
        SSH Key Name of the  Lightsail instance.
        """
        return pulumi.get(self, "ssh_key_name")

    @property
    @pulumi.getter
    def state(self) -> Optional['outputs.InstanceState']:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> Optional[str]:
        """
        Support code to help identify any issues
        """
        return pulumi.get(self, "support_code")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.InstanceTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        Username of the  Lightsail instance.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            add_ons=self.add_ons,
            hardware=self.hardware,
            instance_arn=self.instance_arn,
            is_static_ip=self.is_static_ip,
            key_pair_name=self.key_pair_name,
            location=self.location,
            networking=self.networking,
            private_ip_address=self.private_ip_address,
            public_ip_address=self.public_ip_address,
            resource_type=self.resource_type,
            ssh_key_name=self.ssh_key_name,
            state=self.state,
            support_code=self.support_code,
            tags=self.tags,
            user_name=self.user_name)


def get_instance(instance_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Resource Type definition for AWS::Lightsail::Instance


    :param str instance_name: The names to use for your new Lightsail instance.
    """
    __args__ = dict()
    __args__['instanceName'] = instance_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        add_ons=pulumi.get(__ret__, 'add_ons'),
        hardware=pulumi.get(__ret__, 'hardware'),
        instance_arn=pulumi.get(__ret__, 'instance_arn'),
        is_static_ip=pulumi.get(__ret__, 'is_static_ip'),
        key_pair_name=pulumi.get(__ret__, 'key_pair_name'),
        location=pulumi.get(__ret__, 'location'),
        networking=pulumi.get(__ret__, 'networking'),
        private_ip_address=pulumi.get(__ret__, 'private_ip_address'),
        public_ip_address=pulumi.get(__ret__, 'public_ip_address'),
        resource_type=pulumi.get(__ret__, 'resource_type'),
        ssh_key_name=pulumi.get(__ret__, 'ssh_key_name'),
        state=pulumi.get(__ret__, 'state'),
        support_code=pulumi.get(__ret__, 'support_code'),
        tags=pulumi.get(__ret__, 'tags'),
        user_name=pulumi.get(__ret__, 'user_name'))


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Resource Type definition for AWS::Lightsail::Instance


    :param str instance_name: The names to use for your new Lightsail instance.
    """
    ...
