// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const BridgeFailoverConfigStateEnum = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type BridgeFailoverConfigStateEnum = (typeof BridgeFailoverConfigStateEnum)[keyof typeof BridgeFailoverConfigStateEnum];

export const BridgeFailoverModeEnum = {
    Failover: "FAILOVER",
} as const;

export type BridgeFailoverModeEnum = (typeof BridgeFailoverModeEnum)[keyof typeof BridgeFailoverModeEnum];

export const BridgeOutputResourceBridgeNetworkOutputProtocol = {
    RtpFec: "rtp-fec",
    Rtp: "rtp",
    Udp: "udp",
} as const;

/**
 * The network output protocol.
 */
export type BridgeOutputResourceBridgeNetworkOutputProtocol = (typeof BridgeOutputResourceBridgeNetworkOutputProtocol)[keyof typeof BridgeOutputResourceBridgeNetworkOutputProtocol];

export const BridgeProtocolEnum = {
    RtpFec: "rtp-fec",
    Rtp: "rtp",
    Udp: "udp",
} as const;

export type BridgeProtocolEnum = (typeof BridgeProtocolEnum)[keyof typeof BridgeProtocolEnum];

export const BridgeSourceProtocolEnum = {
    RtpFec: "rtp-fec",
    Rtp: "rtp",
    Udp: "udp",
} as const;

export type BridgeSourceProtocolEnum = (typeof BridgeSourceProtocolEnum)[keyof typeof BridgeSourceProtocolEnum];

export const BridgeStateEnum = {
    Creating: "CREATING",
    Standby: "STANDBY",
    Starting: "STARTING",
    Deploying: "DEPLOYING",
    Active: "ACTIVE",
    Stopping: "STOPPING",
    Deleting: "DELETING",
    Deleted: "DELETED",
    StartFailed: "START_FAILED",
    StartPending: "START_PENDING",
    Updating: "UPDATING",
} as const;

export type BridgeStateEnum = (typeof BridgeStateEnum)[keyof typeof BridgeStateEnum];

export const FlowEncryptionAlgorithm = {
    Aes128: "aes128",
    Aes192: "aes192",
    Aes256: "aes256",
} as const;

/**
 * The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
 */
export type FlowEncryptionAlgorithm = (typeof FlowEncryptionAlgorithm)[keyof typeof FlowEncryptionAlgorithm];

export const FlowEncryptionKeyType = {
    Speke: "speke",
    StaticKey: "static-key",
    SrtPassword: "srt-password",
} as const;

/**
 * The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
 */
export type FlowEncryptionKeyType = (typeof FlowEncryptionKeyType)[keyof typeof FlowEncryptionKeyType];

export const FlowEntitlementEncryptionAlgorithm = {
    Aes128: "aes128",
    Aes192: "aes192",
    Aes256: "aes256",
} as const;

/**
 * The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
 */
export type FlowEntitlementEncryptionAlgorithm = (typeof FlowEntitlementEncryptionAlgorithm)[keyof typeof FlowEntitlementEncryptionAlgorithm];

export const FlowEntitlementEncryptionKeyType = {
    Speke: "speke",
    StaticKey: "static-key",
} as const;

/**
 * The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
 */
export type FlowEntitlementEncryptionKeyType = (typeof FlowEntitlementEncryptionKeyType)[keyof typeof FlowEntitlementEncryptionKeyType];

export const FlowEntitlementEntitlementStatus = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

/**
 *  An indication of whether the entitlement is enabled.
 */
export type FlowEntitlementEntitlementStatus = (typeof FlowEntitlementEntitlementStatus)[keyof typeof FlowEntitlementEntitlementStatus];

export const FlowFailoverConfigFailoverMode = {
    Merge: "MERGE",
    Failover: "FAILOVER",
} as const;

/**
 * The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.
 */
export type FlowFailoverConfigFailoverMode = (typeof FlowFailoverConfigFailoverMode)[keyof typeof FlowFailoverConfigFailoverMode];

export const FlowFailoverConfigState = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type FlowFailoverConfigState = (typeof FlowFailoverConfigState)[keyof typeof FlowFailoverConfigState];

export const FlowOutputEncryptionAlgorithm = {
    Aes128: "aes128",
    Aes192: "aes192",
    Aes256: "aes256",
} as const;

/**
 * The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
 */
export type FlowOutputEncryptionAlgorithm = (typeof FlowOutputEncryptionAlgorithm)[keyof typeof FlowOutputEncryptionAlgorithm];

export const FlowOutputEncryptionKeyType = {
    StaticKey: "static-key",
    SrtPassword: "srt-password",
} as const;

/**
 * The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
 */
export type FlowOutputEncryptionKeyType = (typeof FlowOutputEncryptionKeyType)[keyof typeof FlowOutputEncryptionKeyType];

export const FlowOutputProtocol = {
    ZixiPush: "zixi-push",
    RtpFec: "rtp-fec",
    Rtp: "rtp",
    ZixiPull: "zixi-pull",
    Rist: "rist",
    FujitsuQos: "fujitsu-qos",
    SrtListener: "srt-listener",
    SrtCaller: "srt-caller",
} as const;

/**
 * The protocol that is used by the source or output.
 */
export type FlowOutputProtocol = (typeof FlowOutputProtocol)[keyof typeof FlowOutputProtocol];

export const FlowSourceEncryptionAlgorithm = {
    Aes128: "aes128",
    Aes192: "aes192",
    Aes256: "aes256",
} as const;

/**
 * The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
 */
export type FlowSourceEncryptionAlgorithm = (typeof FlowSourceEncryptionAlgorithm)[keyof typeof FlowSourceEncryptionAlgorithm];

export const FlowSourceEncryptionKeyType = {
    Speke: "speke",
    StaticKey: "static-key",
    SrtPassword: "srt-password",
} as const;

/**
 * The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
 */
export type FlowSourceEncryptionKeyType = (typeof FlowSourceEncryptionKeyType)[keyof typeof FlowSourceEncryptionKeyType];

export const FlowSourceProtocol = {
    ZixiPush: "zixi-push",
    RtpFec: "rtp-fec",
    Rtp: "rtp",
    Rist: "rist",
    FujitsuQos: "fujitsu-qos",
    SrtListener: "srt-listener",
    SrtCaller: "srt-caller",
} as const;

/**
 * The protocol that is used by the source.
 */
export type FlowSourceProtocol = (typeof FlowSourceProtocol)[keyof typeof FlowSourceProtocol];

export const GatewayState = {
    Creating: "CREATING",
    Active: "ACTIVE",
    Updating: "UPDATING",
    Error: "ERROR",
    Deleting: "DELETING",
    Deleted: "DELETED",
} as const;

/**
 * The current status of the gateway.
 */
export type GatewayState = (typeof GatewayState)[keyof typeof GatewayState];
