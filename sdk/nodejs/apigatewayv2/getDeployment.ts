// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.
 */
export function getDeployment(args: GetDeploymentArgs, opts?: pulumi.InvokeOptions): Promise<GetDeploymentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigatewayv2:getDeployment", {
        "apiId": args.apiId,
        "deploymentId": args.deploymentId,
    }, opts);
}

export interface GetDeploymentArgs {
    /**
     * The API identifier.
     */
    apiId: string;
    deploymentId: string;
}

export interface GetDeploymentResult {
    readonly deploymentId?: string;
    /**
     * The description for the deployment resource.
     */
    readonly description?: string;
}
/**
 * The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.
 */
export function getDeploymentOutput(args: GetDeploymentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDeploymentResult> {
    return pulumi.output(args).apply((a: any) => getDeployment(a, opts))
}

export interface GetDeploymentOutputArgs {
    /**
     * The API identifier.
     */
    apiId: pulumi.Input<string>;
    deploymentId: pulumi.Input<string>;
}
