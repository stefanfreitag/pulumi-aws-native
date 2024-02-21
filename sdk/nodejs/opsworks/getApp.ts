// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::OpsWorks::App
 */
export function getApp(args: GetAppArgs, opts?: pulumi.InvokeOptions): Promise<GetAppResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:opsworks:getApp", {
        "id": args.id,
    }, opts);
}

export interface GetAppArgs {
    id: string;
}

export interface GetAppResult {
    readonly appSource?: outputs.opsworks.AppSource;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpsWorks::App` for more information about the expected schema for this property.
     */
    readonly attributes?: any;
    readonly dataSources?: outputs.opsworks.AppDataSource[];
    readonly description?: string;
    readonly domains?: string[];
    readonly enableSsl?: boolean;
    readonly environment?: outputs.opsworks.AppEnvironmentVariable[];
    readonly id?: string;
    readonly name?: string;
    readonly sslConfiguration?: outputs.opsworks.AppSslConfiguration;
    readonly type?: string;
}
/**
 * Resource Type definition for AWS::OpsWorks::App
 */
export function getAppOutput(args: GetAppOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAppResult> {
    return pulumi.output(args).apply((a: any) => getApp(a, opts))
}

export interface GetAppOutputArgs {
    id: pulumi.Input<string>;
}
