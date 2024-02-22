// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS Ground Station Mission Profile resource type for CloudFormation.
 */
export class MissionProfile extends pulumi.CustomResource {
    /**
     * Get an existing MissionProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MissionProfile {
        return new MissionProfile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:groundstation:MissionProfile';

    /**
     * Returns true if the given object is an instance of MissionProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MissionProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MissionProfile.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Post-pass time needed after the contact.
     */
    public readonly contactPostPassDurationSeconds!: pulumi.Output<number | undefined>;
    /**
     * Pre-pass time needed before the contact.
     */
    public readonly contactPrePassDurationSeconds!: pulumi.Output<number | undefined>;
    public readonly dataflowEdges!: pulumi.Output<outputs.groundstation.MissionProfileDataflowEdge[]>;
    /**
     * Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
     */
    public readonly minimumViableContactDurationSeconds!: pulumi.Output<number>;
    /**
     * A name used to identify a mission profile.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.
     */
    public readonly streamsKmsKey!: pulumi.Output<outputs.groundstation.MissionProfileStreamsKmsKey | undefined>;
    /**
     * The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
     */
    public readonly streamsKmsRole!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly trackingConfigArn!: pulumi.Output<string>;

    /**
     * Create a MissionProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MissionProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dataflowEdges === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataflowEdges'");
            }
            if ((!args || args.minimumViableContactDurationSeconds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'minimumViableContactDurationSeconds'");
            }
            if ((!args || args.trackingConfigArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'trackingConfigArn'");
            }
            resourceInputs["contactPostPassDurationSeconds"] = args ? args.contactPostPassDurationSeconds : undefined;
            resourceInputs["contactPrePassDurationSeconds"] = args ? args.contactPrePassDurationSeconds : undefined;
            resourceInputs["dataflowEdges"] = args ? args.dataflowEdges : undefined;
            resourceInputs["minimumViableContactDurationSeconds"] = args ? args.minimumViableContactDurationSeconds : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["streamsKmsKey"] = args ? args.streamsKmsKey : undefined;
            resourceInputs["streamsKmsRole"] = args ? args.streamsKmsRole : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["trackingConfigArn"] = args ? args.trackingConfigArn : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["contactPostPassDurationSeconds"] = undefined /*out*/;
            resourceInputs["contactPrePassDurationSeconds"] = undefined /*out*/;
            resourceInputs["dataflowEdges"] = undefined /*out*/;
            resourceInputs["minimumViableContactDurationSeconds"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
            resourceInputs["streamsKmsKey"] = undefined /*out*/;
            resourceInputs["streamsKmsRole"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["trackingConfigArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MissionProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a MissionProfile resource.
 */
export interface MissionProfileArgs {
    /**
     * Post-pass time needed after the contact.
     */
    contactPostPassDurationSeconds?: pulumi.Input<number>;
    /**
     * Pre-pass time needed before the contact.
     */
    contactPrePassDurationSeconds?: pulumi.Input<number>;
    dataflowEdges: pulumi.Input<pulumi.Input<inputs.groundstation.MissionProfileDataflowEdgeArgs>[]>;
    /**
     * Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
     */
    minimumViableContactDurationSeconds: pulumi.Input<number>;
    /**
     * A name used to identify a mission profile.
     */
    name?: pulumi.Input<string>;
    /**
     * The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.
     */
    streamsKmsKey?: pulumi.Input<inputs.groundstation.MissionProfileStreamsKmsKeyArgs>;
    /**
     * The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
     */
    streamsKmsRole?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    trackingConfigArn: pulumi.Input<string>;
}
