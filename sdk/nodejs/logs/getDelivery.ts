// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * This structure contains information about one delivery in your account.
 *
 * A delivery is a connection between a logical delivery source and a logical delivery destination.
 *
 * For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).
 */
export function getDelivery(args: GetDeliveryArgs, opts?: pulumi.InvokeOptions): Promise<GetDeliveryResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:logs:getDelivery", {
        "deliveryId": args.deliveryId,
    }, opts);
}

export interface GetDeliveryArgs {
    /**
     * The unique ID that identifies this delivery in your account.
     */
    deliveryId: string;
}

export interface GetDeliveryResult {
    /**
     * The Amazon Resource Name (ARN) that uniquely identifies this delivery.
     */
    readonly arn?: string;
    /**
     * Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
     */
    readonly deliveryDestinationType?: string;
    /**
     * The unique ID that identifies this delivery in your account.
     */
    readonly deliveryId?: string;
    /**
     * The tags that have been assigned to this delivery.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * This structure contains information about one delivery in your account.
 *
 * A delivery is a connection between a logical delivery source and a logical delivery destination.
 *
 * For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).
 */
export function getDeliveryOutput(args: GetDeliveryOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDeliveryResult> {
    return pulumi.output(args).apply((a: any) => getDelivery(a, opts))
}

export interface GetDeliveryOutputArgs {
    /**
     * The unique ID that identifies this delivery in your account.
     */
    deliveryId: pulumi.Input<string>;
}
