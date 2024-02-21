// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MWAA::Environment
 */
export function getEnvironment(args: GetEnvironmentArgs, opts?: pulumi.InvokeOptions): Promise<GetEnvironmentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:mwaa:getEnvironment", {
        "name": args.name,
    }, opts);
}

export interface GetEnvironmentArgs {
    name: string;
}

export interface GetEnvironmentResult {
    /**
     * Key/value pairs representing Airflow configuration variables.
     *     Keys are prefixed by their section:
     *
     *     [core]
     *     dags_folder={AIRFLOW_HOME}/dags
     *
     *     Would be represented as
     *
     *     "core.dags_folder": "{AIRFLOW_HOME}/dags"
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MWAA::Environment` for more information about the expected schema for this property.
     */
    readonly airflowConfigurationOptions?: any;
    readonly airflowVersion?: string;
    readonly arn?: string;
    readonly celeryExecutorQueue?: string;
    readonly dagS3Path?: string;
    readonly databaseVpcEndpointService?: string;
    readonly environmentClass?: string;
    readonly executionRoleArn?: string;
    readonly loggingConfiguration?: outputs.mwaa.EnvironmentLoggingConfiguration;
    readonly maxWorkers?: number;
    readonly minWorkers?: number;
    readonly networkConfiguration?: outputs.mwaa.EnvironmentNetworkConfiguration;
    readonly pluginsS3ObjectVersion?: string;
    readonly pluginsS3Path?: string;
    readonly requirementsS3ObjectVersion?: string;
    readonly requirementsS3Path?: string;
    readonly schedulers?: number;
    readonly sourceBucketArn?: string;
    readonly startupScriptS3ObjectVersion?: string;
    readonly startupScriptS3Path?: string;
    /**
     * A map of tags for the environment.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MWAA::Environment` for more information about the expected schema for this property.
     */
    readonly tags?: any;
    readonly webserverAccessMode?: enums.mwaa.EnvironmentWebserverAccessMode;
    readonly webserverUrl?: string;
    readonly webserverVpcEndpointService?: string;
    readonly weeklyMaintenanceWindowStart?: string;
}
/**
 * Resource schema for AWS::MWAA::Environment
 */
export function getEnvironmentOutput(args: GetEnvironmentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEnvironmentResult> {
    return pulumi.output(args).apply((a: any) => getEnvironment(a, opts))
}

export interface GetEnvironmentOutputArgs {
    name: pulumi.Input<string>;
}
