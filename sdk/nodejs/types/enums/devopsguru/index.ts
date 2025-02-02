// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const NotificationChannelInsightSeverity = {
    Low: "LOW",
    Medium: "MEDIUM",
    High: "HIGH",
} as const;

/**
 * DevOps Guru Insight Severity Enum
 */
export type NotificationChannelInsightSeverity = (typeof NotificationChannelInsightSeverity)[keyof typeof NotificationChannelInsightSeverity];

export const NotificationChannelNotificationMessageType = {
    NewInsight: "NEW_INSIGHT",
    ClosedInsight: "CLOSED_INSIGHT",
    NewAssociation: "NEW_ASSOCIATION",
    SeverityUpgraded: "SEVERITY_UPGRADED",
    NewRecommendation: "NEW_RECOMMENDATION",
} as const;

/**
 * DevOps Guru NotificationMessageType Enum
 */
export type NotificationChannelNotificationMessageType = (typeof NotificationChannelNotificationMessageType)[keyof typeof NotificationChannelNotificationMessageType];

export const ResourceCollectionType = {
    AwsCloudFormation: "AWS_CLOUD_FORMATION",
    AwsTags: "AWS_TAGS",
} as const;

/**
 * The type of ResourceCollection
 */
export type ResourceCollectionType = (typeof ResourceCollectionType)[keyof typeof ResourceCollectionType];
