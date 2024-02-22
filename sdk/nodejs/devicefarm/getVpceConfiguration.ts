// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
 */
export function getVpceConfiguration(args: GetVpceConfigurationArgs, opts?: pulumi.InvokeOptions): Promise<GetVpceConfigurationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:devicefarm:getVpceConfiguration", {
        "arn": args.arn,
    }, opts);
}

export interface GetVpceConfigurationArgs {
    arn: string;
}

export interface GetVpceConfigurationResult {
    readonly arn?: string;
    readonly serviceDnsName?: string;
    readonly tags?: outputs.Tag[];
    readonly vpceConfigurationDescription?: string;
    readonly vpceConfigurationName?: string;
    readonly vpceServiceName?: string;
}
/**
 * AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
 */
export function getVpceConfigurationOutput(args: GetVpceConfigurationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVpceConfigurationResult> {
    return pulumi.output(args).apply((a: any) => getVpceConfiguration(a, opts))
}

export interface GetVpceConfigurationOutputArgs {
    arn: pulumi.Input<string>;
}
