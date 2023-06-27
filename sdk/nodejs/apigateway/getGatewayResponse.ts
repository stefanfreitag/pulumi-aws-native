// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGateway::GatewayResponse
 */
export function getGatewayResponse(args: GetGatewayResponseArgs, opts?: pulumi.InvokeOptions): Promise<GetGatewayResponseResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigateway:getGatewayResponse", {
        "id": args.id,
    }, opts);
}

export interface GetGatewayResponseArgs {
    id: string;
}

export interface GetGatewayResponseResult {
    readonly id?: string;
    readonly responseParameters?: any;
    readonly responseTemplates?: any;
    readonly statusCode?: string;
}
/**
 * Resource Type definition for AWS::ApiGateway::GatewayResponse
 */
export function getGatewayResponseOutput(args: GetGatewayResponseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGatewayResponseResult> {
    return pulumi.output(args).apply((a: any) => getGatewayResponse(a, opts))
}

export interface GetGatewayResponseOutputArgs {
    id: pulumi.Input<string>;
}
