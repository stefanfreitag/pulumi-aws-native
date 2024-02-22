// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type
 */
export function getUserAccessLoggingSettings(args: GetUserAccessLoggingSettingsArgs, opts?: pulumi.InvokeOptions): Promise<GetUserAccessLoggingSettingsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:workspacesweb:getUserAccessLoggingSettings", {
        "userAccessLoggingSettingsArn": args.userAccessLoggingSettingsArn,
    }, opts);
}

export interface GetUserAccessLoggingSettingsArgs {
    userAccessLoggingSettingsArn: string;
}

export interface GetUserAccessLoggingSettingsResult {
    readonly associatedPortalArns?: string[];
    /**
     * Kinesis stream ARN to which log events are published.
     */
    readonly kinesisStreamArn?: string;
    readonly tags?: outputs.Tag[];
    readonly userAccessLoggingSettingsArn?: string;
}
/**
 * Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type
 */
export function getUserAccessLoggingSettingsOutput(args: GetUserAccessLoggingSettingsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserAccessLoggingSettingsResult> {
    return pulumi.output(args).apply((a: any) => getUserAccessLoggingSettings(a, opts))
}

export interface GetUserAccessLoggingSettingsOutputArgs {
    userAccessLoggingSettingsArn: pulumi.Input<string>;
}
