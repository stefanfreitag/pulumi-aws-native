// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Document Classifier enables training document classifier models.
 */
export function getDocumentClassifier(args: GetDocumentClassifierArgs, opts?: pulumi.InvokeOptions): Promise<GetDocumentClassifierResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:comprehend:getDocumentClassifier", {
        "arn": args.arn,
    }, opts);
}

export interface GetDocumentClassifierArgs {
    arn: string;
}

export interface GetDocumentClassifierResult {
    readonly arn?: string;
    readonly modelPolicy?: string;
    readonly tags?: outputs.Tag[];
}
/**
 * Document Classifier enables training document classifier models.
 */
export function getDocumentClassifierOutput(args: GetDocumentClassifierOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDocumentClassifierResult> {
    return pulumi.output(args).apply((a: any) => getDocumentClassifier(a, opts))
}

export interface GetDocumentClassifierOutputArgs {
    arn: pulumi.Input<string>;
}
