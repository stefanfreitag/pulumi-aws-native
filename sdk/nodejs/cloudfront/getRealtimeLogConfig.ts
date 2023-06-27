// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::RealtimeLogConfig
 */
export function getRealtimeLogConfig(args: GetRealtimeLogConfigArgs, opts?: pulumi.InvokeOptions): Promise<GetRealtimeLogConfigResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudfront:getRealtimeLogConfig", {
        "arn": args.arn,
    }, opts);
}

export interface GetRealtimeLogConfigArgs {
    arn: string;
}

export interface GetRealtimeLogConfigResult {
    readonly arn?: string;
    readonly endPoints?: outputs.cloudfront.RealtimeLogConfigEndPoint[];
    readonly fields?: string[];
    readonly samplingRate?: number;
}
/**
 * Resource Type definition for AWS::CloudFront::RealtimeLogConfig
 */
export function getRealtimeLogConfigOutput(args: GetRealtimeLogConfigOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRealtimeLogConfigResult> {
    return pulumi.output(args).apply((a: any) => getRealtimeLogConfig(a, opts))
}

export interface GetRealtimeLogConfigOutputArgs {
    arn: pulumi.Input<string>;
}
