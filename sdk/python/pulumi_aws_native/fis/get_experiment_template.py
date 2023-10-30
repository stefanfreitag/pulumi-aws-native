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
    'GetExperimentTemplateResult',
    'AwaitableGetExperimentTemplateResult',
    'get_experiment_template',
    'get_experiment_template_output',
]

@pulumi.output_type
class GetExperimentTemplateResult:
    def __init__(__self__, actions=None, description=None, id=None, log_configuration=None, role_arn=None, stop_conditions=None, targets=None):
        if actions and not isinstance(actions, dict):
            raise TypeError("Expected argument 'actions' to be a dict")
        pulumi.set(__self__, "actions", actions)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_configuration and not isinstance(log_configuration, dict):
            raise TypeError("Expected argument 'log_configuration' to be a dict")
        pulumi.set(__self__, "log_configuration", log_configuration)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if stop_conditions and not isinstance(stop_conditions, list):
            raise TypeError("Expected argument 'stop_conditions' to be a list")
        pulumi.set(__self__, "stop_conditions", stop_conditions)
        if targets and not isinstance(targets, dict):
            raise TypeError("Expected argument 'targets' to be a dict")
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter
    def actions(self) -> Optional['outputs.ExperimentTemplateActionMap']:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional['outputs.ExperimentTemplateLogConfiguration']:
        return pulumi.get(self, "log_configuration")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="stopConditions")
    def stop_conditions(self) -> Optional[Sequence['outputs.ExperimentTemplateStopCondition']]:
        return pulumi.get(self, "stop_conditions")

    @property
    @pulumi.getter
    def targets(self) -> Optional['outputs.ExperimentTemplateTargetMap']:
        return pulumi.get(self, "targets")


class AwaitableGetExperimentTemplateResult(GetExperimentTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExperimentTemplateResult(
            actions=self.actions,
            description=self.description,
            id=self.id,
            log_configuration=self.log_configuration,
            role_arn=self.role_arn,
            stop_conditions=self.stop_conditions,
            targets=self.targets)


def get_experiment_template(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExperimentTemplateResult:
    """
    Resource schema for AWS::FIS::ExperimentTemplate
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:fis:getExperimentTemplate', __args__, opts=opts, typ=GetExperimentTemplateResult).value

    return AwaitableGetExperimentTemplateResult(
        actions=pulumi.get(__ret__, 'actions'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        log_configuration=pulumi.get(__ret__, 'log_configuration'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        stop_conditions=pulumi.get(__ret__, 'stop_conditions'),
        targets=pulumi.get(__ret__, 'targets'))


@_utilities.lift_output_func(get_experiment_template)
def get_experiment_template_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExperimentTemplateResult]:
    """
    Resource schema for AWS::FIS::ExperimentTemplate
    """
    ...
