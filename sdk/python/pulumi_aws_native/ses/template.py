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

__all__ = ['TemplateInitArgs', 'Template']

@pulumi.input_type
class TemplateInitArgs:
    def __init__(__self__, *,
                 template: Optional[pulumi.Input['TemplateArgs']] = None):
        """
        The set of arguments for constructing a Template resource.
        """
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input['TemplateArgs']]:
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input['TemplateArgs']]):
        pulumi.set(self, "template", value)


class Template(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 template: Optional[pulumi.Input[pulumi.InputType['TemplateArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SES::Template

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TemplateInitArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SES::Template

        :param str resource_name: The name of the resource.
        :param TemplateInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TemplateInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 template: Optional[pulumi.Input[pulumi.InputType['TemplateArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TemplateInitArgs.__new__(TemplateInitArgs)

            __props__.__dict__["template"] = template
        super(Template, __self__).__init__(
            'aws-native:ses:Template',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Template':
        """
        Get an existing Template resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TemplateInitArgs.__new__(TemplateInitArgs)

        __props__.__dict__["template"] = None
        return Template(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional['outputs.Template']]:
        return pulumi.get(self, "template")

