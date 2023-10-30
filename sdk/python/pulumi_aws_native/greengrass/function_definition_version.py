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

__all__ = ['FunctionDefinitionVersionInitArgs', 'FunctionDefinitionVersion']

@pulumi.input_type
class FunctionDefinitionVersionInitArgs:
    def __init__(__self__, *,
                 function_definition_id: pulumi.Input[str],
                 functions: pulumi.Input[Sequence[pulumi.Input['FunctionDefinitionVersionFunctionArgs']]],
                 default_config: Optional[pulumi.Input['FunctionDefinitionVersionDefaultConfigArgs']] = None):
        """
        The set of arguments for constructing a FunctionDefinitionVersion resource.
        """
        pulumi.set(__self__, "function_definition_id", function_definition_id)
        pulumi.set(__self__, "functions", functions)
        if default_config is not None:
            pulumi.set(__self__, "default_config", default_config)

    @property
    @pulumi.getter(name="functionDefinitionId")
    def function_definition_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "function_definition_id")

    @function_definition_id.setter
    def function_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_definition_id", value)

    @property
    @pulumi.getter
    def functions(self) -> pulumi.Input[Sequence[pulumi.Input['FunctionDefinitionVersionFunctionArgs']]]:
        return pulumi.get(self, "functions")

    @functions.setter
    def functions(self, value: pulumi.Input[Sequence[pulumi.Input['FunctionDefinitionVersionFunctionArgs']]]):
        pulumi.set(self, "functions", value)

    @property
    @pulumi.getter(name="defaultConfig")
    def default_config(self) -> Optional[pulumi.Input['FunctionDefinitionVersionDefaultConfigArgs']]:
        return pulumi.get(self, "default_config")

    @default_config.setter
    def default_config(self, value: Optional[pulumi.Input['FunctionDefinitionVersionDefaultConfigArgs']]):
        pulumi.set(self, "default_config", value)


warnings.warn("""FunctionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class FunctionDefinitionVersion(pulumi.CustomResource):
    warnings.warn("""FunctionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_config: Optional[pulumi.Input[pulumi.InputType['FunctionDefinitionVersionDefaultConfigArgs']]] = None,
                 function_definition_id: Optional[pulumi.Input[str]] = None,
                 functions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionDefinitionVersionFunctionArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Greengrass::FunctionDefinitionVersion

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FunctionDefinitionVersionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Greengrass::FunctionDefinitionVersion

        :param str resource_name: The name of the resource.
        :param FunctionDefinitionVersionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FunctionDefinitionVersionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_config: Optional[pulumi.Input[pulumi.InputType['FunctionDefinitionVersionDefaultConfigArgs']]] = None,
                 function_definition_id: Optional[pulumi.Input[str]] = None,
                 functions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionDefinitionVersionFunctionArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""FunctionDefinitionVersion is deprecated: FunctionDefinitionVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FunctionDefinitionVersionInitArgs.__new__(FunctionDefinitionVersionInitArgs)

            __props__.__dict__["default_config"] = default_config
            if function_definition_id is None and not opts.urn:
                raise TypeError("Missing required property 'function_definition_id'")
            __props__.__dict__["function_definition_id"] = function_definition_id
            if functions is None and not opts.urn:
                raise TypeError("Missing required property 'functions'")
            __props__.__dict__["functions"] = functions
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["default_config", "function_definition_id", "functions[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(FunctionDefinitionVersion, __self__).__init__(
            'aws-native:greengrass:FunctionDefinitionVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FunctionDefinitionVersion':
        """
        Get an existing FunctionDefinitionVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FunctionDefinitionVersionInitArgs.__new__(FunctionDefinitionVersionInitArgs)

        __props__.__dict__["default_config"] = None
        __props__.__dict__["function_definition_id"] = None
        __props__.__dict__["functions"] = None
        return FunctionDefinitionVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultConfig")
    def default_config(self) -> pulumi.Output[Optional['outputs.FunctionDefinitionVersionDefaultConfig']]:
        return pulumi.get(self, "default_config")

    @property
    @pulumi.getter(name="functionDefinitionId")
    def function_definition_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "function_definition_id")

    @property
    @pulumi.getter
    def functions(self) -> pulumi.Output[Sequence['outputs.FunctionDefinitionVersionFunction']]:
        return pulumi.get(self, "functions")

