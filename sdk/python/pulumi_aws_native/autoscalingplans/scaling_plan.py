# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ScalingPlanArgs', 'ScalingPlan']

@pulumi.input_type
class ScalingPlanArgs:
    def __init__(__self__, *,
                 application_source: pulumi.Input['ScalingPlanApplicationSourceArgs'],
                 scaling_instructions: pulumi.Input[Sequence[pulumi.Input['ScalingPlanScalingInstructionArgs']]]):
        """
        The set of arguments for constructing a ScalingPlan resource.
        """
        pulumi.set(__self__, "application_source", application_source)
        pulumi.set(__self__, "scaling_instructions", scaling_instructions)

    @property
    @pulumi.getter(name="applicationSource")
    def application_source(self) -> pulumi.Input['ScalingPlanApplicationSourceArgs']:
        return pulumi.get(self, "application_source")

    @application_source.setter
    def application_source(self, value: pulumi.Input['ScalingPlanApplicationSourceArgs']):
        pulumi.set(self, "application_source", value)

    @property
    @pulumi.getter(name="scalingInstructions")
    def scaling_instructions(self) -> pulumi.Input[Sequence[pulumi.Input['ScalingPlanScalingInstructionArgs']]]:
        return pulumi.get(self, "scaling_instructions")

    @scaling_instructions.setter
    def scaling_instructions(self, value: pulumi.Input[Sequence[pulumi.Input['ScalingPlanScalingInstructionArgs']]]):
        pulumi.set(self, "scaling_instructions", value)


warnings.warn("""ScalingPlan is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ScalingPlan(pulumi.CustomResource):
    warnings.warn("""ScalingPlan is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_source: Optional[pulumi.Input[pulumi.InputType['ScalingPlanApplicationSourceArgs']]] = None,
                 scaling_instructions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScalingInstructionArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AutoScalingPlans::ScalingPlan

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AutoScalingPlans::ScalingPlan

        :param str resource_name: The name of the resource.
        :param ScalingPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScalingPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_source: Optional[pulumi.Input[pulumi.InputType['ScalingPlanApplicationSourceArgs']]] = None,
                 scaling_instructions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScalingInstructionArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ScalingPlan is deprecated: ScalingPlan is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScalingPlanArgs.__new__(ScalingPlanArgs)

            if application_source is None and not opts.urn:
                raise TypeError("Missing required property 'application_source'")
            __props__.__dict__["application_source"] = application_source
            if scaling_instructions is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_instructions'")
            __props__.__dict__["scaling_instructions"] = scaling_instructions
            __props__.__dict__["scaling_plan_name"] = None
            __props__.__dict__["scaling_plan_version"] = None
        super(ScalingPlan, __self__).__init__(
            'aws-native:autoscalingplans:ScalingPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScalingPlan':
        """
        Get an existing ScalingPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScalingPlanArgs.__new__(ScalingPlanArgs)

        __props__.__dict__["application_source"] = None
        __props__.__dict__["scaling_instructions"] = None
        __props__.__dict__["scaling_plan_name"] = None
        __props__.__dict__["scaling_plan_version"] = None
        return ScalingPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationSource")
    def application_source(self) -> pulumi.Output['outputs.ScalingPlanApplicationSource']:
        return pulumi.get(self, "application_source")

    @property
    @pulumi.getter(name="scalingInstructions")
    def scaling_instructions(self) -> pulumi.Output[Sequence['outputs.ScalingPlanScalingInstruction']]:
        return pulumi.get(self, "scaling_instructions")

    @property
    @pulumi.getter(name="scalingPlanName")
    def scaling_plan_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "scaling_plan_name")

    @property
    @pulumi.getter(name="scalingPlanVersion")
    def scaling_plan_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "scaling_plan_version")

