// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type Definition for AWS::ResilienceHub::App.
 */
export function getApp(args: GetAppArgs, opts?: pulumi.InvokeOptions): Promise<GetAppResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:resiliencehub:getApp", {
        "appArn": args.appArn,
    }, opts);
}

export interface GetAppArgs {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    appArn: string;
}

export interface GetAppResult {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    readonly appArn?: string;
    /**
     * Assessment execution schedule.
     */
    readonly appAssessmentSchedule?: enums.resiliencehub.AppAssessmentSchedule;
    /**
     * A string containing full ResilienceHub app template body.
     */
    readonly appTemplateBody?: string;
    /**
     * App description.
     */
    readonly description?: string;
    /**
     * Indicates if compliance drifts (deviations) were detected while running an assessment for your application.
     */
    readonly driftStatus?: enums.resiliencehub.AppDriftStatus;
    /**
     * The list of events you would like to subscribe and get notification for.
     */
    readonly eventSubscriptions?: outputs.resiliencehub.AppEventSubscription[];
    readonly permissionModel?: outputs.resiliencehub.AppPermissionModel;
    /**
     * Amazon Resource Name (ARN) of the Resiliency Policy.
     */
    readonly resiliencyPolicyArn?: string;
    /**
     * An array of ResourceMapping objects.
     */
    readonly resourceMappings?: outputs.resiliencehub.AppResourceMapping[];
    readonly tags?: outputs.resiliencehub.AppTagMap;
}
/**
 * Resource Type Definition for AWS::ResilienceHub::App.
 */
export function getAppOutput(args: GetAppOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAppResult> {
    return pulumi.output(args).apply((a: any) => getApp(a, opts))
}

export interface GetAppOutputArgs {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    appArn: pulumi.Input<string>;
}
