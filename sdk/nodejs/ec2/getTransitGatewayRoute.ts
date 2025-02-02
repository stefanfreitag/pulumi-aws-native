// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::TransitGatewayRoute
 */
export function getTransitGatewayRoute(args: GetTransitGatewayRouteArgs, opts?: pulumi.InvokeOptions): Promise<GetTransitGatewayRouteResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getTransitGatewayRoute", {
        "id": args.id,
    }, opts);
}

export interface GetTransitGatewayRouteArgs {
    id: string;
}

export interface GetTransitGatewayRouteResult {
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::EC2::TransitGatewayRoute
 */
export function getTransitGatewayRouteOutput(args: GetTransitGatewayRouteOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTransitGatewayRouteResult> {
    return pulumi.output(args).apply((a: any) => getTransitGatewayRoute(a, opts))
}

export interface GetTransitGatewayRouteOutputArgs {
    id: pulumi.Input<string>;
}
