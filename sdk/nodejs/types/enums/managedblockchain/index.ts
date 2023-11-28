// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AccessorNetworkAccessorType = {
    EthereumGoerli: "ETHEREUM_GOERLI",
    EthereumMainnet: "ETHEREUM_MAINNET",
    EthereumMainnetAndGoerli: "ETHEREUM_MAINNET_AND_GOERLI",
    PolygonMainnet: "POLYGON_MAINNET",
    PolygonMumbai: "POLYGON_MUMBAI",
} as const;

export type AccessorNetworkAccessorType = (typeof AccessorNetworkAccessorType)[keyof typeof AccessorNetworkAccessorType];

export const AccessorStatus = {
    Available: "AVAILABLE",
    PendingDeletion: "PENDING_DELETION",
    Deleted: "DELETED",
} as const;

export type AccessorStatus = (typeof AccessorStatus)[keyof typeof AccessorStatus];

export const AccessorType = {
    BillingToken: "BILLING_TOKEN",
} as const;

export type AccessorType = (typeof AccessorType)[keyof typeof AccessorType];
