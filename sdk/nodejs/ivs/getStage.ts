// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Definition for type AWS::IVS::Stage.
 */
export function getStage(args: GetStageArgs, opts?: pulumi.InvokeOptions): Promise<GetStageResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ivs:getStage", {
        "arn": args.arn,
    }, opts);
}

export interface GetStageArgs {
    /**
     * Stage ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: string;
}

export interface GetStageResult {
    /**
     * ID of the active session within the stage.
     */
    readonly activeSessionId?: string;
    /**
     * Stage ARN is automatically generated on creation and assigned as the unique identifier.
     */
    readonly arn?: string;
    /**
     * Stage name
     */
    readonly name?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Definition for type AWS::IVS::Stage.
 */
export function getStageOutput(args: GetStageOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStageResult> {
    return pulumi.output(args).apply((a: any) => getStage(a, opts))
}

export interface GetStageOutputArgs {
    /**
     * Stage ARN is automatically generated on creation and assigned as the unique identifier.
     */
    arn: pulumi.Input<string>;
}
