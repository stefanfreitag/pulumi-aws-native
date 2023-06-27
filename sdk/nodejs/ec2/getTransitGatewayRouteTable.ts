// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::TransitGatewayRouteTable
 */
export function getTransitGatewayRouteTable(args: GetTransitGatewayRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetTransitGatewayRouteTableResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getTransitGatewayRouteTable", {
        "id": args.id,
    }, opts);
}

export interface GetTransitGatewayRouteTableArgs {
    id: string;
}

export interface GetTransitGatewayRouteTableResult {
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::EC2::TransitGatewayRouteTable
 */
export function getTransitGatewayRouteTableOutput(args: GetTransitGatewayRouteTableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTransitGatewayRouteTableResult> {
    return pulumi.output(args).apply((a: any) => getTransitGatewayRouteTable(a, opts))
}

export interface GetTransitGatewayRouteTableOutputArgs {
    id: pulumi.Input<string>;
}
