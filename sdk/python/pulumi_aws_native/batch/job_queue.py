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
from ._enums import *
from ._inputs import *

__all__ = ['JobQueueArgs', 'JobQueue']

@pulumi.input_type
class JobQueueArgs:
    def __init__(__self__, *,
                 compute_environment_order: pulumi.Input[Sequence[pulumi.Input['JobQueueComputeEnvironmentOrderArgs']]],
                 priority: pulumi.Input[int],
                 job_queue_name: Optional[pulumi.Input[str]] = None,
                 scheduling_policy_arn: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['JobQueueState']] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a JobQueue resource.
        :param Any tags: A key-value pair to associate with a resource.
        """
        JobQueueArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compute_environment_order=compute_environment_order,
            priority=priority,
            job_queue_name=job_queue_name,
            scheduling_policy_arn=scheduling_policy_arn,
            state=state,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compute_environment_order: pulumi.Input[Sequence[pulumi.Input['JobQueueComputeEnvironmentOrderArgs']]],
             priority: pulumi.Input[int],
             job_queue_name: Optional[pulumi.Input[str]] = None,
             scheduling_policy_arn: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input['JobQueueState']] = None,
             tags: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compute_environment_order", compute_environment_order)
        _setter("priority", priority)
        if job_queue_name is not None:
            _setter("job_queue_name", job_queue_name)
        if scheduling_policy_arn is not None:
            _setter("scheduling_policy_arn", scheduling_policy_arn)
        if state is not None:
            _setter("state", state)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="computeEnvironmentOrder")
    def compute_environment_order(self) -> pulumi.Input[Sequence[pulumi.Input['JobQueueComputeEnvironmentOrderArgs']]]:
        return pulumi.get(self, "compute_environment_order")

    @compute_environment_order.setter
    def compute_environment_order(self, value: pulumi.Input[Sequence[pulumi.Input['JobQueueComputeEnvironmentOrderArgs']]]):
        pulumi.set(self, "compute_environment_order", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="jobQueueName")
    def job_queue_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "job_queue_name")

    @job_queue_name.setter
    def job_queue_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_queue_name", value)

    @property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheduling_policy_arn")

    @scheduling_policy_arn.setter
    def scheduling_policy_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduling_policy_arn", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['JobQueueState']]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['JobQueueState']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class JobQueue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_environment_order: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobQueueComputeEnvironmentOrderArgs']]]]] = None,
                 job_queue_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 scheduling_policy_arn: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['JobQueueState']] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Batch::JobQueue

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any tags: A key-value pair to associate with a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobQueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Batch::JobQueue

        :param str resource_name: The name of the resource.
        :param JobQueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobQueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            JobQueueArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_environment_order: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobQueueComputeEnvironmentOrderArgs']]]]] = None,
                 job_queue_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 scheduling_policy_arn: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['JobQueueState']] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobQueueArgs.__new__(JobQueueArgs)

            if compute_environment_order is None and not opts.urn:
                raise TypeError("Missing required property 'compute_environment_order'")
            __props__.__dict__["compute_environment_order"] = compute_environment_order
            __props__.__dict__["job_queue_name"] = job_queue_name
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            __props__.__dict__["scheduling_policy_arn"] = scheduling_policy_arn
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["job_queue_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["job_queue_name", "tags"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(JobQueue, __self__).__init__(
            'aws-native:batch:JobQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobQueue':
        """
        Get an existing JobQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobQueueArgs.__new__(JobQueueArgs)

        __props__.__dict__["compute_environment_order"] = None
        __props__.__dict__["job_queue_arn"] = None
        __props__.__dict__["job_queue_name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["scheduling_policy_arn"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        return JobQueue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeEnvironmentOrder")
    def compute_environment_order(self) -> pulumi.Output[Sequence['outputs.JobQueueComputeEnvironmentOrder']]:
        return pulumi.get(self, "compute_environment_order")

    @property
    @pulumi.getter(name="jobQueueArn")
    def job_queue_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "job_queue_arn")

    @property
    @pulumi.getter(name="jobQueueName")
    def job_queue_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "job_queue_name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scheduling_policy_arn")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional['JobQueueState']]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

