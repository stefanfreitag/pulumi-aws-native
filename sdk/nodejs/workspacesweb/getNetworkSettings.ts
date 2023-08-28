// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::WorkSpacesWeb::NetworkSettings Resource Type
 */
export function getNetworkSettings(args: GetNetworkSettingsArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkSettingsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:workspacesweb:getNetworkSettings", {
        "networkSettingsArn": args.networkSettingsArn,
    }, opts);
}

export interface GetNetworkSettingsArgs {
    networkSettingsArn: string;
}

export interface GetNetworkSettingsResult {
    readonly associatedPortalArns?: string[];
    readonly networkSettingsArn?: string;
    readonly securityGroupIds?: string[];
    readonly subnetIds?: string[];
    readonly tags?: outputs.workspacesweb.NetworkSettingsTag[];
    readonly vpcId?: string;
}
/**
 * Definition of AWS::WorkSpacesWeb::NetworkSettings Resource Type
 */
export function getNetworkSettingsOutput(args: GetNetworkSettingsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNetworkSettingsResult> {
    return pulumi.output(args).apply((a: any) => getNetworkSettings(a, opts))
}

export interface GetNetworkSettingsOutputArgs {
    networkSettingsArn: pulumi.Input<string>;
}
