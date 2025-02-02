// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataBrew::Schedule.
 */
export function getSchedule(args: GetScheduleArgs, opts?: pulumi.InvokeOptions): Promise<GetScheduleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:databrew:getSchedule", {
        "name": args.name,
    }, opts);
}

export interface GetScheduleArgs {
    /**
     * Schedule Name
     */
    name: string;
}

export interface GetScheduleResult {
    /**
     * Schedule cron
     */
    readonly cronExpression?: string;
    readonly jobNames?: string[];
}
/**
 * Resource schema for AWS::DataBrew::Schedule.
 */
export function getScheduleOutput(args: GetScheduleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetScheduleResult> {
    return pulumi.output(args).apply((a: any) => getSchedule(a, opts))
}

export interface GetScheduleOutputArgs {
    /**
     * Schedule Name
     */
    name: pulumi.Input<string>;
}
