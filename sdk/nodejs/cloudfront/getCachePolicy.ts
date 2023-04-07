// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::CachePolicy
 */
export function getCachePolicy(args: GetCachePolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetCachePolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudfront:getCachePolicy", {
        "id": args.id,
    }, opts);
}

export interface GetCachePolicyArgs {
    id: string;
}

export interface GetCachePolicyResult {
    readonly cachePolicyConfig?: outputs.cloudfront.CachePolicyConfig;
    readonly id?: string;
    readonly lastModifiedTime?: string;
}
/**
 * Resource Type definition for AWS::CloudFront::CachePolicy
 */
export function getCachePolicyOutput(args: GetCachePolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCachePolicyResult> {
    return pulumi.output(args).apply((a: any) => getCachePolicy(a, opts))
}

export interface GetCachePolicyOutputArgs {
    id: pulumi.Input<string>;
}
