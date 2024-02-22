// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Rekognition::Collection type creates an Amazon Rekognition Collection. A collection is a logical grouping of information about detected faces which can later be referenced for searches on the group
 */
export function getCollection(args: GetCollectionArgs, opts?: pulumi.InvokeOptions): Promise<GetCollectionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rekognition:getCollection", {
        "collectionId": args.collectionId,
    }, opts);
}

export interface GetCollectionArgs {
    collectionId: string;
}

export interface GetCollectionResult {
    readonly arn?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::Rekognition::Collection type creates an Amazon Rekognition Collection. A collection is a logical grouping of information about detected faces which can later be referenced for searches on the group
 */
export function getCollectionOutput(args: GetCollectionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCollectionResult> {
    return pulumi.output(args).apply((a: any) => getCollection(a, opts))
}

export interface GetCollectionOutputArgs {
    collectionId: pulumi.Input<string>;
}
