// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.
 */
export function getEventInvokeConfig(args: GetEventInvokeConfigArgs, opts?: pulumi.InvokeOptions): Promise<GetEventInvokeConfigResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:lambda:getEventInvokeConfig", {
        "functionName": args.functionName,
        "qualifier": args.qualifier,
    }, opts);
}

export interface GetEventInvokeConfigArgs {
    /**
     * The name of the Lambda function.
     */
    functionName: string;
    /**
     * The identifier of a version or alias.
     */
    qualifier: string;
}

export interface GetEventInvokeConfigResult {
    readonly destinationConfig?: outputs.lambda.EventInvokeConfigDestinationConfig;
    /**
     * The maximum age of a request that Lambda sends to a function for processing.
     */
    readonly maximumEventAgeInSeconds?: number;
    /**
     * The maximum number of times to retry when the function returns an error.
     */
    readonly maximumRetryAttempts?: number;
}
/**
 * The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.
 */
export function getEventInvokeConfigOutput(args: GetEventInvokeConfigOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEventInvokeConfigResult> {
    return pulumi.output(args).apply((a: any) => getEventInvokeConfig(a, opts))
}

export interface GetEventInvokeConfigOutputArgs {
    /**
     * The name of the Lambda function.
     */
    functionName: pulumi.Input<string>;
    /**
     * The identifier of a version or alias.
     */
    qualifier: pulumi.Input<string>;
}
