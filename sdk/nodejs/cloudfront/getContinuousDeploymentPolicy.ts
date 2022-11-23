// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::ContinuousDeploymentPolicy
 */
export function getContinuousDeploymentPolicy(args: GetContinuousDeploymentPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetContinuousDeploymentPolicyResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:cloudfront:getContinuousDeploymentPolicy", {
        "id": args.id,
    }, opts);
}

export interface GetContinuousDeploymentPolicyArgs {
    id: string;
}

export interface GetContinuousDeploymentPolicyResult {
    readonly continuousDeploymentPolicyConfig?: outputs.cloudfront.ContinuousDeploymentPolicyConfig;
    readonly id?: string;
    readonly lastModifiedTime?: string;
}

export function getContinuousDeploymentPolicyOutput(args: GetContinuousDeploymentPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetContinuousDeploymentPolicyResult> {
    return pulumi.output(args).apply(a => getContinuousDeploymentPolicy(a, opts))
}

export interface GetContinuousDeploymentPolicyOutputArgs {
    id: pulumi.Input<string>;
}
