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

__all__ = [
    'GetPipelineResult',
    'AwaitableGetPipelineResult',
    'get_pipeline',
    'get_pipeline_output',
]

@pulumi.output_type
class GetPipelineResult:
    def __init__(__self__, parallelism_configuration=None, pipeline_definition=None, pipeline_description=None, pipeline_display_name=None, role_arn=None, tags=None):
        if parallelism_configuration and not isinstance(parallelism_configuration, dict):
            raise TypeError("Expected argument 'parallelism_configuration' to be a dict")
        pulumi.set(__self__, "parallelism_configuration", parallelism_configuration)
        if pipeline_definition and not isinstance(pipeline_definition, dict):
            raise TypeError("Expected argument 'pipeline_definition' to be a dict")
        pulumi.set(__self__, "pipeline_definition", pipeline_definition)
        if pipeline_description and not isinstance(pipeline_description, str):
            raise TypeError("Expected argument 'pipeline_description' to be a str")
        pulumi.set(__self__, "pipeline_description", pipeline_description)
        if pipeline_display_name and not isinstance(pipeline_display_name, str):
            raise TypeError("Expected argument 'pipeline_display_name' to be a str")
        pulumi.set(__self__, "pipeline_display_name", pipeline_display_name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(self) -> Optional['outputs.ParallelismConfigurationProperties']:
        return pulumi.get(self, "parallelism_configuration")

    @property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> Optional[Any]:
        return pulumi.get(self, "pipeline_definition")

    @property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> Optional[str]:
        """
        The description of the Pipeline.
        """
        return pulumi.get(self, "pipeline_description")

    @property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> Optional[str]:
        """
        The display name of the Pipeline.
        """
        return pulumi.get(self, "pipeline_display_name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        Role Arn
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PipelineTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetPipelineResult(GetPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineResult(
            parallelism_configuration=self.parallelism_configuration,
            pipeline_definition=self.pipeline_definition,
            pipeline_description=self.pipeline_description,
            pipeline_display_name=self.pipeline_display_name,
            role_arn=self.role_arn,
            tags=self.tags)


def get_pipeline(pipeline_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineResult:
    """
    Resource Type definition for AWS::SageMaker::Pipeline


    :param str pipeline_name: The name of the Pipeline.
    """
    __args__ = dict()
    __args__['pipelineName'] = pipeline_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getPipeline', __args__, opts=opts, typ=GetPipelineResult).value

    return AwaitableGetPipelineResult(
        parallelism_configuration=pulumi.get(__ret__, 'parallelism_configuration'),
        pipeline_definition=pulumi.get(__ret__, 'pipeline_definition'),
        pipeline_description=pulumi.get(__ret__, 'pipeline_description'),
        pipeline_display_name=pulumi.get(__ret__, 'pipeline_display_name'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_pipeline)
def get_pipeline_output(pipeline_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineResult]:
    """
    Resource Type definition for AWS::SageMaker::Pipeline


    :param str pipeline_name: The name of the Pipeline.
    """
    ...
