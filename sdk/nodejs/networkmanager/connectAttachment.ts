// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::NetworkManager::ConnectAttachment Resource Type Definition
 */
export class ConnectAttachment extends pulumi.CustomResource {
    /**
     * Get an existing ConnectAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConnectAttachment {
        return new ConnectAttachment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:ConnectAttachment';

    /**
     * Returns true if the given object is an instance of ConnectAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConnectAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConnectAttachment.__pulumiType;
    }

    /**
     * The ID of the attachment.
     */
    public /*out*/ readonly attachmentId!: pulumi.Output<string>;
    /**
     * The policy rule number associated with the attachment.
     */
    public /*out*/ readonly attachmentPolicyRuleNumber!: pulumi.Output<number>;
    /**
     * The type of attachment.
     */
    public /*out*/ readonly attachmentType!: pulumi.Output<string>;
    /**
     * The ARN of a core network.
     */
    public /*out*/ readonly coreNetworkArn!: pulumi.Output<string>;
    /**
     * ID of the CoreNetwork that the attachment will be attached to.
     */
    public readonly coreNetworkId!: pulumi.Output<string>;
    /**
     * Creation time of the attachment.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Edge location of the attachment.
     */
    public readonly edgeLocation!: pulumi.Output<string>;
    /**
     * Protocol options for connect attachment
     */
    public readonly options!: pulumi.Output<outputs.networkmanager.ConnectAttachmentOptions>;
    /**
     * The ID of the attachment account owner.
     */
    public /*out*/ readonly ownerAccountId!: pulumi.Output<string>;
    /**
     * The attachment to move from one segment to another.
     */
    public readonly proposedSegmentChange!: pulumi.Output<outputs.networkmanager.ConnectAttachmentProposedSegmentChange | undefined>;
    /**
     * The attachment resource ARN.
     */
    public /*out*/ readonly resourceArn!: pulumi.Output<string>;
    /**
     * The name of the segment attachment.
     */
    public /*out*/ readonly segmentName!: pulumi.Output<string>;
    /**
     * State of the attachment.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Tags for the attachment.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * Id of transport attachment
     */
    public readonly transportAttachmentId!: pulumi.Output<string>;
    /**
     * Last update time of the attachment.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a ConnectAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConnectAttachmentArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.coreNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'coreNetworkId'");
            }
            if ((!args || args.edgeLocation === undefined) && !opts.urn) {
                throw new Error("Missing required property 'edgeLocation'");
            }
            if ((!args || args.options === undefined) && !opts.urn) {
                throw new Error("Missing required property 'options'");
            }
            if ((!args || args.transportAttachmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transportAttachmentId'");
            }
            resourceInputs["coreNetworkId"] = args ? args.coreNetworkId : undefined;
            resourceInputs["edgeLocation"] = args ? args.edgeLocation : undefined;
            resourceInputs["options"] = args ? args.options : undefined;
            resourceInputs["proposedSegmentChange"] = args ? args.proposedSegmentChange : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["transportAttachmentId"] = args ? args.transportAttachmentId : undefined;
            resourceInputs["attachmentId"] = undefined /*out*/;
            resourceInputs["attachmentPolicyRuleNumber"] = undefined /*out*/;
            resourceInputs["attachmentType"] = undefined /*out*/;
            resourceInputs["coreNetworkArn"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["ownerAccountId"] = undefined /*out*/;
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["segmentName"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        } else {
            resourceInputs["attachmentId"] = undefined /*out*/;
            resourceInputs["attachmentPolicyRuleNumber"] = undefined /*out*/;
            resourceInputs["attachmentType"] = undefined /*out*/;
            resourceInputs["coreNetworkArn"] = undefined /*out*/;
            resourceInputs["coreNetworkId"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["edgeLocation"] = undefined /*out*/;
            resourceInputs["options"] = undefined /*out*/;
            resourceInputs["ownerAccountId"] = undefined /*out*/;
            resourceInputs["proposedSegmentChange"] = undefined /*out*/;
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["segmentName"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["transportAttachmentId"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["coreNetworkId", "edgeLocation", "options", "transportAttachmentId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConnectAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConnectAttachment resource.
 */
export interface ConnectAttachmentArgs {
    /**
     * ID of the CoreNetwork that the attachment will be attached to.
     */
    coreNetworkId: pulumi.Input<string>;
    /**
     * Edge location of the attachment.
     */
    edgeLocation: pulumi.Input<string>;
    /**
     * Protocol options for connect attachment
     */
    options: pulumi.Input<inputs.networkmanager.ConnectAttachmentOptionsArgs>;
    /**
     * The attachment to move from one segment to another.
     */
    proposedSegmentChange?: pulumi.Input<inputs.networkmanager.ConnectAttachmentProposedSegmentChangeArgs>;
    /**
     * Tags for the attachment.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * Id of transport attachment
     */
    transportAttachmentId: pulumi.Input<string>;
}
