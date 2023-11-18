// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AddonResolveConflicts = {
    None: "NONE",
    Overwrite: "OVERWRITE",
    Preserve: "PRESERVE",
} as const;

/**
 * Resolve parameter value conflicts
 */
export type AddonResolveConflicts = (typeof AddonResolveConflicts)[keyof typeof AddonResolveConflicts];

export const ClusterAccessConfigAuthenticationMode = {
    ConfigMap: "CONFIG_MAP",
    ApiAndConfigMap: "API_AND_CONFIG_MAP",
    Api: "API",
} as const;

/**
 * Specify the authentication mode that should be used to create your cluster.
 */
export type ClusterAccessConfigAuthenticationMode = (typeof ClusterAccessConfigAuthenticationMode)[keyof typeof ClusterAccessConfigAuthenticationMode];

export const ClusterKubernetesNetworkConfigIpFamily = {
    Ipv4: "ipv4",
    Ipv6: "ipv6",
} as const;

/**
 * Ipv4 or Ipv6. You can only specify ipv6 for 1.21 and later clusters that use version 1.10.1 or later of the Amazon VPC CNI add-on
 */
export type ClusterKubernetesNetworkConfigIpFamily = (typeof ClusterKubernetesNetworkConfigIpFamily)[keyof typeof ClusterKubernetesNetworkConfigIpFamily];

export const ClusterLoggingTypeConfigType = {
    Api: "api",
    Audit: "audit",
    Authenticator: "authenticator",
    ControllerManager: "controllerManager",
    Scheduler: "scheduler",
} as const;

/**
 * name of the log type
 */
export type ClusterLoggingTypeConfigType = (typeof ClusterLoggingTypeConfigType)[keyof typeof ClusterLoggingTypeConfigType];

export const IdentityProviderConfigType = {
    Oidc: "oidc",
} as const;

/**
 * The type of the identity provider configuration.
 */
export type IdentityProviderConfigType = (typeof IdentityProviderConfigType)[keyof typeof IdentityProviderConfigType];
