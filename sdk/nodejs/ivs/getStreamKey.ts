// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IVS::StreamKey
 */
export function getStreamKey(args: GetStreamKeyArgs, opts?: pulumi.InvokeOptions): Promise<GetStreamKeyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ivs:getStreamKey", {
        "arn": args.arn,
    }, opts);
}

export interface GetStreamKeyArgs {
    /**
     * Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: string;
}

export interface GetStreamKeyResult {
    /**
     * Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
     */
    readonly arn?: string;
    /**
     * A list of key-value pairs that contain metadata for the asset model.
     */
    readonly tags?: outputs.Tag[];
    /**
     * Stream-key value.
     */
    readonly value?: string;
}
/**
 * Resource Type definition for AWS::IVS::StreamKey
 */
export function getStreamKeyOutput(args: GetStreamKeyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStreamKeyResult> {
    return pulumi.output(args).apply((a: any) => getStreamKey(a, opts))
}

export interface GetStreamKeyOutputArgs {
    /**
     * Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: pulumi.Input<string>;
}
