// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const UsagePlanKeyKeyType = {
    ApiKey: "API_KEY",
} as const;

/**
 * The type of usage plan key. Currently, the only valid key type is API_KEY.
 */
export type UsagePlanKeyKeyType = (typeof UsagePlanKeyKeyType)[keyof typeof UsagePlanKeyKeyType];
