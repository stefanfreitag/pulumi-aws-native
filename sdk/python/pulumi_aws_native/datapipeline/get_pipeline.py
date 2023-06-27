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

__all__ = [
    'GetPipelineResult',
    'AwaitableGetPipelineResult',
    'get_pipeline',
    'get_pipeline_output',
]

@pulumi.output_type
class GetPipelineResult:
    def __init__(__self__, activate=None, parameter_objects=None, parameter_values=None, pipeline_id=None, pipeline_objects=None, pipeline_tags=None):
        if activate and not isinstance(activate, bool):
            raise TypeError("Expected argument 'activate' to be a bool")
        pulumi.set(__self__, "activate", activate)
        if parameter_objects and not isinstance(parameter_objects, list):
            raise TypeError("Expected argument 'parameter_objects' to be a list")
        pulumi.set(__self__, "parameter_objects", parameter_objects)
        if parameter_values and not isinstance(parameter_values, list):
            raise TypeError("Expected argument 'parameter_values' to be a list")
        pulumi.set(__self__, "parameter_values", parameter_values)
        if pipeline_id and not isinstance(pipeline_id, str):
            raise TypeError("Expected argument 'pipeline_id' to be a str")
        pulumi.set(__self__, "pipeline_id", pipeline_id)
        if pipeline_objects and not isinstance(pipeline_objects, list):
            raise TypeError("Expected argument 'pipeline_objects' to be a list")
        pulumi.set(__self__, "pipeline_objects", pipeline_objects)
        if pipeline_tags and not isinstance(pipeline_tags, list):
            raise TypeError("Expected argument 'pipeline_tags' to be a list")
        pulumi.set(__self__, "pipeline_tags", pipeline_tags)

    @property
    @pulumi.getter
    def activate(self) -> Optional[bool]:
        """
        Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to true.
        """
        return pulumi.get(self, "activate")

    @property
    @pulumi.getter(name="parameterObjects")
    def parameter_objects(self) -> Optional[Sequence['outputs.PipelineParameterObject']]:
        """
        The parameter objects used with the pipeline.
        """
        return pulumi.get(self, "parameter_objects")

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[Sequence['outputs.PipelineParameterValue']]:
        """
        The parameter values used with the pipeline.
        """
        return pulumi.get(self, "parameter_values")

    @property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[str]:
        return pulumi.get(self, "pipeline_id")

    @property
    @pulumi.getter(name="pipelineObjects")
    def pipeline_objects(self) -> Optional[Sequence['outputs.PipelineObject']]:
        """
        The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see Editing Your Pipeline in the AWS Data Pipeline Developer Guide.
        """
        return pulumi.get(self, "pipeline_objects")

    @property
    @pulumi.getter(name="pipelineTags")
    def pipeline_tags(self) -> Optional[Sequence['outputs.PipelineTag']]:
        """
        A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see Controlling Access to Pipelines and Resources in the AWS Data Pipeline Developer Guide.
        """
        return pulumi.get(self, "pipeline_tags")


class AwaitableGetPipelineResult(GetPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineResult(
            activate=self.activate,
            parameter_objects=self.parameter_objects,
            parameter_values=self.parameter_values,
            pipeline_id=self.pipeline_id,
            pipeline_objects=self.pipeline_objects,
            pipeline_tags=self.pipeline_tags)


def get_pipeline(pipeline_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineResult:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    __args__ = dict()
    __args__['pipelineId'] = pipeline_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datapipeline:getPipeline', __args__, opts=opts, typ=GetPipelineResult).value

    return AwaitableGetPipelineResult(
        activate=__ret__.activate,
        parameter_objects=__ret__.parameter_objects,
        parameter_values=__ret__.parameter_values,
        pipeline_id=__ret__.pipeline_id,
        pipeline_objects=__ret__.pipeline_objects,
        pipeline_tags=__ret__.pipeline_tags)


@_utilities.lift_output_func(get_pipeline)
def get_pipeline_output(pipeline_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineResult]:
    """
    An example resource schema demonstrating some basic constructs and validation rules.
    """
    ...
