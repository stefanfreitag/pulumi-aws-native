// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.
 */
export function getApiKey(args: GetApiKeyArgs, opts?: pulumi.InvokeOptions): Promise<GetApiKeyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:apigateway:getApiKey", {
        "apiKeyId": args.apiKeyId,
    }, opts);
}

export interface GetApiKeyArgs {
    /**
     * A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs 
     */
    apiKeyId: string;
}

export interface GetApiKeyResult {
    /**
     * A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs 
     */
    readonly apiKeyId?: string;
    /**
     * An MKT customer identifier, when integrating with the AWS SaaS Marketplace.
     */
    readonly customerId?: string;
    /**
     * The description of the ApiKey.
     */
    readonly description?: string;
    /**
     * Specifies whether the ApiKey can be used by callers.
     */
    readonly enabled?: boolean;
    /**
     * DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
     */
    readonly stageKeys?: outputs.apigateway.ApiKeyStageKey[];
    /**
     * The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.
     */
    readonly tags?: outputs.apigateway.ApiKeyTag[];
}
/**
 * The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.
 */
export function getApiKeyOutput(args: GetApiKeyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApiKeyResult> {
    return pulumi.output(args).apply((a: any) => getApiKey(a, opts))
}

export interface GetApiKeyOutputArgs {
    /**
     * A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs 
     */
    apiKeyId: pulumi.Input<string>;
}
