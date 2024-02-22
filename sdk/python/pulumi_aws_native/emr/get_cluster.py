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

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, auto_termination_policy=None, id=None, instances=None, managed_scaling_policy=None, master_public_dns=None, step_concurrency_level=None, tags=None, visible_to_all_users=None):
        if auto_termination_policy and not isinstance(auto_termination_policy, dict):
            raise TypeError("Expected argument 'auto_termination_policy' to be a dict")
        pulumi.set(__self__, "auto_termination_policy", auto_termination_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances and not isinstance(instances, dict):
            raise TypeError("Expected argument 'instances' to be a dict")
        pulumi.set(__self__, "instances", instances)
        if managed_scaling_policy and not isinstance(managed_scaling_policy, dict):
            raise TypeError("Expected argument 'managed_scaling_policy' to be a dict")
        pulumi.set(__self__, "managed_scaling_policy", managed_scaling_policy)
        if master_public_dns and not isinstance(master_public_dns, str):
            raise TypeError("Expected argument 'master_public_dns' to be a str")
        pulumi.set(__self__, "master_public_dns", master_public_dns)
        if step_concurrency_level and not isinstance(step_concurrency_level, int):
            raise TypeError("Expected argument 'step_concurrency_level' to be a int")
        pulumi.set(__self__, "step_concurrency_level", step_concurrency_level)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if visible_to_all_users and not isinstance(visible_to_all_users, bool):
            raise TypeError("Expected argument 'visible_to_all_users' to be a bool")
        pulumi.set(__self__, "visible_to_all_users", visible_to_all_users)

    @property
    @pulumi.getter(name="autoTerminationPolicy")
    def auto_termination_policy(self) -> Optional['outputs.ClusterAutoTerminationPolicy']:
        return pulumi.get(self, "auto_termination_policy")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> Optional['outputs.ClusterJobFlowInstancesConfig']:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="managedScalingPolicy")
    def managed_scaling_policy(self) -> Optional['outputs.ClusterManagedScalingPolicy']:
        return pulumi.get(self, "managed_scaling_policy")

    @property
    @pulumi.getter(name="masterPublicDns")
    def master_public_dns(self) -> Optional[str]:
        return pulumi.get(self, "master_public_dns")

    @property
    @pulumi.getter(name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> Optional[int]:
        return pulumi.get(self, "step_concurrency_level")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="visibleToAllUsers")
    def visible_to_all_users(self) -> Optional[bool]:
        return pulumi.get(self, "visible_to_all_users")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            auto_termination_policy=self.auto_termination_policy,
            id=self.id,
            instances=self.instances,
            managed_scaling_policy=self.managed_scaling_policy,
            master_public_dns=self.master_public_dns,
            step_concurrency_level=self.step_concurrency_level,
            tags=self.tags,
            visible_to_all_users=self.visible_to_all_users)


def get_cluster(id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Resource Type definition for AWS::EMR::Cluster
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:emr:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        auto_termination_policy=pulumi.get(__ret__, 'auto_termination_policy'),
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'),
        managed_scaling_policy=pulumi.get(__ret__, 'managed_scaling_policy'),
        master_public_dns=pulumi.get(__ret__, 'master_public_dns'),
        step_concurrency_level=pulumi.get(__ret__, 'step_concurrency_level'),
        tags=pulumi.get(__ret__, 'tags'),
        visible_to_all_users=pulumi.get(__ret__, 'visible_to_all_users'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Resource Type definition for AWS::EMR::Cluster
    """
    ...
