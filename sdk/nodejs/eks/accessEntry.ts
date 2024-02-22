// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An object representing an Amazon EKS AccessEntry.
 */
export class AccessEntry extends pulumi.CustomResource {
    /**
     * Get an existing AccessEntry resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AccessEntry {
        return new AccessEntry(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:eks:AccessEntry';

    /**
     * Returns true if the given object is an instance of AccessEntry.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessEntry {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessEntry.__pulumiType;
    }

    /**
     * The ARN of the access entry.
     */
    public /*out*/ readonly accessEntryArn!: pulumi.Output<string>;
    /**
     * An array of access policies that are associated with the access entry.
     */
    public readonly accessPolicies!: pulumi.Output<outputs.eks.AccessEntryAccessPolicy[] | undefined>;
    /**
     * The cluster that the access entry is created for.
     */
    public readonly clusterName!: pulumi.Output<string>;
    /**
     * The Kubernetes groups that the access entry is associated with.
     */
    public readonly kubernetesGroups!: pulumi.Output<string[] | undefined>;
    /**
     * The principal ARN that the access entry is created for.
     */
    public readonly principalArn!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The node type to associate with the access entry.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * The Kubernetes user that the access entry is associated with.
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a AccessEntry resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessEntryArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.clusterName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterName'");
            }
            if ((!args || args.principalArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'principalArn'");
            }
            resourceInputs["accessPolicies"] = args ? args.accessPolicies : undefined;
            resourceInputs["clusterName"] = args ? args.clusterName : undefined;
            resourceInputs["kubernetesGroups"] = args ? args.kubernetesGroups : undefined;
            resourceInputs["principalArn"] = args ? args.principalArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["username"] = args ? args.username : undefined;
            resourceInputs["accessEntryArn"] = undefined /*out*/;
        } else {
            resourceInputs["accessEntryArn"] = undefined /*out*/;
            resourceInputs["accessPolicies"] = undefined /*out*/;
            resourceInputs["clusterName"] = undefined /*out*/;
            resourceInputs["kubernetesGroups"] = undefined /*out*/;
            resourceInputs["principalArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["username"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["clusterName", "principalArn", "type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AccessEntry.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AccessEntry resource.
 */
export interface AccessEntryArgs {
    /**
     * An array of access policies that are associated with the access entry.
     */
    accessPolicies?: pulumi.Input<pulumi.Input<inputs.eks.AccessEntryAccessPolicyArgs>[]>;
    /**
     * The cluster that the access entry is created for.
     */
    clusterName: pulumi.Input<string>;
    /**
     * The Kubernetes groups that the access entry is associated with.
     */
    kubernetesGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The principal ARN that the access entry is created for.
     */
    principalArn: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * The node type to associate with the access entry.
     */
    type?: pulumi.Input<string>;
    /**
     * The Kubernetes user that the access entry is associated with.
     */
    username?: pulumi.Input<string>;
}
