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

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 latency_mode: Optional[pulumi.Input['ChannelLatencyMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recording_configuration_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]] = None,
                 type: Optional[pulumi.Input['ChannelType']] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[bool] authorized: Whether the channel is authorized.
        :param pulumi.Input['ChannelLatencyMode'] latency_mode: Channel latency mode.
        :param pulumi.Input[str] name: Channel
        :param pulumi.Input[str] recording_configuration_arn: Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).
        :param pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]] tags: A list of key-value pairs that contain metadata for the asset model.
        :param pulumi.Input['ChannelType'] type: Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
        """
        if authorized is not None:
            pulumi.set(__self__, "authorized", authorized)
        if latency_mode is not None:
            pulumi.set(__self__, "latency_mode", latency_mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if recording_configuration_arn is not None:
            pulumi.set(__self__, "recording_configuration_arn", recording_configuration_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def authorized(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the channel is authorized.
        """
        return pulumi.get(self, "authorized")

    @authorized.setter
    def authorized(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "authorized", value)

    @property
    @pulumi.getter(name="latencyMode")
    def latency_mode(self) -> Optional[pulumi.Input['ChannelLatencyMode']]:
        """
        Channel latency mode.
        """
        return pulumi.get(self, "latency_mode")

    @latency_mode.setter
    def latency_mode(self, value: Optional[pulumi.Input['ChannelLatencyMode']]):
        pulumi.set(self, "latency_mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Channel
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recordingConfigurationArn")
    def recording_configuration_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).
        """
        return pulumi.get(self, "recording_configuration_arn")

    @recording_configuration_arn.setter
    def recording_configuration_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recording_configuration_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the asset model.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChannelTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ChannelType']]:
        """
        Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ChannelType']]):
        pulumi.set(self, "type", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 latency_mode: Optional[pulumi.Input['ChannelLatencyMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recording_configuration_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['ChannelType']] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IVS::Channel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] authorized: Whether the channel is authorized.
        :param pulumi.Input['ChannelLatencyMode'] latency_mode: Channel latency mode.
        :param pulumi.Input[str] name: Channel
        :param pulumi.Input[str] recording_configuration_arn: Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelTagArgs']]]] tags: A list of key-value pairs that contain metadata for the asset model.
        :param pulumi.Input['ChannelType'] type: Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ChannelArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IVS::Channel

        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 latency_mode: Optional[pulumi.Input['ChannelLatencyMode']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recording_configuration_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChannelTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['ChannelType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelArgs.__new__(ChannelArgs)

            __props__.__dict__["authorized"] = authorized
            __props__.__dict__["latency_mode"] = latency_mode
            __props__.__dict__["name"] = name
            __props__.__dict__["recording_configuration_arn"] = recording_configuration_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
            __props__.__dict__["ingest_endpoint"] = None
            __props__.__dict__["playback_url"] = None
        super(Channel, __self__).__init__(
            'aws-native:ivs:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChannelArgs.__new__(ChannelArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["authorized"] = None
        __props__.__dict__["ingest_endpoint"] = None
        __props__.__dict__["latency_mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["playback_url"] = None
        __props__.__dict__["recording_configuration_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Channel ARN is automatically generated on creation and assigned as the unique identifier.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def authorized(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the channel is authorized.
        """
        return pulumi.get(self, "authorized")

    @property
    @pulumi.getter(name="ingestEndpoint")
    def ingest_endpoint(self) -> pulumi.Output[str]:
        """
        Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.
        """
        return pulumi.get(self, "ingest_endpoint")

    @property
    @pulumi.getter(name="latencyMode")
    def latency_mode(self) -> pulumi.Output[Optional['ChannelLatencyMode']]:
        """
        Channel latency mode.
        """
        return pulumi.get(self, "latency_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Channel
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="playbackUrl")
    def playback_url(self) -> pulumi.Output[str]:
        """
        Channel Playback URL.
        """
        return pulumi.get(self, "playback_url")

    @property
    @pulumi.getter(name="recordingConfigurationArn")
    def recording_configuration_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).
        """
        return pulumi.get(self, "recording_configuration_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ChannelTag']]]:
        """
        A list of key-value pairs that contain metadata for the asset model.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional['ChannelType']]:
        """
        Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
        """
        return pulumi.get(self, "type")

