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
    'GetCanaryResult',
    'AwaitableGetCanaryResult',
    'get_canary',
    'get_canary_output',
]

@pulumi.output_type
class GetCanaryResult:
    def __init__(__self__, artifact_config=None, artifact_s3_location=None, code=None, execution_role_arn=None, failure_retention_period=None, id=None, run_config=None, runtime_version=None, schedule=None, state=None, success_retention_period=None, tags=None, vpc_config=None):
        if artifact_config and not isinstance(artifact_config, dict):
            raise TypeError("Expected argument 'artifact_config' to be a dict")
        pulumi.set(__self__, "artifact_config", artifact_config)
        if artifact_s3_location and not isinstance(artifact_s3_location, str):
            raise TypeError("Expected argument 'artifact_s3_location' to be a str")
        pulumi.set(__self__, "artifact_s3_location", artifact_s3_location)
        if code and not isinstance(code, dict):
            raise TypeError("Expected argument 'code' to be a dict")
        pulumi.set(__self__, "code", code)
        if execution_role_arn and not isinstance(execution_role_arn, str):
            raise TypeError("Expected argument 'execution_role_arn' to be a str")
        pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if failure_retention_period and not isinstance(failure_retention_period, int):
            raise TypeError("Expected argument 'failure_retention_period' to be a int")
        pulumi.set(__self__, "failure_retention_period", failure_retention_period)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if run_config and not isinstance(run_config, dict):
            raise TypeError("Expected argument 'run_config' to be a dict")
        pulumi.set(__self__, "run_config", run_config)
        if runtime_version and not isinstance(runtime_version, str):
            raise TypeError("Expected argument 'runtime_version' to be a str")
        pulumi.set(__self__, "runtime_version", runtime_version)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if success_retention_period and not isinstance(success_retention_period, int):
            raise TypeError("Expected argument 'success_retention_period' to be a int")
        pulumi.set(__self__, "success_retention_period", success_retention_period)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_config and not isinstance(vpc_config, dict):
            raise TypeError("Expected argument 'vpc_config' to be a dict")
        pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter(name="artifactConfig")
    def artifact_config(self) -> Optional['outputs.CanaryArtifactConfig']:
        """
        Provide artifact configuration
        """
        return pulumi.get(self, "artifact_config")

    @property
    @pulumi.getter(name="artifactS3Location")
    def artifact_s3_location(self) -> Optional[str]:
        """
        Provide the s3 bucket output location for test results
        """
        return pulumi.get(self, "artifact_s3_location")

    @property
    @pulumi.getter
    def code(self) -> Optional['outputs.CanaryCode']:
        """
        Provide the canary script source
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[str]:
        """
        Lambda Execution role used to run your canaries
        """
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="failureRetentionPeriod")
    def failure_retention_period(self) -> Optional[int]:
        """
        Retention period of failed canary runs represented in number of days
        """
        return pulumi.get(self, "failure_retention_period")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of the canary
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="runConfig")
    def run_config(self) -> Optional['outputs.CanaryRunConfig']:
        """
        Provide canary run configuration
        """
        return pulumi.get(self, "run_config")

    @property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[str]:
        """
        Runtime version of Synthetics Library
        """
        return pulumi.get(self, "runtime_version")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.CanarySchedule']:
        """
        Frequency to run your canaries
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of the canary
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="successRetentionPeriod")
    def success_retention_period(self) -> Optional[int]:
        """
        Retention period of successful canary runs represented in number of days
        """
        return pulumi.get(self, "success_retention_period")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CanaryTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional['outputs.CanaryVpcConfig']:
        """
        Provide VPC Configuration if enabled.
        """
        return pulumi.get(self, "vpc_config")


class AwaitableGetCanaryResult(GetCanaryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCanaryResult(
            artifact_config=self.artifact_config,
            artifact_s3_location=self.artifact_s3_location,
            code=self.code,
            execution_role_arn=self.execution_role_arn,
            failure_retention_period=self.failure_retention_period,
            id=self.id,
            run_config=self.run_config,
            runtime_version=self.runtime_version,
            schedule=self.schedule,
            state=self.state,
            success_retention_period=self.success_retention_period,
            tags=self.tags,
            vpc_config=self.vpc_config)


def get_canary(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCanaryResult:
    """
    Resource Type definition for AWS::Synthetics::Canary


    :param str name: Name of the canary.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:synthetics:getCanary', __args__, opts=opts, typ=GetCanaryResult).value

    return AwaitableGetCanaryResult(
        artifact_config=pulumi.get(__ret__, 'artifact_config'),
        artifact_s3_location=pulumi.get(__ret__, 'artifact_s3_location'),
        code=pulumi.get(__ret__, 'code'),
        execution_role_arn=pulumi.get(__ret__, 'execution_role_arn'),
        failure_retention_period=pulumi.get(__ret__, 'failure_retention_period'),
        id=pulumi.get(__ret__, 'id'),
        run_config=pulumi.get(__ret__, 'run_config'),
        runtime_version=pulumi.get(__ret__, 'runtime_version'),
        schedule=pulumi.get(__ret__, 'schedule'),
        state=pulumi.get(__ret__, 'state'),
        success_retention_period=pulumi.get(__ret__, 'success_retention_period'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_config=pulumi.get(__ret__, 'vpc_config'))


@_utilities.lift_output_func(get_canary)
def get_canary_output(name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCanaryResult]:
    """
    Resource Type definition for AWS::Synthetics::Canary


    :param str name: Name of the canary.
    """
    ...
