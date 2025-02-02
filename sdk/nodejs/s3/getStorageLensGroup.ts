// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.
 */
export function getStorageLensGroup(args: GetStorageLensGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetStorageLensGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:s3:getStorageLensGroup", {
        "name": args.name,
    }, opts);
}

export interface GetStorageLensGroupArgs {
    name: string;
}

export interface GetStorageLensGroupResult {
    readonly filter?: outputs.s3.StorageLensGroupFilter;
    /**
     * The ARN for the Amazon S3 Storage Lens Group.
     */
    readonly storageLensGroupArn?: string;
    /**
     * A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.
 */
export function getStorageLensGroupOutput(args: GetStorageLensGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStorageLensGroupResult> {
    return pulumi.output(args).apply((a: any) => getStorageLensGroup(a, opts))
}

export interface GetStorageLensGroupOutputArgs {
    name: pulumi.Input<string>;
}
