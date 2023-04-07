// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::NetworkManager::VpcAttachment Resoruce Type
 */
export class VpcAttachment extends pulumi.CustomResource {
    /**
     * Get an existing VpcAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VpcAttachment {
        return new VpcAttachment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:VpcAttachment';

    /**
     * Returns true if the given object is an instance of VpcAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpcAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpcAttachment.__pulumiType;
    }

    /**
     * Id of the attachment.
     */
    public /*out*/ readonly attachmentId!: pulumi.Output<string>;
    /**
     * The policy rule number associated with the attachment.
     */
    public /*out*/ readonly attachmentPolicyRuleNumber!: pulumi.Output<number>;
    /**
     * Attachment type.
     */
    public /*out*/ readonly attachmentType!: pulumi.Output<string>;
    /**
     * The ARN of a core network for the VPC attachment.
     */
    public /*out*/ readonly coreNetworkArn!: pulumi.Output<string>;
    /**
     * The ID of a core network for the VPC attachment.
     */
    public readonly coreNetworkId!: pulumi.Output<string>;
    /**
     * Creation time of the attachment.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The Region where the edge is located.
     */
    public /*out*/ readonly edgeLocation!: pulumi.Output<string>;
    /**
     * Vpc options of the attachment.
     */
    public readonly options!: pulumi.Output<outputs.networkmanager.VpcAttachmentVpcOptions | undefined>;
    /**
     * Owner account of the attachment.
     */
    public /*out*/ readonly ownerAccountId!: pulumi.Output<string>;
    /**
     * The attachment to move from one segment to another.
     */
    public /*out*/ readonly proposedSegmentChange!: pulumi.Output<outputs.networkmanager.VpcAttachmentProposedSegmentChange>;
    /**
     * The ARN of the Resource.
     */
    public /*out*/ readonly resourceArn!: pulumi.Output<string>;
    /**
     * The name of the segment attachment..
     */
    public /*out*/ readonly segmentName!: pulumi.Output<string>;
    /**
     * State of the attachment.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Subnet Arn list
     */
    public readonly subnetArns!: pulumi.Output<string[]>;
    /**
     * Tags for the attachment.
     */
    public readonly tags!: pulumi.Output<outputs.networkmanager.VpcAttachmentTag[] | undefined>;
    /**
     * Last update time of the attachment.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;
    /**
     * The ARN of the VPC.
     */
    public readonly vpcArn!: pulumi.Output<string>;

    /**
     * Create a VpcAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcAttachmentArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.coreNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'coreNetworkId'");
            }
            if ((!args || args.subnetArns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetArns'");
            }
            if ((!args || args.vpcArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcArn'");
            }
            resourceInputs["coreNetworkId"] = args ? args.coreNetworkId : undefined;
            resourceInputs["options"] = args ? args.options : undefined;
            resourceInputs["subnetArns"] = args ? args.subnetArns : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcArn"] = args ? args.vpcArn : undefined;
            resourceInputs["attachmentId"] = undefined /*out*/;
            resourceInputs["attachmentPolicyRuleNumber"] = undefined /*out*/;
            resourceInputs["attachmentType"] = undefined /*out*/;
            resourceInputs["coreNetworkArn"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["edgeLocation"] = undefined /*out*/;
            resourceInputs["ownerAccountId"] = undefined /*out*/;
            resourceInputs["proposedSegmentChange"] = undefined /*out*/;
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
            resourceInputs["subnetArns"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
            resourceInputs["vpcArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VpcAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VpcAttachment resource.
 */
export interface VpcAttachmentArgs {
    /**
     * The ID of a core network for the VPC attachment.
     */
    coreNetworkId: pulumi.Input<string>;
    /**
     * Vpc options of the attachment.
     */
    options?: pulumi.Input<inputs.networkmanager.VpcAttachmentVpcOptionsArgs>;
    /**
     * Subnet Arn list
     */
    subnetArns: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Tags for the attachment.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.networkmanager.VpcAttachmentTagArgs>[]>;
    /**
     * The ARN of the VPC.
     */
    vpcArn: pulumi.Input<string>;
}
