// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElastiCache::ParameterGroup
 */
export function getParameterGroup(args: GetParameterGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetParameterGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticache:getParameterGroup", {
        "id": args.id,
    }, opts);
}

export interface GetParameterGroupArgs {
    id: string;
}

export interface GetParameterGroupResult {
    readonly description?: string;
    readonly id?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ElastiCache::ParameterGroup` for more information about the expected schema for this property.
     */
    readonly properties?: any;
    readonly tags?: outputs.elasticache.ParameterGroupTag[];
}
/**
 * Resource Type definition for AWS::ElastiCache::ParameterGroup
 */
export function getParameterGroupOutput(args: GetParameterGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetParameterGroupResult> {
    return pulumi.output(args).apply((a: any) => getParameterGroup(a, opts))
}

export interface GetParameterGroupOutputArgs {
    id: pulumi.Input<string>;
}
