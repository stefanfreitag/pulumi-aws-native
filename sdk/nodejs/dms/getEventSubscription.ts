// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DMS::EventSubscription
 */
export function getEventSubscription(args: GetEventSubscriptionArgs, opts?: pulumi.InvokeOptions): Promise<GetEventSubscriptionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:dms:getEventSubscription", {
        "id": args.id,
    }, opts);
}

export interface GetEventSubscriptionArgs {
    id: string;
}

export interface GetEventSubscriptionResult {
    readonly enabled?: boolean;
    readonly eventCategories?: string[];
    readonly id?: string;
    readonly snsTopicArn?: string;
    readonly sourceType?: string;
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::DMS::EventSubscription
 */
export function getEventSubscriptionOutput(args: GetEventSubscriptionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEventSubscriptionResult> {
    return pulumi.output(args).apply((a: any) => getEventSubscription(a, opts))
}

export interface GetEventSubscriptionOutputArgs {
    id: pulumi.Input<string>;
}
