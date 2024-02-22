// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Describes a local gateway route table virtual interface group association for a local gateway.
 */
export function getLocalGatewayRouteTableVirtualInterfaceGroupAssociation(args: GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getLocalGatewayRouteTableVirtualInterfaceGroupAssociation", {
        "localGatewayRouteTableVirtualInterfaceGroupAssociationId": args.localGatewayRouteTableVirtualInterfaceGroupAssociationId,
    }, opts);
}

export interface GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationArgs {
    /**
     * The ID of the local gateway route table virtual interface group association.
     */
    localGatewayRouteTableVirtualInterfaceGroupAssociationId: string;
}

export interface GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult {
    /**
     * The ID of the local gateway.
     */
    readonly localGatewayId?: string;
    /**
     * The ARN of the local gateway route table.
     */
    readonly localGatewayRouteTableArn?: string;
    /**
     * The ID of the local gateway route table virtual interface group association.
     */
    readonly localGatewayRouteTableVirtualInterfaceGroupAssociationId?: string;
    /**
     * The owner of the local gateway route table virtual interface group association.
     */
    readonly ownerId?: string;
    /**
     * The state of the local gateway route table virtual interface group association.
     */
    readonly state?: string;
    /**
     * The tags for the local gateway route table virtual interface group association.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Describes a local gateway route table virtual interface group association for a local gateway.
 */
export function getLocalGatewayRouteTableVirtualInterfaceGroupAssociationOutput(args: GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult> {
    return pulumi.output(args).apply((a: any) => getLocalGatewayRouteTableVirtualInterfaceGroupAssociation(a, opts))
}

export interface GetLocalGatewayRouteTableVirtualInterfaceGroupAssociationOutputArgs {
    /**
     * The ID of the local gateway route table virtual interface group association.
     */
    localGatewayRouteTableVirtualInterfaceGroupAssociationId: pulumi.Input<string>;
}
