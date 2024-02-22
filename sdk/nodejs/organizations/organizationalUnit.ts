// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.
 */
export class OrganizationalUnit extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationalUnit resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OrganizationalUnit {
        return new OrganizationalUnit(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:organizations:OrganizationalUnit';

    /**
     * Returns true if the given object is an instance of OrganizationalUnit.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationalUnit {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationalUnit.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of this OU.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The friendly name of this OU.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
     */
    public readonly parentId!: pulumi.Output<string>;
    /**
     * A list of tags that you want to attach to the newly created OU.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a OrganizationalUnit resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OrganizationalUnitArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.parentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'parentId'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parentId"] = args ? args.parentId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["parentId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["parentId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(OrganizationalUnit.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OrganizationalUnit resource.
 */
export interface OrganizationalUnitArgs {
    /**
     * The friendly name of this OU.
     */
    name?: pulumi.Input<string>;
    /**
     * The unique identifier (ID) of the parent root or OU that you want to create the new OU in.
     */
    parentId: pulumi.Input<string>;
    /**
     * A list of tags that you want to attach to the newly created OU.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
