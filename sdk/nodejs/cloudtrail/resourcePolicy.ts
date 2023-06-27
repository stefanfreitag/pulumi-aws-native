// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudTrail::ResourcePolicy
 */
export class ResourcePolicy extends pulumi.CustomResource {
    /**
     * Get an existing ResourcePolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ResourcePolicy {
        return new ResourcePolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudtrail:ResourcePolicy';

    /**
     * Returns true if the given object is an instance of ResourcePolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ResourcePolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ResourcePolicy.__pulumiType;
    }

    /**
     * The ARN of the AWS CloudTrail resource to which the policy applies.
     */
    public readonly resourceArn!: pulumi.Output<string>;
    /**
     * A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.
     */
    public readonly resourcePolicy!: pulumi.Output<any>;

    /**
     * Create a ResourcePolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ResourcePolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.resourceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceArn'");
            }
            if ((!args || args.resourcePolicy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourcePolicy'");
            }
            resourceInputs["resourceArn"] = args ? args.resourceArn : undefined;
            resourceInputs["resourcePolicy"] = args ? args.resourcePolicy : undefined;
        } else {
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["resourcePolicy"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ResourcePolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ResourcePolicy resource.
 */
export interface ResourcePolicyArgs {
    /**
     * The ARN of the AWS CloudTrail resource to which the policy applies.
     */
    resourceArn: pulumi.Input<string>;
    /**
     * A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.
     */
    resourcePolicy: any;
}
