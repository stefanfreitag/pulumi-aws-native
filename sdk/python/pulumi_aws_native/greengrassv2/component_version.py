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

__all__ = ['ComponentVersionArgs', 'ComponentVersion']

@pulumi.input_type
class ComponentVersionArgs:
    def __init__(__self__, *,
                 inline_recipe: Optional[pulumi.Input[str]] = None,
                 lambda_function: Optional[pulumi.Input['ComponentVersionLambdaFunctionRecipeSourceArgs']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a ComponentVersion resource.
        :param Any tags: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::GreengrassV2::ComponentVersion` for more information about the expected schema for this property.
        """
        if inline_recipe is not None:
            pulumi.set(__self__, "inline_recipe", inline_recipe)
        if lambda_function is not None:
            pulumi.set(__self__, "lambda_function", lambda_function)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="inlineRecipe")
    def inline_recipe(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "inline_recipe")

    @inline_recipe.setter
    def inline_recipe(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inline_recipe", value)

    @property
    @pulumi.getter(name="lambdaFunction")
    def lambda_function(self) -> Optional[pulumi.Input['ComponentVersionLambdaFunctionRecipeSourceArgs']]:
        return pulumi.get(self, "lambda_function")

    @lambda_function.setter
    def lambda_function(self, value: Optional[pulumi.Input['ComponentVersionLambdaFunctionRecipeSourceArgs']]):
        pulumi.set(self, "lambda_function", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::GreengrassV2::ComponentVersion` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class ComponentVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inline_recipe: Optional[pulumi.Input[str]] = None,
                 lambda_function: Optional[pulumi.Input[pulumi.InputType['ComponentVersionLambdaFunctionRecipeSourceArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource for Greengrass component version.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any tags: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::GreengrassV2::ComponentVersion` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ComponentVersionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for Greengrass component version.

        :param str resource_name: The name of the resource.
        :param ComponentVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inline_recipe: Optional[pulumi.Input[str]] = None,
                 lambda_function: Optional[pulumi.Input[pulumi.InputType['ComponentVersionLambdaFunctionRecipeSourceArgs']]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentVersionArgs.__new__(ComponentVersionArgs)

            __props__.__dict__["inline_recipe"] = inline_recipe
            __props__.__dict__["lambda_function"] = lambda_function
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["component_name"] = None
            __props__.__dict__["component_version"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["inline_recipe", "lambda_function"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ComponentVersion, __self__).__init__(
            'aws-native:greengrassv2:ComponentVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ComponentVersion':
        """
        Get an existing ComponentVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentVersionArgs.__new__(ComponentVersionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["component_name"] = None
        __props__.__dict__["component_version"] = None
        __props__.__dict__["inline_recipe"] = None
        __props__.__dict__["lambda_function"] = None
        __props__.__dict__["tags"] = None
        return ComponentVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter(name="inlineRecipe")
    def inline_recipe(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "inline_recipe")

    @property
    @pulumi.getter(name="lambdaFunction")
    def lambda_function(self) -> pulumi.Output[Optional['outputs.ComponentVersionLambdaFunctionRecipeSource']]:
        return pulumi.get(self, "lambda_function")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::GreengrassV2::ComponentVersion` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

