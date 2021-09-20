// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AliasRoutingStrategyType = {
    Simple: "SIMPLE",
    Terminal: "TERMINAL",
} as const;

/**
 * Simple routing strategy. The alias resolves to one specific fleet. Use this type when routing to active fleets.
 */
export type AliasRoutingStrategyType = (typeof AliasRoutingStrategyType)[keyof typeof AliasRoutingStrategyType];

export const FleetCertificateConfigurationCertificateType = {
    Disabled: "DISABLED",
    Generated: "GENERATED",
} as const;

export type FleetCertificateConfigurationCertificateType = (typeof FleetCertificateConfigurationCertificateType)[keyof typeof FleetCertificateConfigurationCertificateType];

export const FleetFleetType = {
    OnDemand: "ON_DEMAND",
    Spot: "SPOT",
} as const;

/**
 * Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
 */
export type FleetFleetType = (typeof FleetFleetType)[keyof typeof FleetFleetType];

export const FleetIpPermissionProtocol = {
    Tcp: "TCP",
    Udp: "UDP",
} as const;

/**
 * The network communication protocol used by the fleet.
 */
export type FleetIpPermissionProtocol = (typeof FleetIpPermissionProtocol)[keyof typeof FleetIpPermissionProtocol];

export const FleetNewGameSessionProtectionPolicy = {
    FullProtection: "FullProtection",
    NoProtection: "NoProtection",
} as const;

/**
 * A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
 */
export type FleetNewGameSessionProtectionPolicy = (typeof FleetNewGameSessionProtectionPolicy)[keyof typeof FleetNewGameSessionProtectionPolicy];

export const GameServerGroupBalancingStrategy = {
    SpotOnly: "SPOT_ONLY",
    SpotPreferred: "SPOT_PREFERRED",
    OnDemandOnly: "ON_DEMAND_ONLY",
} as const;

/**
 * The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
 */
export type GameServerGroupBalancingStrategy = (typeof GameServerGroupBalancingStrategy)[keyof typeof GameServerGroupBalancingStrategy];

export const GameServerGroupDeleteOption = {
    SafeDelete: "SAFE_DELETE",
    ForceDelete: "FORCE_DELETE",
    Retain: "RETAIN",
} as const;

/**
 * The type of delete to perform.
 */
export type GameServerGroupDeleteOption = (typeof GameServerGroupDeleteOption)[keyof typeof GameServerGroupDeleteOption];

export const GameServerGroupGameServerProtectionPolicy = {
    NoProtection: "NO_PROTECTION",
    FullProtection: "FULL_PROTECTION",
} as const;

/**
 * A flag that indicates whether instances in the game server group are protected from early termination.
 */
export type GameServerGroupGameServerProtectionPolicy = (typeof GameServerGroupGameServerProtectionPolicy)[keyof typeof GameServerGroupGameServerProtectionPolicy];
