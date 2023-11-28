// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AccountPolicyPolicyType = {
    DataProtectionPolicy: "DATA_PROTECTION_POLICY",
} as const;

/**
 * Type of the policy.
 */
export type AccountPolicyPolicyType = (typeof AccountPolicyPolicyType)[keyof typeof AccountPolicyPolicyType];

export const AccountPolicyScope = {
    All: "ALL",
} as const;

/**
 * Scope for policy application
 */
export type AccountPolicyScope = (typeof AccountPolicyScope)[keyof typeof AccountPolicyScope];

export const LogAnomalyDetectorEvaluationFrequency = {
    FiveMin: "FIVE_MIN",
    TenMin: "TEN_MIN",
    FifteenMin: "FIFTEEN_MIN",
    ThirtyMin: "THIRTY_MIN",
    OneHour: "ONE_HOUR",
} as const;

/**
 * How often log group is evaluated
 */
export type LogAnomalyDetectorEvaluationFrequency = (typeof LogAnomalyDetectorEvaluationFrequency)[keyof typeof LogAnomalyDetectorEvaluationFrequency];

export const LogGroupClass = {
    Standard: "STANDARD",
    InfrequentAccess: "INFREQUENT_ACCESS",
} as const;

/**
 * The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS, with STANDARD being the default class
 */
export type LogGroupClass = (typeof LogGroupClass)[keyof typeof LogGroupClass];

export const MetricFilterMetricTransformationUnit = {
    Seconds: "Seconds",
    Microseconds: "Microseconds",
    Milliseconds: "Milliseconds",
    Bytes: "Bytes",
    Kilobytes: "Kilobytes",
    Megabytes: "Megabytes",
    Gigabytes: "Gigabytes",
    Terabytes: "Terabytes",
    Bits: "Bits",
    Kilobits: "Kilobits",
    Megabits: "Megabits",
    Gigabits: "Gigabits",
    Terabits: "Terabits",
    Percent: "Percent",
    Count: "Count",
    BytesSecond: "Bytes/Second",
    KilobytesSecond: "Kilobytes/Second",
    MegabytesSecond: "Megabytes/Second",
    GigabytesSecond: "Gigabytes/Second",
    TerabytesSecond: "Terabytes/Second",
    BitsSecond: "Bits/Second",
    KilobitsSecond: "Kilobits/Second",
    MegabitsSecond: "Megabits/Second",
    GigabitsSecond: "Gigabits/Second",
    TerabitsSecond: "Terabits/Second",
    CountSecond: "Count/Second",
    None: "None",
} as const;

/**
 * The unit to assign to the metric. If you omit this, the unit is set as None.
 */
export type MetricFilterMetricTransformationUnit = (typeof MetricFilterMetricTransformationUnit)[keyof typeof MetricFilterMetricTransformationUnit];

export const SubscriptionFilterDistribution = {
    Random: "Random",
    ByLogStream: "ByLogStream",
} as const;

/**
 * The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.
 */
export type SubscriptionFilterDistribution = (typeof SubscriptionFilterDistribution)[keyof typeof SubscriptionFilterDistribution];
