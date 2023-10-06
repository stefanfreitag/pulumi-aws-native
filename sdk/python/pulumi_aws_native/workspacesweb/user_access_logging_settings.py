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

__all__ = ['UserAccessLoggingSettingsArgs', 'UserAccessLoggingSettings']

@pulumi.input_type
class UserAccessLoggingSettingsArgs:
    def __init__(__self__, *,
                 kinesis_stream_arn: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['UserAccessLoggingSettingsTagArgs']]]] = None):
        """
        The set of arguments for constructing a UserAccessLoggingSettings resource.
        :param pulumi.Input[str] kinesis_stream_arn: Kinesis stream ARN to which log events are published.
        """
        UserAccessLoggingSettingsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kinesis_stream_arn=kinesis_stream_arn,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kinesis_stream_arn: pulumi.Input[str],
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['UserAccessLoggingSettingsTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("kinesis_stream_arn", kinesis_stream_arn)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> pulumi.Input[str]:
        """
        Kinesis stream ARN to which log events are published.
        """
        return pulumi.get(self, "kinesis_stream_arn")

    @kinesis_stream_arn.setter
    def kinesis_stream_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "kinesis_stream_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserAccessLoggingSettingsTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserAccessLoggingSettingsTagArgs']]]]):
        pulumi.set(self, "tags", value)


class UserAccessLoggingSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kinesis_stream_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserAccessLoggingSettingsTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kinesis_stream_arn: Kinesis stream ARN to which log events are published.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserAccessLoggingSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type

        :param str resource_name: The name of the resource.
        :param UserAccessLoggingSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserAccessLoggingSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserAccessLoggingSettingsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kinesis_stream_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserAccessLoggingSettingsTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserAccessLoggingSettingsArgs.__new__(UserAccessLoggingSettingsArgs)

            if kinesis_stream_arn is None and not opts.urn:
                raise TypeError("Missing required property 'kinesis_stream_arn'")
            __props__.__dict__["kinesis_stream_arn"] = kinesis_stream_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_portal_arns"] = None
            __props__.__dict__["user_access_logging_settings_arn"] = None
        super(UserAccessLoggingSettings, __self__).__init__(
            'aws-native:workspacesweb:UserAccessLoggingSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserAccessLoggingSettings':
        """
        Get an existing UserAccessLoggingSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserAccessLoggingSettingsArgs.__new__(UserAccessLoggingSettingsArgs)

        __props__.__dict__["associated_portal_arns"] = None
        __props__.__dict__["kinesis_stream_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_access_logging_settings_arn"] = None
        return UserAccessLoggingSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "associated_portal_arns")

    @property
    @pulumi.getter(name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> pulumi.Output[str]:
        """
        Kinesis stream ARN to which log events are published.
        """
        return pulumi.get(self, "kinesis_stream_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.UserAccessLoggingSettingsTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userAccessLoggingSettingsArn")
    def user_access_logging_settings_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_access_logging_settings_arn")

