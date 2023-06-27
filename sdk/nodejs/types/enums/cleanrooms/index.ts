// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const CollaborationMemberAbility = {
    CanQuery: "CAN_QUERY",
    CanReceiveResults: "CAN_RECEIVE_RESULTS",
} as const;

export type CollaborationMemberAbility = (typeof CollaborationMemberAbility)[keyof typeof CollaborationMemberAbility];

export const CollaborationQueryLogStatus = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type CollaborationQueryLogStatus = (typeof CollaborationQueryLogStatus)[keyof typeof CollaborationQueryLogStatus];

export const ConfiguredTableAnalysisMethod = {
    DirectQuery: "DIRECT_QUERY",
} as const;

export type ConfiguredTableAnalysisMethod = (typeof ConfiguredTableAnalysisMethod)[keyof typeof ConfiguredTableAnalysisMethod];

export const ConfiguredTableAnalysisRuleType = {
    Aggregation: "AGGREGATION",
    List: "LIST",
} as const;

export type ConfiguredTableAnalysisRuleType = (typeof ConfiguredTableAnalysisRuleType)[keyof typeof ConfiguredTableAnalysisRuleType];

export const MembershipQueryLogStatus = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type MembershipQueryLogStatus = (typeof MembershipQueryLogStatus)[keyof typeof MembershipQueryLogStatus];
