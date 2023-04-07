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

__all__ = ['ReadinessCheckArgs', 'ReadinessCheck']

@pulumi.input_type
class ReadinessCheckArgs:
    def __init__(__self__, *,
                 readiness_check_name: Optional[pulumi.Input[str]] = None,
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ReadinessCheckTagArgs']]]] = None):
        """
        The set of arguments for constructing a ReadinessCheck resource.
        :param pulumi.Input[str] readiness_check_name: Name of the ReadinessCheck to create.
        :param pulumi.Input[str] resource_set_name: The name of the resource set to check.
        :param pulumi.Input[Sequence[pulumi.Input['ReadinessCheckTagArgs']]] tags: A collection of tags associated with a resource.
        """
        if readiness_check_name is not None:
            pulumi.set(__self__, "readiness_check_name", readiness_check_name)
        if resource_set_name is not None:
            pulumi.set(__self__, "resource_set_name", resource_set_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="readinessCheckName")
    def readiness_check_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ReadinessCheck to create.
        """
        return pulumi.get(self, "readiness_check_name")

    @readiness_check_name.setter
    def readiness_check_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "readiness_check_name", value)

    @property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource set to check.
        """
        return pulumi.get(self, "resource_set_name")

    @resource_set_name.setter
    def resource_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_set_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReadinessCheckTagArgs']]]]:
        """
        A collection of tags associated with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReadinessCheckTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ReadinessCheck(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 readiness_check_name: Optional[pulumi.Input[str]] = None,
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadinessCheckTagArgs']]]]] = None,
                 __props__=None):
        """
        Aws Route53 Recovery Readiness Check Schema and API specification.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] readiness_check_name: Name of the ReadinessCheck to create.
        :param pulumi.Input[str] resource_set_name: The name of the resource set to check.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadinessCheckTagArgs']]]] tags: A collection of tags associated with a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ReadinessCheckArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Aws Route53 Recovery Readiness Check Schema and API specification.

        :param str resource_name: The name of the resource.
        :param ReadinessCheckArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReadinessCheckArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 readiness_check_name: Optional[pulumi.Input[str]] = None,
                 resource_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadinessCheckTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReadinessCheckArgs.__new__(ReadinessCheckArgs)

            __props__.__dict__["readiness_check_name"] = readiness_check_name
            __props__.__dict__["resource_set_name"] = resource_set_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["readiness_check_arn"] = None
        super(ReadinessCheck, __self__).__init__(
            'aws-native:route53recoveryreadiness:ReadinessCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReadinessCheck':
        """
        Get an existing ReadinessCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReadinessCheckArgs.__new__(ReadinessCheckArgs)

        __props__.__dict__["readiness_check_arn"] = None
        __props__.__dict__["readiness_check_name"] = None
        __props__.__dict__["resource_set_name"] = None
        __props__.__dict__["tags"] = None
        return ReadinessCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="readinessCheckArn")
    def readiness_check_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the readiness check.
        """
        return pulumi.get(self, "readiness_check_arn")

    @property
    @pulumi.getter(name="readinessCheckName")
    def readiness_check_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the ReadinessCheck to create.
        """
        return pulumi.get(self, "readiness_check_name")

    @property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource set to check.
        """
        return pulumi.get(self, "resource_set_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ReadinessCheckTag']]]:
        """
        A collection of tags associated with a resource.
        """
        return pulumi.get(self, "tags")

