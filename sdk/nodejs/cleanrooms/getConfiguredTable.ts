// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents a table that can be associated with collaborations
 */
export function getConfiguredTable(args: GetConfiguredTableArgs, opts?: pulumi.InvokeOptions): Promise<GetConfiguredTableResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cleanrooms:getConfiguredTable", {
        "configuredTableIdentifier": args.configuredTableIdentifier,
    }, opts);
}

export interface GetConfiguredTableArgs {
    configuredTableIdentifier: string;
}

export interface GetConfiguredTableResult {
    readonly analysisRules?: outputs.cleanrooms.ConfiguredTableAnalysisRule[];
    readonly arn?: string;
    readonly configuredTableIdentifier?: string;
    readonly description?: string;
    readonly name?: string;
    /**
     * An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Represents a table that can be associated with collaborations
 */
export function getConfiguredTableOutput(args: GetConfiguredTableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetConfiguredTableResult> {
    return pulumi.output(args).apply((a: any) => getConfiguredTable(a, opts))
}

export interface GetConfiguredTableOutputArgs {
    configuredTableIdentifier: pulumi.Input<string>;
}
