// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Events::ApiDestination.
 */
export function getApiDestination(args: GetApiDestinationArgs, opts?: pulumi.InvokeOptions): Promise<GetApiDestinationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:events:getApiDestination", {
        "name": args.name,
    }, opts);
}

export interface GetApiDestinationArgs {
    /**
     * Name of the apiDestination.
     */
    name: string;
}

export interface GetApiDestinationResult {
    /**
     * The arn of the api destination.
     */
    readonly arn?: string;
    /**
     * The arn of the connection.
     */
    readonly connectionArn?: string;
    readonly description?: string;
    readonly httpMethod?: enums.events.ApiDestinationHttpMethod;
    /**
     * Url endpoint to invoke.
     */
    readonly invocationEndpoint?: string;
    readonly invocationRateLimitPerSecond?: number;
}
/**
 * Resource Type definition for AWS::Events::ApiDestination.
 */
export function getApiDestinationOutput(args: GetApiDestinationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApiDestinationResult> {
    return pulumi.output(args).apply((a: any) => getApiDestination(a, opts))
}

export interface GetApiDestinationOutputArgs {
    /**
     * Name of the apiDestination.
     */
    name: pulumi.Input<string>;
}
