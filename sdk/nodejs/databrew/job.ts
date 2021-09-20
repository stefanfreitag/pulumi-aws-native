// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataBrew::Job.
 */
export class Job extends pulumi.CustomResource {
    /**
     * Get an existing Job resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Job {
        return new Job(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:databrew:Job';

    /**
     * Returns true if the given object is an instance of Job.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Job {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Job.__pulumiType;
    }

    public readonly dataCatalogOutputs!: pulumi.Output<outputs.databrew.JobDataCatalogOutput[] | undefined>;
    public readonly databaseOutputs!: pulumi.Output<outputs.databrew.JobDatabaseOutput[] | undefined>;
    /**
     * Dataset name
     */
    public readonly datasetName!: pulumi.Output<string | undefined>;
    /**
     * Encryption Key Arn
     */
    public readonly encryptionKeyArn!: pulumi.Output<string | undefined>;
    /**
     * Encryption mode
     */
    public readonly encryptionMode!: pulumi.Output<enums.databrew.JobEncryptionMode | undefined>;
    /**
     * Job Sample
     */
    public readonly jobSample!: pulumi.Output<outputs.databrew.JobJobSample | undefined>;
    /**
     * Log subscription
     */
    public readonly logSubscription!: pulumi.Output<enums.databrew.JobLogSubscription | undefined>;
    /**
     * Max capacity
     */
    public readonly maxCapacity!: pulumi.Output<number | undefined>;
    /**
     * Max retries
     */
    public readonly maxRetries!: pulumi.Output<number | undefined>;
    /**
     * Job name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Output location
     */
    public readonly outputLocation!: pulumi.Output<outputs.databrew.JobOutputLocation | undefined>;
    public readonly outputs!: pulumi.Output<outputs.databrew.JobOutput[] | undefined>;
    /**
     * Profile Job configuration
     */
    public readonly profileConfiguration!: pulumi.Output<outputs.databrew.JobProfileConfiguration | undefined>;
    /**
     * Project name
     */
    public readonly projectName!: pulumi.Output<string | undefined>;
    public readonly recipe!: pulumi.Output<outputs.databrew.JobRecipe | undefined>;
    /**
     * Role arn
     */
    public readonly roleArn!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.databrew.JobTag[] | undefined>;
    /**
     * Timeout
     */
    public readonly timeout!: pulumi.Output<number | undefined>;
    /**
     * Job type
     */
    public readonly type!: pulumi.Output<enums.databrew.JobType>;

    /**
     * Create a Job resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["dataCatalogOutputs"] = args ? args.dataCatalogOutputs : undefined;
            inputs["databaseOutputs"] = args ? args.databaseOutputs : undefined;
            inputs["datasetName"] = args ? args.datasetName : undefined;
            inputs["encryptionKeyArn"] = args ? args.encryptionKeyArn : undefined;
            inputs["encryptionMode"] = args ? args.encryptionMode : undefined;
            inputs["jobSample"] = args ? args.jobSample : undefined;
            inputs["logSubscription"] = args ? args.logSubscription : undefined;
            inputs["maxCapacity"] = args ? args.maxCapacity : undefined;
            inputs["maxRetries"] = args ? args.maxRetries : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["outputLocation"] = args ? args.outputLocation : undefined;
            inputs["outputs"] = args ? args.outputs : undefined;
            inputs["profileConfiguration"] = args ? args.profileConfiguration : undefined;
            inputs["projectName"] = args ? args.projectName : undefined;
            inputs["recipe"] = args ? args.recipe : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["timeout"] = args ? args.timeout : undefined;
            inputs["type"] = args ? args.type : undefined;
        } else {
            inputs["dataCatalogOutputs"] = undefined /*out*/;
            inputs["databaseOutputs"] = undefined /*out*/;
            inputs["datasetName"] = undefined /*out*/;
            inputs["encryptionKeyArn"] = undefined /*out*/;
            inputs["encryptionMode"] = undefined /*out*/;
            inputs["jobSample"] = undefined /*out*/;
            inputs["logSubscription"] = undefined /*out*/;
            inputs["maxCapacity"] = undefined /*out*/;
            inputs["maxRetries"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["outputLocation"] = undefined /*out*/;
            inputs["outputs"] = undefined /*out*/;
            inputs["profileConfiguration"] = undefined /*out*/;
            inputs["projectName"] = undefined /*out*/;
            inputs["recipe"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["timeout"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Job.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Job resource.
 */
export interface JobArgs {
    dataCatalogOutputs?: pulumi.Input<pulumi.Input<inputs.databrew.JobDataCatalogOutputArgs>[]>;
    databaseOutputs?: pulumi.Input<pulumi.Input<inputs.databrew.JobDatabaseOutputArgs>[]>;
    /**
     * Dataset name
     */
    datasetName?: pulumi.Input<string>;
    /**
     * Encryption Key Arn
     */
    encryptionKeyArn?: pulumi.Input<string>;
    /**
     * Encryption mode
     */
    encryptionMode?: pulumi.Input<enums.databrew.JobEncryptionMode>;
    /**
     * Job Sample
     */
    jobSample?: pulumi.Input<inputs.databrew.JobJobSampleArgs>;
    /**
     * Log subscription
     */
    logSubscription?: pulumi.Input<enums.databrew.JobLogSubscription>;
    /**
     * Max capacity
     */
    maxCapacity?: pulumi.Input<number>;
    /**
     * Max retries
     */
    maxRetries?: pulumi.Input<number>;
    /**
     * Job name
     */
    name: pulumi.Input<string>;
    /**
     * Output location
     */
    outputLocation?: pulumi.Input<inputs.databrew.JobOutputLocationArgs>;
    outputs?: pulumi.Input<pulumi.Input<inputs.databrew.JobOutputArgs>[]>;
    /**
     * Profile Job configuration
     */
    profileConfiguration?: pulumi.Input<inputs.databrew.JobProfileConfigurationArgs>;
    /**
     * Project name
     */
    projectName?: pulumi.Input<string>;
    recipe?: pulumi.Input<inputs.databrew.JobRecipeArgs>;
    /**
     * Role arn
     */
    roleArn: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.databrew.JobTagArgs>[]>;
    /**
     * Timeout
     */
    timeout?: pulumi.Input<number>;
    /**
     * Job type
     */
    type: pulumi.Input<enums.databrew.JobType>;
}
