// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.
 */
export function getApp(args: GetAppArgs, opts?: pulumi.InvokeOptions): Promise<GetAppResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:amplify:getApp", {
        "arn": args.arn,
    }, opts);
}

export interface GetAppArgs {
    arn: string;
}

export interface GetAppResult {
    readonly appId?: string;
    readonly appName?: string;
    readonly arn?: string;
    readonly buildSpec?: string;
    readonly customHeaders?: string;
    readonly customRules?: outputs.amplify.AppCustomRule[];
    readonly defaultDomain?: string;
    readonly description?: string;
    readonly enableBranchAutoDeletion?: boolean;
    readonly environmentVariables?: outputs.amplify.AppEnvironmentVariable[];
    readonly iAMServiceRole?: string;
    readonly name?: string;
    readonly platform?: enums.amplify.AppPlatform;
    readonly repository?: string;
    readonly tags?: outputs.amplify.AppTag[];
}

export function getAppOutput(args: GetAppOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAppResult> {
    return pulumi.output(args).apply(a => getApp(a, opts))
}

export interface GetAppOutputArgs {
    arn: pulumi.Input<string>;
}
