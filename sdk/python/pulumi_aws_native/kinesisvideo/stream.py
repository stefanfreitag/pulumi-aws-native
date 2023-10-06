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

__all__ = ['StreamArgs', 'Stream']

@pulumi.input_type
class StreamArgs:
    def __init__(__self__, *,
                 data_retention_in_hours: Optional[pulumi.Input[int]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 media_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StreamTagArgs']]]] = None):
        """
        The set of arguments for constructing a Stream resource.
        :param pulumi.Input[int] data_retention_in_hours: The number of hours till which Kinesis Video will retain the data in the stream
        :param pulumi.Input[str] device_name: The name of the device that is writing to the stream.
        :param pulumi.Input[str] kms_key_id: AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        :param pulumi.Input[str] media_type: The media type of the stream. Consumers of the stream can use this information when processing the stream.
        :param pulumi.Input[str] name: The name of the Kinesis Video stream.
        :param pulumi.Input[Sequence[pulumi.Input['StreamTagArgs']]] tags: An array of key-value pairs associated with the Kinesis Video Stream.
        """
        StreamArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_retention_in_hours=data_retention_in_hours,
            device_name=device_name,
            kms_key_id=kms_key_id,
            media_type=media_type,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_retention_in_hours: Optional[pulumi.Input[int]] = None,
             device_name: Optional[pulumi.Input[str]] = None,
             kms_key_id: Optional[pulumi.Input[str]] = None,
             media_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['StreamTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if data_retention_in_hours is not None:
            _setter("data_retention_in_hours", data_retention_in_hours)
        if device_name is not None:
            _setter("device_name", device_name)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)
        if media_type is not None:
            _setter("media_type", media_type)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="dataRetentionInHours")
    def data_retention_in_hours(self) -> Optional[pulumi.Input[int]]:
        """
        The number of hours till which Kinesis Video will retain the data in the stream
        """
        return pulumi.get(self, "data_retention_in_hours")

    @data_retention_in_hours.setter
    def data_retention_in_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "data_retention_in_hours", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the device that is writing to the stream.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[pulumi.Input[str]]:
        """
        The media type of the stream. Consumers of the stream can use this information when processing the stream.
        """
        return pulumi.get(self, "media_type")

    @media_type.setter
    def media_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "media_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kinesis Video stream.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StreamTagArgs']]]]:
        """
        An array of key-value pairs associated with the Kinesis Video Stream.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StreamTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Stream(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_retention_in_hours: Optional[pulumi.Input[int]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 media_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type Definition for AWS::KinesisVideo::Stream

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] data_retention_in_hours: The number of hours till which Kinesis Video will retain the data in the stream
        :param pulumi.Input[str] device_name: The name of the device that is writing to the stream.
        :param pulumi.Input[str] kms_key_id: AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        :param pulumi.Input[str] media_type: The media type of the stream. Consumers of the stream can use this information when processing the stream.
        :param pulumi.Input[str] name: The name of the Kinesis Video stream.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamTagArgs']]]] tags: An array of key-value pairs associated with the Kinesis Video Stream.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StreamArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type Definition for AWS::KinesisVideo::Stream

        :param str resource_name: The name of the resource.
        :param StreamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            StreamArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_retention_in_hours: Optional[pulumi.Input[int]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 media_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamArgs.__new__(StreamArgs)

            __props__.__dict__["data_retention_in_hours"] = data_retention_in_hours
            __props__.__dict__["device_name"] = device_name
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["media_type"] = media_type
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Stream, __self__).__init__(
            'aws-native:kinesisvideo:Stream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Stream':
        """
        Get an existing Stream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StreamArgs.__new__(StreamArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["data_retention_in_hours"] = None
        __props__.__dict__["device_name"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["media_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return Stream(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Kinesis Video stream.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataRetentionInHours")
    def data_retention_in_hours(self) -> pulumi.Output[Optional[int]]:
        """
        The number of hours till which Kinesis Video will retain the data in the stream
        """
        return pulumi.get(self, "data_retention_in_hours")

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the device that is writing to the stream.
        """
        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> pulumi.Output[Optional[str]]:
        """
        The media type of the stream. Consumers of the stream can use this information when processing the stream.
        """
        return pulumi.get(self, "media_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Kinesis Video stream.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StreamTag']]]:
        """
        An array of key-value pairs associated with the Kinesis Video Stream.
        """
        return pulumi.get(self, "tags")

