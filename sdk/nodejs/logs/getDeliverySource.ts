// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 *  A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
 *
 * Only some AWS services support being configured as a delivery source. These services are listed as Supported [V2 Permissions] in the table at [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).
 */
export function getDeliverySource(args: GetDeliverySourceArgs, opts?: pulumi.InvokeOptions): Promise<GetDeliverySourceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:logs:getDeliverySource", {
        "name": args.name,
    }, opts);
}

export interface GetDeliverySourceArgs {
    /**
     * The unique name of the Log source.
     */
    name: string;
}

export interface GetDeliverySourceResult {
    /**
     * The Amazon Resource Name (ARN) that uniquely identifies this delivery source.
     */
    readonly arn?: string;
    /**
     * The type of logs being delivered. Only mandatory when the resourceArn could match more than one. In such a case, the error message will contain all the possible options.
     */
    readonly logType?: string;
    /**
     * This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.
     */
    readonly resourceArns?: string[];
    /**
     * The AWS service that is sending logs.
     */
    readonly service?: string;
    /**
     * The tags that have been assigned to this delivery source.
     */
    readonly tags?: outputs.Tag[];
}
/**
 *  A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
 *
 * Only some AWS services support being configured as a delivery source. These services are listed as Supported [V2 Permissions] in the table at [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).
 */
export function getDeliverySourceOutput(args: GetDeliverySourceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDeliverySourceResult> {
    return pulumi.output(args).apply((a: any) => getDeliverySource(a, opts))
}

export interface GetDeliverySourceOutputArgs {
    /**
     * The unique name of the Log source.
     */
    name: pulumi.Input<string>;
}
