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

__all__ = ['LocationNfsArgs', 'LocationNfs']

@pulumi.input_type
class LocationNfsArgs:
    def __init__(__self__, *,
                 on_prem_config: pulumi.Input['LocationNfsOnPremConfigArgs'],
                 mount_options: Optional[pulumi.Input['LocationNfsMountOptionsArgs']] = None,
                 server_hostname: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LocationNfsTagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationNfs resource.
        :param pulumi.Input[str] server_hostname: The name of the NFS server. This value is the IP address or DNS name of the NFS server.
        :param pulumi.Input[str] subdirectory: The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.
        :param pulumi.Input[Sequence[pulumi.Input['LocationNfsTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "on_prem_config", on_prem_config)
        if mount_options is not None:
            pulumi.set(__self__, "mount_options", mount_options)
        if server_hostname is not None:
            pulumi.set(__self__, "server_hostname", server_hostname)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> pulumi.Input['LocationNfsOnPremConfigArgs']:
        return pulumi.get(self, "on_prem_config")

    @on_prem_config.setter
    def on_prem_config(self, value: pulumi.Input['LocationNfsOnPremConfigArgs']):
        pulumi.set(self, "on_prem_config", value)

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input['LocationNfsMountOptionsArgs']]:
        return pulumi.get(self, "mount_options")

    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input['LocationNfsMountOptionsArgs']]):
        pulumi.set(self, "mount_options", value)

    @property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NFS server. This value is the IP address or DNS name of the NFS server.
        """
        return pulumi.get(self, "server_hostname")

    @server_hostname.setter
    def server_hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_hostname", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[str]]:
        """
        The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdirectory", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocationNfsTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocationNfsTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LocationNfs(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mount_options: Optional[pulumi.Input[pulumi.InputType['LocationNfsMountOptionsArgs']]] = None,
                 on_prem_config: Optional[pulumi.Input[pulumi.InputType['LocationNfsOnPremConfigArgs']]] = None,
                 server_hostname: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationNfsTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataSync::LocationNFS

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] server_hostname: The name of the NFS server. This value is the IP address or DNS name of the NFS server.
        :param pulumi.Input[str] subdirectory: The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationNfsTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationNfsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataSync::LocationNFS

        :param str resource_name: The name of the resource.
        :param LocationNfsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationNfsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mount_options: Optional[pulumi.Input[pulumi.InputType['LocationNfsMountOptionsArgs']]] = None,
                 on_prem_config: Optional[pulumi.Input[pulumi.InputType['LocationNfsOnPremConfigArgs']]] = None,
                 server_hostname: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationNfsTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationNfsArgs.__new__(LocationNfsArgs)

            __props__.__dict__["mount_options"] = mount_options
            if on_prem_config is None and not opts.urn:
                raise TypeError("Missing required property 'on_prem_config'")
            __props__.__dict__["on_prem_config"] = on_prem_config
            __props__.__dict__["server_hostname"] = server_hostname
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["server_hostname"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LocationNfs, __self__).__init__(
            'aws-native:datasync:LocationNfs',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationNfs':
        """
        Get an existing LocationNfs resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationNfsArgs.__new__(LocationNfsArgs)

        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["mount_options"] = None
        __props__.__dict__["on_prem_config"] = None
        __props__.__dict__["server_hostname"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        return LocationNfs(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the NFS location.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[str]:
        """
        The URL of the NFS location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> pulumi.Output[Optional['outputs.LocationNfsMountOptions']]:
        return pulumi.get(self, "mount_options")

    @property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> pulumi.Output['outputs.LocationNfsOnPremConfig']:
        return pulumi.get(self, "on_prem_config")

    @property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the NFS server. This value is the IP address or DNS name of the NFS server.
        """
        return pulumi.get(self, "server_hostname")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[str]]:
        """
        The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LocationNfsTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

