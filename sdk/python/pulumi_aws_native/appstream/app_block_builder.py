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

__all__ = ['AppBlockBuilderArgs', 'AppBlockBuilder']

@pulumi.input_type
class AppBlockBuilderArgs:
    def __init__(__self__, *,
                 instance_type: pulumi.Input[str],
                 platform: pulumi.Input[str],
                 vpc_config: pulumi.Input['AppBlockBuilderVpcConfigArgs'],
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderAccessEndpointArgs']]]] = None,
                 app_block_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_default_internet_access: Optional[pulumi.Input[bool]] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderTagArgs']]]] = None):
        """
        The set of arguments for constructing a AppBlockBuilder resource.
        """
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "vpc_config", vpc_config)
        if access_endpoints is not None:
            pulumi.set(__self__, "access_endpoints", access_endpoints)
        if app_block_arns is not None:
            pulumi.set(__self__, "app_block_arns", app_block_arns)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enable_default_internet_access is not None:
            pulumi.set(__self__, "enable_default_internet_access", enable_default_internet_access)
        if iam_role_arn is not None:
            pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Input[str]:
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: pulumi.Input[str]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Input['AppBlockBuilderVpcConfigArgs']:
        return pulumi.get(self, "vpc_config")

    @vpc_config.setter
    def vpc_config(self, value: pulumi.Input['AppBlockBuilderVpcConfigArgs']):
        pulumi.set(self, "vpc_config", value)

    @property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderAccessEndpointArgs']]]]:
        return pulumi.get(self, "access_endpoints")

    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderAccessEndpointArgs']]]]):
        pulumi.set(self, "access_endpoints", value)

    @property
    @pulumi.getter(name="appBlockArns")
    def app_block_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "app_block_arns")

    @app_block_arns.setter
    def app_block_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "app_block_arns", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_default_internet_access")

    @enable_default_internet_access.setter
    def enable_default_internet_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_default_internet_access", value)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "iam_role_arn")

    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_role_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppBlockBuilderTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AppBlockBuilder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppBlockBuilderAccessEndpointArgs']]]]] = None,
                 app_block_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_default_internet_access: Optional[pulumi.Input[bool]] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppBlockBuilderTagArgs']]]]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['AppBlockBuilderVpcConfigArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppStream::AppBlockBuilder.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppBlockBuilderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppStream::AppBlockBuilder.

        :param str resource_name: The name of the resource.
        :param AppBlockBuilderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppBlockBuilderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppBlockBuilderAccessEndpointArgs']]]]] = None,
                 app_block_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_default_internet_access: Optional[pulumi.Input[bool]] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppBlockBuilderTagArgs']]]]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['AppBlockBuilderVpcConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppBlockBuilderArgs.__new__(AppBlockBuilderArgs)

            __props__.__dict__["access_endpoints"] = access_endpoints
            __props__.__dict__["app_block_arns"] = app_block_arns
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_default_internet_access"] = enable_default_internet_access
            __props__.__dict__["iam_role_arn"] = iam_role_arn
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["name"] = name
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__.__dict__["platform"] = platform
            __props__.__dict__["tags"] = tags
            if vpc_config is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_config'")
            __props__.__dict__["vpc_config"] = vpc_config
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AppBlockBuilder, __self__).__init__(
            'aws-native:appstream:AppBlockBuilder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AppBlockBuilder':
        """
        Get an existing AppBlockBuilder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppBlockBuilderArgs.__new__(AppBlockBuilderArgs)

        __props__.__dict__["access_endpoints"] = None
        __props__.__dict__["app_block_arns"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_default_internet_access"] = None
        __props__.__dict__["iam_role_arn"] = None
        __props__.__dict__["instance_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_config"] = None
        return AppBlockBuilder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.AppBlockBuilderAccessEndpoint']]]:
        return pulumi.get(self, "access_endpoints")

    @property
    @pulumi.getter(name="appBlockArns")
    def app_block_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "app_block_arns")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_default_internet_access")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AppBlockBuilderTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output['outputs.AppBlockBuilderVpcConfig']:
        return pulumi.get(self, "vpc_config")

