// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for StateMachine
 */
export function getStateMachine(args: GetStateMachineArgs, opts?: pulumi.InvokeOptions): Promise<GetStateMachineResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:stepfunctions:getStateMachine", {
        "arn": args.arn,
    }, opts);
}

export interface GetStateMachineArgs {
    arn: string;
}

export interface GetStateMachineResult {
    readonly arn?: string;
    readonly definitionString?: string;
    readonly loggingConfiguration?: outputs.stepfunctions.StateMachineLoggingConfiguration;
    readonly name?: string;
    readonly roleArn?: string;
    readonly stateMachineRevisionId?: string;
    readonly tags?: outputs.Tag[];
    readonly tracingConfiguration?: outputs.stepfunctions.StateMachineTracingConfiguration;
}
/**
 * Resource schema for StateMachine
 */
export function getStateMachineOutput(args: GetStateMachineOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStateMachineResult> {
    return pulumi.output(args).apply((a: any) => getStateMachine(a, opts))
}

export interface GetStateMachineOutputArgs {
    arn: pulumi.Input<string>;
}
