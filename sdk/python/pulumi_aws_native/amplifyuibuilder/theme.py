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

__all__ = ['ThemeArgs', 'Theme']

@pulumi.input_type
class ThemeArgs:
    def __init__(__self__, *,
                 values: pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]],
                 app_id: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]] = None,
                 tags: Optional[pulumi.Input['ThemeTagsArgs']] = None):
        """
        The set of arguments for constructing a Theme resource.
        """
        ThemeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            values=values,
            app_id=app_id,
            environment_name=environment_name,
            name=name,
            overrides=overrides,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             values: pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]],
             app_id: Optional[pulumi.Input[str]] = None,
             environment_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             overrides: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]] = None,
             tags: Optional[pulumi.Input['ThemeTagsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("values", values)
        if app_id is not None:
            _setter("app_id", app_id)
        if environment_name is not None:
            _setter("environment_name", environment_name)
        if name is not None:
            _setter("name", name)
        if overrides is not None:
            _setter("overrides", overrides)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]]:
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThemeValuesArgs']]]]):
        pulumi.set(self, "overrides", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ThemeTagsArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ThemeTagsArgs']]):
        pulumi.set(self, "tags", value)


class Theme(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeValuesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ThemeTagsArgs']]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeValuesArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::AmplifyUIBuilder::Theme Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThemeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::AmplifyUIBuilder::Theme Resource Type

        :param str resource_name: The name of the resource.
        :param ThemeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThemeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ThemeArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeValuesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ThemeTagsArgs']]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThemeValuesArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ThemeArgs.__new__(ThemeArgs)

            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["name"] = name
            __props__.__dict__["overrides"] = overrides
            if tags is not None and not isinstance(tags, ThemeTagsArgs):
                tags = tags or {}
                def _setter(key, value):
                    tags[key] = value
                ThemeTagsArgs._configure(_setter, **tags)
            __props__.__dict__["tags"] = tags
            if values is None and not opts.urn:
                raise TypeError("Missing required property 'values'")
            __props__.__dict__["values"] = values
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["tags"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Theme, __self__).__init__(
            'aws-native:amplifyuibuilder:Theme',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Theme':
        """
        Get an existing Theme resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThemeArgs.__new__(ThemeArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["environment_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["overrides"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["values"] = None
        return Theme(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Output[Optional[Sequence['outputs.ThemeValues']]]:
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.ThemeTags']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def values(self) -> pulumi.Output[Sequence['outputs.ThemeValues']]:
        return pulumi.get(self, "values")

