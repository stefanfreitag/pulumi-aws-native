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

__all__ = ['StudioComponentArgs', 'StudioComponent']

@pulumi.input_type
class StudioComponentArgs:
    def __init__(__self__, *,
                 studio_id: pulumi.Input[str],
                 type: pulumi.Input['StudioComponentType'],
                 configuration: Optional[pulumi.Input[Union['StudioComponentConfiguration0PropertiesArgs', 'StudioComponentConfiguration1PropertiesArgs', 'StudioComponentConfiguration2PropertiesArgs', 'StudioComponentConfiguration3PropertiesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 initialization_scripts: Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentInitializationScriptArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 script_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentScriptParameterKeyValueArgs']]]] = None,
                 secure_initialization_role_arn: Optional[pulumi.Input[str]] = None,
                 subtype: Optional[pulumi.Input['StudioComponentSubtype']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StudioComponent resource.
        :param pulumi.Input[str] studio_id: <p>The studio ID. </p>
        :param pulumi.Input[str] description: <p>The description.</p>
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ec2_security_group_ids: <p>The EC2 security groups that control access to the studio component.</p>
        :param pulumi.Input[Sequence[pulumi.Input['StudioComponentInitializationScriptArgs']]] initialization_scripts: <p>Initialization scripts for studio components.</p>
        :param pulumi.Input[str] name: <p>The name for the studio component.</p>
        :param pulumi.Input[Sequence[pulumi.Input['StudioComponentScriptParameterKeyValueArgs']]] script_parameters: <p>Parameters for the studio component scripts.</p>
        """
        pulumi.set(__self__, "studio_id", studio_id)
        pulumi.set(__self__, "type", type)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ec2_security_group_ids is not None:
            pulumi.set(__self__, "ec2_security_group_ids", ec2_security_group_ids)
        if initialization_scripts is not None:
            pulumi.set(__self__, "initialization_scripts", initialization_scripts)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if runtime_role_arn is not None:
            pulumi.set(__self__, "runtime_role_arn", runtime_role_arn)
        if script_parameters is not None:
            pulumi.set(__self__, "script_parameters", script_parameters)
        if secure_initialization_role_arn is not None:
            pulumi.set(__self__, "secure_initialization_role_arn", secure_initialization_role_arn)
        if subtype is not None:
            pulumi.set(__self__, "subtype", subtype)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Input[str]:
        """
        <p>The studio ID. </p>
        """
        return pulumi.get(self, "studio_id")

    @studio_id.setter
    def studio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "studio_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['StudioComponentType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['StudioComponentType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Union['StudioComponentConfiguration0PropertiesArgs', 'StudioComponentConfiguration1PropertiesArgs', 'StudioComponentConfiguration2PropertiesArgs', 'StudioComponentConfiguration3PropertiesArgs']]]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Union['StudioComponentConfiguration0PropertiesArgs', 'StudioComponentConfiguration1PropertiesArgs', 'StudioComponentConfiguration2PropertiesArgs', 'StudioComponentConfiguration3PropertiesArgs']]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        <p>The description.</p>
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ec2SecurityGroupIds")
    def ec2_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        <p>The EC2 security groups that control access to the studio component.</p>
        """
        return pulumi.get(self, "ec2_security_group_ids")

    @ec2_security_group_ids.setter
    def ec2_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ec2_security_group_ids", value)

    @property
    @pulumi.getter(name="initializationScripts")
    def initialization_scripts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentInitializationScriptArgs']]]]:
        """
        <p>Initialization scripts for studio components.</p>
        """
        return pulumi.get(self, "initialization_scripts")

    @initialization_scripts.setter
    def initialization_scripts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentInitializationScriptArgs']]]]):
        pulumi.set(self, "initialization_scripts", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        <p>The name for the studio component.</p>
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="runtimeRoleArn")
    def runtime_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "runtime_role_arn")

    @runtime_role_arn.setter
    def runtime_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "runtime_role_arn", value)

    @property
    @pulumi.getter(name="scriptParameters")
    def script_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentScriptParameterKeyValueArgs']]]]:
        """
        <p>Parameters for the studio component scripts.</p>
        """
        return pulumi.get(self, "script_parameters")

    @script_parameters.setter
    def script_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StudioComponentScriptParameterKeyValueArgs']]]]):
        pulumi.set(self, "script_parameters", value)

    @property
    @pulumi.getter(name="secureInitializationRoleArn")
    def secure_initialization_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secure_initialization_role_arn")

    @secure_initialization_role_arn.setter
    def secure_initialization_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secure_initialization_role_arn", value)

    @property
    @pulumi.getter
    def subtype(self) -> Optional[pulumi.Input['StudioComponentSubtype']]:
        return pulumi.get(self, "subtype")

    @subtype.setter
    def subtype(self, value: Optional[pulumi.Input['StudioComponentSubtype']]):
        pulumi.set(self, "subtype", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StudioComponent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[Union[pulumi.InputType['StudioComponentConfiguration0PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration1PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration2PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration3PropertiesArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 initialization_scripts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentInitializationScriptArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 script_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentScriptParameterKeyValueArgs']]]]] = None,
                 secure_initialization_role_arn: Optional[pulumi.Input[str]] = None,
                 studio_id: Optional[pulumi.Input[str]] = None,
                 subtype: Optional[pulumi.Input['StudioComponentSubtype']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input['StudioComponentType']] = None,
                 __props__=None):
        """
        Represents a studio component that connects a non-Nimble Studio resource in your account to your studio

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: <p>The description.</p>
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ec2_security_group_ids: <p>The EC2 security groups that control access to the studio component.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentInitializationScriptArgs']]]] initialization_scripts: <p>Initialization scripts for studio components.</p>
        :param pulumi.Input[str] name: <p>The name for the studio component.</p>
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentScriptParameterKeyValueArgs']]]] script_parameters: <p>Parameters for the studio component scripts.</p>
        :param pulumi.Input[str] studio_id: <p>The studio ID. </p>
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StudioComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a studio component that connects a non-Nimble Studio resource in your account to your studio

        :param str resource_name: The name of the resource.
        :param StudioComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StudioComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[Union[pulumi.InputType['StudioComponentConfiguration0PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration1PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration2PropertiesArgs'], pulumi.InputType['StudioComponentConfiguration3PropertiesArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 initialization_scripts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentInitializationScriptArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 script_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StudioComponentScriptParameterKeyValueArgs']]]]] = None,
                 secure_initialization_role_arn: Optional[pulumi.Input[str]] = None,
                 studio_id: Optional[pulumi.Input[str]] = None,
                 subtype: Optional[pulumi.Input['StudioComponentSubtype']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input['StudioComponentType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StudioComponentArgs.__new__(StudioComponentArgs)

            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["description"] = description
            __props__.__dict__["ec2_security_group_ids"] = ec2_security_group_ids
            __props__.__dict__["initialization_scripts"] = initialization_scripts
            __props__.__dict__["name"] = name
            __props__.__dict__["runtime_role_arn"] = runtime_role_arn
            __props__.__dict__["script_parameters"] = script_parameters
            __props__.__dict__["secure_initialization_role_arn"] = secure_initialization_role_arn
            if studio_id is None and not opts.urn:
                raise TypeError("Missing required property 'studio_id'")
            __props__.__dict__["studio_id"] = studio_id
            __props__.__dict__["subtype"] = subtype
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["studio_component_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["studio_id", "subtype", "tags.*"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(StudioComponent, __self__).__init__(
            'aws-native:nimblestudio:StudioComponent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StudioComponent':
        """
        Get an existing StudioComponent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StudioComponentArgs.__new__(StudioComponentArgs)

        __props__.__dict__["configuration"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["ec2_security_group_ids"] = None
        __props__.__dict__["initialization_scripts"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["runtime_role_arn"] = None
        __props__.__dict__["script_parameters"] = None
        __props__.__dict__["secure_initialization_role_arn"] = None
        __props__.__dict__["studio_component_id"] = None
        __props__.__dict__["studio_id"] = None
        __props__.__dict__["subtype"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StudioComponent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        <p>The description.</p>
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ec2SecurityGroupIds")
    def ec2_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        <p>The EC2 security groups that control access to the studio component.</p>
        """
        return pulumi.get(self, "ec2_security_group_ids")

    @property
    @pulumi.getter(name="initializationScripts")
    def initialization_scripts(self) -> pulumi.Output[Optional[Sequence['outputs.StudioComponentInitializationScript']]]:
        """
        <p>Initialization scripts for studio components.</p>
        """
        return pulumi.get(self, "initialization_scripts")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        <p>The name for the studio component.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="runtimeRoleArn")
    def runtime_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "runtime_role_arn")

    @property
    @pulumi.getter(name="scriptParameters")
    def script_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.StudioComponentScriptParameterKeyValue']]]:
        """
        <p>Parameters for the studio component scripts.</p>
        """
        return pulumi.get(self, "script_parameters")

    @property
    @pulumi.getter(name="secureInitializationRoleArn")
    def secure_initialization_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "secure_initialization_role_arn")

    @property
    @pulumi.getter(name="studioComponentId")
    def studio_component_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "studio_component_id")

    @property
    @pulumi.getter(name="studioId")
    def studio_id(self) -> pulumi.Output[str]:
        """
        <p>The studio ID. </p>
        """
        return pulumi.get(self, "studio_id")

    @property
    @pulumi.getter
    def subtype(self) -> pulumi.Output[Optional['StudioComponentSubtype']]:
        return pulumi.get(self, "subtype")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['StudioComponentType']:
        return pulumi.get(self, "type")

