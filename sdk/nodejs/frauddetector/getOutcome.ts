// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An outcome for rule evaluation.
 */
export function getOutcome(args: GetOutcomeArgs, opts?: pulumi.InvokeOptions): Promise<GetOutcomeResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:frauddetector:getOutcome", {
        "arn": args.arn,
    }, opts);
}

export interface GetOutcomeArgs {
    /**
     * The outcome ARN.
     */
    arn: string;
}

export interface GetOutcomeResult {
    /**
     * The outcome ARN.
     */
    readonly arn?: string;
    /**
     * The timestamp when the outcome was created.
     */
    readonly createdTime?: string;
    /**
     * The outcome description.
     */
    readonly description?: string;
    /**
     * The timestamp when the outcome was last updated.
     */
    readonly lastUpdatedTime?: string;
    /**
     * Tags associated with this outcome.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * An outcome for rule evaluation.
 */
export function getOutcomeOutput(args: GetOutcomeOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOutcomeResult> {
    return pulumi.output(args).apply((a: any) => getOutcome(a, opts))
}

export interface GetOutcomeOutputArgs {
    /**
     * The outcome ARN.
     */
    arn: pulumi.Input<string>;
}
