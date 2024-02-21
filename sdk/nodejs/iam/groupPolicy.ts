// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Schema for IAM Group Policy
 */
export class GroupPolicy extends pulumi.CustomResource {
    /**
     * Get an existing GroupPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): GroupPolicy {
        return new GroupPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iam:GroupPolicy';

    /**
     * Returns true if the given object is an instance of GroupPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GroupPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GroupPolicy.__pulumiType;
    }

    /**
     * The name of the group to associate the policy with.
     */
    public readonly groupName!: pulumi.Output<string>;
    /**
     * The policy document.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::GroupPolicy` for more information about the expected schema for this property.
     */
    public readonly policyDocument!: pulumi.Output<any | undefined>;
    /**
     * The name of the policy document.
     */
    public readonly policyName!: pulumi.Output<string>;

    /**
     * Create a GroupPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.groupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupName'");
            }
            if ((!args || args.policyName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyName'");
            }
            resourceInputs["groupName"] = args ? args.groupName : undefined;
            resourceInputs["policyDocument"] = args ? args.policyDocument : undefined;
            resourceInputs["policyName"] = args ? args.policyName : undefined;
        } else {
            resourceInputs["groupName"] = undefined /*out*/;
            resourceInputs["policyDocument"] = undefined /*out*/;
            resourceInputs["policyName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["groupName", "policyName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(GroupPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a GroupPolicy resource.
 */
export interface GroupPolicyArgs {
    /**
     * The name of the group to associate the policy with.
     */
    groupName: pulumi.Input<string>;
    /**
     * The policy document.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::GroupPolicy` for more information about the expected schema for this property.
     */
    policyDocument?: any;
    /**
     * The name of the policy document.
     */
    policyName: pulumi.Input<string>;
}
