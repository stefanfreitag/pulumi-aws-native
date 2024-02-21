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

__all__ = ['InputArgs', 'Input']

@pulumi.input_type
class InputArgs:
    def __init__(__self__, *,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationRequestArgs']]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input['InputDeviceSettingsArgs']]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowRequestArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceRequestArgs']]]] = None,
                 tags: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input['InputVpcRequestArgs']] = None):
        """
        The set of arguments for constructing a Input resource.
        :param Any tags: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaLive::Input` for more information about the expected schema for this property.
        """
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if input_devices is not None:
            pulumi.set(__self__, "input_devices", input_devices)
        if input_security_groups is not None:
            pulumi.set(__self__, "input_security_groups", input_security_groups)
        if media_connect_flows is not None:
            pulumi.set(__self__, "media_connect_flows", media_connect_flows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vpc is not None:
            pulumi.set(__self__, "vpc", vpc)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationRequestArgs']]]]:
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationRequestArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputDeviceSettingsArgs']]]]:
        return pulumi.get(self, "input_devices")

    @input_devices.setter
    def input_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputDeviceSettingsArgs']]]]):
        pulumi.set(self, "input_devices", value)

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "input_security_groups")

    @input_security_groups.setter
    def input_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "input_security_groups", value)

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowRequestArgs']]]]:
        return pulumi.get(self, "media_connect_flows")

    @media_connect_flows.setter
    def media_connect_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowRequestArgs']]]]):
        pulumi.set(self, "media_connect_flows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceRequestArgs']]]]:
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceRequestArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaLive::Input` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input['InputVpcRequestArgs']]:
        return pulumi.get(self, "vpc")

    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input['InputVpcRequestArgs']]):
        pulumi.set(self, "vpc", value)


warnings.warn("""Input is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Input(pulumi.CustomResource):
    warnings.warn("""Input is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationRequestArgs']]]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDeviceSettingsArgs']]]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowRequestArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceRequestArgs']]]]] = None,
                 tags: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input[pulumi.InputType['InputVpcRequestArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MediaLive::Input

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any tags: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaLive::Input` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InputArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MediaLive::Input

        :param str resource_name: The name of the resource.
        :param InputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationRequestArgs']]]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDeviceSettingsArgs']]]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowRequestArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceRequestArgs']]]]] = None,
                 tags: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input[pulumi.InputType['InputVpcRequestArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Input is deprecated: Input is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InputArgs.__new__(InputArgs)

            __props__.__dict__["destinations"] = destinations
            __props__.__dict__["input_devices"] = input_devices
            __props__.__dict__["input_security_groups"] = input_security_groups
            __props__.__dict__["media_connect_flows"] = media_connect_flows
            __props__.__dict__["name"] = name
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["sources"] = sources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["vpc"] = vpc
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["type", "vpc"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Input, __self__).__init__(
            'aws-native:medialive:Input',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Input':
        """
        Get an existing Input resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InputArgs.__new__(InputArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["destinations"] = None
        __props__.__dict__["input_devices"] = None
        __props__.__dict__["input_security_groups"] = None
        __props__.__dict__["media_connect_flows"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vpc"] = None
        return Input(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence['outputs.InputDestinationRequest']]]:
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> pulumi.Output[Optional[Sequence['outputs.InputDeviceSettings']]]:
        return pulumi.get(self, "input_devices")

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "input_security_groups")

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> pulumi.Output[Optional[Sequence['outputs.InputMediaConnectFlowRequest']]]:
        return pulumi.get(self, "media_connect_flows")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.InputSourceRequest']]]:
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaLive::Input` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vpc(self) -> pulumi.Output[Optional['outputs.InputVpcRequest']]:
        return pulumi.get(self, "vpc")

