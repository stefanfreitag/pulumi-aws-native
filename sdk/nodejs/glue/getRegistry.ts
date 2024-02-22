// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * This resource creates a Registry for authoring schemas as part of Glue Schema Registry.
 */
export function getRegistry(args: GetRegistryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:glue:getRegistry", {
        "arn": args.arn,
    }, opts);
}

export interface GetRegistryArgs {
    /**
     * Amazon Resource Name for the created Registry.
     */
    arn: string;
}

export interface GetRegistryResult {
    /**
     * Amazon Resource Name for the created Registry.
     */
    readonly arn?: string;
    /**
     * A description of the registry. If description is not provided, there will not be any default value for this.
     */
    readonly description?: string;
    /**
     * List of tags to tag the Registry
     */
    readonly tags?: outputs.Tag[];
}
/**
 * This resource creates a Registry for authoring schemas as part of Glue Schema Registry.
 */
export function getRegistryOutput(args: GetRegistryOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRegistryResult> {
    return pulumi.output(args).apply((a: any) => getRegistry(a, opts))
}

export interface GetRegistryOutputArgs {
    /**
     * Amazon Resource Name for the created Registry.
     */
    arn: pulumi.Input<string>;
}
