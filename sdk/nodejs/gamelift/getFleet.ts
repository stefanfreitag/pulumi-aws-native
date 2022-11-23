// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.
 */
export function getFleet(args: GetFleetArgs, opts?: pulumi.InvokeOptions): Promise<GetFleetResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:gamelift:getFleet", {
        "fleetId": args.fleetId,
    }, opts);
}

export interface GetFleetArgs {
    /**
     * Unique fleet ID
     */
    fleetId: string;
}

export interface GetFleetResult {
    /**
     * Configuration for Anywhere fleet.
     */
    readonly anywhereConfiguration?: outputs.gamelift.FleetAnywhereConfiguration;
    /**
     * A human-readable description of a fleet.
     */
    readonly description?: string;
    /**
     * [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
     */
    readonly desiredEC2Instances?: number;
    /**
     * A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
     */
    readonly eC2InboundPermissions?: outputs.gamelift.FleetIpPermission[];
    /**
     * Unique fleet ID
     */
    readonly fleetId?: string;
    readonly locations?: outputs.gamelift.FleetLocationConfiguration[];
    /**
     * [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
     */
    readonly maxSize?: number;
    /**
     * The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
     */
    readonly metricGroups?: string[];
    /**
     * [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
     */
    readonly minSize?: number;
    /**
     * A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
     */
    readonly name?: string;
    /**
     * A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
     */
    readonly newGameSessionProtectionPolicy?: enums.gamelift.FleetNewGameSessionProtectionPolicy;
    /**
     * A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
     */
    readonly resourceCreationLimitPolicy?: outputs.gamelift.FleetResourceCreationLimitPolicy;
    /**
     * Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
     *
     * This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
     */
    readonly runtimeConfiguration?: outputs.gamelift.FleetRuntimeConfiguration;
}

export function getFleetOutput(args: GetFleetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFleetResult> {
    return pulumi.output(args).apply(a => getFleet(a, opts))
}

export interface GetFleetOutputArgs {
    /**
     * Unique fleet ID
     */
    fleetId: pulumi.Input<string>;
}
