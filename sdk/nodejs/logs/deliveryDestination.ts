// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * This structure contains information about one delivery destination in your account.
 *
 * A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.
 */
export class DeliveryDestination extends pulumi.CustomResource {
    /**
     * Get an existing DeliveryDestination resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DeliveryDestination {
        return new DeliveryDestination(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:logs:DeliveryDestination';

    /**
     * Returns true if the given object is an instance of DeliveryDestination.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DeliveryDestination {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DeliveryDestination.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.
     *
     * The policy must be in JSON string format.
     *
     * Length Constraints: Maximum length of 51200
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Logs::DeliveryDestination` for more information about the expected schema for this property.
     */
    public readonly deliveryDestinationPolicy!: pulumi.Output<any | undefined>;
    /**
     * Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.
     */
    public /*out*/ readonly deliveryDestinationType!: pulumi.Output<string>;
    /**
     * The ARN of the AWS resource that will receive the logs.
     */
    public readonly destinationResourceArn!: pulumi.Output<string | undefined>;
    /**
     * The name of this delivery destination.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The tags that have been assigned to this delivery destination.
     */
    public readonly tags!: pulumi.Output<outputs.logs.DeliveryDestinationTag[] | undefined>;

    /**
     * Create a DeliveryDestination resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DeliveryDestinationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["deliveryDestinationPolicy"] = args ? args.deliveryDestinationPolicy : undefined;
            resourceInputs["destinationResourceArn"] = args ? args.destinationResourceArn : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["deliveryDestinationType"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["deliveryDestinationPolicy"] = undefined /*out*/;
            resourceInputs["deliveryDestinationType"] = undefined /*out*/;
            resourceInputs["destinationResourceArn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["destinationResourceArn", "name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DeliveryDestination.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DeliveryDestination resource.
 */
export interface DeliveryDestinationArgs {
    /**
     * IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.
     *
     * The policy must be in JSON string format.
     *
     * Length Constraints: Maximum length of 51200
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Logs::DeliveryDestination` for more information about the expected schema for this property.
     */
    deliveryDestinationPolicy?: any;
    /**
     * The ARN of the AWS resource that will receive the logs.
     */
    destinationResourceArn?: pulumi.Input<string>;
    /**
     * The name of this delivery destination.
     */
    name?: pulumi.Input<string>;
    /**
     * The tags that have been assigned to this delivery destination.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.logs.DeliveryDestinationTagArgs>[]>;
}
