// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::Stage
 */
export function getStage(args: GetStageArgs, opts?: pulumi.InvokeOptions): Promise<GetStageResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigatewayv2:getStage", {
        "id": args.id,
    }, opts);
}

export interface GetStageArgs {
    id: string;
}

export interface GetStageResult {
    readonly accessLogSettings?: outputs.apigatewayv2.StageAccessLogSettings;
    readonly accessPolicyId?: string;
    readonly autoDeploy?: boolean;
    readonly clientCertificateId?: string;
    readonly defaultRouteSettings?: outputs.apigatewayv2.StageRouteSettings;
    readonly deploymentId?: string;
    readonly description?: string;
    readonly id?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Stage` for more information about the expected schema for this property.
     */
    readonly routeSettings?: any;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Stage` for more information about the expected schema for this property.
     */
    readonly stageVariables?: any;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Stage` for more information about the expected schema for this property.
     */
    readonly tags?: any;
}
/**
 * Resource Type definition for AWS::ApiGatewayV2::Stage
 */
export function getStageOutput(args: GetStageOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStageResult> {
    return pulumi.output(args).apply((a: any) => getStage(a, opts))
}

export interface GetStageOutputArgs {
    id: pulumi.Input<string>;
}
