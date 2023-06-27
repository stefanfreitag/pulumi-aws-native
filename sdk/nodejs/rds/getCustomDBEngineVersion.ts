// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
 */
export function getCustomDBEngineVersion(args: GetCustomDBEngineVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomDBEngineVersionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rds:getCustomDBEngineVersion", {
        "engine": args.engine,
        "engineVersion": args.engineVersion,
    }, opts);
}

export interface GetCustomDBEngineVersionArgs {
    /**
     * The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
     */
    engine: string;
    /**
     * The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
     */
    engineVersion: string;
}

export interface GetCustomDBEngineVersionResult {
    /**
     * The ARN of the custom engine version.
     */
    readonly dBEngineVersionArn?: string;
    /**
     * An optional description of your CEV.
     */
    readonly description?: string;
    /**
     * The availability status to be assigned to the CEV.
     */
    readonly status?: enums.rds.CustomDBEngineVersionStatus;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.rds.CustomDBEngineVersionTag[];
}
/**
 * The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
 */
export function getCustomDBEngineVersionOutput(args: GetCustomDBEngineVersionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCustomDBEngineVersionResult> {
    return pulumi.output(args).apply((a: any) => getCustomDBEngineVersion(a, opts))
}

export interface GetCustomDBEngineVersionOutputArgs {
    /**
     * The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
     */
    engine: pulumi.Input<string>;
    /**
     * The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
     */
    engineVersion: pulumi.Input<string>;
}
