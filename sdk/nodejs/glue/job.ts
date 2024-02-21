// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::Job
 *
 * @deprecated Job is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
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
        pulumi.log.warn("Job is deprecated: Job is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Job(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:Job';

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

    public readonly allocatedCapacity!: pulumi.Output<number | undefined>;
    public readonly command!: pulumi.Output<outputs.glue.JobCommand>;
    public readonly connections!: pulumi.Output<outputs.glue.JobConnectionsList | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    public readonly defaultArguments!: pulumi.Output<any | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly executionClass!: pulumi.Output<string | undefined>;
    public readonly executionProperty!: pulumi.Output<outputs.glue.JobExecutionProperty | undefined>;
    public readonly glueVersion!: pulumi.Output<string | undefined>;
    public readonly logUri!: pulumi.Output<string | undefined>;
    public readonly maxCapacity!: pulumi.Output<number | undefined>;
    public readonly maxRetries!: pulumi.Output<number | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    public readonly nonOverridableArguments!: pulumi.Output<any | undefined>;
    public readonly notificationProperty!: pulumi.Output<outputs.glue.JobNotificationProperty | undefined>;
    public readonly numberOfWorkers!: pulumi.Output<number | undefined>;
    public readonly role!: pulumi.Output<string>;
    public readonly securityConfiguration!: pulumi.Output<string | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly timeout!: pulumi.Output<number | undefined>;
    public readonly workerType!: pulumi.Output<string | undefined>;

    /**
     * Create a Job resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Job is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Job is deprecated: Job is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.command === undefined) && !opts.urn) {
                throw new Error("Missing required property 'command'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            resourceInputs["allocatedCapacity"] = args ? args.allocatedCapacity : undefined;
            resourceInputs["command"] = args ? args.command : undefined;
            resourceInputs["connections"] = args ? args.connections : undefined;
            resourceInputs["defaultArguments"] = args ? args.defaultArguments : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["executionClass"] = args ? args.executionClass : undefined;
            resourceInputs["executionProperty"] = args ? args.executionProperty : undefined;
            resourceInputs["glueVersion"] = args ? args.glueVersion : undefined;
            resourceInputs["logUri"] = args ? args.logUri : undefined;
            resourceInputs["maxCapacity"] = args ? args.maxCapacity : undefined;
            resourceInputs["maxRetries"] = args ? args.maxRetries : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nonOverridableArguments"] = args ? args.nonOverridableArguments : undefined;
            resourceInputs["notificationProperty"] = args ? args.notificationProperty : undefined;
            resourceInputs["numberOfWorkers"] = args ? args.numberOfWorkers : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["securityConfiguration"] = args ? args.securityConfiguration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["timeout"] = args ? args.timeout : undefined;
            resourceInputs["workerType"] = args ? args.workerType : undefined;
        } else {
            resourceInputs["allocatedCapacity"] = undefined /*out*/;
            resourceInputs["command"] = undefined /*out*/;
            resourceInputs["connections"] = undefined /*out*/;
            resourceInputs["defaultArguments"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["executionClass"] = undefined /*out*/;
            resourceInputs["executionProperty"] = undefined /*out*/;
            resourceInputs["glueVersion"] = undefined /*out*/;
            resourceInputs["logUri"] = undefined /*out*/;
            resourceInputs["maxCapacity"] = undefined /*out*/;
            resourceInputs["maxRetries"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["nonOverridableArguments"] = undefined /*out*/;
            resourceInputs["notificationProperty"] = undefined /*out*/;
            resourceInputs["numberOfWorkers"] = undefined /*out*/;
            resourceInputs["role"] = undefined /*out*/;
            resourceInputs["securityConfiguration"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["timeout"] = undefined /*out*/;
            resourceInputs["workerType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Job.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Job resource.
 */
export interface JobArgs {
    allocatedCapacity?: pulumi.Input<number>;
    command: pulumi.Input<inputs.glue.JobCommandArgs>;
    connections?: pulumi.Input<inputs.glue.JobConnectionsListArgs>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    defaultArguments?: any;
    description?: pulumi.Input<string>;
    executionClass?: pulumi.Input<string>;
    executionProperty?: pulumi.Input<inputs.glue.JobExecutionPropertyArgs>;
    glueVersion?: pulumi.Input<string>;
    logUri?: pulumi.Input<string>;
    maxCapacity?: pulumi.Input<number>;
    maxRetries?: pulumi.Input<number>;
    name?: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    nonOverridableArguments?: any;
    notificationProperty?: pulumi.Input<inputs.glue.JobNotificationPropertyArgs>;
    numberOfWorkers?: pulumi.Input<number>;
    role: pulumi.Input<string>;
    securityConfiguration?: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Job` for more information about the expected schema for this property.
     */
    tags?: any;
    timeout?: pulumi.Input<number>;
    workerType?: pulumi.Input<string>;
}
