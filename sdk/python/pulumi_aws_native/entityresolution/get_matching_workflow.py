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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetMatchingWorkflowResult',
    'AwaitableGetMatchingWorkflowResult',
    'get_matching_workflow',
    'get_matching_workflow_output',
]

@pulumi.output_type
class GetMatchingWorkflowResult:
    def __init__(__self__, created_at=None, description=None, input_source_config=None, output_source_config=None, resolution_techniques=None, role_arn=None, tags=None, updated_at=None, workflow_arn=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if input_source_config and not isinstance(input_source_config, list):
            raise TypeError("Expected argument 'input_source_config' to be a list")
        pulumi.set(__self__, "input_source_config", input_source_config)
        if output_source_config and not isinstance(output_source_config, list):
            raise TypeError("Expected argument 'output_source_config' to be a list")
        pulumi.set(__self__, "output_source_config", output_source_config)
        if resolution_techniques and not isinstance(resolution_techniques, dict):
            raise TypeError("Expected argument 'resolution_techniques' to be a dict")
        pulumi.set(__self__, "resolution_techniques", resolution_techniques)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if workflow_arn and not isinstance(workflow_arn, str):
            raise TypeError("Expected argument 'workflow_arn' to be a str")
        pulumi.set(__self__, "workflow_arn", workflow_arn)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the MatchingWorkflow
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inputSourceConfig")
    def input_source_config(self) -> Optional[Sequence['outputs.MatchingWorkflowInputSource']]:
        return pulumi.get(self, "input_source_config")

    @property
    @pulumi.getter(name="outputSourceConfig")
    def output_source_config(self) -> Optional[Sequence['outputs.MatchingWorkflowOutputSource']]:
        return pulumi.get(self, "output_source_config")

    @property
    @pulumi.getter(name="resolutionTechniques")
    def resolution_techniques(self) -> Optional['outputs.MatchingWorkflowResolutionTechniques']:
        return pulumi.get(self, "resolution_techniques")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="workflowArn")
    def workflow_arn(self) -> Optional[str]:
        return pulumi.get(self, "workflow_arn")


class AwaitableGetMatchingWorkflowResult(GetMatchingWorkflowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMatchingWorkflowResult(
            created_at=self.created_at,
            description=self.description,
            input_source_config=self.input_source_config,
            output_source_config=self.output_source_config,
            resolution_techniques=self.resolution_techniques,
            role_arn=self.role_arn,
            tags=self.tags,
            updated_at=self.updated_at,
            workflow_arn=self.workflow_arn)


def get_matching_workflow(workflow_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMatchingWorkflowResult:
    """
    MatchingWorkflow defined in AWS Entity Resolution service


    :param str workflow_name: The name of the MatchingWorkflow
    """
    __args__ = dict()
    __args__['workflowName'] = workflow_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:entityresolution:getMatchingWorkflow', __args__, opts=opts, typ=GetMatchingWorkflowResult).value

    return AwaitableGetMatchingWorkflowResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        input_source_config=pulumi.get(__ret__, 'input_source_config'),
        output_source_config=pulumi.get(__ret__, 'output_source_config'),
        resolution_techniques=pulumi.get(__ret__, 'resolution_techniques'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        workflow_arn=pulumi.get(__ret__, 'workflow_arn'))


@_utilities.lift_output_func(get_matching_workflow)
def get_matching_workflow_output(workflow_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMatchingWorkflowResult]:
    """
    MatchingWorkflow defined in AWS Entity Resolution service


    :param str workflow_name: The name of the MatchingWorkflow
    """
    ...
