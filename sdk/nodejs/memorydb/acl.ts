// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MemoryDB::ACL
 */
export class Acl extends pulumi.CustomResource {
    /**
     * Get an existing Acl resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Acl {
        return new Acl(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:memorydb:Acl';

    /**
     * Returns true if the given object is an instance of Acl.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Acl {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Acl.__pulumiType;
    }

    /**
     * The name of the acl.
     */
    public readonly aclName!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the acl.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Indicates acl status. Can be "creating", "active", "modifying", "deleting".
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this cluster.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * List of users associated to this acl.
     */
    public readonly userNames!: pulumi.Output<string[] | undefined>;

    /**
     * Create a Acl resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AclArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["aclName"] = args ? args.aclName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["userNames"] = args ? args.userNames : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["aclName"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["userNames"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["aclName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Acl.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Acl resource.
 */
export interface AclArgs {
    /**
     * The name of the acl.
     */
    aclName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this cluster.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * List of users associated to this acl.
     */
    userNames?: pulumi.Input<pulumi.Input<string>[]>;
}
