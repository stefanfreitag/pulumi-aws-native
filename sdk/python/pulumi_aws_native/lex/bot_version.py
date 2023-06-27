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

__all__ = ['BotVersionArgs', 'BotVersion']

@pulumi.input_type
class BotVersionArgs:
    def __init__(__self__, *,
                 bot_id: pulumi.Input[str],
                 bot_version_locale_specification: pulumi.Input[Sequence[pulumi.Input['BotVersionLocaleSpecificationArgs']]],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BotVersion resource.
        """
        pulumi.set(__self__, "bot_id", bot_id)
        pulumi.set(__self__, "bot_version_locale_specification", bot_version_locale_specification)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bot_id")

    @bot_id.setter
    def bot_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bot_id", value)

    @property
    @pulumi.getter(name="botVersionLocaleSpecification")
    def bot_version_locale_specification(self) -> pulumi.Input[Sequence[pulumi.Input['BotVersionLocaleSpecificationArgs']]]:
        return pulumi.get(self, "bot_version_locale_specification")

    @bot_version_locale_specification.setter
    def bot_version_locale_specification(self, value: pulumi.Input[Sequence[pulumi.Input['BotVersionLocaleSpecificationArgs']]]):
        pulumi.set(self, "bot_version_locale_specification", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class BotVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_id: Optional[pulumi.Input[str]] = None,
                 bot_version_locale_specification: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BotVersionLocaleSpecificationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BotVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.

        :param str resource_name: The name of the resource.
        :param BotVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BotVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_id: Optional[pulumi.Input[str]] = None,
                 bot_version_locale_specification: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BotVersionLocaleSpecificationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BotVersionArgs.__new__(BotVersionArgs)

            if bot_id is None and not opts.urn:
                raise TypeError("Missing required property 'bot_id'")
            __props__.__dict__["bot_id"] = bot_id
            if bot_version_locale_specification is None and not opts.urn:
                raise TypeError("Missing required property 'bot_version_locale_specification'")
            __props__.__dict__["bot_version_locale_specification"] = bot_version_locale_specification
            __props__.__dict__["description"] = description
            __props__.__dict__["bot_version"] = None
        super(BotVersion, __self__).__init__(
            'aws-native:lex:BotVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BotVersion':
        """
        Get an existing BotVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BotVersionArgs.__new__(BotVersionArgs)

        __props__.__dict__["bot_id"] = None
        __props__.__dict__["bot_version"] = None
        __props__.__dict__["bot_version_locale_specification"] = None
        __props__.__dict__["description"] = None
        return BotVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bot_id")

    @property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bot_version")

    @property
    @pulumi.getter(name="botVersionLocaleSpecification")
    def bot_version_locale_specification(self) -> pulumi.Output[Sequence['outputs.BotVersionLocaleSpecification']]:
        return pulumi.get(self, "bot_version_locale_specification")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

