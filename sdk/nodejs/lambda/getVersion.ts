// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lambda::Version
 */
export function getVersion(args: GetVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetVersionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:lambda:getVersion", {
        "functionArn": args.functionArn,
    }, opts);
}

export interface GetVersionArgs {
    /**
     * The ARN of the version.
     */
    functionArn: string;
}

export interface GetVersionResult {
    /**
     * The ARN of the version.
     */
    readonly functionArn?: string;
    /**
     * The version number.
     */
    readonly version?: string;
}
/**
 * Resource Type definition for AWS::Lambda::Version
 */
export function getVersionOutput(args: GetVersionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVersionResult> {
    return pulumi.output(args).apply((a: any) => getVersion(a, opts))
}

export interface GetVersionOutputArgs {
    /**
     * The ARN of the version.
     */
    functionArn: pulumi.Input<string>;
}
