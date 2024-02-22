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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['EvaluationFormArgs', 'EvaluationForm']

@pulumi.input_type
class EvaluationFormArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 items: pulumi.Input[Sequence[pulumi.Input['EvaluationFormBaseItemArgs']]],
                 status: pulumi.Input['EvaluationFormStatus'],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 scoring_strategy: Optional[pulumi.Input['EvaluationFormScoringStrategyArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a EvaluationForm resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param pulumi.Input[Sequence[pulumi.Input['EvaluationFormBaseItemArgs']]] items: The list of evaluation form items.
        :param pulumi.Input['EvaluationFormStatus'] status: The status of the evaluation form.
        :param pulumi.Input[str] title: The title of the evaluation form.
        :param pulumi.Input[str] description: The description of the evaluation form.
        :param pulumi.Input['EvaluationFormScoringStrategyArgs'] scoring_strategy: The scoring strategy.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: One or more tags.
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        pulumi.set(__self__, "items", items)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if scoring_strategy is not None:
            pulumi.set(__self__, "scoring_strategy", scoring_strategy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input['EvaluationFormBaseItemArgs']]]:
        """
        The list of evaluation form items.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input['EvaluationFormBaseItemArgs']]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['EvaluationFormStatus']:
        """
        The status of the evaluation form.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['EvaluationFormStatus']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the evaluation form.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the evaluation form.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="scoringStrategy")
    def scoring_strategy(self) -> Optional[pulumi.Input['EvaluationFormScoringStrategyArgs']]:
        """
        The scoring strategy.
        """
        return pulumi.get(self, "scoring_strategy")

    @scoring_strategy.setter
    def scoring_strategy(self, value: Optional[pulumi.Input['EvaluationFormScoringStrategyArgs']]):
        pulumi.set(self, "scoring_strategy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class EvaluationForm(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EvaluationFormBaseItemArgs']]]]] = None,
                 scoring_strategy: Optional[pulumi.Input[pulumi.InputType['EvaluationFormScoringStrategyArgs']]] = None,
                 status: Optional[pulumi.Input['EvaluationFormStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::EvaluationForm

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the evaluation form.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EvaluationFormBaseItemArgs']]]] items: The list of evaluation form items.
        :param pulumi.Input[pulumi.InputType['EvaluationFormScoringStrategyArgs']] scoring_strategy: The scoring strategy.
        :param pulumi.Input['EvaluationFormStatus'] status: The status of the evaluation form.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: One or more tags.
        :param pulumi.Input[str] title: The title of the evaluation form.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EvaluationFormArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::EvaluationForm

        :param str resource_name: The name of the resource.
        :param EvaluationFormArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EvaluationFormArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EvaluationFormBaseItemArgs']]]]] = None,
                 scoring_strategy: Optional[pulumi.Input[pulumi.InputType['EvaluationFormScoringStrategyArgs']]] = None,
                 status: Optional[pulumi.Input['EvaluationFormStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EvaluationFormArgs.__new__(EvaluationFormArgs)

            __props__.__dict__["description"] = description
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            if items is None and not opts.urn:
                raise TypeError("Missing required property 'items'")
            __props__.__dict__["items"] = items
            __props__.__dict__["scoring_strategy"] = scoring_strategy
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["evaluation_form_arn"] = None
        super(EvaluationForm, __self__).__init__(
            'aws-native:connect:EvaluationForm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EvaluationForm':
        """
        Get an existing EvaluationForm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EvaluationFormArgs.__new__(EvaluationFormArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["evaluation_form_arn"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["items"] = None
        __props__.__dict__["scoring_strategy"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        return EvaluationForm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the evaluation form.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="evaluationFormArn")
    def evaluation_form_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the evaluation form.
        """
        return pulumi.get(self, "evaluation_form_arn")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Sequence['outputs.EvaluationFormBaseItem']]:
        """
        The list of evaluation form items.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="scoringStrategy")
    def scoring_strategy(self) -> pulumi.Output[Optional['outputs.EvaluationFormScoringStrategy']]:
        """
        The scoring strategy.
        """
        return pulumi.get(self, "scoring_strategy")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['EvaluationFormStatus']:
        """
        The status of the evaluation form.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the evaluation form.
        """
        return pulumi.get(self, "title")

