// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.
 */
export function getTransitGatewayRouteTableAttachment(args: GetTransitGatewayRouteTableAttachmentArgs, opts?: pulumi.InvokeOptions): Promise<GetTransitGatewayRouteTableAttachmentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:networkmanager:getTransitGatewayRouteTableAttachment", {
        "attachmentId": args.attachmentId,
    }, opts);
}

export interface GetTransitGatewayRouteTableAttachmentArgs {
    /**
     * The ID of the attachment.
     */
    attachmentId: string;
}

export interface GetTransitGatewayRouteTableAttachmentResult {
    /**
     * The ID of the attachment.
     */
    readonly attachmentId?: string;
    /**
     * The policy rule number associated with the attachment.
     */
    readonly attachmentPolicyRuleNumber?: number;
    /**
     * The type of attachment.
     */
    readonly attachmentType?: string;
    /**
     * The ARN of a core network for the VPC attachment.
     */
    readonly coreNetworkArn?: string;
    /**
     * The ID of a core network where you're creating a site-to-site VPN attachment.
     */
    readonly coreNetworkId?: string;
    /**
     * Creation time of the attachment.
     */
    readonly createdAt?: string;
    /**
     * The Region where the edge is located.
     */
    readonly edgeLocation?: string;
    /**
     * Owner account of the attachment.
     */
    readonly ownerAccountId?: string;
    /**
     * The attachment to move from one segment to another.
     */
    readonly proposedSegmentChange?: outputs.networkmanager.TransitGatewayRouteTableAttachmentProposedSegmentChange;
    /**
     * The ARN of the Resource.
     */
    readonly resourceArn?: string;
    /**
     * The name of the segment that attachment is in.
     */
    readonly segmentName?: string;
    /**
     * The state of the attachment.
     */
    readonly state?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.networkmanager.TransitGatewayRouteTableAttachmentTag[];
    /**
     * Last update time of the attachment.
     */
    readonly updatedAt?: string;
}
/**
 * AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.
 */
export function getTransitGatewayRouteTableAttachmentOutput(args: GetTransitGatewayRouteTableAttachmentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTransitGatewayRouteTableAttachmentResult> {
    return pulumi.output(args).apply((a: any) => getTransitGatewayRouteTableAttachment(a, opts))
}

export interface GetTransitGatewayRouteTableAttachmentOutputArgs {
    /**
     * The ID of the attachment.
     */
    attachmentId: pulumi.Input<string>;
}
