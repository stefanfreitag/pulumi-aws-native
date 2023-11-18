// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.
 */
export function getEventDataStore(args: GetEventDataStoreArgs, opts?: pulumi.InvokeOptions): Promise<GetEventDataStoreResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudtrail:getEventDataStore", {
        "eventDataStoreArn": args.eventDataStoreArn,
    }, opts);
}

export interface GetEventDataStoreArgs {
    /**
     * The ARN of the event data store.
     */
    eventDataStoreArn: string;
}

export interface GetEventDataStoreResult {
    /**
     * The advanced event selectors that were used to select events for the data store.
     */
    readonly advancedEventSelectors?: outputs.cloudtrail.EventDataStoreAdvancedEventSelector[];
    /**
     * The mode that the event data store will use to charge for event storage.
     */
    readonly billingMode?: string;
    /**
     * The timestamp of the event data store's creation.
     */
    readonly createdTimestamp?: string;
    /**
     * The ARN of the event data store.
     */
    readonly eventDataStoreArn?: string;
    /**
     * Indicates whether the event data store is ingesting events.
     */
    readonly ingestionEnabled?: boolean;
    /**
     * Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.
     */
    readonly insightSelectors?: outputs.cloudtrail.EventDataStoreInsightSelector[];
    /**
     * Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store
     */
    readonly insightsDestination?: string;
    /**
     * Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
     */
    readonly kmsKeyId?: string;
    /**
     * Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
     */
    readonly multiRegionEnabled?: boolean;
    /**
     * The name of the event data store.
     */
    readonly name?: string;
    /**
     * Indicates that an event data store is collecting logged events for an organization.
     */
    readonly organizationEnabled?: boolean;
    /**
     * The retention period, in days.
     */
    readonly retentionPeriod?: number;
    /**
     * The status of an event data store. Values are STARTING_INGESTION, ENABLED, STOPPING_INGESTION, STOPPED_INGESTION and PENDING_DELETION.
     */
    readonly status?: string;
    readonly tags?: outputs.cloudtrail.EventDataStoreTag[];
    /**
     * Indicates whether the event data store is protected from termination.
     */
    readonly terminationProtectionEnabled?: boolean;
    /**
     * The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
     */
    readonly updatedTimestamp?: string;
}
/**
 * A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.
 */
export function getEventDataStoreOutput(args: GetEventDataStoreOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEventDataStoreResult> {
    return pulumi.output(args).apply((a: any) => getEventDataStore(a, opts))
}

export interface GetEventDataStoreOutputArgs {
    /**
     * The ARN of the event data store.
     */
    eventDataStoreArn: pulumi.Input<string>;
}
