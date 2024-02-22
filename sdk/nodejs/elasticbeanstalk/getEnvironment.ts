// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticBeanstalk::Environment
 */
export function getEnvironment(args: GetEnvironmentArgs, opts?: pulumi.InvokeOptions): Promise<GetEnvironmentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticbeanstalk:getEnvironment", {
        "environmentName": args.environmentName,
    }, opts);
}

export interface GetEnvironmentArgs {
    /**
     * A unique name for the environment.
     */
    environmentName: string;
}

export interface GetEnvironmentResult {
    /**
     * Your description for this environment.
     */
    readonly description?: string;
    readonly endpointUrl?: string;
    /**
     * The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.
     */
    readonly operationsRole?: string;
    /**
     * The Amazon Resource Name (ARN) of the custom platform to use with the environment.
     */
    readonly platformArn?: string;
    /**
     * Specifies the tags applied to resources in the environment.
     */
    readonly tags?: outputs.Tag[];
    /**
     * Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
     */
    readonly tier?: outputs.elasticbeanstalk.EnvironmentTier;
    /**
     * The name of the application version to deploy.
     */
    readonly versionLabel?: string;
}
/**
 * Resource Type definition for AWS::ElasticBeanstalk::Environment
 */
export function getEnvironmentOutput(args: GetEnvironmentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEnvironmentResult> {
    return pulumi.output(args).apply((a: any) => getEnvironment(a, opts))
}

export interface GetEnvironmentOutputArgs {
    /**
     * A unique name for the environment.
     */
    environmentName: pulumi.Input<string>;
}
