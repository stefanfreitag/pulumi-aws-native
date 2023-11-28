// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Logs::LogGroup
 */
export class LogGroup extends pulumi.CustomResource {
    /**
     * Get an existing LogGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LogGroup {
        return new LogGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:logs:LogGroup';

    /**
     * Returns true if the given object is an instance of LogGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LogGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LogGroup.__pulumiType;
    }

    /**
     * The CloudWatch log group ARN.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The body of the policy document you want to use for this topic.
     *
     * You can only add one policy per topic.
     *
     * The policy must be in JSON string format.
     *
     * Length Constraints: Maximum length of 30720
     */
    public readonly dataProtectionPolicy!: pulumi.Output<any | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS, with STANDARD being the default class
     */
    public readonly logGroupClass!: pulumi.Output<enums.logs.LogGroupClass | undefined>;
    /**
     * The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
     */
    public readonly logGroupName!: pulumi.Output<string | undefined>;
    /**
     * The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, and 3653.
     */
    public readonly retentionInDays!: pulumi.Output<number | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.logs.LogGroupTag[] | undefined>;

    /**
     * Create a LogGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: LogGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["dataProtectionPolicy"] = args ? args.dataProtectionPolicy : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["logGroupClass"] = args ? args.logGroupClass : undefined;
            resourceInputs["logGroupName"] = args ? args.logGroupName : undefined;
            resourceInputs["retentionInDays"] = args ? args.retentionInDays : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["dataProtectionPolicy"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["logGroupClass"] = undefined /*out*/;
            resourceInputs["logGroupName"] = undefined /*out*/;
            resourceInputs["retentionInDays"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["logGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(LogGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a LogGroup resource.
 */
export interface LogGroupArgs {
    /**
     * The body of the policy document you want to use for this topic.
     *
     * You can only add one policy per topic.
     *
     * The policy must be in JSON string format.
     *
     * Length Constraints: Maximum length of 30720
     */
    dataProtectionPolicy?: any;
    /**
     * The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS, with STANDARD being the default class
     */
    logGroupClass?: pulumi.Input<enums.logs.LogGroupClass>;
    /**
     * The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
     */
    logGroupName?: pulumi.Input<string>;
    /**
     * The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, and 3653.
     */
    retentionInDays?: pulumi.Input<number>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.logs.LogGroupTagArgs>[]>;
}
