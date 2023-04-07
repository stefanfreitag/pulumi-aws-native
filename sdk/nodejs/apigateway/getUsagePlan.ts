// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGateway::UsagePlan
 */
export function getUsagePlan(args: GetUsagePlanArgs, opts?: pulumi.InvokeOptions): Promise<GetUsagePlanResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigateway:getUsagePlan", {
        "id": args.id,
    }, opts);
}

export interface GetUsagePlanArgs {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    id: string;
}

export interface GetUsagePlanResult {
    /**
     * The API stages to associate with this usage plan.
     */
    readonly apiStages?: outputs.apigateway.UsagePlanApiStage[];
    /**
     * A description of the usage plan.
     */
    readonly description?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id?: string;
    /**
     * Configures the number of requests that users can make within a given interval.
     */
    readonly quota?: outputs.apigateway.UsagePlanQuotaSettings;
    /**
     * An array of arbitrary tags (key-value pairs) to associate with the usage plan.
     */
    readonly tags?: outputs.apigateway.UsagePlanTag[];
    /**
     * Configures the overall request rate (average requests per second) and burst capacity.
     */
    readonly throttle?: outputs.apigateway.UsagePlanThrottleSettings;
    /**
     * A name for the usage plan.
     */
    readonly usagePlanName?: string;
}
/**
 * Resource Type definition for AWS::ApiGateway::UsagePlan
 */
export function getUsagePlanOutput(args: GetUsagePlanOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUsagePlanResult> {
    return pulumi.output(args).apply((a: any) => getUsagePlan(a, opts))
}

export interface GetUsagePlanOutputArgs {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    id: pulumi.Input<string>;
}
