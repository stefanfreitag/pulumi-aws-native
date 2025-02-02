// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export function getIntegration(args: GetIntegrationArgs, opts?: pulumi.InvokeOptions): Promise<GetIntegrationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rds:getIntegration", {
        "integrationArn": args.integrationArn,
    }, opts);
}

export interface GetIntegrationArgs {
    /**
     * The ARN of the integration.
     */
    integrationArn: string;
}

export interface GetIntegrationResult {
    readonly createTime?: string;
    /**
     * The ARN of the integration.
     */
    readonly integrationArn?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export function getIntegrationOutput(args: GetIntegrationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIntegrationResult> {
    return pulumi.output(args).apply((a: any) => getIntegration(a, opts))
}

export interface GetIntegrationOutputArgs {
    /**
     * The ARN of the integration.
     */
    integrationArn: pulumi.Input<string>;
}
