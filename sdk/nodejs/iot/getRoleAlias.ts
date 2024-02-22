// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.
 */
export function getRoleAlias(args: GetRoleAliasArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleAliasResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iot:getRoleAlias", {
        "roleAlias": args.roleAlias,
    }, opts);
}

export interface GetRoleAliasArgs {
    roleAlias: string;
}

export interface GetRoleAliasResult {
    readonly credentialDurationSeconds?: number;
    readonly roleAliasArn?: string;
    readonly roleArn?: string;
    readonly tags?: outputs.Tag[];
}
/**
 * Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.
 */
export function getRoleAliasOutput(args: GetRoleAliasOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRoleAliasResult> {
    return pulumi.output(args).apply((a: any) => getRoleAlias(a, opts))
}

export interface GetRoleAliasOutputArgs {
    roleAlias: pulumi.Input<string>;
}
