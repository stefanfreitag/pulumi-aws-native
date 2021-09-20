// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MWAA::Environment
 */
export class Environment extends pulumi.CustomResource {
    /**
     * Get an existing Environment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Environment {
        return new Environment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mwaa:Environment';

    /**
     * Returns true if the given object is an instance of Environment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Environment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Environment.__pulumiType;
    }

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
     */
    public readonly airflowConfigurationOptions!: pulumi.Output<any | undefined>;
    public readonly airflowVersion!: pulumi.Output<string | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly dagS3Path!: pulumi.Output<string | undefined>;
    public readonly environmentClass!: pulumi.Output<string | undefined>;
    public readonly executionRoleArn!: pulumi.Output<string | undefined>;
    public readonly kmsKey!: pulumi.Output<string | undefined>;
    public readonly loggingConfiguration!: pulumi.Output<outputs.mwaa.EnvironmentLoggingConfiguration | undefined>;
    public readonly maxWorkers!: pulumi.Output<number | undefined>;
    public readonly minWorkers!: pulumi.Output<number | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly networkConfiguration!: pulumi.Output<outputs.mwaa.EnvironmentNetworkConfiguration | undefined>;
    public readonly pluginsS3ObjectVersion!: pulumi.Output<string | undefined>;
    public readonly pluginsS3Path!: pulumi.Output<string | undefined>;
    public readonly requirementsS3ObjectVersion!: pulumi.Output<string | undefined>;
    public readonly requirementsS3Path!: pulumi.Output<string | undefined>;
    public readonly schedulers!: pulumi.Output<number | undefined>;
    public readonly sourceBucketArn!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.mwaa.EnvironmentTagMap | undefined>;
    public readonly webserverAccessMode!: pulumi.Output<enums.mwaa.EnvironmentWebserverAccessMode | undefined>;
    public /*out*/ readonly webserverUrl!: pulumi.Output<string>;
    public readonly weeklyMaintenanceWindowStart!: pulumi.Output<string | undefined>;

    /**
     * Create a Environment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EnvironmentArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["airflowConfigurationOptions"] = args ? args.airflowConfigurationOptions : undefined;
            inputs["airflowVersion"] = args ? args.airflowVersion : undefined;
            inputs["dagS3Path"] = args ? args.dagS3Path : undefined;
            inputs["environmentClass"] = args ? args.environmentClass : undefined;
            inputs["executionRoleArn"] = args ? args.executionRoleArn : undefined;
            inputs["kmsKey"] = args ? args.kmsKey : undefined;
            inputs["loggingConfiguration"] = args ? args.loggingConfiguration : undefined;
            inputs["maxWorkers"] = args ? args.maxWorkers : undefined;
            inputs["minWorkers"] = args ? args.minWorkers : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkConfiguration"] = args ? args.networkConfiguration : undefined;
            inputs["pluginsS3ObjectVersion"] = args ? args.pluginsS3ObjectVersion : undefined;
            inputs["pluginsS3Path"] = args ? args.pluginsS3Path : undefined;
            inputs["requirementsS3ObjectVersion"] = args ? args.requirementsS3ObjectVersion : undefined;
            inputs["requirementsS3Path"] = args ? args.requirementsS3Path : undefined;
            inputs["schedulers"] = args ? args.schedulers : undefined;
            inputs["sourceBucketArn"] = args ? args.sourceBucketArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["webserverAccessMode"] = args ? args.webserverAccessMode : undefined;
            inputs["weeklyMaintenanceWindowStart"] = args ? args.weeklyMaintenanceWindowStart : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["webserverUrl"] = undefined /*out*/;
        } else {
            inputs["airflowConfigurationOptions"] = undefined /*out*/;
            inputs["airflowVersion"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["dagS3Path"] = undefined /*out*/;
            inputs["environmentClass"] = undefined /*out*/;
            inputs["executionRoleArn"] = undefined /*out*/;
            inputs["kmsKey"] = undefined /*out*/;
            inputs["loggingConfiguration"] = undefined /*out*/;
            inputs["maxWorkers"] = undefined /*out*/;
            inputs["minWorkers"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["networkConfiguration"] = undefined /*out*/;
            inputs["pluginsS3ObjectVersion"] = undefined /*out*/;
            inputs["pluginsS3Path"] = undefined /*out*/;
            inputs["requirementsS3ObjectVersion"] = undefined /*out*/;
            inputs["requirementsS3Path"] = undefined /*out*/;
            inputs["schedulers"] = undefined /*out*/;
            inputs["sourceBucketArn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["webserverAccessMode"] = undefined /*out*/;
            inputs["webserverUrl"] = undefined /*out*/;
            inputs["weeklyMaintenanceWindowStart"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Environment.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Environment resource.
 */
export interface EnvironmentArgs {
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
     */
    airflowConfigurationOptions?: any;
    airflowVersion?: pulumi.Input<string>;
    dagS3Path?: pulumi.Input<string>;
    environmentClass?: pulumi.Input<string>;
    executionRoleArn?: pulumi.Input<string>;
    kmsKey?: pulumi.Input<string>;
    loggingConfiguration?: pulumi.Input<inputs.mwaa.EnvironmentLoggingConfigurationArgs>;
    maxWorkers?: pulumi.Input<number>;
    minWorkers?: pulumi.Input<number>;
    name: pulumi.Input<string>;
    networkConfiguration?: pulumi.Input<inputs.mwaa.EnvironmentNetworkConfigurationArgs>;
    pluginsS3ObjectVersion?: pulumi.Input<string>;
    pluginsS3Path?: pulumi.Input<string>;
    requirementsS3ObjectVersion?: pulumi.Input<string>;
    requirementsS3Path?: pulumi.Input<string>;
    schedulers?: pulumi.Input<number>;
    sourceBucketArn?: pulumi.Input<string>;
    tags?: pulumi.Input<inputs.mwaa.EnvironmentTagMapArgs>;
    webserverAccessMode?: pulumi.Input<enums.mwaa.EnvironmentWebserverAccessMode>;
    weeklyMaintenanceWindowStart?: pulumi.Input<string>;
}
