# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LogStreamArgs', 'LogStream']

@pulumi.input_type
class LogStreamArgs:
    def __init__(__self__, *,
                 log_group_name: pulumi.Input[str],
                 log_stream_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LogStream resource.
        :param pulumi.Input[str] log_group_name: The name of the log group where the log stream is created.
        :param pulumi.Input[str] log_stream_name: The name of the log stream. The name must be unique wihtin the log group.
        """
        LogStreamArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             log_group_name: pulumi.Input[str],
             log_stream_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("log_group_name", log_group_name)
        if log_stream_name is not None:
            _setter("log_stream_name", log_stream_name)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[str]:
        """
        The name of the log group where the log stream is created.
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_group_name", value)

    @property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the log stream. The name must be unique wihtin the log group.
        """
        return pulumi.get(self, "log_stream_name")

    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_stream_name", value)


class LogStream(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 log_stream_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Logs::LogStream

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] log_group_name: The name of the log group where the log stream is created.
        :param pulumi.Input[str] log_stream_name: The name of the log stream. The name must be unique wihtin the log group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogStreamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Logs::LogStream

        :param str resource_name: The name of the resource.
        :param LogStreamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogStreamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            LogStreamArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 log_stream_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogStreamArgs.__new__(LogStreamArgs)

            if log_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'log_group_name'")
            __props__.__dict__["log_group_name"] = log_group_name
            __props__.__dict__["log_stream_name"] = log_stream_name
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["log_group_name", "log_stream_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LogStream, __self__).__init__(
            'aws-native:logs:LogStream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LogStream':
        """
        Get an existing LogStream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LogStreamArgs.__new__(LogStreamArgs)

        __props__.__dict__["log_group_name"] = None
        __props__.__dict__["log_stream_name"] = None
        return LogStream(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[str]:
        """
        The name of the log group where the log stream is created.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the log stream. The name must be unique wihtin the log group.
        """
        return pulumi.get(self, "log_stream_name")

