// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::TableOptimizer
 */
export function getTableOptimizer(args: GetTableOptimizerArgs, opts?: pulumi.InvokeOptions): Promise<GetTableOptimizerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:glue:getTableOptimizer", {
        "id": args.id,
    }, opts);
}

export interface GetTableOptimizerArgs {
    id: string;
}

export interface GetTableOptimizerResult {
    readonly id?: string;
    readonly tableOptimizerConfiguration?: outputs.glue.TableOptimizerConfiguration;
}
/**
 * Resource Type definition for AWS::Glue::TableOptimizer
 */
export function getTableOptimizerOutput(args: GetTableOptimizerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTableOptimizerResult> {
    return pulumi.output(args).apply((a: any) => getTableOptimizer(a, opts))
}

export interface GetTableOptimizerOutputArgs {
    id: pulumi.Input<string>;
}
