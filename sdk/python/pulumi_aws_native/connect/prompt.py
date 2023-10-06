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

__all__ = ['PromptArgs', 'Prompt']

@pulumi.input_type
class PromptArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PromptTagArgs']]]] = None):
        """
        The set of arguments for constructing a Prompt resource.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input[str] description: The description of the prompt.
        :param pulumi.Input[str] name: The name of the prompt.
        :param pulumi.Input[str] s3_uri: S3 URI of the customer's audio file for creating prompts resource..
        :param pulumi.Input[Sequence[pulumi.Input['PromptTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        PromptArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_arn=instance_arn,
            description=description,
            name=name,
            s3_uri=s3_uri,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_arn: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             s3_uri: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['PromptTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_arn", instance_arn)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if s3_uri is not None:
            _setter("s3_uri", s3_uri)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the prompt.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the prompt.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[str]]:
        """
        S3 URI of the customer's audio file for creating prompts resource..
        """
        return pulumi.get(self, "s3_uri")

    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_uri", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PromptTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PromptTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Prompt(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PromptTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::Prompt

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the prompt.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input[str] name: The name of the prompt.
        :param pulumi.Input[str] s3_uri: S3 URI of the customer's audio file for creating prompts resource..
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PromptTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PromptArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::Prompt

        :param str resource_name: The name of the resource.
        :param PromptArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PromptArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PromptArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PromptTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PromptArgs.__new__(PromptArgs)

            __props__.__dict__["description"] = description
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["s3_uri"] = s3_uri
            __props__.__dict__["tags"] = tags
            __props__.__dict__["prompt_arn"] = None
        super(Prompt, __self__).__init__(
            'aws-native:connect:Prompt',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Prompt':
        """
        Get an existing Prompt resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PromptArgs.__new__(PromptArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["prompt_arn"] = None
        __props__.__dict__["s3_uri"] = None
        __props__.__dict__["tags"] = None
        return Prompt(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the prompt.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the prompt.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="promptArn")
    def prompt_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the prompt.
        """
        return pulumi.get(self, "prompt_arn")

    @property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Output[Optional[str]]:
        """
        S3 URI of the customer's audio file for creating prompts resource..
        """
        return pulumi.get(self, "s3_uri")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PromptTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

