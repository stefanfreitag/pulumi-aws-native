// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network.
 */
export function getAccessLogSubscription(args: GetAccessLogSubscriptionArgs, opts?: pulumi.InvokeOptions): Promise<GetAccessLogSubscriptionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:vpclattice:getAccessLogSubscription", {
        "arn": args.arn,
    }, opts);
}

export interface GetAccessLogSubscriptionArgs {
    arn: string;
}

export interface GetAccessLogSubscriptionResult {
    readonly arn?: string;
    readonly destinationArn?: string;
    readonly id?: string;
    readonly resourceArn?: string;
    readonly resourceId?: string;
    readonly tags?: outputs.Tag[];
}
/**
 * Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network.
 */
export function getAccessLogSubscriptionOutput(args: GetAccessLogSubscriptionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAccessLogSubscriptionResult> {
    return pulumi.output(args).apply((a: any) => getAccessLogSubscription(a, opts))
}

export interface GetAccessLogSubscriptionOutputArgs {
    arn: pulumi.Input<string>;
}
