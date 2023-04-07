// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::ConnectCampaigns::Campaign Resource Type
 */
export function getCampaign(args: GetCampaignArgs, opts?: pulumi.InvokeOptions): Promise<GetCampaignResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:connectcampaigns:getCampaign", {
        "arn": args.arn,
    }, opts);
}

export interface GetCampaignArgs {
    /**
     * Amazon Connect Campaign Arn
     */
    arn: string;
}

export interface GetCampaignResult {
    /**
     * Amazon Connect Campaign Arn
     */
    readonly arn?: string;
    readonly dialerConfig?: outputs.connectcampaigns.CampaignDialerConfig;
    /**
     * Amazon Connect Campaign Name
     */
    readonly name?: string;
    readonly outboundCallConfig?: outputs.connectcampaigns.CampaignOutboundCallConfig;
    /**
     * One or more tags.
     */
    readonly tags?: outputs.connectcampaigns.CampaignTag[];
}
/**
 * Definition of AWS::ConnectCampaigns::Campaign Resource Type
 */
export function getCampaignOutput(args: GetCampaignOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCampaignResult> {
    return pulumi.output(args).apply((a: any) => getCampaign(a, opts))
}

export interface GetCampaignOutputArgs {
    /**
     * Amazon Connect Campaign Arn
     */
    arn: pulumi.Input<string>;
}
