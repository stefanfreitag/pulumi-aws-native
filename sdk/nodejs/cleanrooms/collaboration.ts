// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents a collaboration between AWS accounts that allows for secure data collaboration
 */
export class Collaboration extends pulumi.CustomResource {
    /**
     * Get an existing Collaboration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Collaboration {
        return new Collaboration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cleanrooms:Collaboration';

    /**
     * Returns true if the given object is an instance of Collaboration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Collaboration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Collaboration.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public /*out*/ readonly collaborationIdentifier!: pulumi.Output<string>;
    public readonly creatorDisplayName!: pulumi.Output<string>;
    public readonly creatorMemberAbilities!: pulumi.Output<enums.cleanrooms.CollaborationMemberAbility[]>;
    public readonly creatorPaymentConfiguration!: pulumi.Output<outputs.cleanrooms.CollaborationPaymentConfiguration | undefined>;
    public readonly dataEncryptionMetadata!: pulumi.Output<outputs.cleanrooms.CollaborationDataEncryptionMetadata | undefined>;
    public readonly description!: pulumi.Output<string>;
    public readonly members!: pulumi.Output<outputs.cleanrooms.CollaborationMemberSpecification[]>;
    public readonly name!: pulumi.Output<string>;
    public readonly queryLogStatus!: pulumi.Output<enums.cleanrooms.CollaborationQueryLogStatus>;
    /**
     * An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Collaboration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CollaborationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.creatorDisplayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'creatorDisplayName'");
            }
            if ((!args || args.creatorMemberAbilities === undefined) && !opts.urn) {
                throw new Error("Missing required property 'creatorMemberAbilities'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.members === undefined) && !opts.urn) {
                throw new Error("Missing required property 'members'");
            }
            if ((!args || args.queryLogStatus === undefined) && !opts.urn) {
                throw new Error("Missing required property 'queryLogStatus'");
            }
            resourceInputs["creatorDisplayName"] = args ? args.creatorDisplayName : undefined;
            resourceInputs["creatorMemberAbilities"] = args ? args.creatorMemberAbilities : undefined;
            resourceInputs["creatorPaymentConfiguration"] = args ? args.creatorPaymentConfiguration : undefined;
            resourceInputs["dataEncryptionMetadata"] = args ? args.dataEncryptionMetadata : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["members"] = args ? args.members : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["queryLogStatus"] = args ? args.queryLogStatus : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["collaborationIdentifier"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["collaborationIdentifier"] = undefined /*out*/;
            resourceInputs["creatorDisplayName"] = undefined /*out*/;
            resourceInputs["creatorMemberAbilities"] = undefined /*out*/;
            resourceInputs["creatorPaymentConfiguration"] = undefined /*out*/;
            resourceInputs["dataEncryptionMetadata"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["members"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["queryLogStatus"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["creatorDisplayName", "creatorMemberAbilities[*]", "creatorPaymentConfiguration", "dataEncryptionMetadata", "members[*]", "queryLogStatus"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Collaboration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Collaboration resource.
 */
export interface CollaborationArgs {
    creatorDisplayName: pulumi.Input<string>;
    creatorMemberAbilities: pulumi.Input<pulumi.Input<enums.cleanrooms.CollaborationMemberAbility>[]>;
    creatorPaymentConfiguration?: pulumi.Input<inputs.cleanrooms.CollaborationPaymentConfigurationArgs>;
    dataEncryptionMetadata?: pulumi.Input<inputs.cleanrooms.CollaborationDataEncryptionMetadataArgs>;
    description: pulumi.Input<string>;
    members: pulumi.Input<pulumi.Input<inputs.cleanrooms.CollaborationMemberSpecificationArgs>[]>;
    name?: pulumi.Input<string>;
    queryLogStatus: pulumi.Input<enums.cleanrooms.CollaborationQueryLogStatus>;
    /**
     * An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
