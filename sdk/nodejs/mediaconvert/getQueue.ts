// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MediaConvert::Queue
 */
export function getQueue(args: GetQueueArgs, opts?: pulumi.InvokeOptions): Promise<GetQueueResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:mediaconvert:getQueue", {
        "id": args.id,
    }, opts);
}

export interface GetQueueArgs {
    id: string;
}

export interface GetQueueResult {
    readonly arn?: string;
    readonly description?: string;
    readonly id?: string;
    readonly pricingPlan?: string;
    readonly status?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Queue` for more information about the expected schema for this property.
     */
    readonly tags?: any;
}
/**
 * Resource Type definition for AWS::MediaConvert::Queue
 */
export function getQueueOutput(args: GetQueueOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetQueueResult> {
    return pulumi.output(args).apply((a: any) => getQueue(a, opts))
}

export interface GetQueueOutputArgs {
    id: pulumi.Input<string>;
}
