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

__all__ = [
    'GetFleetResult',
    'AwaitableGetFleetResult',
    'get_fleet',
    'get_fleet_output',
]

@pulumi.output_type
class GetFleetResult:
    def __init__(__self__, anywhere_configuration=None, description=None, desired_ec2_instances=None, ec2_inbound_permissions=None, fleet_id=None, locations=None, max_size=None, metric_groups=None, min_size=None, name=None, new_game_session_protection_policy=None, resource_creation_limit_policy=None, runtime_configuration=None):
        if anywhere_configuration and not isinstance(anywhere_configuration, dict):
            raise TypeError("Expected argument 'anywhere_configuration' to be a dict")
        pulumi.set(__self__, "anywhere_configuration", anywhere_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if desired_ec2_instances and not isinstance(desired_ec2_instances, int):
            raise TypeError("Expected argument 'desired_ec2_instances' to be a int")
        pulumi.set(__self__, "desired_ec2_instances", desired_ec2_instances)
        if ec2_inbound_permissions and not isinstance(ec2_inbound_permissions, list):
            raise TypeError("Expected argument 'ec2_inbound_permissions' to be a list")
        pulumi.set(__self__, "ec2_inbound_permissions", ec2_inbound_permissions)
        if fleet_id and not isinstance(fleet_id, str):
            raise TypeError("Expected argument 'fleet_id' to be a str")
        pulumi.set(__self__, "fleet_id", fleet_id)
        if locations and not isinstance(locations, list):
            raise TypeError("Expected argument 'locations' to be a list")
        pulumi.set(__self__, "locations", locations)
        if max_size and not isinstance(max_size, int):
            raise TypeError("Expected argument 'max_size' to be a int")
        pulumi.set(__self__, "max_size", max_size)
        if metric_groups and not isinstance(metric_groups, list):
            raise TypeError("Expected argument 'metric_groups' to be a list")
        pulumi.set(__self__, "metric_groups", metric_groups)
        if min_size and not isinstance(min_size, int):
            raise TypeError("Expected argument 'min_size' to be a int")
        pulumi.set(__self__, "min_size", min_size)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if new_game_session_protection_policy and not isinstance(new_game_session_protection_policy, str):
            raise TypeError("Expected argument 'new_game_session_protection_policy' to be a str")
        pulumi.set(__self__, "new_game_session_protection_policy", new_game_session_protection_policy)
        if resource_creation_limit_policy and not isinstance(resource_creation_limit_policy, dict):
            raise TypeError("Expected argument 'resource_creation_limit_policy' to be a dict")
        pulumi.set(__self__, "resource_creation_limit_policy", resource_creation_limit_policy)
        if runtime_configuration and not isinstance(runtime_configuration, dict):
            raise TypeError("Expected argument 'runtime_configuration' to be a dict")
        pulumi.set(__self__, "runtime_configuration", runtime_configuration)

    @property
    @pulumi.getter(name="anywhereConfiguration")
    def anywhere_configuration(self) -> Optional['outputs.FleetAnywhereConfiguration']:
        """
        Configuration for Anywhere fleet.
        """
        return pulumi.get(self, "anywhere_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A human-readable description of a fleet.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="desiredEc2Instances")
    def desired_ec2_instances(self) -> Optional[int]:
        """
        [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        """
        return pulumi.get(self, "desired_ec2_instances")

    @property
    @pulumi.getter(name="ec2InboundPermissions")
    def ec2_inbound_permissions(self) -> Optional[Sequence['outputs.FleetIpPermission']]:
        """
        A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
        """
        return pulumi.get(self, "ec2_inbound_permissions")

    @property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> Optional[str]:
        """
        Unique fleet ID
        """
        return pulumi.get(self, "fleet_id")

    @property
    @pulumi.getter
    def locations(self) -> Optional[Sequence['outputs.FleetLocationConfiguration']]:
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[int]:
        """
        [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="metricGroups")
    def metric_groups(self) -> Optional[Sequence[str]]:
        """
        The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
        """
        return pulumi.get(self, "metric_groups")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[int]:
        """
        [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> Optional['FleetNewGameSessionProtectionPolicy']:
        """
        A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
        """
        return pulumi.get(self, "new_game_session_protection_policy")

    @property
    @pulumi.getter(name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(self) -> Optional['outputs.FleetResourceCreationLimitPolicy']:
        """
        A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
        """
        return pulumi.get(self, "resource_creation_limit_policy")

    @property
    @pulumi.getter(name="runtimeConfiguration")
    def runtime_configuration(self) -> Optional['outputs.FleetRuntimeConfiguration']:
        """
        Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.

        This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
        """
        return pulumi.get(self, "runtime_configuration")


class AwaitableGetFleetResult(GetFleetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetResult(
            anywhere_configuration=self.anywhere_configuration,
            description=self.description,
            desired_ec2_instances=self.desired_ec2_instances,
            ec2_inbound_permissions=self.ec2_inbound_permissions,
            fleet_id=self.fleet_id,
            locations=self.locations,
            max_size=self.max_size,
            metric_groups=self.metric_groups,
            min_size=self.min_size,
            name=self.name,
            new_game_session_protection_policy=self.new_game_session_protection_policy,
            resource_creation_limit_policy=self.resource_creation_limit_policy,
            runtime_configuration=self.runtime_configuration)


def get_fleet(fleet_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetResult:
    """
    The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.


    :param str fleet_id: Unique fleet ID
    """
    __args__ = dict()
    __args__['fleetId'] = fleet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getFleet', __args__, opts=opts, typ=GetFleetResult).value

    return AwaitableGetFleetResult(
        anywhere_configuration=pulumi.get(__ret__, 'anywhere_configuration'),
        description=pulumi.get(__ret__, 'description'),
        desired_ec2_instances=pulumi.get(__ret__, 'desired_ec2_instances'),
        ec2_inbound_permissions=pulumi.get(__ret__, 'ec2_inbound_permissions'),
        fleet_id=pulumi.get(__ret__, 'fleet_id'),
        locations=pulumi.get(__ret__, 'locations'),
        max_size=pulumi.get(__ret__, 'max_size'),
        metric_groups=pulumi.get(__ret__, 'metric_groups'),
        min_size=pulumi.get(__ret__, 'min_size'),
        name=pulumi.get(__ret__, 'name'),
        new_game_session_protection_policy=pulumi.get(__ret__, 'new_game_session_protection_policy'),
        resource_creation_limit_policy=pulumi.get(__ret__, 'resource_creation_limit_policy'),
        runtime_configuration=pulumi.get(__ret__, 'runtime_configuration'))


@_utilities.lift_output_func(get_fleet)
def get_fleet_output(fleet_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetResult]:
    """
    The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.


    :param str fleet_id: Unique fleet ID
    """
    ...
