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
from ._enums import *
from ._inputs import *

__all__ = ['LaunchTemplateArgs', 'LaunchTemplate']

@pulumi.input_type
class LaunchTemplateArgs:
    def __init__(__self__, *,
                 launch_template_data: pulumi.Input['LaunchTemplateDataArgs'],
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]] = None,
                 version_description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LaunchTemplate resource.
        :param pulumi.Input[str] launch_template_name: A name for the launch template.
        :param pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]] tag_specifications: The tags to apply to the launch template on creation.
        :param pulumi.Input[str] version_description: A description for the first version of the launch template.
        """
        pulumi.set(__self__, "launch_template_data", launch_template_data)
        if launch_template_name is not None:
            pulumi.set(__self__, "launch_template_name", launch_template_name)
        if tag_specifications is not None:
            pulumi.set(__self__, "tag_specifications", tag_specifications)
        if version_description is not None:
            pulumi.set(__self__, "version_description", version_description)

    @property
    @pulumi.getter(name="launchTemplateData")
    def launch_template_data(self) -> pulumi.Input['LaunchTemplateDataArgs']:
        return pulumi.get(self, "launch_template_data")

    @launch_template_data.setter
    def launch_template_data(self, value: pulumi.Input['LaunchTemplateDataArgs']):
        pulumi.set(self, "launch_template_data", value)

    @property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the launch template.
        """
        return pulumi.get(self, "launch_template_name")

    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_template_name", value)

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]]:
        """
        The tags to apply to the launch template on creation.
        """
        return pulumi.get(self, "tag_specifications")

    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LaunchTemplateTagSpecificationArgs']]]]):
        pulumi.set(self, "tag_specifications", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the first version of the launch template.
        """
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_description", value)


class LaunchTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 launch_template_data: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateDataArgs']]] = None,
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateTagSpecificationArgs']]]]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::LaunchTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] launch_template_name: A name for the launch template.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateTagSpecificationArgs']]]] tag_specifications: The tags to apply to the launch template on creation.
        :param pulumi.Input[str] version_description: A description for the first version of the launch template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LaunchTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::LaunchTemplate

        :param str resource_name: The name of the resource.
        :param LaunchTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LaunchTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 launch_template_data: Optional[pulumi.Input[pulumi.InputType['LaunchTemplateDataArgs']]] = None,
                 launch_template_name: Optional[pulumi.Input[str]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LaunchTemplateTagSpecificationArgs']]]]] = None,
                 version_description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LaunchTemplateArgs.__new__(LaunchTemplateArgs)

            if launch_template_data is None and not opts.urn:
                raise TypeError("Missing required property 'launch_template_data'")
            __props__.__dict__["launch_template_data"] = launch_template_data
            __props__.__dict__["launch_template_name"] = launch_template_name
            __props__.__dict__["tag_specifications"] = tag_specifications
            __props__.__dict__["version_description"] = version_description
            __props__.__dict__["default_version_number"] = None
            __props__.__dict__["latest_version_number"] = None
            __props__.__dict__["launch_template_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["launch_template_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LaunchTemplate, __self__).__init__(
            'aws-native:ec2:LaunchTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LaunchTemplate':
        """
        Get an existing LaunchTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LaunchTemplateArgs.__new__(LaunchTemplateArgs)

        __props__.__dict__["default_version_number"] = None
        __props__.__dict__["latest_version_number"] = None
        __props__.__dict__["launch_template_data"] = None
        __props__.__dict__["launch_template_id"] = None
        __props__.__dict__["launch_template_name"] = None
        __props__.__dict__["tag_specifications"] = None
        __props__.__dict__["version_description"] = None
        return LaunchTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultVersionNumber")
    def default_version_number(self) -> pulumi.Output[str]:
        """
        The default version of the launch template
        """
        return pulumi.get(self, "default_version_number")

    @property
    @pulumi.getter(name="latestVersionNumber")
    def latest_version_number(self) -> pulumi.Output[str]:
        """
        The latest version of the launch template
        """
        return pulumi.get(self, "latest_version_number")

    @property
    @pulumi.getter(name="launchTemplateData")
    def launch_template_data(self) -> pulumi.Output['outputs.LaunchTemplateData']:
        return pulumi.get(self, "launch_template_data")

    @property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> pulumi.Output[str]:
        """
        LaunchTemplate ID generated by service
        """
        return pulumi.get(self, "launch_template_id")

    @property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the launch template.
        """
        return pulumi.get(self, "launch_template_name")

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.LaunchTemplateTagSpecification']]]:
        """
        The tags to apply to the launch template on creation.
        """
        return pulumi.get(self, "tag_specifications")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the first version of the launch template.
        """
        return pulumi.get(self, "version_description")

