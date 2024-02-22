// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoTAnalytics::Channel
 */
export function getChannel(args: GetChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetChannelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iotanalytics:getChannel", {
        "channelName": args.channelName,
    }, opts);
}

export interface GetChannelArgs {
    channelName: string;
}

export interface GetChannelResult {
    readonly channelStorage?: outputs.iotanalytics.ChannelStorage;
    readonly id?: string;
    readonly retentionPeriod?: outputs.iotanalytics.ChannelRetentionPeriod;
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::IoTAnalytics::Channel
 */
export function getChannelOutput(args: GetChannelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetChannelResult> {
    return pulumi.output(args).apply((a: any) => getChannel(a, opts))
}

export interface GetChannelOutputArgs {
    channelName: pulumi.Input<string>;
}
